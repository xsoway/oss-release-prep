<p align="center">
  <img src="https://img.shields.io/badge/oss--release--prep-1.0-blue" alt="oss-release-prep 版本">
  <img src="https://img.shields.io/badge/license-MIT-green" alt="许可证">
  <img src="https://img.shields.io/badge/status-stable-success" alt="状态">
  <img src="https://img.shields.io/badge/bilingual-EN%20%E4%B8%AD%20ZH-orange" alt="中英双语 EN+ZH">
</p>

<h1 align="center">oss-release-prep</h1>

<p align="center">
  <strong>开源发布准备与中英双语 README 生成</strong>
</p>

<p align="center">
  <a href="./README.md">English</a>
</p>

<p align="center">
  <b>检查 · 补全 · 生成中英双语 README · 发布门禁</b>
</p>

---

## 目录

- [这是什么](#这是什么)
- [为什么需要](#为什么需要)
- [核心概念](#核心概念)
- [功能特点](#功能特点)
- [目录结构](#目录结构)
- [快速开始](#快速开始)
- [使用方式](#使用方式)
- [发布检查清单（A–K）](#发布检查清单ak)
- [安全边界与设计原则](#安全边界与设计原则)
- [校验与测试](#校验与测试)
- [常见问题（FAQ）](#常见问题faq)
- [路线图](#路线图)
- [贡献指南](#贡献指南)
- [许可证](#许可证)
- [维护者](#维护者)

## 这是什么

`oss-release-prep` 是一个 **Codex Skill**：把任意项目整理成符合 GitHub 开源要求的状态，并产出规范、详细、**中英双语可切换**的 README。它把"能不能发布"拆成一个个可验证的检查项，把"写 README"变成一份结构化、以证据为准的文档。

**以证据而非直觉为准**：每个发布项都被核对并记录；缺失文件、敏感信息、结构问题、License、证据链都会被显式暴露。`git push` / `gh repo create` 等发布动作**绝不**在未获用户明确授权时执行。

## 为什么需要

发布到 GitHub 看似简单，但凭感觉走一遍会留下真实风险。本 Skill 用可验证的纪律替代常见直觉：

| 凭直觉（反例） | 本 Skill（正例） |
|---|---|
| "看起来差不多就行" | 每项都有证据（命令输出、文件存在、git 状态） |
| 只写一个 README，内容随意 | 固定结构：徽章 + 目录 + 结构 + 快速开始 + License + 维护者 |
| 一个文件里中英混排 | 两个独立文件 + 互指的切换链接 |
| 想发就发 | 敏感信息扫描、License 检查、构建/测试验证、发布动作门禁 |
| 漏掉产物与其他推广位 | 发布产物、About/topics、Discussions、项目主页 |

## 核心概念

- **证据链**：一个检查项只有被可引用事实（命令输出、文件存在、git 状态、代码位置）支撑才算通过；无依据的"应该没问题"视为未通过，并记录下一步。
- **敏感信息红线（硬阻断）**：API key（`sk-…`、`ghp_…`、`AKIA…`）、token、cookie、私钥、密码、个人数据、绝对本机路径**严禁**公开。任一命中**立即中止发布**；即使尚未推送也不豁免。
- **双语双文件 README**：`README.md`（英文）+ `README.zh-CN.md`（中文）独立成文、结构镜像、切换链接互指；禁止单个文件内中英混排。
- **门禁式发布**：推广动作（`git push`、`gh repo create`、覆盖线上内容）仅在用户显式授权时执行；否则如实报告"未执行"并给出可复制的命令。
- **验证分层**：静态检查、结构校验、实际运行、发布动作分别报告；任何未执行的一步都如实标注，不被当作"已通过"。

## 功能特点

- **发布检查清单（A–K）**：对版本库状态（A）、必备文件（B）、README 质量（C）、敏感信息（D）、可验证性（E）、动作门禁（F）、可发现性（G）、主页（H）、社区运营（I）、发布产物（J）、发布质量门禁（K）逐项核对并记录证据。
- **双语 README**：`README.md`（英文）+ `README.zh-CN.md`（中文），独立文件、互指切换链接、结构镜像。
- **详细文档**：固定大纲（概念、结构、快速开始、配置、集成、FAQ、路线图、贡献指南）。
- **补齐工件**：按需创建/修复 `LICENSE`、`.gitignore`、`.gitattributes`、缺失的 README 章节、徽章与结构说明。
- **发布可发现性**：配置一行定位的 `About`、GitHub `topics`（如 `ai`、`llm`、`skill`、`persona`、`self-memory`）与 GitHub Discussions。
- **项目主页**：可选的 gruvbox-material 黑金风格 `index.html`，内置中英切换，可从仓库 `About` 链接访问。
- **发布产物**：指导把可下载构建产物（如 `uv build` 的 sdist + wheel）附到 release，并用 `gh release view` 验证。
- **发布质量门禁**：更新监管工具后，先做一次外部 reviewer 代码审查再发布。
- **安全**：无真实密钥 / 个人数据 / 绝对路径；发布动作需显式授权。
- **可校验**：自带 `scripts/validate_skill_package.py` 与包契约单测。
- **可评测**：带 `evals/` 三个基于规则的用例（成功路径 / 信息缺失 / 边界拦截），锁定预期行为。

## 目录结构

```text
oss-release-prep/
├── SKILL.md                        # 激活入口（frontmatter + 规则）
├── prompts/oss-release-prep.md     # 完整执行规范
├── agents/openai.yaml              # 可发现元数据
├── references/
│   ├── readme-style.md             # README 结构与详细度基准
│   └── release-checklist.md        # 发布前逐项检查表（A–K，D 节为硬阻断）
├── examples/release-checklist-sample.md   # 检查清单输出样例（不含真实密钥）
├── evals/
│   ├── eval.yaml
│   └── cases/                      # basic-success / edge-incomplete-input / edge-scope-boundary
├── scripts/validate_skill_package.py
└── tests/test_oss_release_prep.py  # 本地单测（unittest）
```

| 路径 | 职责 |
|---|---|
| `SKILL.md` | 激活入口；说明何时使用、输出格式、工作流、README 规范、常见误区、最佳实践。 |
| `prompts/oss-release-prep.md` | 完整执行规范：输入、敏感信息红线、勘察→检查→补齐→生成流程、质量要求。 |
| `agents/openai.yaml` | 供 Agent 运行时自动推荐的发现元数据。 |
| `references/readme-style.md` | README 结构与详细度基准。 |
| `references/release-checklist.md` | A–K 逐项检查表；D 节为发布硬阻断。 |
| `examples/release-checklist-sample.md` | 代表性检查清单输出，澄清预期格式。 |
| `evals/` | 基于规则的评测 harness：一个成功用例、两个边界用例。 |
| `scripts/validate_skill_package.py` | 静态契约校验 + 密钥/绝对路径扫描。 |
| `tests/test_oss_release_prep.py` | 本地单测（unittest），守护包契约。 |

## 快速开始

**环境要求：** Python 3，无第三方依赖。

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

把本 Skill 指向一个项目，它会：

1. **勘察仓库**——目录结构、构建/测试命令、依赖与运行环境、git 状态、现有 README / License / 忽略规则、是否存在敏感文件。
2. **跑发布检查清单**——按 `references/release-checklist.md` 逐项核对并记录证据。
3. **补齐缺失工件**——按需创建/修复 `LICENSE`、`.gitignore`、`.gitattributes`、缺失的 README 章节、徽章与结构说明。
4. **生成中英双语 README**——`README.md`（英）+ `README.zh-CN.md`（中），结构镜像、切换链接互指。
5. **提升可发现性**（可选）——About 描述、topics、GitHub Discussions、gruvbox-material 双语主页。
6. **构建发布产物**（可选）——`uv build` 的 sdist/wheel 附为 release assets；更新监管工具后做一次外部 reviewer 代码审查作为质量门禁。
7. **交付**——报告改了什么、如何验证、产物路径、风险/回滚，并把敏感信息扫描结果作为独立证据项。

发布动作（`git push`、`gh repo create`）仅在您显式授权时执行；否则本 Skill 把可复制的命令交给您运行。

## 发布检查清单（A–K）

每一项都需要证据（命令输出、文件存在、git 状态、代码位置）；缺证据即视为未通过。

| 节 | 关注点 | 要点 |
|---|---|---|
| **A** | 版本库状态 | `git init` + 已提交、默认分支、无被跟踪的敏感文件。 |
| **B** | 必备文件 | `README.md`、`README.zh-CN.md`、`LICENSE`、`.gitignore`、`.gitattributes`。 |
| **C** | README 质量 | 徽章 + 定位 + 目录 + 快速开始 + 结构/用法 + License + 维护者；命令要能跑通。 |
| **D** | 敏感信息扫描（红线） | 无 API key / token / cookie / 私钥 / 个人数据 / 绝对本机路径。**命中即阻断发布。** |
| **E** | 可验证性 | 构建/测试命令已运行并通过（或记录原因）；依赖与安装步骤有据可查。 |
| **F** | 动作门禁 | `git push` / `gh repo create` 仅在显式要求时执行；未授权动作如实报告。 |
| **G** | 可发现性 | 一行 `About`、topics（`ai`、`llm`、`skill`、`persona`、`self-memory`），用 `gh repo view` 验证。 |
| **H** | 项目主页 | gruvbox-material 黑金风格 `index.html`，内置中英切换，`About` 提供链接。 |
| **I** | 社区运营 | 启用 GitHub Discussions 且至少一个类别；提问/贡献入口指向它。 |
| **J** | 发布产物 | `uv build` 的 sdist/wheel 附到 release，用 `gh release view` 验证。 |
| **K** | 发布质量门禁 | 监管工具清理干净（`make-code-clean`、`code-review-graph`）；更新工具后做外部 reviewer 代码审查。 |

## 安全边界与设计原则

- **敏感信息红线居首且最高**——优先于其它所有规则；不因"尚未推送"而豁免。
- **绝不占位伪造**——示例绝不用"改几个字符的真实密钥"冒充；一律用无意义占位符（`sk-YOUR_KEY_HERE`、`<token>`），且不与真实值同构。
- **以证据为准**——只写有依据的结论；未验证项如实标注。
- **不虚构内容**——技术栈、构建/测试命令、依赖均以本项目为准，不外借、不编造。
- **双语一致**——两版覆盖同一组主题、结构镜像；命令、目录树、徽章可共享，叙述各自独立成文。
- **发布动作显式授权**。
- **验证分层不被混淆**——静态检查 ≠ 已发布 ≠ 已验证行为。

## 校验与测试

- 包契约 + 密钥/绝对路径扫描：
  ```bash
  python3 scripts/validate_skill_package.py .
  ```
- 本地单测：
  ```bash
  python3 -m unittest discover -s tests
  ```
- 评测 harness（三个基于规则的用例）：`evals/eval.yaml`，用例 `basic-success`、`edge-incomplete-input`、`edge-scope-boundary`。

## 常见问题（FAQ）

**它会自己 `git push` 或建仓库吗？**
不会。发布动作需要您的显式授权；未授权时如实报告"未执行"并给出可复制的命令。

**只支持 Python 项目吗？**
不是。检查清单适用于任意仓库；发布产物命令（`uv build`）是 Python 示例，非 Python 项目改用等价产物（二进制、JS bundle、容器镜像等）。

**发现密钥会怎样？**
红线命中即中止发布：先移除密钥、轮换已泄露凭据、用 `git filter-repo` 等清除 git 历史，重扫零命中后再继续。

**为什么是两个 README 而不是一个文件混排？**
两个独立文件、结构镜像、切换链接互指。GitHub 会自动把 `README.zh-CN.md` 识别为语言变体，仓库首页出现切换 tab。

**我的项目很小，需要全部章节吗？**
不需要。默认产出详尽版，但章节按项目实际情况取舍；基准与两个详细度级别见 `references/readme-style.md`。

## 路线图

- [x] 带硬阻断密钥扫描的证据化发布检查清单（A–K）
- [x] 结构镜像的双文件中英 README 生成
- [x] 工件补齐：LICENSE / .gitignore / .gitattributes / README 章节
- [x] 发布可发现性：About、topics、GitHub Discussions
- [x] gruvbox-material 中英双语项目主页（`index.html`）
- [x] 发布产物指引（`uv build` sdist/wheel）与发布质量门禁
- [x] 包契约校验器 + 单测 + 基于规则的评测用例
- [ ] 更丰富的第三方 `gh` / release 自动化模板
- [ ] 除中英外更多语言变体

## 贡献指南

欢迎提交 Pull Request。提交前请确保包契约保持绿色：

```bash
python3 scripts/validate_skill_package.py .
python3 -m unittest discover -s tests
```

请遵循本 Skill 自己的证据规则：说明改了什么、如何验证、有何风险；任何文件都不得放入真实密钥、个人数据或绝对本机路径。

## 许可证

[MIT](./LICENSE)

## 维护者

[xsoway](https://github.com/xsoway) · <xulanzhong521@gmail.com>