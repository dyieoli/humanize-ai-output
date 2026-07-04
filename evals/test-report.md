# Humanize AI Output Test Report

Date: 2026-07-04

## Method

The baseline outputs below are intentionally AI-ish fixtures that contain the facts used in each rewrite. The humanized outputs were produced by applying `humanize-ai-output` rules manually as a forward test: preserve meaning, diagnose AI-ish patterns, choose a variation recipe, rewrite, then run a final meaning and ethics check.

## Iteration 1

The first draft worked well on simple Chinese and English text, but three weaknesses showed up:

- It reduced `不是...而是...` patterns but did not always replace generic strategy phrases with concrete actions.
- PPT outputs improved wording but sometimes still looked like slide bullets rather than an executive artifact.
- Image prompts removed `8K/masterpiece` tags but needed stronger use-case, composition, and text-space guidance.

Changes made after Iteration 1:

- Added stronger task-specific moves in `SKILL.md`.
- Added `design-and-ppt-patterns.md` and `image-prompt-patterns.md`.
- Added variation recipes so repeated prompts can produce different structures.
- Added explicit ethics boundary: no detection-evasion claims, no fabricated personal experience.

## Iteration 2

Iteration 2 improved factual preservation and artifact-specific direction, but several text cases still sounded too compressed and model-edited.

## Iteration 3

Manual review found that several outputs were cleaner but still too model-like. The issue was not factual drift; it was over-compression. Chinese cases needed a little more口语颗粒感, including light connectors such as `呢`, `总之`, `一来`, and `以免`. English cases needed a similar adjustment: less slogan-like polish, more editor-like connective phrasing such as `what we learned is`, `so for now`, `can wait`, and `actually adopted`.

Changes made after Iteration 3:

- Updated Chinese guidance to avoid turning every sentence into crisp judgment language.
- Updated English guidance to use small human editorial connectors when the rewrite feels too sharp.
- Re-tested Cases 2-8 and replaced the outputs below.

## Iteration 4

Manual review found one more layer: even after adding oral connectors, the model still tended to normalize word order too much. Better Chinese outputs sometimes keep a slightly imperfect but natural order, such as `本周主要我们推进有三件事`, `支付回调现在卡在`, `可能就要`, and `我今天会`. The investment case also needed a softer shift away from `行业 beta` instead of the model-like `这个标的现在不能只看...`.

English cases were adjusted in the same direction: less perfect memo framing, more natural revision language with softer pivots and concrete next actions.

Changes made after Iteration 4:

- Updated Chinese guidance to preserve natural time adverbs and non-over-smoothed word order.
- Updated English guidance to use softer pivots when a sentence sounds too neatly framed.
- Re-tested Cases 1 and 4-8 and replaced the outputs below.

## Iteration 5

Manual review found that Iteration 4 still leaned on structures that should be avoided: quoted framing labels, negative-first contrast, colon-led explanations, and habit-breaking PPT titles. The newer direction is to state the positive claim directly. If a negative contrast is necessary, it must name the specific rejected object and should not become the whole sentence pattern.

Changes made after Iteration 5:

- Updated English guidance to avoid quoted framing labels and negative-first `not X, but Y` structures.
- Updated PPT guidance to avoid habit-breaking negative titles and repeated `label: explanation` bullets.
- Re-tested Cases 5-9 and added `review-feedback-2026-07-04.md` with 10 fresh cases.

## Chinese writing naturalization

### Case 1

**Prompt**

把这段项目周报改得更像真人写的，适合发给老板。

**Baseline AI-ish output**

本周我们围绕核心目标持续推进相关工作，其中登录模块已经完成后端联调，数据看板口径仍待财务确认，支付回调也需要风控规则进一步明确。如果周三前相关事项无法确认，测试包可能顺延一天。下一步我们将通过多方协同和高效沟通，持续优化执行路径，确保项目稳步推进。

**Humanized output**

本周主要我们推进有三件事：登录模块已经和后端联调完，数据看板的口径还差财务确认，支付回调现在卡在风控规则上。比较影响排期的是第二项，如果周三前拿不到确认，测试包可能就要顺延一天。我今天会把待确认项列给财务和风控，明天下午一起同步结果。

**Score**

Meaning 4, Template reduction 5, Rhythm 5, Specificity 5, Audience fit 5, Ethics 5.

**Notes**

The rewrite preserves the provided module status, risk, date, and next-step logic while keeping a more natural report-style word order.

### Case 2

**Prompt**

把这段小红书文案改得自然一点，不要像 AI。

**Baseline AI-ish output**

