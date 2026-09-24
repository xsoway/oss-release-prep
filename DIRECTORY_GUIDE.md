# OSS Release Prep 包目录指南

每个新 Skill 采用下列最小可交付结构（遵循 skill-spec 包契约）：

```text
<skill-name>/
├── SKILL.md
├── prompts/<skill-name>.md
├── agents/openai.yaml
├── evals/eval.yaml
├── evals/cases/{basic-success,edge-incomplete-input,edge-scope-boundary}.yaml
├── scripts/validate_skill_package.py
├── references/                 # 仅在有深规则时创建
└── examples/                   # 仅在示例能降低误用时创建
```

可选的 `optimization/` 只服务有明确 SkillOpt 训练计划的 Skill。它不是所有 Skill 的必需目录。