# Python Learning Repository & Static Website Architecture

## 1. Purpose

This repository is the source of truth for a structured Python-learning knowledge base and a statically compiled website that presents that knowledge base.

The architecture has two deliberately separated concerns:

1. **Learning content** lives under `notes/`, `practice/`, and `projects/`.
2. **Presentation** lives under `website/` and is compiled with **Vite + React + TypeScript** into static files for deployment on **Cloudflare Pages**.

The website is not the source of truth. It is a generated presentation layer over the repository content.

> Core rule: content must remain useful even if the `website/` directory is removed.

---

## 2. Final Repository Structure

The current repository intentionally starts small while leaving room for the architecture to scale.

```text
.
├── LICENSE
├── README.md
├── archive/
│   ├── extra/
│   ├── important-ques/
│   ├── old-notes/
│   ├── old-practice-que/
│   └── old-practice-que-mysol/
├── notes/
│   ├── index.md
│   ├── metadata.json
│   ├── notes-tracker.py
│   ├── 00-syntax-and-basics/
│   │   ├── 00-variables-and-datatypes/
│   │   │   ├── 00-integer.md
│   │   │   ├── 00-reference-file-1.py
│   │   │   ├── 01-float.md
│   │   │   └── ...
│   │   ├── 01-operators/
│   │   └── ...
│   └── ...
├── practice/
│   └── index.md
├── projects/
│   └── index.md
└── website/
    ├── AGENTS.md
    ├── ARCHITECTURE.md
    └── DESIGN.md
```

The archived material is intentionally outside the active information architecture. It must not be automatically surfaced in the public notes navigation unless explicitly promoted later.

---

## 3. Architectural Principles

### 3.1 Content-first

Markdown and Python source files are canonical learning artifacts. Website code must consume them rather than duplicate their content.

### 3.2 Deterministic structure

Numeric prefixes (`NN-`) encode sibling ordering. They are structural, not display text.

Example:

```text
00-syntax-and-basics/
01-control-flow/
02-data-structures/
```

Within a topic:

```text
00-variables-and-datatypes/
01-operators/
```

Within a note group:

```text
00-integer.md
01-float.md
02-string.md
```

The website displays the human-readable name after removing exactly the leading numeric ordering prefix and separator.

### 3.3 Generated artifacts are disposable

`notes/index.md` and `notes/metadata.json` are generated from the active content tree and canonical note metadata. Manual edits to generated sections must not be required for correctness.

### 3.4 Static runtime

The production website must not require a server, API, database, Node.js runtime, or server-side rendering at request time. Node.js is build tooling only.

Vite's production build produces a static-hosting-ready bundle in `dist` by default. Cloudflare Pages supports React builds with `npm run build` and `dist` as the build directory. See the official documentation in the Source References section.

### 3.5 Build-time intelligence

Repository scanning, metadata generation, Markdown extraction, heading extraction, reference-file resolution, and route manifest generation should happen at build time. The browser receives already-structured content/data.

### 3.6 One-way data flow

```text
Repository files
      │
      ├── notes/*.md
      ├── notes/*.py
      ├── notes/metadata.json
      └── notes/index.md
             │
             ▼
      Content/build pipeline
             │
             ▼
      typed website data
             │
             ▼
      React components
             │
             ▼
      Vite production build
             │
             ▼
          dist/
             │
             ▼
       Cloudflare Pages
```

The browser must never need to scan the Git repository itself.

---

# 4. Content Information Architecture

## 4.1 Three-level topic model

The active learning hierarchy is deliberately limited to three semantic levels:

```text
Python Learning
└── 1.1 Syntax & Basics
    └── 1.1.1 Variables & Data Types
        ├── Integer
        ├── Float
        └── String
```

Filesystem representation:

```text
notes/
└── 00-syntax-and-basics/
    └── 00-variables-and-datatypes/
        ├── 00-integer.md
        ├── 01-float.md
        └── 02-string.md
```