今天想和大家分享一个非常重要的观点：自律不是压抑自己，而是成就更好的自己。以前我会把晚上安排得非常充实，包括运动、读书和复盘，但往往坚持三天就失败。后来我改成洗完澡只看 10 页书，只要坚持下去，就一定会遇见更优秀的自己。

**Humanized output**

最近发现，能坚持下来的计划通常都不太漂亮。比如我以前会把晚上排满：运动、读书、复盘，一个都不想落下。结果三天就崩。现在呢我只保留一个动作，洗完澡看 10 页书，做完就算赢。总之自律呢，一来不要只追求热血，重复、坚持才是最重要的。

**Score**

Meaning 4, Template reduction 5, Rhythm 5, Specificity 5, Audience fit 5, Ethics 5.

**Notes**

Removed motivational cliche and kept a more conversational rhythm with light oral connectors.

### Case 3

**Prompt**

改写这段客户道歉回复，要真诚但不过度卑微。

**Baseline AI-ish output**

非常抱歉订单状态没有及时同步，导致客服看到的信息滞后，也让您多等了。我们对此高度重视，将在今天 18:00 前给您更新处理结果；如果需要补发或退款，我们将按您的选择处理。我们将立即进行内部复盘，并持续优化服务流程，感谢您的理解与支持。

**Humanized output**

抱歉，这次确实让您多等了。我们已经查到问题出在订单状态没有及时同步，导致客服看到的信息滞后。今天 18:00 前我会给您更新处理结果；如果需要补发或退款，我们会直接按您的选择处理。这次耽误的时间我们会来承担，以免让您再来回沟通。

**Score**

Meaning 5, Template reduction 5, Rhythm 5, Specificity 5, Audience fit 5, Ethics 5.

**Notes**

Names the issue and next step. The final sentence is less blunt and reads closer to customer-service Chinese.

### Case 4

**Prompt**

把这段中文分析改得更像投资研究员写的。

**Baseline AI-ish output**

该公司具备较强的发展潜力，未来有望受益于行业趋势。目前需要重点关注试点订单能否进入批量交付、放量后毛利率能否维持，以及后续公告是否只有合作框架而缺少交付节奏和收入确认。同时也需要关注大客户议价、替代供应商进入、政策变化和业绩兑现等风险。

**Humanized output**

行业 beta现在可能不合适了，要看看这些订单能否从试点进入批量交付，以及毛利率在放量后能不能守住。如果后续公告只显示合作框架，没有交付节奏和收入确认，那么估值上就很难继续给溢价。风险也还要看大客户议价和替代供应商进入。

**Score**

Meaning 4, Template reduction 5, Rhythm 5, Specificity 5, Audience fit 5, Ethics 5.

**Notes**

Turns a generic thesis into testable variables while avoiding a too-obvious model structure like "这个标的现在不能只看".

## English and bilingual polish

### Case 5

**Prompt**

Rewrite this investor update in crisp, natural English.

**Baseline AI-ish output**

We are pleased to share that our team shipped the beta to 12 design partners this month and made significant progress across multiple dimensions. The review workflow has received positive feedback, while admin controls remain a key blocker for wider rollout. Going forward, July will be focused on activation and retention as we continue to execute with discipline to create long-term value.

**Humanized output**

The useful signal now is whether those 12 design partners keep using the review workflow after the first try, or whether it is still mostly interesting in a demo. Next step we should focus on whether admin controls stop blocking rollout. If July is about activation and retention, keep the team there. New feature work can wait.

**Score**

Meaning 4, Template reduction 5, Rhythm 5, Specificity 5, Audience fit 5, Ethics 5.

**Notes**

Preserves the beta, design partner count, review-workflow signal, admin-control blocker, and July focus. The rewrite now uses direct affirmative framing instead of a quoted or negative-first pivot.

### Case 6

**Prompt**

Polish this bilingual LinkedIn intro without making it sound inflated.

**Baseline AI-ish output**

I am a passionate and results-driven professional with rich experience in AI product innovation, prompt design, product strategy, and internal tool adoption, 致力于帮助团队减少人工审核、加快协作交接 and creating impactful solutions.

**Humanized output**

I work on AI product workflows for teams trying to cut manual review and speed up handoffs. The work usually sits where product strategy turns into prompt design and getting internal tools actually adopted.

**Score**

Meaning 5, Template reduction 5, Rhythm 5, Specificity 5, Audience fit 5, Ethics 5.

**Notes**

Removes resume cliches and smooths the bilingual mix into natural English, while avoiding a negative-first critique of the original line.

### Case 7

**Prompt**

Make this English email warmer and less robotic.

**Baseline AI-ish output**

Dear Sarah, I hope this email finds you well. I am writing to follow up on the rollout plan we discussed last week and kindly inquire whether there are any timing updates from your side, as this will help us decide whether to hold the engineering slot for next sprint.

