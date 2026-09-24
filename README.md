<p align="center">
  <img src="https://img.shields.io/badge/oss--release--prep-1.0-blue" alt="oss-release-prep version">
  <img src="https://img.shields.io/badge/license-MIT-green" alt="license">
  <img src="https://img.shields.io/badge/status-stable-success" alt="status">
  <img src="https://img.shields.io/badge/bilingual-EN%20%E4%B8%AD%20ZH-orange" alt="bilingual EN+ZH">
</p>

<h1 align="center">oss-release-prep</h1>

<p align="center">
  <strong>Open-source release prep &amp; bilingual README generation</strong>
</p>

<p align="center">
  <a href="./README.zh-CN.md">中文</a>
</p>

<p align="center">
  <b>Check · Prepare · Generate bilingual README · Publish gate</b>
</p>

---

## Table of Contents

- [What is it](#what-is-it)
- [Why](#why)
- [Core Concepts](#core-concepts)
- [Features](#features)
- [Structure](#structure)
- [Quick Start](#quick-start)
- [Usage](#usage)
- [Release Checklist (A–K)](#release-checklist-a--k)
- [Safety & Design Principles](#safety--design-principles)
- [Validating & Testing](#validating--testing)
- [FAQ](#faq)
- [Roadmap](#roadmap)
- [Contributing](#contributing)
- [License](#license)
- [Maintainer](#maintainer)

## What is it

`oss-release-prep` is a **Codex Skill** that prepares any project for open-source release on GitHub and generates a well-structured, detailed, **bilingual (English + Chinese) README**. It turns *"is it publishable?"* into a checklist of verifiable items, and turns *"write a README"* into a structured, evidence-driven document.

**Evidence over instinct:** every release item is checked and recorded; missing files, sensitive info, structural issues, License, and evidence chains are surfaced explicitly. Publishing actions (`git push`, `gh repo create`) are **never** executed without explicit user authorization.

## Why

Publishing to GitHub seems trivial, but a naive pass leaves real risks behind. This skill replaces common instincts with verifiable discipline:

| Instinct (anti-pattern) | This skill |
|---|---|
| "Looks about right" | Every item has evidence (command output, file existence, git state) |
| One README, any content | Fixed structure: badges + ToC + structure + quick start + license + maintainer |
| Single mixed-language file | Two independent files with working switch links |
| Publish on a whim | Sensitive-info scan, License check, build/test verification, explicit action gating |
| Leaves out assets/topics | Release artifacts, About/topics, Discussions, and a project homepage |

## Core Concepts

- **Evidence chain**: a check passes only when backed by a citable fact (command output, file existence, git state, code location). Unsupported claims count as *not passing*, and the next step is recorded.
- **Secret red line (hard block)**: API keys (`sk-…`, `ghp_…`, `AKIA…`), tokens, cookies, private keys, passwords, personal data, and absolute local paths (host-specific paths like `~/…#HOME…`) must **never** be published. Any hit **immediately aborts the release**; this applies even when nothing has been pushed yet.
- **Dual-file bilingual README**: `README.md` (English) + `README.zh-CN.md` (Chinese) are independent files with mirrored structure and cross-referenced switch links. No mixed-language files.
- **Gated publishing**: promotion actions (`git push`, `gh repo create`, overwriting live content) run only with explicit user authorization; otherwise the skill reports them as unexecuted and gives the exact command to run.
- **Verification tiers**: static checks, structural validation, actual runs, and publishing actions are reported separately; anything not executed is labeled as such rather than assumed to pass.

## Features

- **Release checklist (A–K)**: structured, evidence-backed check of repo state (A), required files (B), README quality (C), sensitive info (D), verifiability (E), action gate (F), discoverability (G), homepage (H), community ops (I), release assets (J), and release quality gate (K).
- **Bilingual README**: `README.md` (English) + `README.zh-CN.md` (Chinese), independent files, cross-referenced switch links, mirrored structure.
- **Detailed docs**: follows a fixed outline (concepts, structure, quick start, config, integrations, FAQ, roadmap, contributing).
- **Artifact repair**: creates or fixes missing `LICENSE`, `.gitignore`, `.gitattributes`, missing README sections, badges, and structure descriptions.
- **Publish discoverability**: configures a one-line `About` description, GitHub `topics` (e.g. `ai`, `llm`, `skill`, `persona`, `self-memory`), and GitHub Discussions.
- **Project homepage**: optional gruvbox-material black-and-gold `index.html` with built-in EN ⇄ 中文 switching, linkable from the repository `About`. Style / interaction / content-layout follow the reference site https://xsoway.github.io/obsidian-ai-vault-scaffold/ (full spec + mandatory headless-browser self-test after generation in SKILL.md「项目主页（index.html）规范」).
- **Release assets**: instructs attaching downloadable build artifacts (e.g. `uv build` sdist + wheel) to a release, and verifying them with `gh release view`.
- **Release quality gate**: after updating governance tools, runs one external-reviewer code review before publishing.
- **Safety**: no real secrets / personal data / absolute paths; publishing actions require explicit authorization.
- **Validatable**: ships `scripts/validate_skill_package.py` and a unit test for its own package contract.
- **Evaluated**: ships `evals/` with three rule-based cases (basic success / incomplete input / scope-boundary) to lock in expected behavior.

## Structure

```text
oss-release-prep/
├── SKILL.md                        # activation entry (frontmatter + rules)
├── prompts/oss-release-prep.md     # full execution spec
├── agents/openai.yaml              # discovery metadata
├── references/
│   ├── readme-style.md             # README structure & detail baseline
│   └── release-checklist.md        # per-item release checklist (A–K, hard-block section D)
├── examples/release-checklist-sample.md   # sample checklist output (no real secrets)
├── evals/
│   ├── eval.yaml
│   └── cases/                      # basic-success / edge-incomplete-input / edge-scope-boundary
├── scripts/validate_skill_package.py
└── tests/test_oss_release_prep.py  # local unit tests (unittest)
```

| Path | Responsibility |
|---|---|
| `SKILL.md` | Activation entry; describes when to use, output formats, workflow, README spec, pitfalls, best practices. |
| `prompts/oss-release-prep.md` | Full execution spec: input, secret red line, survey → checklist → repair → generate flow, quality requirements. |
| `agents/openai.yaml` | Discovery metadata used by agent runtimes to auto-suggest the skill. |
| `references/readme-style.md` | Baseline for README structure and detail level. |
| `references/release-checklist.md` | The A–K checklist; section D is the publish hard block. |
| `examples/release-checklist-sample.md` | A representative checklist output to disambiguate expected format. |
| `evals/` | Rule-based evaluation harness: one success case, two edge cases. |
| `scripts/validate_skill_package.py` | Static contract validation + secret/absolute-path scan. |
| `tests/test_oss_release_prep.py` | Local unit tests (unittest) guarding the package contract. |

## Quick Start

**Requirements:** Python 3, no third-party dependencies.

**Validate this package's contract**

```bash
python3 scripts/validate_skill_package.py .
# → PASS: oss-release-prep package contract
```

**Run the local unit tests**

```bash
python3 -m unittest discover -s tests
```

## Usage

Point the skill at a project and it will:

1. **Survey** the repository — directory structure, build/test commands, dependencies and runtime, git state, existing README / License / ignore rules, and any sensitive files.
2. **Run the release checklist** — verify every item against `references/release-checklist.md` and record evidence.
3. **Repair missing artifacts** — create or fix `LICENSE`, `.gitignore`, `.gitattributes`, missing README sections, badges, and structure descriptions.
4. **Generate bilingual READMEs** — `README.md` (EN) + `README.zh-CN.md` (ZH), mirrored structure, cross-referenced switch links.
5. **Promote discoverability** (optional) — About description, topics, GitHub Discussions, and a gruvbox-material bilingual homepage modeled on https://xsoway.github.io/obsidian-ai-vault-scaffold/; run a headless-browser interaction self-test after generating.
6. **Build release assets** (optional) — `uv build` sdist/wheel attached as release assets; external-reviewer code review as a quality gate.
7. **Deliver** — report what changed, how to verify, artifact paths, risks/rollback, and the secret-scan result as an explicit evidence item.

Publishing actions (`git push`, `gh repo create`) are only run when you explicitly authorize them; otherwise the skill hands you the exact commands to run.

## Release Checklist (A–K)

Each item requires evidence (command output, file existence, git state, code location). Missing evidence means *not passing*.

| Section | Concern | Highlights |
|---|---|---|
| **A** | Repository state | `git init` + commits, default branch, no tracked secrets. |
| **B** | Required files | `README.md`, `README.zh-CN.md`, `LICENSE`, `.gitignore`, `.gitattributes`. |
| **C** | README quality | Badges + positioning + ToC + quick start + structure/usage + license + maintainer; commands must run. |
| **D** | Sensitive-info scan (red line) | No API keys / tokens / cookies / private keys / personal data / absolute local paths. **Hit ⇒ block release.** |
| **E** | Verifiability | Build/test commands run and pass (or reason recorded); deps and install steps documented. |
| **F** | Action gate | `git push` / `gh repo create` only on explicit request; unexecuted actions reported. |
| **G** | Discoverability | One-line `About`, topics (`ai`, `llm`, `skill`, `persona`, `self-memory`), verified via `gh repo view`. |
| **H** | Project homepage | gruvbox-material black-and-gold `index.html`, built-in EN ⇄ 中文 switch, linked from `About`. Style/layout/interactions follow https://xsoway.github.io/obsidian-ai-vault-scaffold/; headless-browser self-test after generation. |
| **I** | Community ops | GitHub Discussions enabled with at least one category; Q&A/contribution entry points to it. |
| **J** | Release assets | `uv build` sdist/wheel attached to the release; verified via `gh release view`. |
| **K** | Release quality gate | Governance tools clean (`make-code-clean`, `code-review-graph`); external-reviewer review after tool updates. |

## Safety & Design Principles

- **Secret red line is first and highest.** It outranks every other rule and is not exempted because code is not yet pushed.
- **No placeholder-forging**: samples never "disguise" a real key by changing a few characters; they use meaningless placeholders (`sk-YOUR_KEY_HERE`, `<token>`) that are not isomorphic to real values.
- **Evidence over instinct** — supported claims only; anything unverified is labeled.
- **No fabricated content** — tech stack, build/test commands, and dependencies come from this project, never borrowed or invented.
- **Bilingual consistency** — the two READMEs cover the same topics with mirrored structure; commands, tree, and badges may be shared, prose is written independently.
- **Explicit authorization for publishing actions**.
- **Verification tiers are never conflated** — static check ≠ published ≠ behavior verified.

## Validating & Testing

- Package contract + secret/absolute-path scan:
  ```bash
  python3 scripts/validate_skill_package.py .
  ```
- Local unit tests:
  ```bash
  python3 -m unittest discover -s tests
  ```
- Evaluation harness (three rule-based cases): `evals/eval.yaml` with cases `basic-success`, `edge-incomplete-input`, `edge-scope-boundary`.

## FAQ

**Does it run `git push` or create a repo by itself?**
No. Publishing actions require your explicit authorization. If not authorized, the skill reports them as unexecuted and prints the exact commands.

**Does it handle only Python projects?**
No. The checklist applies to any repo; release-asset commands (`uv build`) are Python-specific examples, and non-Python projects use equivalent artifacts (binaries, JS bundles, container images).

**What happens if a secret is found?**
Anything on the red line aborts the release immediately: remove the secret, rotate leaked credentials, purge git history (e.g. `git filter-repo`), then re-scan until zero hits before continuing.

**Why two README files instead of one mixed file?**
Two independent files with mirrored structure and cross-referenced switch links. GitHub also auto-detects `README.zh-CN.md` as a language variant and shows a switch tab on the repo home page.

**My project is tiny. Do I need every section?**
No. The default is the detailed version, but sections are kept or dropped based on the project. The baseline and two detail levels are described in `references/readme-style.md`.

## Roadmap

- [x] Evidence-backed release checklist (A–K) with hard-block secret scan
- [x] Dual-file bilingual README generation with mirrored structure
- [x] Artifact repair: LICENSE / .gitignore / .gitattributes / README sections
- [x] Publish discoverability: About, topics, GitHub Discussions
- [x] gruvbox-material bilingual project homepage (`index.html`)
- [x] Release assets guidance (`uv build` sdist/wheel) and release quality gate
- [x] Package contract validator + unit tests + rule-based eval cases
- [ ] Broader third-party `gh`/release automation templates
- [ ] Additional language variants beyond EN + ZH

## Contributing

Pull requests welcome. Before opening one, verify your change keeps the package contract green:

```bash
python3 scripts/validate_skill_package.py .
python3 -m unittest discover -s tests
```

Please follow the skill's own evidence rule: describe what changed, how it was verified, and any risks. Never place real secrets, personal data, or absolute local paths in any file.

## License

[MIT](./LICENSE)

## Maintainer

[xsoway](https://github.com/xsoway) · <xulanzhong521@gmail.com>