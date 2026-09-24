<p align="center">
  <img src="https://img.shields.io/badge/oss--release--prep-1.0-blue" alt="oss-release-prep version">
  <img src="https://img.shields.io/badge/license-MIT-green" alt="license">
  <img src="https://img.shields.io/badge/status-stable-success" alt="status">
</p>

<h1 align="center">oss-release-prep</h1>

<p align="center">
  <strong>Open-source release prep & README generation</strong>
</p>

<p align="center">
  <a href="./README.zh-CN.md">中文</a>
</p>

<p align="center">
  <b>Check · Prepare · Generate bilingual README</b>
</p>

---

## What is it

`oss-release-prep` is a Codex Skill that prepares any project for open-source release on GitHub and generates a well-structured, detailed, bilingual (English + Chinese) README. It turns "is it publishable?" into a checklist of verifiable items, and turns "write a README" into a structured, evidence-driven document.

Evidence over instinct: every release item is checked and recorded; missing files, sensitive info, structural issues, License, and evidence chains are surfaced explicitly. Publishing actions (`git push`, `gh repo create`) are never executed without explicit user authorization.

## Why

| Instinct (anti-pattern) | This skill |
|---|---|
| "Looks about right" | Every item has evidence (command output, file existence, git state) |
| One README, any content | Fixed structure: badges + structure + quick start + license + maintainer |
| Single mixed-language file | Two independent files with working switch links |
| Publish on a whim | Sensitive-info scan, License check, build/test verification, explicit action gating |

## Features

- **Release checklist**: structured, evidence-backed check of repo state, required files, README quality, sensitive info, and verifiability.
- **Bilingual README**: `README.md` (English) + `README.zh-CN.md` (Chinese), independent files, cross-referenced switch links, mirrored structure.
- **Detailed docs**: follows a fixed outline (concepts, structure, quick start, config, integrations, FAQ, roadmap, contributing).
- **Safety**: no real secrets / personal data / absolute paths; publishing actions require explicit authorization.
- **Validatable**: ships `scripts/validate_skill_package.py` and a unit test for its own package contract.

## Structure

```text
oss-release-prep/
├── SKILL.md                        # activation entry
├── prompts/oss-release-prep.md     # full execution spec
├── agents/openai.yaml              # discovery metadata
├── references/
│   ├── readme-style.md             # README structure & detail baseline
│   └── release-checklist.md        # per-item release checklist
├── examples/release-checklist-sample.md
├── evals/
│   ├── eval.yaml
│   └── cases/                      # basic-success / edge-incomplete / edge-scope-boundary
├── scripts/validate_skill_package.py
└── tests/test_oss_release_prep.py  # local unit tests (unittest)
```

## Quick Start

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

Point the skill at a project and it will: survey the repository, run the release checklist, create missing artifacts (LICENSE / .gitignore / .gitattributes / README), and generate bilingual READMEs. Report what changed, how to verify, artifact paths, and risks.

## License

[MIT](./LICENSE)

## Maintainer

[xsoway](https://github.com/xsoway) · <xulanzhong521@gmail.com>