The numeric directory/file prefixes are implementation ordering keys. The semantic hierarchy is represented by directory depth.

### Required invariant

Active notes must not introduce arbitrary fourth-level topic directories.

If a concept becomes too large, use additional Markdown headings inside the note or split it into sibling notes rather than creating an uncontrolled fourth taxonomy layer.

---

## 4.2 `notes/index.md`

`notes/index.md` is the generated Markdown representation of the active notes tree.

It is designed to serve two audiences:

- humans browsing the repository directly;
- the website build pipeline as a simple, readable navigation manifest.

Example generated representation:

```markdown
# Python Learning

- Syntax & Basics
  - Variables & Data Types
    - Integer
    - Float
    - String
  - Operators
    - Arithmetic Operators
    - Assignment Operators
```

### Index generation rules

1. Scan only the active `notes/` content tree.
2. Ignore `archive/`, hidden directories, `metadata.json`, `notes-tracker.py`, and unrelated files.
3. Use numeric prefixes only for sorting.
4. Strip the leading `NN-` from displayed directory/note names.
5. Prefer the Markdown frontmatter `title` when present? **No**: the canonical display title is derived from the note filename unless a future explicit title field is introduced by the architecture. This avoids a title-source conflict.
6. Link each note entry to its website route or repository-relative Markdown path according to the generated index contract. The route representation used by the website must be derived from metadata rather than duplicated manually.
7. Preserve deterministic alphabetical/numeric ordering based on the `NN-` prefix.
8. Regeneration must produce byte-for-byte stable output when source files have not changed, apart from explicitly time-stamped generated metadata where applicable.

### Display-name normalization

A filename such as:

```text
00-integer.md
```

is displayed as:

```text
Integer
```

Recommended normalization pipeline:

```text
00-variable-name.md
       ↓
remove extension
       ↓
remove one leading NN-
       ↓
replace hyphens/underscores with spaces
       ↓
human title casing where safe
       ↓
Variable Name
```

Do not aggressively rewrite acronyms or user-authored terminology. A future explicit title field may override this behavior if needed.

---

# 5. Note File Contract

## 5.1 Canonical note file

Each learning note is a Markdown file:

```text
notes/<topic>/<subtopic>/<NN-note-name>.md
```

Example:

```text
notes/00-syntax-and-basics/00-variables-and-datatypes/00-integer.md
```

The filename determines ordering and the default display title.

---

## 5.2 YAML frontmatter contract

The tracker must canonicalize note frontmatter so that **only `date` and `time` remain**.

Canonical form:

```yaml
---
date: 2026-08-30
time: "17:54:00+05:30"
---
```

Rules:

1. Existing frontmatter is parsed.
2. `date` is retained if valid; otherwise the tracker inserts the current date.
3. `time` is retained if valid; otherwise the tracker inserts the current local time with timezone offset when possible.
4. All other YAML keys are removed.
5. No second YAML frontmatter block may be created.
6. If the Markdown file has no frontmatter, create it at the beginning.
7. Content below frontmatter must be preserved byte-for-byte as far as practical; the tracker should not rewrite ordinary Markdown prose merely because metadata is normalized.
8. Date/time normalization must be deterministic and documented.
9. The tracker should update date/time only when creating missing metadata, not on every run. Otherwise every tracker run would dirty unchanged notes and create unnecessary Git changes.

### Important interpretation

`date` and `time` are content-file metadata. `metadata.json` may additionally contain generated/build metadata such as path, slug, headings, hash, order, references, and generation timestamp. These are separate layers and must not be copied into Markdown YAML.

---

# 6. Reference Python Files

A Markdown note may have source/reference Python files beside it.

Example:

```text
00-integer.md
00-reference-file-1.py
00-reference-file-2.py
```

Reference files share the note's `NN` prefix.

### Association rule

For a note:

```text
00-integer.md
```

candidate reference files are:

```text
00-reference-file-1.py
00-reference-file-2.py
...
```

The tracker should record explicit references in metadata in sorted order.

