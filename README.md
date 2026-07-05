# Humanize AI Output Skill

A Codex skill for naturalizing AI-assisted Chinese writing, English and bilingual copy, PPT/document language, design briefs, and image prompts.

**Tagline:** make AI-assisted output feel edited, specific, and publishable.

This skill targets the patterns that make AI output feel generic: over-balanced contrast, vague abstraction, repetitive sentence rhythm, translationese, inflated adjectives, and slide/prompt phrasing that sounds mechanically assembled.

## What It Does

- **中文文字自然化**: reduce stiff phrasing, repeated `不是...而是...`, slogan-like transitions, and abstract business terms.
- **English / bilingual polish**: remove corporate fog, translationese, inflated resume language, and awkward Chinese-English label stuffing.
- **PPT / document de-templating**: turn generic slide copy into claim-first, evidence-aware, audience-specific material.
- **Image prompt de-AI-styling**: replace prompt cliches like `8K masterpiece cinematic` with concrete art direction.

## Before / After

### 中文商业分析

**Before**

> 这件事不是简单的效率提升，而是一次组织能力的系统性升级。当前需求、数据和审批分散在三条线上，没人对最终交付负责。企业需要从组织、流程、技术、数据四个维度协同发力，把每周重复出现的审批和数据核对沉淀为可持续增长的新引擎。

**After**

> 这件事的关键在组织分工。需求、数据和审批分散在三条线上，没人对最终交付负责。第一步可以先固定一个跨部门 owner，把每周重复出现的审批和数据核对列出来，再决定哪些环节值得自动化。

**What changed**

- Replaced slogan-like phrasing with a concrete operational problem.
- Removed forced contrast and kept the recommendation direct.
- Added a first move instead of a generic recommendation.

### English Investor Update

**Before**

> We are pleased to share that our team shipped the beta to 12 design partners this month and made significant progress across multiple dimensions. The review workflow has received positive feedback, while admin controls remain a key blocker for wider rollout. Going forward, July will be focused on activation and retention as we continue to execute with discipline to create long-term value.

**After**

> The useful signal now is whether those 12 design partners keep using the review workflow after the first try, or whether it is still mostly interesting in a demo. Next step we should focus on whether admin controls stop blocking rollout. If July is about activation and retention, keep the team there. New feature work can wait.

**What changed**

- Replaced investor-speak with milestones and friction.
- Added a clear adoption signal and next-month focus.
- Preserved a professional tone without generic polish.

### PPT Recommendation

**Before**

> 建议从组织、流程、技术、数据四个维度协同发力，围绕重复交接场景明确 owner、统一输入和审核标准、自动化每周重复发生的检查，并以每次交接节省的小时数作为衡量指标。

**After**

> **Fix ownership before adding more AI tools**
>
> - Name one owner for each repeated workflow.
> - Standardize the input and review criteria.
> - Automate only the checks that repeat every week.
> - Track hours saved per completed handoff.

### Image Prompt

**Before**

> A stunning cyberpunk night-market sci-fi festival poster with layered signs, wet pavement, food stalls, pedestrians, room for title typography in the upper-left area, cyan red and warm white neon lights, futuristic vibes, epic composition, detailed, sharp, 4K, masterpiece, no readable text.

**After**

> Poster background for a night-market sci-fi festival. Low-angle street view with layered signs, wet pavement, food stalls, and pedestrians partly silhouetted. Leave the upper-left third clear for typography. Neon palette limited to cyan, red, and warm white. Graphic poster style, crisp shapes, no readable text in the image.

## Install

Clone the repo and copy the skill folder into your Codex skills directory:

```bash
git clone https://github.com/zhaoyun/humanize-ai-output.git
mkdir -p ~/.codex/skills
cp -R humanize-ai-output/skills/humanize-ai-output ~/.codex/skills/
```

Then use:

```text
Use $humanize-ai-output to revise this draft while preserving facts and avoiding over-polish.
```

## Usage

```text
Use $humanize-ai-output to make this Chinese project update sound less like AI.
```

```text
Use $humanize-ai-output to polish this bilingual LinkedIn bio without making it inflated.
```

```text
Use $humanize-ai-output to de-template this strategy slide and make the recommendation sharper.
```

```text
Use $humanize-ai-output to rewrite this image prompt as real art direction.
```

## Evaluation

The public evaluation set lives in [`evals/`](evals/):

- [`evals/prompts.md`](evals/prompts.md): 50 common prompts across four capability areas.
- [`evals/rubric.md`](evals/rubric.md): scoring criteria.
- [`evals/test-report.md`](evals/test-report.md): baseline outputs, skill outputs, per-case Penalty gate scores, iteration notes, and final assessment.

Run release checks:

```bash
python3 tests/validate_release.py
# Optional, if you have the Codex skill-creator validator installed:
python3 <path-to-skill-creator>/scripts/quick_validate.py skills/humanize-ai-output
```

Helper scripts:

```bash
python3 skills/humanize-ai-output/scripts/style_seed.py --task chinese
python3 skills/humanize-ai-output/scripts/ai_tone_lint.py examples/chinese-writing/project-update.txt
```

## Repository Layout

```text
skills/humanize-ai-output/
  SKILL.md
  agents/openai.yaml
  references/
  scripts/
examples/
evals/
tests/
```

## Ethics

This project is for editing quality, clarity, tone, audience fit, layout specificity, and prompt usefulness. It should not be used to misrepresent authorship, evade academic or workplace disclosure rules, fabricate human experience, or claim that output can bypass AI detection systems.

## Contributing

Useful contributions:

- New before/after examples.
- Missed AI-ish phrasing patterns.
- Bad rewrites where meaning drifted.
- More evaluation cases in Chinese, English, bilingual, PPT/document, and image-prompt scenarios.

Please include the original prompt, baseline output, revised output, and a short note on what changed.

## Release Checklist

- [x] `SKILL.md` has final frontmatter and no scaffold placeholders.
- [x] `agents/openai.yaml` matches the final skill purpose.
- [x] README includes install, usage, examples, evals, and ethics.
- [x] 50 eval cases are documented.
- [x] Per-case Penalty gate scores are documented.
- [x] Helper scripts run with `--help`.
- [x] `python3 tests/validate_release.py` passes.
- [x] License added.

Suggested GitHub topics: `codex-skill`, `writing`, `editing`, `ai-output`, `prompting`, `humanize-ai`, `presentation-design`.