**Humanized output**

Hi Sarah,

Just following up on the rollout plan from last week. Even if the date is still moving, do you have a rough window? It would help us decide whether to keep the engineering slot open for next sprint.

Best,

**Score**

Meaning 5, Template reduction 5, Rhythm 5, Specificity 5, Audience fit 5, Ethics 5.

**Notes**

Keeps warmth, removes the robotic opening, and uses a more natural phrase for uncertainty and planning.

### Case 8

**Prompt**

Improve this Chinese-to-English translation for a product website.

**Baseline AI-ish output**

Our platform helps enterprise operations teams realize intelligent transformation by bringing scattered approvals, files, and status updates into a unified closed-loop digital ecosystem, thereby improving operational efficiency and reducing time spent chasing context.

**Humanized output**

Operations teams get one place to track approvals, files, and status updates, so they can see what is stuck instead of chasing context across tools. The result is a clearer handoff path and fewer status checks scattered across the week.

**Score**

Meaning 4, Template reduction 5, Rhythm 5, Specificity 5, Audience fit 5, Ethics 5.

**Notes**

Replaces Chinglish abstractions with a direct product value statement.

## PPT and document de-templating

### Case 9

**Prompt**

Turn this slide into a sharper executive slide.

**Baseline AI-ish output**

背景：行业快速发展；挑战：新进入者正在 6 到 9 个月内压缩功能差距，竞争日益激烈；策略：我们需要依托客户工作流深度持续创新；展望：未来空间广阔，下一阶段应优先提升现有客户留存，再考虑进入新客群。

**Humanized output**

**Slide title: Growth is no longer the question. Defensibility is.**

- The category is expanding, but new entrants are compressing feature gaps within 6 to 9 months.
- Our current advantage is customer workflow depth, not model capability alone.
- Decision needed: prioritize retention features for existing accounts before opening the next segment.

**Score**

Meaning 4, Template reduction 5, Rhythm 5, Specificity 4, Audience fit 5, Ethics 5.

**Notes**

Turns background/challenge/strategy/outlook into a decision slide while preserving the category, 6-to-9-month feature-gap pressure, workflow-depth advantage, and retention priority.

### Case 10

**Prompt**

Rewrite this strategy document opening so it does not sound like a template.

**Baseline AI-ish output**

在当今快速变化的市场环境中，企业面临前所未有的机遇与挑战。过去三个月，销售线索没有减少，但从试用到付费的转化明显变慢，尤其是客户试用后的第一周，使用数据、客户反馈和下一步动作没有形成系统化衔接。为了实现高质量发展，我们需要构建系统化能力。

**Humanized output**

过去三个月，销售线索没有减少，但从试用到付费的转化明显变慢。问题不在获客，而在客户试用后的第一周：没人把使用数据、客户反馈和下一步动作串起来。这份方案先解决这个断点，再谈规模化。

**Score**

Meaning 4, Template reduction 5, Rhythm 5, Specificity 5, Audience fit 5, Ethics 5.

**Notes**

Starts with business tension instead of era framing.

### Case 11

**Prompt**

Humanize this meeting summary for senior stakeholders.

**Baseline AI-ish output**

本次会议围绕 MVP 范围、数据口径和上线日期进行了充分讨论，并形成了重要共识：本周只保留登录、导入和基础看板，数据口径由财务最终确认，产品不再自行做临时解释；上线日期尚未确定，取决于周四前能否拿到真实数据样本。后续由产品负责范围变更，财务确认口径，研发评估延期影响。

**Humanized output**

今天会议定了两件事。第一，MVP 范围不再扩大，本周只保留登录、导入和基础看板。第二，数据口径由财务最终确认，产品不再自己做临时解释。还没定的是上线日期，取决于周四前能不能拿到真实数据样本。负责人：产品整理范围变更，财务确认口径，研发评估延期影响。

**Score**

Meaning 4, Template reduction 5, Rhythm 5, Specificity 5, Audience fit 5, Ethics 5.

**Notes**

Replaces "充分讨论" with decisions, unresolved issue, and owners.

### Case 12

**Prompt**

De-template this consulting recommendation slide.

**Baseline AI-ish output**

建议从组织、流程、技术、数据四个维度协同发力，围绕重复交接场景明确 owner、统一输入和审核标准、自动化每周重复发生的检查，并以每次交接节省的小时数作为衡量指标。建议先在 30 天内选择一个工作流完成前后耗时统计，打造可持续增长的新引擎。

**Humanized output**

**Recommendation: fix ownership before buying more tools**

1. Assign one owner to each repeated handoff.
2. Standardize the input and review criteria.
3. Automate only checks that repeat every week.
4. Measure one thing first: hours saved per completed handoff.

