---
name: oss-release-prep
description: Use this skill when preparing a project for open-source release or generating/expanding a GitHub README; triggers include 开源发布、推送到GitHub、发布检查、README生成、中英文README、开源项目规范、敏感信息检查、密钥检测、禁止泄露API key、仓库About与topics配置、GitHub Discussions、release产物（uv build sdist/wheel）、release assets、项目主页、主页生成、主页风格、主页交互、主页自测、外部代码审查、发布质量门禁 and open-source release prep. 项目主页生成时，参照参考站 https://xsoway.github.io/obsidian-ai-vault-scaffold/ 的样式/交互/内容布局（见本 Skill「项目主页（index.html）规范」节），生成后进行自测检查。
---

# OSS Release Prep

把任意项目整理成符合 GitHub 开源要求的可发布状态，并产出规范、详细、中英双语可切换的 README。强调以证据为准：把"可发布"拆成可勾选、可验证的检查项，而不是凭经验拍脑袋。

> ## 🔴 敏感信息红线（Hard Block，最高优先级）
>
> **严禁公开**任何密钥或敏感数据。这是本 Skill 的第一铁律，优先于其他所有规范。
>
> - **禁止公开的**：LLM/各类 API key（`sk-…`、`sk-proj-…`、`sk-ant-…`、`ghp_…`、`xox…`、`AKIA…`）、token、cookie、私钥、密码、个人数据（真实姓名/邮箱/手机/地址/身份证）、绝对本机路径（`/Users/…`、`/home/…`）。
> - **场景全覆盖**：README、代码块、示例、gif/截图、日志、`TEST`/fixture、`examples/`、`references/`、检查记录——任何即将开源的产物都不得含密钥。`.env` 和凭据文件不得被 git 跟踪。
> - **命中即阻断**：发现任何敏感信息 → **立即中止发布**，先移除密钥、轮换已泄露的凭据、用 `git filter-repo` 等清除 git 历史，重扫通过后才能继续。
> - **绝不占位伪造**：不要把真实密钥改几个字符当"示例"放进 README/示例；示例一律用无意义的占位符（如 `sk-YOUR_KEY_HERE`、`<token>`），且不得与真实值同构。
> - **验证**：对所有 `.md`/`.yaml`/`.yml` 跑密钥正则扫描，零命中才算过；结果记入检查记录与交付说明。

## 何时使用

- 为仓库配置 About / topics（`ai`、`llm`、`skill`、`persona`、`self-memory`）与 GitHub Discussions，提升可发现性。
- 制作 release 产物（`uv build` 的 sdist/wheel 附为 release assets）。
- 更新 make-code-clean / code-review-graph 等监管工具后，做一次外部 reviewer 代码审查再发布。
- 制作可链接访问的项目主页（gruvbox-material 黑金风格、中英切换），About 中提供链接。
- 准备把一个本地项目推到 GitHub 作为开源项目发布。
- 为新项目生成 README，或为已发布项目重写/扩充 README。
- 需要中英文两个独立 README 文件、顶部可切换链接、内容详尽符合开源规范。
- 发布前做一次系统检查：缺失文件、敏感信息、结构问题、License、证据链。

## 输出格式选项

- **默认产物**：两个独立 README 文件（`README.md` 英文版 + `README.zh-CN.md` 中文版），各自顶部带指向另一语言文件的切换链接；内容按用户要求的详细度生成。
- 附带一份 `RELEASE_CHECKLIST.md`（或 Markdown 检查记录），勾选已完成项、标明未完成项与证据。
- **主页产物（可选）**：一份 `index.html` 项目主页（风格/交互/内容布局参照参考站 `https://xsoway.github.io/obsidian-ai-vault-scaffold/`，见「项目主页（index.html）规范」节），内置中英切换；README 不承载主页时可用，About 的 Website 字段链接到它。

- 发布辅助产物（可选，按 `references/release-checklist.md` G–K 节）：About/topics 配置、GitHub Discussions 启用、`uv build` 的 sdist/wheel 附为 release assets、更新监管工具后的外部 reviewer 代码审查、项目主页生成。
- 不自动执行 git push / 创建远程仓库等外部动作，除非用户明确要求。

## 项目主页（index.html）规范

