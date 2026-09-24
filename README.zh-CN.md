<p align="center">
  <img src="https://img.shields.io/badge/oss--release--prep-1.0-blue" alt="oss-release-prep 版本">
  <img src="https://img.shields.io/badge/license-MIT-green" alt="许可证">
  <img src="https://img.shields.io/badge/status-stable-success" alt="状态">
</p>

<h1 align="center">oss-release-prep</h1>

<p align="center">
  <strong>开源发布准备与 README 生成</strong>
</p>

<p align="center">
  <a href="./README.md">English</a>
</p>

<p align="center">
  <b>检查 · 补全 · 生成中英双语 README</b>
</p>

---

## 这是什么

`oss-release-prep` 是一个 Codex Skill：把任意项目整理成符合 GitHub 开源要求的状态，并产出规范、详细、中英双语可切换的 README。它把"能不能发布"拆成一个个可验证的检查项，把"写 README"变成一份结构化、以证据为准的文档。

以证据而非直觉为准：每个发布项都被核对并记录；缺失文件、敏感信息、结构问题、License、证据链都会被显式暴露。`git push` / `gh repo create` 等发布动作**绝不**在未获用户明确授权时执行。

## 为什么需要

| 凭直觉（反例） | 本 Skill（正例） |
|---|---|
| "看起来差不多就行" | 每项都有证据（命令输出、文件存在、git 状态） |
| 只写一个 README，内容随意 | 固定结构：徽章 + 结构 + 快速开始 + License + 维护者 |
| 一个文件里中英混排 | 两个独立文件 + 互指的切换链接 |
| 想发就发 | 敏感信息扫描、License 检查、构建/测试验证、发布动作门禁 |

## 功能特点

- **发布检查清单**：对仓库状态、必备文件、README 质量、敏感信息、可验证性逐项核对并记录证据。
- **双语 README**：`README.md`（英文）+ `README.zh-CN.md`（中文），独立文件、互指切换链接、结构镜像。
- **详细文档**：固定大纲（概念、结构、快速开始、配置、集成、FAQ、路线图、贡献指南）。
- **安全**：无真实密钥 / 个人数据 / 绝对路径；发布动作需显式授权。
- **可校验**：自带 `scripts/validate_skill_package.py` 与包契约单测。

## 目录结构

```text
oss-release-prep/
├── SKILL.md                        # 激活入口
├── prompts/oss-release-prep.md     # 完整执行规范
├── agents/openai.yaml              # 可发现元数据
├── references/
│   ├── readme-style.md             # README 结构与详细度基准
│   └── release-checklist.md        # 发布前逐项检查表
├── examples/release-checklist-sample.md
├── evals/
│   ├── eval.yaml
│   └── cases/                      # 成功路径 / 信息缺失 / 边界拦截
├── scripts/validate_skill_package.py
└── tests/test_oss_release_prep.py  # 本地单测（unittest）
```

## 快速开始

**校验本包契约**

```bash
python3 scripts/validate_skill_package.py .
# → PASS: oss-release-prep package contract
```

**运行本地单测**

```bash
python3 -m unittest discover -s tests
```

## 使用方式

把本 Skill 指向一个项目，它会：勘察仓库 → 跑发布检查清单 → 补建缺失工件（LICENSE / .gitignore / .gitattributes / README）→ 生成中英双语 README。交付时报告改了什么、如何验证、产物路径、风险与回滚。

## 许可证

[MIT](./LICENSE)

## 维护者

[xsoway](https://github.com/xsoway) · <xulanzhong521@gmail.com>