### Stronger naming rule

The `NN-reference-file-K.py` convention is intentionally scoped to sibling files. The tracker must never assume that an arbitrary `.py` in the directory belongs to the Markdown note.

### UI behavior

The note page exposes references in the right-side overview panel under a separate `Reference Files` section.

Clicking a reference file:

1. must not navigate away from the note;
2. opens an in-page code viewer/overlay/panel;
3. displays syntax-highlighted Python;
4. provides Copy;
5. provides Download;
6. uses the original reference filename for download.

The browser download must be generated from repository content packaged into the static build. There must be no runtime server call.

---

# 7. `notes/metadata.json`

`metadata.json` is the machine-readable content index used by the website build.

It is generated by `notes/notes-tracker.py` and must not be hand-maintained.

## 7.1 Design goal

The metadata file should make the website deterministic without repeatedly discovering repository structure at runtime.

## 7.2 Recommended schema

Top-level:

```json
{
  "schemaVersion": 1,
  "generatedAt": "2026-08-30T17:54:00+05:30",
  "contentRoot": "notes",
  "sections": {
    "notes": []
  }
}
```

Each topic node should contain enough information to render navigation:

```json
{
  "id": "notes/00-syntax-and-basics/00-variables-and-datatypes/00-integer",
  "type": "note",
  "order": 0,
  "name": "00-integer.md",
  "title": "Integer",
  "slug": "integer",
  "relativePath": "00-syntax-and-basics/00-variables-and-datatypes/00-integer.md",
  "route": "/notes/syntax-and-basics/variables-and-datatypes/integer",
  "date": "2026-08-30",
  "time": "17:54:00+05:30",
  "headings": [],
  "references": [],
  "contentHash": "..."
}
```

The exact JSON implementation may evolve, but these concepts should remain available:

- stable identity;
- type (`topic`, `subtopic`, `note` or equivalent);
- numeric order;
- display title;
- relative source path;
- canonical route;
- frontmatter date/time;
- extracted Markdown headings;
- reference Python files;
- content hash;
- schema version.

### Do not duplicate full Markdown in metadata

`metadata.json` should contain structure and indexes, not full note bodies. This avoids a second copy of every note and reduces generated-file churn.

---

# 8. Stable IDs and Routes

The website must not use array indexes as durable identities.

### Stable identity

Prefer a normalized repository-relative path as the base ID:

```text
notes/00-syntax-and-basics/00-variables-and-datatypes/00-integer.md
```

The route is derived from the same semantic path after removing ordering prefixes.

Example:

```text
/notes/syntax-and-basics/variables-and-datatypes/integer
```

### Route invariants

- route generation must be deterministic;
- route components must be URL-safe;
- ordering prefixes must never appear in public URLs;
- renaming a note may intentionally change its route;
- route collisions must fail the build rather than silently overwrite one note.

If route stability across renames becomes important later, add explicit stable IDs to generated metadata rather than relying on filenames.

---

# 9. Markdown Rendering Architecture

The website must render the original Markdown semantics rather than maintain hand-written React pages for individual notes.

Recommended build-time flow:

```text
Markdown file
   ↓
frontmatter parse
   ↓
Markdown parse
   ↓
heading extraction
   ↓
AST / sanitized HTML representation
   ↓
typed note model
   ↓
React renderer
```

### Rendering requirements

Support at minimum:

- headings H1-H6;
- paragraphs;
- emphasis/strong;
- ordered and unordered lists;
- links;
- blockquotes;
- inline code;
- fenced code blocks;
- horizontal rules;
- tables where required;
- task lists if used;
- safe raw HTML handling if enabled.

### Security rule

Markdown is content, but it is still untrusted input from a tooling perspective. Do not blindly inject unsanitized HTML. Any raw HTML support must be explicitly sanitized or disabled.

---

# 10. Note Page Layout

Every note page follows the same information architecture.

