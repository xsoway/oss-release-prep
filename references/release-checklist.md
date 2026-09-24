# 发布前逐项检查表

推送前逐项确认；每一项都要有证据（命令输出、文件存在、git 状态、代码位置）。缺证据即视为未通过，如实标注并给出下一步。

> **发布红线（HARD BLOCK）**：敏感信息（API key / token / cookie / 私钥 / 个人数据 / 绝对本机路径）严禁公开。任一检查命中即**中止发布**，先移除/轮换，再谈其余项。公开后无法安全撤回——轮换密钥、强制重写历史都不能保证清除。

## A. 版本库状态

- [ ] 项目已 `git init` 且已提交（`git log` 有提交记录）。
- [ ] 明确默认分支（`main`），本地与远程跟踪关系正确（`git status -sb`）。
- [ ] 无未提交的敏感文件被跟踪（凭据、`.env`、私钥、构建产物）。

## B. 必备文件

- [ ] `README.md`（英文版）存在。
- [ ] `README.zh-CN.md`（中文版，如需双语）存在，切换链接互指正确。
- [ ] `LICENSE` 存在且选择了 License（MIT / Apache-2.0 / GPL…），版权年份与作者正确。
- [ ] `.gitignore` 排除运行产物、IDE 文件、OS 文件、密钥。
- [ ] `.gitattributes`（可选）统一行尾（`* text=auto eol=lf`）。

## C. README 质量

- [ ] 结构：徽章 + 定位 + 目录 + 快速开始 + 结构/用法 + License + 维护者（按 `references/readme-style.md`）。
- [ ] 快速开始里每个命令有依据且能跑通（已实际运行并获得预期输出）。
- [ ] 目录树、配置项、功能描述与代码一致，无过时/虚构内容。
- [ ] 双语两版信息一致，覆盖同一组主题。

## D. 敏感信息扫描（发布红线）

**严禁公开**：任何 API key、token、cookie、私钥、密码、个人数据、绝对本机路径一旦进入即将开源的文件，一律视为发布阻断。

- [ ] 无真实 API key / token / cookie / 私钥 / 密码（`sk-…`、`sk-proj-…`、`sk-ant-…`、`ghp_…`、`xox…`、`AKIA…`、`authorization:`、`api key`、`api_key`、`secret`、`bearer …`、`BEGIN … PRIVATE KEY`）。
- [ ] 无模型默认凭据 / 示例密钥 / `key = "…values…"` 高熵占位疑似值。
- [ ] 无个人数据：真实姓名、邮箱、手机、地址、身份证、浏览器指纹。
- [ ] 无绝对本机路径（`/Users/…`、`/home/…`）；一律改用 `./`、用户名占位或相对路径。
- [ ] `.env`、凭据文件、构建产物、日志文件不被 git 跟踪，且已加入 `.gitignore`。
- [ ] 示例、测试数据、README 代码块、gif/截图里无真实用户数据或密钥。
- [ ] 字符集/正则扫描通过：对所有 `.md`/`.yaml`/`.yml` 运行密钥正则扫描，零命中。

命中任何一个 `[ ]` 未勾选 → **阻断发布**：先移出密钥、轮换泄露的凭据、从 git 历史清除（`git filter-repo` 等），重扫通过后再继续。

## E. 可验证性

- [ ] 构建 / 测试命令已运行且通过（或明确记录未运行原因与风险）。
- [ ] 依赖、运行环境、安装步骤在 README 有据可查。
- [ ] 若提供校验/辅助脚本，给出运行方法与输出解读。

## F. 发布动作授权（绝不默认执行）

- [ ] `git push` / 创建远程仓库（`gh repo create`）/ 覆盖线上内容：仅在用户显式要求时执行。
- [ ] 未授权时明确说明未执行，并给出用户可复制的命令。


## G. 发布可发现性（About / Topics / Discussions）

提升项目在 GitHub 上的可发现性，便于社区搜索与提问。推广位设置不改变代码行为，但属于发布就绪的一部分。

- [ ] 仓库 `About` 填写一行定位描述（一句话说明"这是什么 + 核心价值"）。
- [ ] `Topics` 已配置关键标签，至少覆盖：`ai`、`llm`、`skill`、`persona`、`self-memory`（按项目实际再扩展，如 `agent`、`codex`、`cli`）。命令示例：
  ```bash
  gh repo edit <owner>/<repo> \
    --add-topic ai --add-topic llm --add-topic skill \
    --add-topic persona --add-topic self-memory
  ```
