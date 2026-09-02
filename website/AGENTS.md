# AGENTS.md — Repository Website Engineering Rules

This file is the operating contract for AI agents working on this repository's website and its content/build integration.

The website is a **static presentation layer** over the learning repository. Agents must preserve that architecture.

---

# 1. Mission

Build and maintain a polished static learning website that presents the repository's Python notes, and later its practice material and projects.

The website must remain:

- static at production runtime;
- content-driven;
- deterministic;
- accessible;
- maintainable;
- consistent with `DESIGN.md`;
- compliant with `ARCHITECTURE.md`;
- safe to regenerate from repository source files.

The repository content is the source of truth. The website must not become the canonical storage location for learning notes.

---

# 2. Read These Files First

Before making any meaningful change, inspect:

```text
README.md
website/ARCHITECTURE.md
website/DESIGN.md
website/AGENTS.md
```

Then inspect the relevant active content under:

```text
notes/
practice/
projects/
```

Do not use archived material as current website content unless the user explicitly asks for it.

---

# 3. Authority Hierarchy

When two instructions appear to conflict, use this priority order:

1. Explicit user request in the current task.
2. Repository architecture in `website/ARCHITECTURE.md`.
3. Current visual requirements in `website/DESIGN.md`.
4. Durable operating rules in this `AGENTS.md`.
5. Existing implementation details.
6. Agent assumptions.

Never let an implementation detail silently override the documented architecture.

---

# 4. Core Repository Model

Treat the repository as:

```text
content source
   ↓
metadata/index generation
   ↓
static website build
   ↓
Cloudflare Pages
```

The current active content structure is:

```text
notes/
├── index.md
├── metadata.json
├── notes-tracker.py
└── NN-topic/
    └── NN-subtopic/
        ├── NN-note.md
        └── NN-reference-file-K.py
```

Projects and practice will use the same philosophy later but are not fully implemented yet.

---

# 5. Never Confuse Archive with Active Content

`archive/` contains old material that the user explicitly wants to preserve without treating it as current learning content.

Agents must:

- never delete archive material merely to “clean up” the project;
- never automatically include archive content in public note navigation;
- never migrate archive files silently;
- never rewrite archived notes when normalizing active-note metadata.

Archive migration requires an explicit user-directed task.

---

# 6. Content Is Not React Code

Do not create one manually maintained React page per Markdown note.

Bad:

```text
src/pages/IntegerPage.tsx
src/pages/FloatPage.tsx
src/pages/StringPage.tsx
```

Preferred:

```text
one reusable note page
        ↓
metadata identifies requested note
        ↓
Markdown content is rendered dynamically from generated/static build data
```

New notes should become visible because content metadata changes, not because an agent writes another page component.

---

# 7. `notes/index.md` Is Generated

`notes/index.md` is a generated navigation manifest.

Agents must not manually patch its generated note entries to fix a navigation issue.

Instead:

1. fix the source directory/file naming or tracker logic;
2. run the tracker;
3. inspect the generated result;
4. build the website;
5. verify the route.

If an intentional manually authored section is ever added to `index.md`, clearly separate it from generated content with a documented marker. Until then, treat the file as fully generated.

---

# 8. `notes/metadata.json` Is Generated

Never hand-edit `notes/metadata.json` to make the website work.

Fix the source or `notes-tracker.py`, then regenerate.

Metadata must remain derived from the current filesystem and note metadata.

Do not store complete Markdown bodies in `metadata.json` unless the architecture is deliberately revised.

---

# 9. Frontmatter Rules

Active Markdown notes may contain YAML frontmatter, but the canonical allowed fields are only:

```yaml
---
date: YYYY-MM-DD
time: HH:MM:SS+TZ
---
```

When maintaining `notes/notes-tracker.py`, ensure that it:

- preserves valid existing `date`;
- preserves valid existing `time`;
- adds missing values;
- removes all other YAML keys;
- does not add a new frontmatter block when one already exists;
- does not rewrite timestamps on every run just because the tracker was executed.