```text
┌──────────────────────────────────────────────────────────────┐
│ Navbar                                                       │
├──────────────┬───────────────────────────┬───────────────────┤
│ Topic        │ Actual Markdown Note      │ Overview / TOC    │
│ Navigation   │                           │                   │
│              │                           │ Headings          │
│ current note │                           │                   │
│ highlighted  │                           │ Reference Files   │
│              │                           │                   │
├──────────────┴───────────────────────────┴───────────────────┤
│ Footer                                                       │
└──────────────────────────────────────────────────────────────┘
```

## 10.1 Left panel: topic navigator

Shows the overall topic/subtopic hierarchy.

Requirements:

- current note highlighted;
- collapsible/hideable;
- current branch automatically expanded;
- keyboard accessible;
- does not lose current location when toggled;
- navigation derived from metadata.

## 10.2 Middle panel: note content

Displays the exact Markdown content in styled rendered form.

Requirements:

- typography optimized for reading code and explanations;
- code blocks with copy controls;
- anchorable headings;
- stable heading IDs;
- preservation of code formatting;
- responsive behavior for smaller screens.

## 10.3 Right panel: overview

The overview is generated from the headings inside the current Markdown document.

Example:

```text
Overview
  Introduction
  Syntax
  Examples
  Common Mistakes

Reference Files
  integer-reference-file-1.py
  integer-reference-file-2.py
```

Clicking an overview heading scrolls to the corresponding heading in the current note.

### Heading rules

- Do not hard-code the overview.
- Exclude the document title when it is redundant with the page title.
- Preserve heading nesting.
- Generate collision-safe anchor IDs.
- Duplicate heading text must not produce duplicate IDs.

---

# 11. Website Information Architecture

Global navigation:

```text
Python Learning

Notes
Projects
Practice
Links
Donate

GitHub icon + current repository star count
```

## 11.1 Homepage

The homepage includes:

- Hero section;
- repository/learning identity;
- introductory details;
- learning-topic discovery;
- calls to explore notes/projects/practice;
- repository/GitHub information;
- footer;
- the supplied visual background/hero/code content when provided later.

Visual rules are defined in `website/DESIGN.md`; architecture must not duplicate visual specifications there.

## 11.2 Notes page

Shows the nested topic hierarchy generated from `notes/index.md` / `metadata.json`.

Clicking a topic or note must lead directly to its generated note route.

## 11.3 Projects and Practice

These are architectural placeholders for now.

The same content-driven principles should eventually be applied:

```text
projects/
practice/
```

but their detailed schemas are intentionally deferred to a later implementation phase.

## 11.4 Links

A static collection of external links/resources. It should not require a backend.

## 11.5 Donate

A static informational/payment-link destination. Any payment/QR behavior belongs to `DESIGN.md` and the later UI implementation, not this architecture contract.

---

# 12. GitHub Repository Metadata

The navbar may display the repository's current public star count.

Because the site is static, this data cannot depend on a runtime API request if the goal is a serverless/static page with deterministic offline behavior.

Recommended architecture:

```text
GitHub repository metadata
        ↓
build-time fetch or explicitly supplied build variable
        ↓
static generated metadata
        ↓
website
```

Requirements:

- build must remain successful when the star-count source is temporarily unavailable;
- show a safe fallback rather than a broken UI;
- do not expose private credentials;
- do not put GitHub tokens in client-side code;
- optionally cache the last successful value for build resilience.

A future automation workflow can refresh this generated metadata on a schedule, but that is an enhancement and not required for the initial architecture.

---

# 13. Static Build Boundary

The repository and website must have a clear build boundary.

Recommended layout inside `website/`:

```text
website/
├── src/
├── public/
├── scripts/
├── package.json
├── tsconfig.json
├── vite.config.ts
└── ...
```

The production output is:

```text
website/dist/
```

or the configured root-equivalent Vite output directory.

### Build phases