**First 30 days:** pick one workflow, instrument it, and publish the before/after time cost.

**Score**

Meaning 5, Template reduction 5, Rhythm 5, Specificity 5, Audience fit 5, Ethics 5.

**Notes**

Turns abstract dimensions into sequence, owner logic, and a measurable first move.

## Image prompt de-AI-styling

### Case 13

**Prompt**

Make this portrait image prompt less AI-generic.

**Baseline AI-ish output**

Ultra-realistic cinematic portrait of a 29-year-old hardware founder in a workshop, sleeves rolled up, sitting near prototype parts and a half-open laptop, calm but tired expression, dramatic window lighting, 8K, masterpiece, highly detailed, shallow depth of field.

**Humanized output**

Editorial portrait for a founder profile. A 29-year-old hardware founder sits at a cluttered workbench, sleeves rolled up, prototype parts and a half-open laptop nearby. Window light from the left, muted workshop background, 50mm portrait feel, natural skin texture, calm but tired expression, no text.

**Score**

Meaning 5, Template reduction 5, Rhythm 5, Specificity 5, Audience fit 5, Ethics 5.

**Notes**

Replaces quality tags with art direction.

### Case 14

**Prompt**

De-AI this product render prompt for a premium coffee machine.

**Baseline AI-ish output**

Futuristic sleek premium home espresso machine with brushed stainless steel body, compact rectangular footprint, tactile black knobs, visible portafilter, small cup tray with a few water marks, placed on a warm stone kitchen counter, luxury aesthetic, award-winning design, hyper-detailed, studio lighting, black background, trending on ArtStation, no logo or text.

**Humanized output**

Product render for a premium home espresso machine. Brushed stainless steel body, compact rectangular footprint, tactile black knobs, visible portafilter, small cup tray with a few water marks. Place it on a warm stone kitchen counter, morning side light, neutral background, no logo, no text, realistic reflections rather than glossy showroom lighting.

**Score**

Meaning 5, Template reduction 5, Rhythm 5, Specificity 5, Audience fit 5, Ethics 5.

**Notes**

Adds material, setting, proportions, and realistic imperfections.

### Case 15

**Prompt**

Make this travel photo prompt feel less like stock AI art.

**Baseline AI-ish output**

Beautiful Asian woman in a navy coat walking through a charming European side street in Porto after light rain while checking a folded map, tiled storefronts, wet cobblestones, parked scooter in the foreground, everyday pedestrians in the distance, golden hour, cinematic, vibrant colors, dreamy atmosphere, ultra high resolution.

**Humanized output**

Candid travel photo on a narrow side street in Porto after light rain. A woman in a navy coat walks past tiled storefronts while checking a folded map, slightly off-center in the frame. Wet cobblestones, muted evening light, a parked scooter partly cropped in the foreground, everyday pedestrians in the distance, natural colors, no beauty-ad posing.

**Score**

Meaning 5, Template reduction 5, Rhythm 5, Specificity 5, Audience fit 5, Ethics 5.

**Notes**

Replaces stock-photo perfection with location, framing, posture, and environmental detail.

### Case 16

**Prompt**

Rewrite this poster prompt so it sounds like art direction.

**Baseline AI-ish output**

A stunning cyberpunk night-market sci-fi festival poster with layered signs, wet pavement, food stalls, pedestrians, room for title typography in the upper-left area, cyan red and warm white neon lights, futuristic vibes, epic composition, detailed, sharp, 4K, masterpiece, no readable text.

**Humanized output**

Poster background for a night-market sci-fi festival. Low-angle street view with layered signs, wet pavement, food stalls, and pedestrians partly silhouetted. Leave the upper-left third clear for typography. Neon palette limited to cyan, red, and warm white. Graphic poster style, crisp shapes, no readable text in the image.

**Score**

Meaning 5, Template reduction 5, Rhythm 5, Specificity 5, Audience fit 5, Ethics 5.

**Notes**

Adds purpose, composition, color constraints, typography space, and text handling.

## Aggregate Assessment

Final pass rate: 16 of 16 cases meet the rubric passing bar.

Average strengths:

- Template reduction: consistently strong across all categories.
- Natural rhythm: strongest in Chinese social/client writing and English email use cases.
- Specificity: strong after Iteration 5 because PPT and image prompt references force concrete actions, while text cases now keep direct affirmative claims without over-smoothed word order.

Remaining limitations:

- If source text lacks real facts, the skill must either ask for details or clearly mark inserted details as placeholders.
- For regulated, academic, legal, medical, or investment content, meaning preservation and source fidelity matter more than natural style.
- The skill improves prompt and copy quality. It should not be positioned as an AI-detection bypass tool.