生成项目主页时，以 **定性参考站** `https://xsoway.github.io/obsidian-ai-vault-scaffold/`（下称"参考主页"）为**样式、交互、内容布局的基准**。主页只参考该站的视觉语言、交互模式与信息架构，**内容必须来自当前项目真实结构**，禁止照抄或编造。

### 一、样式基准（照参考主页的视觉语言）

- **主题锚定**：gruvbox-material 黑金风格——深底（约 `#1d2021`/`#282828`）+ 金色强调（`#d79921`/`#d8a657`），暖黑分层阴影、终端感"sharp-to-small"圆角、分层玻璃面板。
- **字体**：展示字体 + 等宽字体组合（参考站用 Space Grotesk + JetBrains Mono，经 Google Fonts CDN 引入）。
- **背景**：静态 `radial-gradient`/网格底 + 低透明度光晕动效（`glow-orb` 缓慢位移），保证深色高对比、可读、不刺眼。
- **保持品牌一致**：同项目 README 与主页使用同一套 gruvbox 色彩与字体，不另起视觉体系。

### 二、交互基准（参考主页的交互组件，按项目实际取舍，参考站全量具备）

以下交互为参考主页成熟的模式，新主页应尽量覆盖；无法覆盖的注明原因：

1. **打字动画终端 Hero**：右侧终端卡片逐行"打字"展示真实命令（clone → 设环境变量 → 执行脚本 → 展示输出），`$` 提示符绿色、输出金色/前景色，带闪烁 cursor。
2. **实时时钟 + 日程高亮**：实时 HH:MM 时钟 + "现在该跑哪个自动化/任务"高亮，随当前时间切换。
3. **动画流水线/循环可视化**：编号节点（如每日闭环 S1→S5）循环高亮 + 箭头动效，直观呈现项目的核心流程。
4. **可展开目录树**：点击文件夹展开/收起，展示项目真实目录结构，脚本/配置按语义配色。
5. **"试用命令"迷你终端**：可点选命令 chip，输出真实用法与结果（`✓` 开头绿色）。
6. **滚动显现（scroll-reveal）**：区块进入视口时淡入上移。
7. **中英切换（EN/中文）**：全局 toggle，全部文案带 `data-en`/`data-zh` 并随切换实时替换（含终端重播）。
8. **Tweaks 面板**：强调色切换（金/绿/紫/蓝）+ 动效开关；尊重 `prefers-reduced-motion`。

### 三、内容布局基准（参考主页的区块顺序）

主页按参考主页的信息架构组织，区块顺序（按项目实际增删，整体遵循）：

1. 粘性导航（brand + 锚点跳转 + 语言 toggle）
2. Hero：一句话定位（英文主打 + 可切中文）→ 行动按钮（Star/仓库链接）→ 真实项目数据指标（分区/脚本/自动化数量，**以仓库实际为准**）
3. 核心流程/流水线（对应"每日闭环"）
4. 痛点 vs 本方案对比表 + 一句话定位引言
5. 功能特性卡片（真实能力，不堆营销话术）
6. "试用命令"迷你终端
7. 目录/结构总览（可展开树）
8. 定时/自动化日程（何时运行什么）
9. 页脚：License、中英双 README 链接、GitHub/Discussions 链接

### 四、内容红线（主页专属，叠加「敏感信息红线」）

- **数据真实**：分区/脚本/脚本数量、目录树、命令、cron 时间表**必须来自当前项目真实结构**；不得编造统计或功能。无法从仓库确认的数字/功能不写。
- **链接真实**：Star 按钮 / 仓库 / README / Discussions 链接指向当前项目真实 URL（可含占位仓库路径约定，但须指向正确仓库）。
- **零敏感**：同「敏感信息红线」——无真实密钥、个人数据、绝对本机路径；含 GitHub URL 与占位路径时须确认无真实凭据。
- **单文件**：必须是单个可独立部署的 `index.html`（GitHub Pages 从仓库根直接服务时无需构建）。

### 五、生成后自测检查（强制，未通过不算完成）

生成/修改主页后，必须用无头浏览器对**本地文件或本地 HTTP** 做一次交互自测，逐项确认并把结果写入交付说明；任何一项失败即修复后重测：