Do not store title, slug, tags, headings, route, or generated hashes in Markdown frontmatter under the current architecture.

Those belong in generated metadata when needed.

---

# 10. Filename and Directory Rules

Active topic/subtopic/note filenames must have a numeric ordering prefix:

```text
NN-name
```

Examples:

```text
00-syntax-and-basics
01-operators
00-integer.md
01-float.md
```

The prefix controls ordering.

The displayed name and public URL must omit the numeric prefix.

Do not silently rename user content solely to make the UI prettier. Rename only when it is required by the content contract and the change is part of the requested task.

---

# 11. Ordering Rules

Ordering is numeric, not lexical.

The parser should understand a variable-width integer prefix, even though the repository convention normally uses two digits.

Examples:

```text
00
01
02
10
11
```

Duplicate sibling order numbers must be treated as a validation error.

Do not invent alphabetical tie-breakers to hide malformed source structure.

---

# 12. Title Rules

By default, display titles come from the filename after removing:

1. the `.md` extension;
2. the leading numeric prefix and hyphen;
3. filename separators such as hyphens/underscores as appropriate.

Example:

```text
00-integer.md
```

becomes:

```text
Integer
```

Do not aggressively title-case acronyms or technical identifiers.

Do not introduce a second title source without updating `ARCHITECTURE.md`.

---

# 13. Reference File Rules

A Python reference file is associated with a note only when it follows the defined naming convention:

```text
NN-reference-file-K.py
```

Example:

```text
00-integer.md
00-reference-file-1.py
00-reference-file-2.py
```

Do not automatically attach every `.py` file in the directory to the note.

Reference files must be:

- discoverable by metadata generation;
- viewable in the note page;
- copyable;
- downloadable using their original filename.

No backend fetch may be required at runtime.

---

# 14. Static-Only Rule

Production code must work as a static site.

Allowed:

- React;
- TypeScript;
- Vite;
- client-side routing;
- client-side state;
- build scripts;
- static JSON/data;
- build-time API requests for non-critical metadata;
- local browser storage for optional preferences.

Not allowed without an explicit architecture change:

- runtime backend;
- database dependency;
- authentication requirement;
- server-side Markdown fetching;
- server-rendered note pages;
- runtime GitHub token usage;
- API-dependent core note rendering.

Node.js is build tooling, not a production runtime requirement.

---

# 15. Vite Rules

The website must remain a Vite project.

Use the Vite production build for deployable output:

```bash
npm run build
```

The deployment artifact should be the generated `dist/` directory unless `vite.config.ts` explicitly defines another documented output directory.

Do not introduce a second competing build system without updating `ARCHITECTURE.md`.

---

# 16. Cloudflare Pages Rules

The intended deployment target is Cloudflare Pages.

The expected production relationship is:

```text
Git repository
   ↓
Cloudflare Pages build
   ↓
npm run build
   ↓
dist
```

Do not add Cloudflare Workers/server functionality merely because Cloudflare supports it. The intended project is static.

SPA deep links must remain functional on Pages.

---

# 17. Website Navigation Contract

The global navbar includes:

```text
Home (Brand Title: python-learning)
Notes
Projects
Practice
Links (Dropdown on desktop, dedicated route /links)
Donate (Clean CTA button — NO currency/rupee logo)
GitHub icon + Repository star badge
Mobile hamburger menu toggle (3 clean SVG lines -> SVG X)
```

The homepage includes a WebGL Ribbon Field hero and a Three.js Emerald Horizon footer (strictly adhering to the **`vignette: 0` zero vignette rule**), with visual details governed by `DESIGN.md`.

Do not remove a navigation item to simplify implementation unless the user explicitly asks for it.

### Mobile Navigation Drawer Rule:
All full-screen mobile menu drawers must be rendered via `createPortal(drawer, document.body)` to avoid clipping and entrapment inside parent containers with CSS `backdrop-filter`.

---

# 18. Notes Page & Responsive Layout Contract

The Notes landing page must expose the nested active topic structure.