```text
Phase 1  Validate repository/content
Phase 2  Normalize note frontmatter
Phase 3  Generate notes/metadata.json
Phase 4  Generate notes/index.md
Phase 5  Load content into website build
Phase 6  Validate routes/references/headings
Phase 7  Vite production build
Phase 8  Optional static preview
```

The exact orchestration can be implemented as npm scripts later, e.g.:

```text
npm run content:check
npm run content:generate
npm run build
npm run preview
```

The final production artifact must be deployable as a static directory.

---

# 14. Consuming Content Outside `website/`

The website source lives in `website/`, but its content source lives in `notes/`.

This is intentional and must not be “simplified” by moving the notes into `website/src`.

Two supported implementation patterns exist:

### Pattern A — Build-time importer

Website build tooling directly resolves repository files during build.

```text
website build script
        ↓
../notes
```

### Pattern B — Generated content staging

A build script copies/normalizes only the required static content into a generated directory under `website/` before Vite runs.

```text
../notes
   ↓
website/.generated/
   ↓
Vite
```

Pattern B is preferred when Vite's filesystem sandboxing, globbing, or deployment packaging would otherwise make imports from outside the website root fragile.

Generated staging content must never become the canonical source.

---

# 15. Build-Time Validation

The build must fail loudly on structural errors.

At minimum validate:

### Filename validation

- invalid numeric prefixes;
- duplicate sibling order numbers;
- missing `.md` note files where expected;
- malformed reference-file names;
- unsupported file types in active note folders.

### Hierarchy validation

- unexpected topic depth;
- empty topic directories;
- duplicate semantic titles where route generation would collide;
- malformed directory names;
- forbidden hidden/system files.

### Metadata validation

- malformed frontmatter;
- missing `date` or `time` after normalization;
- unsupported YAML fields remaining in frontmatter;
- invalid date/time values.

### Reference validation

- reference file points to no matching note;
- duplicate reference names;
- unreadable Python files;
- unsafe path traversal attempts.

### Website validation

- route collisions;
- missing referenced content;
- broken Markdown links when those are declared to be validated;
- duplicate heading IDs;
- missing current-note references in navigation.

A content error should not be silently converted into a broken page.

---

# 16. Path and Filesystem Safety

All repository-relative paths must be normalized and validated before use.

Reject or safely ignore:

```text
../../outside-file.py
..\\outside-file.py
absolute paths
symlink escapes outside the repository/content root
```

The tracker and website build tools must operate only within their declared roots.

Do not trust filenames when constructing output paths without validation.

---

# 17. Deterministic Ordering

Ordering is encoded by numeric prefixes.

### Required parser

Accept exactly the intended leading numeric ordering pattern, for example:

```regex
^(\d+)-(.+)$
```

Use the numeric value for ordering rather than lexicographical filename ordering.

This avoids:

```text
1-topic
10-topic
2-topic
```

being interpreted incorrectly.

For consistency, active content should normally use two-digit prefixes (`00`–`99`). The architecture may support more digits, but the website must not depend on a fixed width.

### Duplicate order numbers

Two siblings with the same numeric prefix should be a validation error unless an explicit future tie-breaking policy is introduced.

---

# 18. Search Architecture

The first version should implement client-side search over generated static metadata/content.

No server is required.

Recommended search document fields:

- title;
- topic path;
- note slug;
- headings;
- normalized note text;
- tags later if introduced;
- reference filenames where useful.

For small-to-medium learning-note collections, a static in-browser index is sufficient.

If the repository becomes very large, generate a compact search index at build time rather than parsing every Markdown file in the browser.

---

# 19. Accessibility

Architecture-level requirements:

- semantic HTML;
- keyboard navigation;
- visible focus states;
- accessible names for icon-only buttons;
- no information conveyed by color alone;
- skip-to-content mechanism;
- dialog/overlay focus management for reference code viewers;
- reduced-motion support;
- reasonable contrast;
- responsive behavior without hiding critical content.

Visual implementation belongs in `DESIGN.md`.

---

# 20. Performance

Because the site is content-heavy and static:

- avoid loading every full note into the initial page unnecessarily;
- prefer route-level/content-level loading where practical;
- keep metadata compact;
- do not ship duplicate Markdown and HTML copies unless justified;
- code highlighting should not dominate initial bundle cost;
- optimize repository images and other static assets;
- use hashed Vite assets for cache safety.

Large notes should not make the global navigation payload unnecessarily large.

---

# 21. Client Routing Strategy

The site should use clean routes such as:

```text
/
/notes
/notes/syntax-and-basics/variables-and-datatypes/integer
/projects
/practice
/links
/donate
```

Routes should be handled as an SPA where the deployment configuration supports fallback to the root document. Cloudflare Pages documents SPA behavior in which, without a top-level `404.html`, unmatched paths can be routed to the application root.

Even with SPA fallback, the application must provide its own in-app 404 state for unknown logical routes.

### Deep-link invariant

Opening a note URL directly, refreshing it, or entering it in a new tab must produce the same note page as navigating there from `/notes`.

---

# 22. Note Navigation State

The current note is determined from the URL, not only React in-memory state.

This ensures:

- refresh persistence;
- shareable links;
- browser back/forward support;
- deep linking;
- consistent current-note highlighting.

Left navigation collapse state may be persisted locally, but persisted UI state must never be required to understand the current content.

---

# 23. Reference Code Viewer Architecture

Reference code is content, not a second page type.

```text
Note Page
  └── Reference Files
       └── Code Viewer
            ├── filename
            ├── syntax highlighting
            ├── copy
            └── download
```

The code viewer should support:

- long-file scrolling;
- line wrapping toggle if desired;
- line numbers if desired;
- copy feedback;
- accessible close behavior;
- escape-to-close for overlays;
- preserved scroll position in the underlying note;
- downloadable content with the original `.py` filename.

Download must use exact file content packaged at build time.

---

# 24. Future Content Domains

`practice/` and `projects/` will later adopt schemas similar to `notes/`.

They should not be mixed into the initial notes taxonomy.

Future likely shapes:

```text
practice/
├── index.md
├── metadata.json
├── practice-tracker.py
└── ...

projects/
├── index.md
├── metadata.json
├── project-tracker.py
└── ...
```

The website architecture should therefore model content as extensible sections rather than hard-coding “notes” throughout every component.

Conceptually:

```text
ContentSection
├── notes
├── practice
└── projects
```

Only `notes` is fully implemented initially.

---

# 25. Separation from `DESIGN.md`

`ARCHITECTURE.md` defines:

- file structure;
- content contracts;
- data flow;
- build pipeline;
- routing;
- validation;
- component responsibilities at a structural level;
- static-hosting constraints.

`DESIGN.md` defines:

- visual language;
- typography;
- spacing;
- colors;
- motion;
- component appearance;
- hero/footer visuals;
- interaction styling;
- responsive visual behavior.

Do not duplicate visual decisions into this file. If a visual requirement conflicts with the architectural constraints, preserve the architecture and adapt the visual implementation.

---

# 26. Separation from `AGENTS.md`

`AGENTS.md` is the operational rulebook for AI agents and coding workflows.

It defines:

- how to inspect the repository;
- which files are authoritative;
- what must be validated;
- what agents may change;
- approval requirements;
- commit requirements;
- how to update itself when new durable preferences are discovered.

`ARCHITECTURE.md` should remain stable and descriptive rather than becoming a task log.

---

# 27. Recommended Component/Data Boundaries

A scalable website should roughly separate:

```text
src/
├── app/
│   ├── router
│   ├── providers
│   └── app-shell
├── components/
│   ├── navigation/
│   ├── note/
│   ├── markdown/
│   ├── code-viewer/
│   ├── common/
│   └── layout/
├── pages/
│   ├── home
│   ├── notes
│   ├── note
│   ├── projects
│   ├── practice
│   ├── links
│   └── donate
├── content/
│   ├── types
│   ├── loaders
│   └── adapters
├── lib/
│   ├── slug
│   ├── headings
│   ├── paths
│   └── validation
└── styles/
```