- [ ] 验证：`gh repo view <owner>/<repo> --json description,repositoryTopics`，确认描述与 topics 已生效。
- [ ] 若提供了官方主页（见 H. 节主页），`About` 的 Website 字段已填主页链接。

## H. 项目主页（可选，推荐）

为项目制作一个可链接访问的官方主页（`index.html`），`About` 中提供该链接，提升品牌与可发现性。主页风格默认采用 **gruvbox-material 黑金风格**，并支持**中英文切换**。

- [ ] `index.html` 存在，风格为 gruvbox-material 黑金（深色底 #282828 / #1d2021 + 金色强调 #d79921 / #d8a657，配粗体终端感排版；可作为 GitHub Pages 页面部署，或本地静态页）。
- [ ] 页面顶部提供中英切换控件（`简体中文 ⇄ English`），两种语言内容都在单页内、即时切换无需刷新。
- [ ] 页面信息与 README 一致：定位、功能、安装/构建/测试命令、License、维护者；无真实密钥/个人数据/绝对路径。
- [ ] `About` 的 Website 字段指向主页链接（如 `https://<owner>.github.io/<repo>/` 或仓库内 `index.html`）。
- [ ] 验证：本地打开页面，中英切换正常、链接可达、内容未经脱敏检查即视为未通过。

## I. 社区运营（GitHub Discussions）

- [ ] 已启用 GitHub Discussions（设置 → Features → Discussions，或 `gh` 引导开启）。
- [ ] 配置了至少一个类别（如 Q&A / General / Ideas），便于提问与设计讨论。
- [ ] README 或主页中的"提问/贡献"入口指向 Discussions（而非只留 issue）。
- [ ] 验证：仓库页面可见 Discussions tab，或 `gh api` 查询可用。

## J. 发布产物与 Release Assets

发布 release 时随附可直接下载的构建产物（如 `uv build` 生成的 sdist + wheel），而非只打 tag 或发源码包。

- [ ] 已用构建工具产出可分发的产物。若项目是 Python 包，使用 `uv`：
  ```bash
  uv build
  # 产出 dist/<name>-<version>.tar.gz (sdist) 与 dist/<name>-<version>-py3-none-any.whl
  ```
  非 Python 项目按技术栈选用等价产物（编译二进制、JS bundle、容器镜像 tar 等）。
- [ ] 已执行 `uv run --locked pytest -q`（或项目对应测试命令）通过，`dist/` 产物基于通过测试的源码构建。
- [ ] `gh release create <tag> dist/* --title ... --notes ...` 将 sdist/wheel 附为 release assets。
- [ ] 验证：`gh release view <tag> --json assets`，确认资产列表含 `.whl` 与 `.tar.gz`。
- [ ] 敏感信息红线同样适用于 `dist/`：产物不含密钥、个人数据、绝对路径。

## K. 发布质量门禁（监管工具 + 外部审查）

发布前完成代码质量门禁，尤其在**更新了 make-code-clean / code-review-graph 等项目管理/监管工具之后**：

- [ ] 已运行项目监管工具并清理到干净状态：`make-code-clean`（代码清洁）、`code-review-graph`（构建/更新项目的知识图谱）。
- [ ] **更新监管工具自身后，做一次外部 reviewer 代码审查**：让独立于本次改动的 reviewer（或团队外 reviewer）审查 change，重点核对：改动是否引入回归、是否破坏现有接口/行为、新增规则是否可执行可验证。
- [ ] 外部审查意见已处理或明确记录未采纳原因；审查结论（通过/待修）记入交付说明。
- [ ] 关键改动有回归测试 / 验证命令，且已运行通过。

## 输出模板


交付时给出检查表结果：每项 `[x]`/`[ ]` + 证据列；未完成项给出修复步骤。例：

```text
- [x] LICENSE 存在（MIT，版权 xsoway）  证据：文件存在，README 链接有效
- [x] D 敏感信息扫描通过                    证据：密钥正则扫描零命中（validate 无 fail）
- [ ] git push 未执行                       原因：未获授权；待用户确认后运行 gh repo create / git push
```