Selecting a note must navigate to its actual note route.

### Desktop Layout (`>= 1024px` / `>= 1100px`):
```text
Left (280px)   = sticky topic/navigation panel
Middle         = actual Markdown note content (max-width 820px)
Right (240px)  = in-page Table of Contents + Reference Python files + Practice link
```

### Mobile & Tablet Layout (`< 1024px`):
```text
Left           = off-canvas slide-out drawer (320px max) with backdrop blur, body scroll locking,
                 auto-close on note tap, and a floating 'Topics' pill button when closed.
Middle         = primary reading area with touch-scrollable breadcrumbs,
                 collapsible 'On this page' Table of Contents accordion (< 1100px),
                 and stacked Prev/Next navigation cards.
```

The left region:
- highlights the current note;
- is hideable/collapsible;
- keeps the current branch visible.

The middle region:
- renders Markdown faithfully with Prism syntax highlighting;
- supports formatted code with copy feedback;
- provides horizontal touch scrolling for tables and code blocks.

The right region:
- derives its overview from Markdown headings;
- scrolls smoothly to the selected heading;
- lists reference `.py` files opening the in-page code viewer modal;
- provides direct jump links to related Practice exercises.

---

# 19. Connected Theory & Practice Pairing Contract

The `practice/` domain mirrors the exact same topic and subtopic folder hierarchy as `notes/`:

```text
notes/NN-topic/NN-subtopic/NN-name.md
practice/NN-topic/NN-subtopic/NN-name.md
```

### Pairing Rule:
1. When a practice file exists with the matching slug/name in the same subfolder structure as a note, the system treats them as a **Connected Theory & Practice Pair**.
2. **Note Detail UI**: Must render a prominent "Practice Related Exercises" button in the overview/right panel linking directly to `/practice/<topic>/<subtopic>/<name>`.
3. **Practice UI**: Must render a "View Theory Notes" button linking directly back to `/notes/<topic>/<subtopic>/<name>`.
4. The content tracker must record these bidirectional routes in `metadata.json`.

---

# 20. Markdown Heading Rules

Heading IDs must be deterministic and unique.

Example:

```markdown
## Overview
## Examples
## Overview
```

must produce unique anchor IDs, such as:

```text
overview
overview-2
```

The exact slug algorithm may evolve, but it must remain deterministic within a build.

The right-side overview must preserve heading hierarchy.

Do not include redundant metadata blocks as “headings” unless they are actual Markdown headings.

---

# 20. Code Viewer Rules

Reference code viewers should be reusable components.

Required behavior:

- show original filename;
- syntax highlight Python;
- copy contents;
- download contents;
- remain on the same note route;
- close cleanly;
- be keyboard accessible;
- support long code files.

The downloadable file must contain the actual source text, not rendered HTML.

---

# 21. Search Rules

Search must work without a backend.

Prefer build-generated searchable data over fetching the repository from GitHub at runtime.

Search should eventually cover:

- note title;
- topic/subtopic;
- headings;
- note body text;
- reference filenames when useful.

For performance, do not place the entire repository in one giant browser object unless the collection is demonstrably small.

---

# 22. Accessibility Rules

Every feature must consider keyboard and screen-reader use.

Minimum requirements:

- semantic landmarks;
- keyboard-focusable controls;
- visible focus;
- meaningful labels on icon-only buttons;
- accessible dialogs/overlays;
- no keyboard traps;
- reduced-motion support;
- sufficient contrast;
- responsive reading layout.

Never sacrifice accessibility just to match a visual effect.

---

# 23. Security Rules

Treat Markdown and Python content as input data.

Never:

- execute note code in the browser;
- inject unsanitized HTML from Markdown;
- interpolate filenames directly into trusted HTML without escaping;
- trust user-controlled route parameters without validation;
- allow path traversal outside repository content roots.

Code snippets are for display/download unless a future explicit execution sandbox is designed.

---

# 24. Windows/Linux Compatibility

This repository is expected to be usable across Windows and Linux/WSL workflows.