This is a conceptual boundary, not a mandate to create every folder immediately.

Avoid a giant `App.tsx` that owns routing, Markdown parsing, navigation, GitHub data, and visual state simultaneously.

---

# 28. Build and Deployment Contract

For Cloudflare Pages, the expected static deployment contract is:

```text
Repository root
   ↓
install dependencies
   ↓
content generation/validation
   ↓
npm run build
   ↓
website/dist/
   ↓
Cloudflare Pages
```

Cloudflare's React Pages guidance uses `npm run build` and `dist` for deployment, and Pages can automatically rebuild when connected to a Git repository.

Vite's production build is designed for static hosting and outputs `dist` by default.

Do not introduce SSR, API routes, server-only rendering, database requirements, or runtime backend dependencies unless this architecture is deliberately revised.

---

# 29. Testing Strategy

The project should eventually contain four distinct test layers:

### Content tests

Validate:

- hierarchy;
- filenames;
- frontmatter;
- references;
- generated index;
- metadata schema.

### Unit tests

Validate pure functions:

- prefix parsing;
- title normalization;
- route generation;
- heading ID generation;
- reference association.

### Build tests

Run a clean production build and ensure:

- every metadata note resolves;
- every route resolves;
- every reference file is packaged;
- no route collision exists;
- no broken imports exist.

### Browser/UI tests

Eventually test:

- topic navigation;
- deep links;
- note overview scrolling;
- copy/download behavior;
- responsive navigation;
- reference viewer;
- not-found state.

---

# 30. Edge Cases and Resolutions

## 30.1 Existing YAML with unrelated fields

**Risk:** tracker leaves old metadata behind.

**Resolution:** canonicalize frontmatter to `date` + `time` only.

## 30.2 Missing date/time

**Risk:** notes become inconsistent.

**Resolution:** insert missing values once; do not refresh existing values on every run.

## 30.3 Duplicate ordering numbers

**Risk:** unstable navigation.

**Resolution:** fail validation.

## 30.4 Numeric prefixes greater than 99

**Risk:** parser assumes exactly two digits.

**Resolution:** parse one-or-more digits; display logic strips the complete numeric prefix.

## 30.5 Note filename does not contain numeric prefix

**Risk:** undetermined order.

**Resolution:** validation error for active notes.

## 30.6 Duplicate generated routes

**Risk:** one note becomes unreachable.

**Resolution:** fail build and print both conflicting source paths.

## 30.7 Duplicate Markdown headings

**Risk:** overview links collide.

**Resolution:** deterministic slug suffixes, e.g. `example`, `example-2`, `example-3`.

## 30.8 Reference Python file without a matching note prefix

**Risk:** orphaned source code.

**Resolution:** either report as orphaned during validation or ignore explicitly according to a documented rule. Do not silently associate it with the wrong note.

## 30.9 Reference file renamed independently of note

**Risk:** stale metadata.

**Resolution:** regenerate metadata from the filesystem every content build.

## 30.10 Deleted note remains in metadata

**Risk:** website links to dead content.

**Resolution:** metadata is regenerated from current filesystem state; no stale-note retention.

## 30.11 Manual modification of generated files

**Risk:** changes disappear.

**Resolution:** generated regions/files are overwritten by the tracker. Agents must not manually “fix” generated output instead of fixing the source.

## 30.12 Markdown contains raw HTML/script-like content

**Risk:** unsafe HTML rendering.

**Resolution:** sanitize or disable raw HTML rendering.

## 30.13 Windows vs Linux paths

**Risk:** metadata and routes differ between environments.

**Resolution:** normalize all repository paths to forward-slash POSIX form in metadata, regardless of host OS.

## 30.14 Unicode filenames

**Risk:** URL and filesystem normalization differences.

**Resolution:** preserve source filenames, but generate normalized URL slugs and validate collisions.

