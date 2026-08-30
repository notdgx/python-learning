#!/usr/bin/env python3
"""Deterministic metadata/index manager for the active Python learning notes tree.

Usage:
    python notes/notes-tracker.py                 # check + normalize + generate
    python notes/notes-tracker.py check           # validate only
    python notes/notes-tracker.py normalize       # normalize YAML frontmatter
    python notes/notes-tracker.py generate        # generate index + metadata
    python notes/notes-tracker.py --root notes

The script intentionally treats active notes as source-of-truth. archive/ is ignored.
Generated files: notes/index.md and notes/metadata.json.
"""

from __future__ import annotations

import argparse
import hashlib
import json
import re
import sys
from dataclasses import dataclass, asdict
from datetime import datetime
from pathlib import Path
from typing import Any, Iterable

try:
    import yaml  # PyYAML; preferred because frontmatter may contain quoted/scalar YAML.
except ImportError:
    yaml = None

ORDER_RE = re.compile(r"^(\d+)-(.*)$")
FRONTMATTER_RE = re.compile(r"\A\ufeff?---[ \t]*\r?\n(?P<body>.*?)(?:\r?\n)?---[ \t]*(?:\r?\n|\Z)", re.DOTALL)
HEADING_RE = re.compile(r"^(#{1,6})[ \t]+(.+?)[ \t]*#*[ \t]*$", re.MULTILINE)
REF_RE = re.compile(r"^(?P<order>\d+)-reference-file-(?P<index>\d+)\.py$", re.IGNORECASE)
SAFE_SLUG_RE = re.compile(r"[^a-z0-9]+")
DATE_RE = re.compile(r"^\d{4}-\d{2}-\d{2}$")
TIME_RE = re.compile(r"^\d{2}:\d{2}:\d{2}(?:[+-]\d{2}:\d{2}|Z)?$")

GENERATED_NAMES = {"index.md", "metadata.json", "notes-tracker.py"}
IGNORED_DIRS = {"archive", ".git", "__pycache__", "node_modules"}


class TrackerError(Exception):
    """Expected, user-actionable tracker failure."""


@dataclass(frozen=True)
class Heading:
    id: str
    text: str
    level: int


@dataclass(frozen=True)
class ReferenceFile:
    name: str
    sourcePath: str
    order: int
    referenceIndex: int
    sha256: str
    sizeBytes: int


@dataclass(frozen=True)
class Note:
    id: str
    title: str
    route: str
    sourcePath: str
    order: int
    date: str
    time: str
    headings: tuple[Heading, ...]
    references: tuple[ReferenceFile, ...]
    sha256: str
    sizeBytes: int


def now_local() -> datetime:
    return datetime.now().astimezone()


def parse_order(name: str) -> tuple[int, str]:
    match = ORDER_RE.match(name)
    if not match:
        raise TrackerError(
            f"Invalid ordered name '{name}'. Expected '<NN>-<name>' (for example '00-integer.md')."
        )
    return int(match.group(1)), match.group(2)


def strip_order(name: str) -> str:
    match = ORDER_RE.match(name)
    return match.group(2) if match else name


def humanize(stem_or_name: str) -> str:
    text = Path(stem_or_name).stem
    text = strip_order(text)
    text = text.replace("_", " ").replace("-", " ")
    text = re.sub(r"\s+", " ", text).strip()
    if not text:
        return "Untitled"
    return " ".join(word if word.isupper() else word[:1].upper() + word[1:] for word in text.split())


def slugify(text: str) -> str:
    value = text.strip().lower().replace("_", "-")
    value = SAFE_SLUG_RE.sub("-", value).strip("-")
    return value or "untitled"


def relative_posix(path: Path, root: Path) -> str:
    return path.relative_to(root.parent).as_posix()