Use:

- repository-relative paths;
- forward slashes in generated metadata/routes;
- path libraries rather than hard-coded separators;
- UTF-8 file encoding;
- explicit newline handling when necessary.

Do not assume `/` or `\\` when writing Python path logic manually.

---

# 25. Generated Files and Atomicity

When a script generates:

```text
notes/index.md
notes/metadata.json
```

it should, where practical:

1. scan and validate;
2. construct the complete result in memory/temp storage;
3. write the result atomically.

The goal is to avoid leaving corrupted/truncated generated files if the process fails halfway through.

---

# 26. Change Workflow for Content/Architecture

Before changing code:

1. inspect the relevant source structure;
2. identify the authoritative file;
3. check `ARCHITECTURE.md` for constraints;
4. check `DESIGN.md` for visual constraints;
5. make the smallest coherent change;
6. regenerate generated artifacts;
7. run validation/build;
8. inspect the actual result;
9. report what changed.

Do not modify unrelated areas merely because they are nearby.

---

# 27. Definition of “Done” for Website Changes

A website change is not done merely because TypeScript compiles.

For meaningful changes, verify as applicable:

```text
content generation
↓
metadata generation
↓
website build
↓
static preview
↓
route behavior
↓
visual behavior
↓
accessibility basics
```

Check both:

- the source repository;
- the resulting website behavior.

---

# 28. No Silent Destructive Changes

Agents must not:

- delete notes;
- delete archive files;
- rewrite large sets of notes for formatting reasons;
- rename many files without explaining why;
- remove user content because it is unused;
- discard old metadata without a source-of-truth explanation.

Preserve content unless removal is explicitly requested.

---

# 29. Approval Gate Before Commits

**Agents must never create the final website commit merely because their implementation is complete.**

The workflow is:

```text
Agent modifies files
      ↓
Agent validates/builds
      ↓
Agent shows result/status to user
      ↓
User inspects
      ↓
User explicitly approves
      ↓
Commit website changes
```

A user saying that the task is “done,” “looks good,” “approved,” or otherwise explicitly authorizing the finished changes counts as approval.

Until explicit approval is received, do not create the website commit.

---

# 30. Website Commit Naming

Website commits must use the format:

```text
(website-update-N) - <summary>
```

Examples:

```text
(website-update-1) - Initial static notes interface
(website-update-2) - Add Markdown note rendering
(website-update-3) - Add reference code viewer
```

`N` is a monotonically increasing website-update number.

Do not guess a previous number. Inspect Git history and continue the sequence.

The summary should describe the actual approved website change.

---

# 31. Commit Scope

Before an approved website commit:

- inspect `git status`;
- inspect the staged diff;
- ensure unrelated user changes are not accidentally staged;
- include generated files only when they are intended outputs of the change;
- do not stage archive changes unless explicitly requested.

A commit must not contain surprise formatting sweeps or unrelated refactors.

---

# 32. Durable User Preferences

This file is intended to accumulate durable project-specific instructions.

When the user provides a new preference or rule that should apply to future work, agents should:

1. identify whether it is durable rather than task-specific;
2. add a concise rule to this `AGENTS.md` under the most appropriate section;
3. avoid duplicating an existing rule;
4. preserve the user's intent;
5. tell the user that the preference has been incorporated into the agent rules.

Examples of durable preferences:

- navigation conventions;
- naming conventions;
- approval requirements;
- code-quality rules;
- animation behavior;
- recurring interaction preferences;
- preferred development commands.

Do not record secrets, credentials, tokens, or highly personal information.

---

# 33. When Architecture Must Be Updated

Update `ARCHITECTURE.md` when a change affects:

- source-of-truth rules;
- data flow;
- file schemas;
- route conventions;
- build/deployment model;
- generated artifact contracts;
- content hierarchy;
- major component boundaries;
- static-vs-runtime responsibilities.

Do not change architecture documentation merely to describe a small bug fix.

---

# 34. When Design Must Be Updated