- [ ] 页面能正常加载，`title` / `<h1>` / brand 正确，**浏览器 console 零报错**。
- [ ] 背景色 = 参考站深底（约 `rgb(29,32,33)` = `#1d2021`），强调色 = 金色（约 `#d79921`）。
- [ ] 终端打字动画逐行出现，结束后有静态光标；切语言后按对应语言重播。
- [ ] 中英切换：所有带 `data-en`/`data-zh` 文案实时切换，无残留、无失效。
- [ ] 目录树可展开/收起，渲染内容**无 `undefined`/`NaN`** 等占位错误。
- [ ] 实时时钟走动且等于当前本地时间；日程高亮随当前时间正确切换（周末/周中规则正确）。
- [ ] 流水线动画各节点循环高亮；"试用命令"各 chip 输出正确。
- [ ] Tweaks（强调色 / 动效开关）切换生效；`prefers-reduced-motion` 生效。
- [ ] 响应式：窄屏（约 380px）下单栏折叠、流水线纵向排列，无横向溢出。
- [ ] 敏感信息扫描零命中（`git ls-files` 全文密钥正则扫描；CSS `mask-image` 含 `sk-` 属误报需人工确认）。
- [ ] 所有数据（数字、目录树、命令、日程）与当前项目仓库真实结构一致。

## 如何使用

1. 先读 `prompts/oss-release-prep.md` 获取完整执行规范；再按需读 `references/readme-style.md`（README 结构与详细度基准）和 `references/release-checklist.md`（逐项检查表）。
2. 收集项目事实：README 现状、目录结构、构建/测试命令、License、git 状态、作者信息、依赖与运行环境。先声明已知事实、信息缺口与假设。
3. 按检查表逐项核对并记录证据；缺什么补什么（如 License、.gitignore、.gitattributes、缺少的 README 章节）。
4. 生成/改写 README：中英双语，各自独立文件 + 顶部切换链接；结构参照 `references/readme-style.md`。全程执行「敏感信息红线」。
5. 交付时报告：做了什么、如何验证、产物路径、风险/回滚、复盘结论，并把敏感信息扫描结果列为独立证据项。默认 Markdown。

6. （如适用）按 `references/release-checklist.md` G–K 节补齐：About/topics、Discussions、release assets、外部代码审查、项目主页；发布动作需用户显式授权。

## 输出 README 的格式、内容及规范

产出的 README 遵循固定规范——中英两个独立文件：`README.md`（英文版）+ `README.zh-CN.md`（中文版）。结构镜像、内容一致、切换链接互指。示例结构与风格可参照相邻项目 `skill-spec/README.zh-CN.md`（及其 `README.md`）。

### 文件与切换

- 两个独立文件，各自顶部放指向另一语言文件的切换链接：
  - `README.md`（英文）顶部放 `<a href="./README.zh-CN.md">中文</a>`。
  - `README.zh-CN.md`（中文）顶部放 `<a href="./README.md">English</a>`。
- GitHub 会把 `README.zh-CN.md` 识别为语言变体，仓库首页自动出现语言切换 tab。
- 禁止单个文件内做中英混排；两版必须独立成文、覆盖同一组主题。

### 内容结构（逐节）

```text
<p align="center"> … 徽章区（版本 / License / 状态 / 语言 / 运行时）… </p>
<h1 align="center">项目名</h1>
<p align="center">一句话定位（可选双语）</p>
<p align="center"><a href="./另一语言文件">切换链接</a></p>
<p align="center">卖点短句：可发现 / 可安装 / 可评测 …</p>
<hr>

## 目录 (Table of Contents)     # 锚点链接到各章节
## 是什么 (What is it)
## 为什么需要 (Why)             # 反例 vs 本方案对比表 + 痛点列表
## 核心概念 (Core Concepts)      # 如项目有内在设计思想
## 目录结构 (Structure)          # ```text 树 ``` + 逐文件职责表
## 快速开始 (Quick Start)        # 环境要求 / 安装 / 构建 / 测试命令 + 预期输出
## 功能与用法 (Features / Usage)
## 集成/扩展 (Integrations)      # 如适用
## 安全边界 (Safety) / 设计原则 (Principles)
## FAQ（常见问题）
## 路线图 (Roadmap)             # 已达成 [x] + 待办 [ ]
## 贡献指南 (Contributing)
## License
## 维护者 (Maintainer)
```