def sha256_file(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for chunk in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest()


def read_text(path: Path) -> str:
    try:
        return path.read_text(encoding="utf-8-sig")
    except UnicodeDecodeError as exc:
        raise TrackerError(f"Unable to decode UTF-8 Markdown file: {path}: {exc}") from exc
    except OSError as exc:
        raise TrackerError(f"Unable to read {path}: {exc}") from exc


def write_text_if_changed(path: Path, content: str) -> bool:
    current = None
    if path.exists():
        try:
            current = path.read_text(encoding="utf-8")
        except UnicodeDecodeError as exc:
            raise TrackerError(f"Generated file is not valid UTF-8: {path}: {exc}") from exc
    if current == content:
        return False
    path.write_text(content, encoding="utf-8", newline="\n")
    return True


def parse_frontmatter(text: str) -> tuple[dict[str, Any], str, bool]:
    match = FRONTMATTER_RE.match(text)
    if not match:
        return {}, text, False
    body = match.group("body")
    remainder = text[match.end():]
    if yaml is None:
        raise TrackerError(
            "PyYAML is required to parse Markdown frontmatter. Install it with: pip install pyyaml"
        )
    try:
        data = yaml.safe_load(body) or {}
    except Exception as exc:
        raise TrackerError(f"Invalid YAML frontmatter: {exc}") from exc
    if not isinstance(data, dict):
        raise TrackerError("Frontmatter must be a YAML mapping/object.")
    return data, remainder, True


def normalize_date(value: Any, default: str) -> str:
    if value is None or value == "":
        return default
    text = str(value).strip()
    if not DATE_RE.fullmatch(text):
        # Accept datetime/date objects emitted by PyYAML.
        if hasattr(value, "isoformat"):
            text = value.isoformat()[:10]
        if not DATE_RE.fullmatch(text):
            raise TrackerError(f"Invalid frontmatter date '{value}'. Expected YYYY-MM-DD.")
    try:
        datetime.strptime(text, "%Y-%m-%d")
    except ValueError as exc:
        raise TrackerError(f"Invalid frontmatter date '{text}'.") from exc
    return text


def normalize_time(value: Any, default: str) -> str:
    if value is None or value == "":
        return default
    text = str(value).strip()
    # PyYAML may load 12:34:56 as a datetime.time object.
    if hasattr(value, "isoformat") and not isinstance(value, str):
        text = value.isoformat()
    text = text.replace(" ", "")
    if not TIME_RE.fullmatch(text):
        raise TrackerError(
            f"Invalid frontmatter time '{value}'. Expected HH:MM:SS, optionally with timezone offset."
        )
    return text


def yaml_quote_time(value: str) -> str:
    # Quote time explicitly so YAML parsers cannot reinterpret it as another scalar type.
    escaped = value.replace('"', '\\"')
    return f'"{escaped}"'


def canonical_frontmatter(date_value: str, time_value: str) -> str:
    return f"---\ndate: {date_value}\ntime: {yaml_quote_time(time_value)}\n---\n"


def normalize_note(path: Path, *, touch_missing_only: bool = True) -> tuple[str, str, bool]:
    """Normalize YAML to exactly date/time and return body + metadata values + changed flag."""
    original = read_text(path)
    data, body, has_frontmatter = parse_frontmatter(original)
    current = now_local()

    date_default = current.date().isoformat()
    time_default = current.strftime("%H:%M:%S%z")
    if len(time_default) == 9:  # +HHMM -> +HH:MM
        time_default = time_default[:-2] + ":" + time_default[-2:]

    date_value = normalize_date(data.get("date"), date_default)
    time_value = normalize_time(data.get("time"), time_default)

    # Preserve all Markdown after frontmatter, but normalize its initial separator exactly.
    body = body.lstrip("\ufeff")
    if body and not body.startswith("\n"):
        body = "\n" + body
    # If there was no frontmatter, don't accidentally eat content.
    if has_frontmatter:
        new_text = canonical_frontmatter(date_value, time_value) + body.lstrip("\n")
        # Keep a single blank line between frontmatter and content when content exists.
        if body.strip():
            new_text = canonical_frontmatter(date_value, time_value) + body.lstrip("\n")
    else:
        new_text = canonical_frontmatter(date_value, time_value)
        if original:
            new_text += "\n" + original

    changed = new_text != original
    if changed:
        write_text_if_changed(path, new_text)
        # Read back exact canonical content used for parsing.
        new_text = read_text(path)
        _, body, _ = parse_frontmatter(new_text)
    return date_value, time_value, changed


def strip_inline_markup(text: str) -> str:
    value = re.sub(r"!\[([^]]*)\]\([^)]*\)", r"\1", text)
    value = re.sub(r"\[([^]]+)\]\([^)]*\)", r"\1", value)
    value = re.sub(r"[`*_~]", "", value)
    return value.strip()


def heading_ids(headings: Iterable[tuple[int, str]]) -> tuple[Heading, ...]:
    used: dict[str, int] = {}
    output: list[Heading] = []
    for level, raw in headings:
        text = strip_inline_markup(raw)
        base = slugify(text)
        count = used.get(base, 0)
        used[base] = count + 1
        identifier = base if count == 0 else f"{base}-{count + 1}"
        output.append(Heading(identifier, text, level))
    return tuple(output)


def extract_headings(text: str) -> tuple[Heading, ...]:
    _, body, _ = parse_frontmatter(text)
    candidates: list[tuple[int, str]] = []
    in_fence = False
    fence_char = ""
    for line in body.splitlines():
        stripped = line.strip()
        fence = re.match(r"^(```+|~~~+)", stripped)
        if fence:
            token = fence.group(1)
            if not in_fence:
                in_fence = True
                fence_char = token[0]
            elif token[0] == fence_char:
                in_fence = False
            continue
        if in_fence:
            continue
        match = re.match(r"^(#{1,6})[ \t]+(.+?)[ \t]*#*[ \t]*$", line)
        if match:
            candidates.append((len(match.group(1)), match.group(2)))
    return heading_ids(candidates)


def discover_note_files(root: Path) -> list[Path]:
    files: list[Path] = []
    for path in root.rglob("*.md"):
        relative = path.relative_to(root)
        parts = relative.parts
        if any(part in IGNORED_DIRS or part.startswith(".") for part in parts):
            continue
        if path.name in GENERATED_NAMES:
            continue
        if len(parts) != 3:
            raise TrackerError(
                f"Invalid active note depth: {path}. Expected notes/<topic>/<subtopic>/<NN-note>.md."
            )
        files.append(path)
    return sorted(files, key=lambda p: tuple((parse_order(part)[0] if i < 2 else parse_order(p.name)[0]) for i, part in enumerate(p.relative_to(root).parts)))


def discover_active_dirs(root: Path) -> list[tuple[Path, int, str]]:
    results: list[tuple[Path, int, str]] = []
    for path in root.iterdir():
        if not path.is_dir() or path.name in IGNORED_DIRS or path.name.startswith("."):
            continue
        order, _ = parse_order(path.name)
        results.append((path, order, humanize(path.name)))
    for topic_dir, _, _ in results:
        for child in topic_dir.iterdir():
            if not child.is_dir() or child.name in IGNORED_DIRS or child.name.startswith("."):
                continue
            parse_order(child.name)
    return sorted(results, key=lambda x: (x[1], x[0].name))


def validate_unique_orders(entries: list[Path], label: str) -> None:
    seen: dict[int, Path] = {}
    for path in entries:
        order, _ = parse_order(path.name)
        if order in seen:
            raise TrackerError(
                f"Duplicate {label} order '{order:02d}' in:\n- {seen[order]}\n- {path}\n\n"
                "Rename one sibling so every ordered sibling has a unique NN prefix."
            )
        seen[order] = path


def validate_tree(root: Path) -> None:
    if not root.exists():
        raise TrackerError(f"Notes root does not exist: {root}")
    if not root.is_dir():
        raise TrackerError(f"Notes root is not a directory: {root}")

    topics = [p for p in root.iterdir() if p.is_dir() and p.name not in IGNORED_DIRS and not p.name.startswith(".")]
    validate_unique_orders(topics, "topic")

    note_files = discover_note_files(root)
    # Validate topic and subtopic NN prefixes and exactly three levels.
    for path in note_files:
        rel = path.relative_to(root).parts
        topic, subtopic, filename = rel
        parse_order(topic)
        parse_order(subtopic)
        note_order, _ = parse_order(filename)
        if path.suffix.lower() != ".md":
            raise TrackerError(f"Unexpected note extension: {path}")
        siblings = list(path.parent.glob("*.md"))
        siblings = [p for p in siblings if p.name not in GENERATED_NAMES]
        validate_unique_orders(siblings, f"note in {path.parent}")
        if note_order < 0:
            raise TrackerError(f"Invalid note order: {path}")

        # Reference files are only accepted using the explicit same-order convention.
        references = [p for p in path.parent.glob("*.py") if REF_RE.fullmatch(p.name)]
        for ref in references:
            ref_match = REF_RE.fullmatch(ref.name)
            assert ref_match
            if int(ref_match.group("order")) != note_order:
                raise TrackerError(
                    f"Reference order mismatch: {ref} belongs beside {path.name} but has a different NN prefix."
                )


def make_route(path: Path, root: Path) -> str:
    rel = path.relative_to(root).with_suffix("")
    pieces = [slugify(strip_order(part)) for part in rel.parts]
    return "/notes/" + "/".join(pieces)


def find_references(note_path: Path, note_order: int, root: Path) -> tuple[ReferenceFile, ...]:
    found: list[ReferenceFile] = []
    candidates = []
    for path in note_path.parent.glob("*.py"):
        match = REF_RE.fullmatch(path.name)
        if not match:
            continue
        if int(match.group("order")) == note_order:
            candidates.append((path, int(match.group("index"))))
    candidates.sort(key=lambda pair: (pair[1], pair[0].name))
    seen_indices: set[int] = set()
    for path, index in candidates:
        if index in seen_indices:
            raise TrackerError(f"Duplicate reference file index {index} beside {note_path}.")
        seen_indices.add(index)
        found.append(
            ReferenceFile(
                name=path.name,
                sourcePath=relative_posix(path, root),
                order=note_order,
                referenceIndex=index,
                sha256=sha256_file(path),
                sizeBytes=path.stat().st_size,
            )
        )
    return tuple(found)


def build_notes(root: Path, normalize: bool) -> tuple[Note, ...]:
    files = discover_note_files(root)
    notes: list[Note] = []
    for path in files:
        order, _ = parse_order(path.name)
        if normalize:
            date_value, time_value, _ = normalize_note(path)
        else:
            text = read_text(path)
            data, _, has = parse_frontmatter(text)
            if not has:
                raise TrackerError(f"Missing YAML frontmatter: {path}. Run the tracker to add date/time.")
            date_value = normalize_date(data.get("date"), "")
            time_value = normalize_time(data.get("time"), "")
            if not date_value or not time_value:
                raise TrackerError(f"Missing date/time metadata: {path}")
        text = read_text(path)
        headings = extract_headings(text)
        references = find_references(path, order, root)
        route = make_route(path, root)
        rel = relative_posix(path, root)
        # Stable id is based on source path, not mutable title.
        note_id = hashlib.sha256(rel.encode("utf-8")).hexdigest()[:16]
        notes.append(
            Note(
                id=note_id,
                title=humanize(path.name),
                route=route,
                sourcePath=rel,
                order=order,
                date=date_value,
                time=time_value,
                headings=headings,
                references=references,
                sha256=sha256_file(path),
                sizeBytes=path.stat().st_size,
            )
        )
    return tuple(notes)


def tree_sort_key(path: Path) -> tuple[int, ...]:
    values: list[int] = []
    for part in path.parts:
        match = ORDER_RE.match(part)
        if match:
            values.append(int(match.group(1)))
    return tuple(values)


def generate_index(root: Path, notes: tuple[Note, ...]) -> str:
    groups: dict[str, dict[str, list[Note]]] = {}
    for note in notes:
        rel = Path(note.sourcePath)
        topic, subtopic, _ = rel.parts
        groups.setdefault(topic, {}).setdefault(subtopic, []).append(note)

    lines = ["# Python Learning", "", ""]
    topic_dirs = sorted(groups, key=lambda x: (parse_order(x)[0], x))
    for topic in topic_dirs:
        lines.append(f"- {humanize(topic)}")
        subtopics = groups[topic]
        for subtopic in sorted(subtopics, key=lambda x: (parse_order(x)[0], x)):
            lines.append(f"  - {humanize(subtopic)}")
            ordered_notes = sorted(subtopics[subtopic], key=lambda n: (n.order, n.sourcePath))
            for note in ordered_notes:
                lines.append(f"    - [{note.title}]({note.route})")
    return "\n".join(lines).rstrip() + "\n"


def build_metadata(root: Path, notes: tuple[Note, ...], generated_at: str) -> dict[str, Any]:
    topics: dict[str, dict[str, Any]] = {}
    for note in notes:
        rel = Path(note.sourcePath)
        topic_dir, subtopic_dir, _ = rel.parts
        topic = topics.setdefault(
            topic_dir,
            {
                "id": hashlib.sha256(topic_dir.encode()).hexdigest()[:16],
                "title": humanize(topic_dir),
                "order": parse_order(topic_dir)[0],
                "slug": slugify(strip_order(topic_dir)),
                "subtopics": {},
            },
        )
        subtopics = topic["subtopics"]
        subtopics.setdefault(
            subtopic_dir,
            {
                "id": hashlib.sha256(f"{topic_dir}/{subtopic_dir}".encode()).hexdigest()[:16],
                "title": humanize(subtopic_dir),
                "order": parse_order(subtopic_dir)[0],
                "slug": slugify(strip_order(subtopic_dir)),
                "notes": [],
            },
        )["notes"].append({
            "id": note.id,
            "title": note.title,
            "route": note.route,
            "sourcePath": note.sourcePath,
            "order": note.order,
            "date": note.date,
            "time": note.time,
            "headings": [asdict(h) for h in note.headings],
            "references": [asdict(r) for r in note.references],
            "sha256": note.sha256,
            "sizeBytes": note.sizeBytes,
        })

    topic_list = []
    for topic_key in sorted(topics, key=lambda x: (topics[x]["order"], x)):
        topic = topics[topic_key]
        topic["subtopics"] = [
            topic["subtopics"][key]
            for key in sorted(topic["subtopics"], key=lambda x: (topic["subtopics"][x]["order"], x))
        ]
        for subtopic in topic["subtopics"]:
            subtopic["notes"].sort(key=lambda n: (n["order"], n["sourcePath"]))
        topic_list.append(topic)

    return {
        "schemaVersion": 1,
        "generatedAt": generated_at,
        "contentRoot": "notes",
        "sections": {
            "notes": {
                "id": "notes",
                "title": "Python Learning",
                "topics": topic_list,
            }
        },
        "stats": {
            "topics": len(topic_list),
            "subtopics": sum(len(t["subtopics"]) for t in topic_list),
            "notes": len(notes),
            "referenceFiles": sum(len(n.references) for n in notes),
        },
    }


def detect_route_collisions(notes: tuple[Note, ...]) -> None:
    seen: dict[str, str] = {}
    for note in notes:
        if note.route in seen:
            raise TrackerError(
                f"Route collision '{note.route}' between:\n- {seen[note.route]}\n- {note.sourcePath}\n"
                "Rename or relocate one source note."
            )
        seen[note.route] = note.sourcePath


def detect_reference_collisions(notes: tuple[Note, ...]) -> None:
    for note in notes:
        names: set[str] = set()
        for ref in note.references:
            if ref.name in names:
                raise TrackerError(f"Duplicate reference filename '{ref.name}' for {note.sourcePath}.")
            names.add(ref.name)


def check_generated_integrity(root: Path, expected_index: str, expected_metadata: dict[str, Any]) -> list[str]:
    warnings: list[str] = []
    index_path = root / "index.md"
    metadata_path = root / "metadata.json"
    if not index_path.exists():
        warnings.append(f"Generated index is missing: {index_path}")
    else:
        actual = read_text(index_path)
        if actual != expected_index:
            warnings.append(f"Generated index is stale: {index_path}")
    if not metadata_path.exists():
        warnings.append(f"Metadata file is missing: {metadata_path}")
    else:
        try:
            current = json.loads(metadata_path.read_text(encoding="utf-8"))
        except json.JSONDecodeError as exc:
            warnings.append(f"Metadata file contains invalid JSON: {metadata_path}: {exc}")
        else:
            # Compare semantic content excluding generation timestamp, since it is allowed to change on generation.
            expected_without_time = dict(expected_metadata)
            current_without_time = dict(current)
            expected_without_time.pop("generatedAt", None)
            current_without_time.pop("generatedAt", None)
            if current_without_time != expected_without_time:
                warnings.append(f"Metadata file is stale: {metadata_path}")
    return warnings


def generate(root: Path, *, normalize: bool) -> tuple[int, list[str]]:
    validate_tree(root)
    notes = build_notes(root, normalize=normalize)
    detect_route_collisions(notes)
    detect_reference_collisions(notes)
    generated_at = now_local().isoformat(timespec="seconds")
    index = generate_index(root, notes)
    metadata = build_metadata(root, notes, generated_at)
    index_changed = write_text_if_changed(root / "index.md", index)
    metadata_text = json.dumps(metadata, indent=2, ensure_ascii=False) + "\n"
    metadata_changed = write_text_if_changed(root / "metadata.json", metadata_text)
    changes = []
    if index_changed:
        changes.append("updated index.md")
    if metadata_changed:
        changes.append("updated metadata.json")
    return 0, changes


def check(root: Path) -> int:
    validate_tree(root)
    # Check mode does not mutate notes. It still needs to parse/validate current frontmatter.
    notes = build_notes(root, normalize=False)
    detect_route_collisions(notes)
    detect_reference_collisions(notes)
    expected = generate_index(root, notes)
    expected_metadata = build_metadata(root, notes, generated_at="__ignored__")
    warnings = check_generated_integrity(root, expected, expected_metadata)
    if warnings:
        for warning in warnings:
            print(f"WARNING: {warning}", file=sys.stderr)
        return 2
    print(f"OK: {len(notes)} notes validated; generated artifacts are current.")
    return 0


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("command", nargs="?", choices=["check", "normalize", "generate"], default="generate")
    parser.add_argument("--root", type=Path, default=Path(__file__).resolve().parent, help="Notes directory (default: this script's directory)")
    args = parser.parse_args()
    root = args.root.resolve()
    try:
        if args.command == "check":
            return check(root)
        if args.command == "normalize":
            code, changes = generate(root, normalize=True)
            print("OK: normalization complete." if not changes else "OK: " + "; ".join(changes))
            return code
        code, changes = generate(root, normalize=True)
        if changes:
            print("OK: " + "; ".join(changes))
        else:
            print("OK: no generated changes required.")
        return code
    except TrackerError as exc:
        print(f"ERROR: {exc}", file=sys.stderr)
        return 1
    except KeyboardInterrupt:
        print("ERROR: interrupted by user.", file=sys.stderr)
        return 130
    except OSError as exc:
        print(f"ERROR: filesystem operation failed: {exc}", file=sys.stderr)
        return 1


if __name__ == "__main__":
    raise SystemExit(main())