Update `DESIGN.md` when a durable visual rule changes, such as:

- typography;
- colors;
- spacing system;
- hero behavior;
- footer behavior;
- responsive layout;
- animation language;
- component appearance;
- interaction visuals.

Do not put visual styling rules into `ARCHITECTURE.md` merely because an agent needs them to implement a component.

---

# 35. Avoid Architecture Drift

Do not introduce a new library merely because it is popular.

Before adding a dependency, ask:

- does the current stack already solve this?
- does it support static output?
- does it increase bundle size significantly?
- does it complicate build-time content handling?
- does it create a runtime backend dependency?
- is it compatible with the repository's architecture?

Prefer the smallest dependency set that gives a strong result.

---

# 36. Preferred Implementation Strategy for Content Integration

The website should consume **typed content models**, not raw filesystem strings scattered across UI components.

Conceptual model:

```ts
Note
├── id
├── title
├── route
├── sourcePath
├── order
├── date
├── time
├── headings[]
├── references[]
└── content
```

React components should receive this model rather than knowing how to parse numeric filename prefixes or discover sibling Python files.

Parsing belongs in content/build utilities.

---

# 37. Keep Parser Logic Centralized

Only a small number of functions should understand filename conventions.

Centralize:

- `parseOrderPrefix()`;
- `displayNameFromPath()`;
- `slugFromPath()`;
- `resolveReferenceFiles()`;
- `normalizeFrontmatter()`;
- `generateHeadingIds()`.

Do not duplicate prefix stripping logic in five different React components.

---

# 38. Error Messages Must Be Actionable

When validation fails, print:

- the exact source path;
- the rule that failed;
- what the agent/user should change.

Bad:

```text
Invalid content
```

Good:

```text
Duplicate note order `02` in:
- notes/00-syntax-and-basics/00-vars/02-string.md
- notes/00-syntax-and-basics/00-vars/02-bool.md

Rename one note so sibling order is unique.
```

---

# 39. Generated Index Semantics

The generated `notes/index.md` should reflect the exact active filesystem state.

The index must:

- include all active topics/subtopics/notes;
- exclude archive content;
- exclude generated helper files;
- hide numeric prefixes;
- preserve numeric ordering;
- be deterministic.

Do not create a second manually maintained navigation tree in the website source.

---

# 40. Content URL Rules

Public note URLs should omit numeric ordering prefixes.

Example:

```text
source:
notes/00-syntax-and-basics/00-variables-and-datatypes/00-integer.md

public route:
/notes/syntax-and-basics/variables-and-datatypes/integer
```

Do not put filesystem paths with `NN-` prefixes into user-visible URLs unless the architecture is explicitly changed.

---

# 41. Renaming and Moving Notes

Treat note moves/renames as content operations, not cosmetic changes.

After any move/rename:

1. regenerate metadata;
2. regenerate index;
3. verify route changes;
4. check internal links;
5. build the site;
6. inspect navigation.

Never leave stale generated references.

---

# 42. GitHub Star Count

The current repository star count is a non-critical enhancement.

Rules:

- it must not block note rendering;
- no secret token may be exposed to the client;
- a failed metadata fetch must have a fallback;
- do not poll GitHub from every browser visit;
- prefer build-time or pre-generated data.

---

# 43. Testing Commands

The exact scripts may evolve, but the intended workflow is:

```bash
# validate/generate content
python notes/notes-tracker.py

# install/build website
npm install
npm run build

# preview production build
npm run preview
```

The tracker may eventually expose explicit subcommands such as:

```bash
python notes/notes-tracker.py check
python notes/notes-tracker.py normalize
python notes/notes-tracker.py generate
```

If implemented, document them in the tracker itself and keep their behavior deterministic.

---

# 44. Do Not Depend on Runtime GitHub Content

The website must remain usable if GitHub is down after deployment.

Therefore:

- note content must be packaged into the static build;
- navigation must be packaged into the static build;
- reference Python files must be packaged into the static build;
- the site must not fetch raw Markdown from GitHub at runtime for core pages.