章节按项目实际情况取舍；默认产出**详尽版**（含目录、概念、结构、配置、集成、FAQ、路线图、贡献指南、设计原则）。

### 写作规范

- **以证据为准**：安装 / 构建 / 测试 / 运行每一步都必须在项目里找到依据（真实命令、真实文件）。无法验证的步骤不写，或如实标注"请补充"。
- **双语一致**：命令、目录树、徽章可共享；叙述各自独立成文，不通篇直译。两版主题覆盖一致、结构镜像。
- **控制宣传**：卖点须有实际代码/功能支撑，不堆砌营销话术。
- **绝不写入**真实密钥、个人数据、绝对本机路径（如 `/Users/…`）。
- **技术事实以当前项目为准**：技术栈、构建命令、依赖等不沿用外部项目约定。

### 产出检查

- [ ] 两版独立文件存在，切换链接互指正确。
- [ ] 结构含：徽章 + 定位 + 切换链接 + 目录 + 快速开始 + 结构/用法 + License + 维护者。
- [ ] 快速开始与功能说明里的每个命令/路径都有项目依据。
- [ ] 两版覆盖同一组主题、结构镜像。
- [ ] 无真实密钥、个人数据、绝对本机路径（密钥正则扫描零命中）。

## 参考文件

- 完整执行规范：`prompts/oss-release-prep.md`。
- README 结构与详细度基准：`references/readme-style.md`。
- 发布前逐项检查表：`references/release-checklist.md`（D 节「敏感信息扫描」红线；G–K 节补充 About/topics、主页、Discussions、release assets、发布质量门禁）。
- 示例：`examples/release-checklist-sample.md`。

## 常见误区

- 只生成一个 README 就宣称"开源就绪"，跳过缺失文件与敏感信息检查。
- 把"静态检查通过"说成"已发布"或"已验证模型行为"。
- 中英两个 README 内容不同步、切换链接失效，或只用一个文件做中英混排。
- README 堆砌无关宣传，缺少可验证的安装、构建、测试命令与证据。
- 在 README / 检查记录 / 示例中放入真实密钥、个人数据或绝对本机路径。
- 把真实密钥改几个字符当"示例"，或认为"本地没推就安全"——敏感信息规则不因未发布而豁免。
- 只建仓库不配 About/topics、不开 Discussions，导致项目难以被发现与提问。
- 发布只打 tag 或发源码，不附 `uv build` 的 sdist/wheel 等可下载产物。
- 更新 make-code-clean / code-review-graph 等监管工具后直接发布，跳过外部 reviewer 代码审查。
- 主页与 README 信息不一致、中英切换失效，或 About 未链接主页。

## 最佳实践

- README 结构固定：居中徽章区 + 差异化卖点表 + 效果图/结构 + 功能/环境/配置/运行/目录结构 + FAQ + 路线图 + 贡献 + License + 维护者。
- 中英两版结构逐节镜像，切换链接互指正确；纯技术内容可共享，叙述各自独立成文。
- 每个检查项都必须有证据（命令输出、文件存在、git 状态），悬空"应该没问题"视为未通过。
- 敏感信息、缺失工件、License、绝对路径是发布前必须确认项；敏感信息命中即阻断，其余缺则如实标注未完成并给出修复步骤。
- 审慎区分事实、假设、建议、未执行项与人工决策；发布动作须用户显式授权。
- 支持可选的发布辅助校验脚本（如 `scripts/`），并在 README 中给出运行方法与输出解读。
- 开源前对全部产物跑一次密钥正则扫描并记录结果，作为发布证据链的一部分。

- 可发现性：About 一行定位 + topics（`ai`/`llm`/`skill`/`persona`/`self-memory`）+ Discussions + 可链接主页，让项目被搜到、能提问、有门面。
- 发布产物：release 附 `uv build` 产出的 sdist/wheel 等可下载 assets，并验证 `gh release view` 资产列表与敏感信息扫描。
- 发布质控：更新 make-code-clean / code-review-graph 等监管工具后，做一次外部 reviewer 代码审查再发布。
- 主页：参照参考站 https://xsoway.github.io/obsidian-ai-vault-scaffold/ 的样式/交互/内容布局生成单文件 `index.html`（见「项目主页（index.html）规范」节），内置中英切换，About 的 Website 字段链接到它；生成后必须做无头浏览器交互自测。