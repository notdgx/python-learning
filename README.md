# python-learning

A structured, in-depth technical Python 3.12+ knowledge repository and static web application maintained by **notdgx**.

---

## 📖 Overview

`python-learning` covers Python from low-level execution mechanics, bytecode, memory models, and symbol tables to advanced language paradigms, hands-on projects, and curated practice challenges.

The repository is organized into three content domains and a static presentation website:

- **`notes/`**: Canonical learning notes written in Markdown with embedded Python reference files (`NN-reference-file-K.py`).
- **`practice/`**: Structured practice questions and interview challenges mirroring the exact `notes/` topic hierarchy for automatic bidirectional jumping.
- **`projects/`**: Hands-on CLI utilities, automation scripts, and architectural implementations.
- **`website/`**: Static React + Vite + TypeScript web application compiled for static hosting on Cloudflare Pages.

---

## 🛠️ Architecture & Core Principles

1. **Content First**: Markdown and Python source files are the authoritative source of truth.
2. **Deterministic Ordering**: Numeric ordering prefixes (`NN-`) define sequence while remaining hidden in public display names and routes.
3. **Automated Metadata Pipeline**: `notes/notes-tracker.py` normalizes YAML frontmatter, extracts headings, resolves sibling `.py` reference files, and generates `notes/metadata.json` and `notes/index.md`.
4. **Static Runtime**: Zero runtime backend dependencies, zero API latency; completely statically compilable into `website/dist/`.
5. **Mobile & Accessible**: Dual-mode topic drawer with backdrop blur, React portal-rendered navigation drawers, responsive clamp typography, and full keyboard accessibility.
6. **Connected Theory & Practice**: Files with matching subfolder and slug paths across `notes/` and `practice/` are automatically connected with bidirectional jump links.

---

## 🚀 Getting Started

### 1. Synchronize & Validate Content Metadata
From the repository root:
```bash
# Normalize note frontmatter and regenerate metadata.json + index.md
python3 notes/notes-tracker.py

# Or check content integrity
python3 notes/notes-tracker.py check
```

### 2. Run Website in Development
```bash
cd website
npm install
npm run dev
```
Open `http://localhost:5173/` in your browser.

### 3. Build for Production
```bash
cd website
npm run build
```
The optimized static build output will be generated in `website/dist/`.

### 4. Preview Production Build
```bash
cd website
npm run preview
```

---

## 📚 Documentation & Specifications

- **[ARCHITECTURE.md](website/ARCHITECTURE.md)**: Full technical architecture, data flow, metadata schemas, routing invariants, mobile portal design, and system replication blueprint.
- **[AGENTS.md](website/AGENTS.md)**: Operating rules, content contracts, commit guidelines, and engineering standards for AI agents and contributors.
- **[DESIGN.md](website/DESIGN.md)**: Dark developer design system, typography scales, color palette, component specifications, WebGL shader invariants (`vignette = 0`), and touch interaction patterns.

---

## ⚖️ License & Attribution

Crafted for high-performance developer learning by **notdgx**.  
Copyright &copy; 2026 notdgx. All rights reserved.