## 30.15 Case-only filename differences

**Risk:** works on case-sensitive Linux but collides on case-insensitive Windows.

**Resolution:** validation should detect case-insensitive path/route collisions.

## 30.16 Symlinks/junctions

**Risk:** content escapes the intended tree.

**Resolution:** reject links that resolve outside the declared content root.

## 30.17 Empty directories

**Risk:** invisible topics.

**Resolution:** empty active topic folders should fail validation or be reported clearly; do not generate empty navigation nodes silently.

## 30.18 Huge Markdown files

**Risk:** large browser bundles.

**Resolution:** consider build-time route splitting or generated per-note content chunks if scale requires it.

## 30.19 GitHub API unavailable during build

**Risk:** unrelated site builds fail.

**Resolution:** star count is non-critical; use fallback/cached data and continue.

## 30.20 Deep link on static hosting

**Risk:** refreshing `/notes/.../integer` produces a 404.

**Resolution:** use the deployment's SPA fallback configuration and maintain an application-level 404 state.

## 30.21 Browser refresh loses note panel state

**Risk:** current note works but UI context disappears.

**Resolution:** derive current note from URL and optionally persist only non-critical UI preferences.

## 30.22 User changes filename/order

**Risk:** route and index change unexpectedly.

**Resolution:** treat filename/directory changes as intentional content-structure changes; regenerate metadata and test route output.

## 30.23 Build sees partially edited content

**Risk:** malformed metadata during simultaneous edits.

**Resolution:** tracker should fail atomically where practical and avoid writing half-generated JSON/index files.

---

# 31. Future Enhancements

The architecture intentionally leaves room for:

- generated RSS/feed-like static indexes;
- per-note previous/next navigation;
- breadcrumbs;
- last-updated indicators;
- reading-time estimates;
- note tags;
- topic progress indicators;
- full-text search index;
- command palette/search UI;
- favorites/bookmarks stored locally;
- print-friendly note views;
- static sitemap generation;
- JSON-LD/SEO metadata generation;
- Open Graph metadata;
- offline caching/PWA if later desired;
- build-time link checking;
- automatic content statistics;
- GitHub repository release/commit metadata;
- practice/project schemas built on the same content model.

These are enhancements, not reasons to violate the static-first architecture.

---

# 32. Non-Goals

The initial architecture does **not** require:

- a backend server;
- a database;
- authentication;
- CMS software;
- runtime Markdown fetching from GitHub;
- runtime GitHub API calls for essential functionality;
- SSR;
- server-side note storage;
- manual per-note React components.

---

# 33. Definition of Done for the Initial Website

The initial implementation is architecturally complete when:

1. `notes/` follows the defined hierarchy.
2. `notes/notes-tracker.py` can normalize frontmatter without destroying note content.
3. `notes/metadata.json` is generated deterministically.
4. `notes/index.md` is generated from active notes.
5. Numeric prefixes are used only for ordering and are hidden from displayed names/routes.
6. Notes render from Markdown automatically.
7. Note headings generate the right-side overview.
8. Reference Python files appear beside the overview.
9. Reference files can be viewed, copied, and downloaded without a backend.
10. The left topic navigator highlights the current note and can be hidden.
11. `/notes` exposes the nested learning hierarchy.
12. Direct note routes work after refresh on static hosting.
13. The website builds with Vite into a static output directory.
14. Cloudflare Pages can deploy the resulting `dist` output.
15. Agents follow `AGENTS.md` and do not commit website changes before explicit user approval.
16. Visual implementation follows `DESIGN.md` without architectural duplication.

---

# 34. Source References

- Vite — Static Site Deployment: https://vite.dev/guide/static-deploy
- Vite — Production Build: https://vite.dev/guide/build
- Cloudflare Pages — React: https://developers.cloudflare.com/pages/framework-guides/deploy-a-react-site/
- Cloudflare Pages — Serving Pages / SPA Rendering: https://developers.cloudflare.com/pages/configuration/serving-pages/