External links are fine; core note rendering must be local to the built site.

---

# 45. Offline/No-Network Principle

After a successful production build, the website's core content should work without internet access, apart from intentionally external services such as external links or optional live metadata.

This is a useful architectural test:

```text
Build complete
↓
disconnect network
↓
serve dist/
↓
Notes should still render
```

---

# 46. Visual Changes Require Real Inspection

For UI work, do not assume that successful compilation means the design is correct.

Inspect the rendered result and verify:

- spacing;
- overflow;
- typography;
- mobile behavior;
- topic panel behavior;
- overview alignment;
- code viewer usability;
- footer/hero integrity.

Follow `DESIGN.md` rather than inventing a different style language.

---

# 47. Avoid Hidden State Bugs

The route is the source of truth for which note is open.

Do not make the selected note depend only on a React state variable that disappears on refresh.

Optional UI state such as sidebar collapsed/open can be local state or local storage, but it must not change the note identity.

---

# 48. Responsive Rules

On smaller screens, the three-column note layout may collapse into a staged/mobile layout, but all information must remain accessible.

At minimum:

- note content remains primary;
- topic navigation becomes an accessible drawer/sheet/section;
- overview remains reachable;
- reference files remain reachable;
- no horizontal page overflow is introduced.

Exact visual breakpoints belong in `DESIGN.md`.

---

# 49. Future Practice and Projects

Do not prematurely build a complete practice/projects system.

However, new website code should avoid naming everything specifically around `notes` when a general content abstraction is cheap and clear.

Prefer:

```text
ContentSection
```

over deeply hard-coded logic such as:

```text
if path starts with /notes everywhere
```

Keep the first implementation simple while preserving this extension point.

---

# 50. Final Agent Checklist

Before presenting a completed implementation:

```text
[ ] Read AGENTS.md
[ ] Read ARCHITECTURE.md
[ ] Read DESIGN.md
[ ] Identify source-of-truth files
[ ] Do not modify archive content unnecessarily
[ ] Keep static production architecture
[ ] Keep Vite + React + TypeScript
[ ] Keep numeric-prefix ordering semantics
[ ] Keep NN- hidden from display/routes
[ ] Keep frontmatter limited to date/time
[ ] Regenerate index/metadata from source
[ ] Validate route collisions
[ ] Validate reference files
[ ] Validate heading IDs
[ ] Build successfully
[ ] Inspect rendered website
[ ] Check responsive behavior where relevant
[ ] Check accessibility basics
[ ] Inspect git diff/status
[ ] Do NOT commit until user explicitly approves
[ ] After approval use (website-update-N) - ...
[ ] Add new durable preferences to AGENTS.md when appropriate
```

---

# 51. Current Project Boundary

At the current stage, the agent's primary implementation scope is:

```text
notes/
website/
```

The intended next major implementation is `notes/notes-tracker.py`, followed by the Vite/React website implementation.

Practice/projects behavior is intentionally deferred.

---

# 52. Governing Rule

When in doubt:

> Preserve the repository's content, keep the website statically buildable, derive website state from source content, obey `ARCHITECTURE.md` and `DESIGN.md`, and wait for explicit user approval before committing website changes.

---

# 53. Build & Operational Commands

Always use these standard commands:

```bash
# Normalize and synchronize note metadata (from repo root)
python3 notes/notes-tracker.py normalize

# Check metadata integrity (from repo root)
python3 notes/notes-tracker.py check

# Build static production bundle into website/dist/
cd website && npm run build

# Preview static build locally
cd website && npm run preview
```

### Authoritative Animation Invariants:
1. Hero: Ribbon Field WebGL (`RibbonFieldBackground`) with continuous slow hue cycling and pointer drift.
2. Footer: Emerald Horizon Three.js (`EmeraldHorizonBackground`) with synchronized hue cycling and **`vignette = 0` (zero vignette rule)**.
3. Both animations preserve aspect ratio (`object-fit: cover` logic with crop, never stretching/distorting).


