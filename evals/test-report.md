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

## Iteration 6

Manual review found two remaining leak paths: broad trailing `not` frames in English slide copy, and Chinese `问题不在...而在...` openings in document copy. Both now count as high-penalty structures in a second correction pass.

Changes made after Iteration 6:

- Added a 95-point penalty gate that counts forbidden structures before output is accepted.
- Updated `ai_tone_lint.py --score` so broad contrast, negative-first, colon-led, quoted-label, and plus-stack patterns can fail automatically.
- Re-tested Cases 9-11 and replaced the outputs below.

## Iteration 7

The main evaluation set was expanded from 16 to 50 cases so the skill is tested across more writing, document, slide, bilingual, support, product, research, and image-prompt situations.

Changes made after Iteration 7:

- Added 34 new cases across Chinese writing, English and bilingual polish, PPT/document de-templating, and image prompt de-AI-styling.
- Kept the 95-point penalty gate on every accepted humanized output.
- Updated `evals/prompts.md` so every new report case has a matching fixture.

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

**Penalty gate**

Score 100 / 100, threshold 95. Findings: none.

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

**Penalty gate**

Score 100 / 100, threshold 95. Findings: none.

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

**Penalty gate**

Score 100 / 100, threshold 95. Findings: none.

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

**Penalty gate**

Score 100 / 100, threshold 95. Findings: none.

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

**Penalty gate**

Score 100 / 100, threshold 95. Findings: none.

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

**Penalty gate**

Score 100 / 100, threshold 95. Findings: none.

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

**Penalty gate**

Score 100 / 100, threshold 95. Findings: none.

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

**Penalty gate**

Score 100 / 100, threshold 95. Findings: none.

**Notes**

Replaces Chinglish abstractions with a direct product value statement.

## PPT and document de-templating

### Case 9

**Prompt**

Turn this slide into a sharper executive slide.

**Baseline AI-ish output**

背景：行业快速发展；挑战：新进入者正在 6 到 9 个月内压缩功能差距，竞争日益激烈；策略：我们需要依托客户工作流深度持续创新；展望：未来空间广阔，下一阶段应优先提升现有客户留存，再考虑进入新客群。

**Humanized output**

**Retention features should lead the next segment plan**

- The category is still expanding, and new entrants are closing feature gaps within 6 to 9 months.
- Customer workflow depth is the current advantage.
- Prioritize retention features for existing accounts before opening the next segment.

**Score**

Meaning 4, Template reduction 5, Rhythm 5, Specificity 4, Audience fit 5, Ethics 5.

**Penalty gate**

Score 100 / 100, threshold 95. Findings: none.

**Notes**

Turns background/challenge/strategy/outlook into a decision slide while preserving the category, 6-to-9-month feature-gap pressure, workflow-depth advantage, and retention priority.

### Case 10

**Prompt**

Rewrite this strategy document opening so it does not sound like a template.

**Baseline AI-ish output**

在当今快速变化的市场环境中，企业面临前所未有的机遇与挑战。过去三个月，销售线索没有减少，但从试用到付费的转化明显变慢，尤其是客户试用后的第一周，使用数据、客户反馈和下一步动作没有形成系统化衔接。为了实现高质量发展，我们需要构建系统化能力。

**Humanized output**

过去三个月，销售线索保持稳定，但从试用到付费的转化明显变慢。客户试用后的第一周需要重点梳理，使用数据、客户反馈和下一步动作现在没有串起来。这份方案优先处理这个断点，再看后续规模化。

**Score**

Meaning 4, Template reduction 5, Rhythm 5, Specificity 5, Audience fit 5, Ethics 5.

**Penalty gate**

Score 100 / 100, threshold 95. Findings: none.

**Notes**

Starts with business tension instead of era framing.

### Case 11

**Prompt**

Humanize this meeting summary for senior stakeholders.

**Baseline AI-ish output**

本次会议围绕 MVP 范围、数据口径和上线日期进行了充分讨论，并形成了重要共识：本周只保留登录、导入和基础看板，数据口径由财务最终确认，产品不再自行做临时解释；上线日期尚未确定，取决于周四前能否拿到真实数据样本。后续由产品负责范围变更，财务确认口径，研发评估延期影响。

**Humanized output**

今天会议定了两件事。第一，MVP 范围不再扩大，本周只保留登录、导入和基础看板。第二，数据口径由财务最终确认，产品不再自己做临时解释。还没定的是上线日期，取决于周四前能不能拿到真实数据样本。后续分工也先这样定，产品整理范围变更，财务确认口径，研发评估延期影响。

**Score**

Meaning 4, Template reduction 5, Rhythm 5, Specificity 5, Audience fit 5, Ethics 5.

**Penalty gate**

Score 100 / 100, threshold 95. Findings: none.

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

**Penalty gate**

Score 100 / 100, threshold 95. Findings: none.

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

**Penalty gate**

Score 100 / 100, threshold 95. Findings: none.

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

**Penalty gate**

Score 100 / 100, threshold 95. Findings: none.

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

**Penalty gate**

Score 100 / 100, threshold 95. Findings: none.

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

**Penalty gate**

Score 100 / 100, threshold 95. Findings: none.

**Notes**

Adds purpose, composition, color constraints, typography space, and text handling.

## Expanded coverage cases

### Case 17

**Prompt**

把这段团队通知改得自然一点，适合发在项目群里。

**Baseline AI-ish output**

各位同事，为了进一步提升项目协同效率，确保本周版本发布目标顺利达成，请大家积极配合相关工作安排。测试同学需尽快完成回归验证，研发同学需及时修复问题，产品同学需持续跟进需求闭环。

**Humanized output**

大家同步一下本周发版节奏。测试今天先跑主流程回归，问题单按阻塞程度标出来；研发优先看支付和导入两个模块，其他小问题先放到明天上午统一处理。产品这边今晚把需求变更和验收口径补齐，避免明天边测边改。

**Score**

Meaning 5, Template reduction 5, Rhythm 5, Specificity 5, Audience fit 5, Ethics 5.

**Penalty gate**

Score 100 / 100, threshold 95. Findings: none.

**Notes**

Turns empty coordination language into owners, timing, and concrete work order.

### Case 18

**Prompt**

把这段产品更新说明改得像真实产品经理写的。

**Baseline AI-ish output**

本次版本升级围绕用户体验优化和功能完善展开，新增消息筛选能力，优化列表加载速度，并修复若干已知问题，致力于为用户带来更加高效、稳定、便捷的使用体验。

**Humanized output**

这个版本主要改了三处。消息页现在可以按未读、@我、评论筛选，找通知会快一点；列表首次加载减少了一段空白等待；另外修了附件预览偶尔打不开的问题。已经更新到最新版的用户可以直接使用，不需要重新配置。

**Score**

Meaning 5, Template reduction 5, Rhythm 5, Specificity 5, Audience fit 5, Ethics 5.

**Penalty gate**

Score 100 / 100, threshold 95. Findings: none.

**Notes**

Names visible changes and keeps the tone close to a real release note.

### Case 19

**Prompt**

改写这段创始人公开说明，要克制、可信。

**Baseline AI-ish output**

对于近期发货延迟给用户造成的不便，我们深表歉意。我们高度重视每一位用户的体验，将持续优化供应链管理能力，提升履约效率，以更加负责任的态度回馈广大用户的信任。

**Humanized output**

近期部分订单发货延迟，给用户带来了额外等待，我们在这里向大家说明情况。延迟主要来自外壳到仓后的质检返工，原计划周三发出的订单需要顺延两天。目前补料和复检已经完成，已付款订单会在本周五前陆续发出，物流单号会通过短信同步。需要退款的用户可以在订单页提交申请，我们会在当天处理。

**Score**

Meaning 4, Template reduction 5, Rhythm 5, Specificity 5, Audience fit 5, Ethics 5.

**Penalty gate**

Score 100 / 100, threshold 95. Findings: none.

**Notes**

Replaces PR wording with reason, shipping date, refund path, and accountability.

### Case 20

**Prompt**

把这段学习心得改得更像个人记录。

**Baseline AI-ish output**

学习英语的关键不是短期突击，而是建立长期坚持的习惯。通过每天背单词、听听力和进行口语练习，可以逐步提升综合语言能力，实现自我成长。

**Humanized output**

最近学英语最有用的办法反而很小。每天早上听 12 分钟新闻，晚上只复盘 8 个生词，周末再把这一周说不顺的句子整理一遍。量不大，所以能一直做下去。三周下来，开会时至少不会每句话都先在脑子里翻译一遍。

**Score**

Meaning 4, Template reduction 5, Rhythm 5, Specificity 5, Audience fit 5, Ethics 5.

**Penalty gate**

Score 100 / 100, threshold 95. Findings: none.

**Notes**

Keeps the habit idea but grounds it in small routines and a believable outcome.

### Case 21

**Prompt**

把这段投研风险提示改得更像内部备忘录。

**Baseline AI-ish output**

该标的虽然具备较强成长性，但仍需警惕多重风险因素，包括下游需求波动、原材料价格上涨、客户集中度较高以及行业竞争加剧等因素对公司盈利能力产生的不利影响。

**Humanized output**

这家公司短期先看两个风险。第一是前三大客户占比太高，明年议价如果提前发生，毛利率会先受压。第二是铜价和运费这两个成本项，目前还没有看到完整传导机制。行业竞争可以继续跟踪，但对下个季度业绩影响没那么直接。

**Score**

Meaning 4, Template reduction 5, Rhythm 5, Specificity 5, Audience fit 5, Ethics 5.

**Penalty gate**

Score 100 / 100, threshold 95. Findings: none.

**Notes**

Ranks risks and separates near-term earnings pressure from broader monitoring items.

### Case 22

**Prompt**

改写这封候选人拒信，要真诚但不拖沓。

**Baseline AI-ish output**

非常感谢您参与本次面试流程。经过综合评估，我们认为您的经历与当前岗位要求仍存在一定差距，因此很遗憾本次无法继续推进。祝您未来职业发展顺利。

**Humanized output**

感谢您参与本次面试流程。我们认真讨论后，决定优先推进一位企业客户实施经验更贴近当前岗位的候选人，因此这次暂不继续后续流程。您的产品判断和沟通表达给团队留下了比较深的印象；如果后续有更偏策略或增长方向的机会，我们会再与您联系。祝您接下来的求职顺利。

**Score**

Meaning 4, Template reduction 5, Rhythm 5, Specificity 4, Audience fit 5, Ethics 5.

**Penalty gate**

Score 100 / 100, threshold 95. Findings: none.

**Notes**

Keeps the rejection clear while giving a specific, respectful reason.

### Case 23

**Prompt**

把这段社群活动邀请改得更像人写的。

**Baseline AI-ish output**

为了帮助大家更好地了解 AI 工具在个人成长和职场效率提升中的应用价值，我们将举办一次线上分享活动，欢迎大家积极报名参与，共同探索 AI 时代的新机遇。

**Humanized output**

我们将在本周四 20:00 举办一场线上分享，主题是 AI 工具在周报撰写、面试准备和资料整理中的实际用法。分享会以真实案例为主，不展开宏观趋势讨论，更适合刚开始使用 AI、希望形成固定工作方法的同学。欢迎在群内接龙报名，会议链接会提前发送。

**Score**

Meaning 4, Template reduction 5, Rhythm 5, Specificity 5, Audience fit 5, Ethics 5.

**Penalty gate**

Score 100 / 100, threshold 95. Findings: none.

**Notes**

Turns a generic invitation into topic, time, audience, and signup action.

### Case 24

**Prompt**

把这段运营 SOP 改得更可执行。

**Baseline AI-ish output**

用户反馈需要及时响应并形成闭环，相关负责人应根据问题类型进行分类处理，持续优化用户体验，并通过数据分析不断提升运营效率。

**Humanized output**

收到用户反馈后先按三类处理。支付、登录、数据丢失直接标红，10 分钟内拉研发看；功能建议进需求池，每周三集中评估；普通咨询由客服当天回复。每条反馈都要留下处理结果和下一步动作，周五运营汇总一页表。

**Score**

Meaning 5, Template reduction 5, Rhythm 5, Specificity 5, Audience fit 5, Ethics 5.

**Penalty gate**

Score 100 / 100, threshold 95. Findings: none.

**Notes**

Adds categories, response times, owners, and a weekly artifact.

### Case 25

**Prompt**

把这段用户评价改得真实一点，少一点广告感。

**Baseline AI-ish output**

这款笔记软件极大提升了我的工作效率，界面简洁美观，功能强大完善，让我在学习和工作中都能获得前所未有的流畅体验，强烈推荐给每一个追求高效的人。

**Humanized output**

我主要拿它记会议和整理读书笔记。好用的地方是搜索快，之前写过的内容不用翻很久；同步偶尔会慢半拍，但还能接受。整体更适合每天都有零散记录的人，重度排版需求可能要再配合别的工具。

**Score**

Meaning 4, Template reduction 5, Rhythm 5, Specificity 5, Audience fit 5, Ethics 5.

**Penalty gate**

Score 100 / 100, threshold 95. Findings: none.

**Notes**

Adds usage context, a real limitation, and a narrower recommendation.

### Case 26

**Prompt**

把这段论文致谢改得自然、得体。

**Baseline AI-ish output**

在论文完成过程中，我得到了导师、同学和家人的大力支持与帮助，在此向所有给予我关心、指导和鼓励的人表示最诚挚的感谢。

**Humanized output**

在本论文的选题、写作和修改过程中，导师在研究问题收窄、章节结构调整和论证细节上给予了细致指导。几位同学认真阅读了初稿，并提出了许多有价值的修改建议。家人在写作期间给予我持续支持，也为我保留了安静完成论文的时间。谨向所有给予帮助和鼓励的人表示诚挚感谢。

**Score**

Meaning 5, Template reduction 5, Rhythm 5, Specificity 5, Audience fit 5, Ethics 5.

**Penalty gate**

Score 100 / 100, threshold 95. Findings: none.

**Notes**

Keeps the formal setting while replacing generic thanks with concrete support.

### Case 27

**Prompt**

Rewrite this renewal email so it sounds like a real account manager.

**Baseline AI-ish output**

Dear Alex, we are excited to continue partnering with your team and would like to proactively discuss renewal options that can unlock additional value across your organization while ensuring a seamless continuation of service.

**Humanized output**

Hi Alex,

Your current plan renews at the end of August, so I wanted to start the conversation early. Usage has been steady across the support and ops teams, and the only open question I see is whether you want to add seats for finance. Are you free Tuesday or Wednesday for a 20-minute renewal check-in?

Best,

**Score**

Meaning 4, Template reduction 5, Rhythm 5, Specificity 5, Audience fit 5, Ethics 5.

**Penalty gate**

Score 100 / 100, threshold 95. Findings: none.

**Notes**

Replaces sales phrasing with timing, usage context, and a specific meeting ask.

### Case 28

**Prompt**

Rewrite this founder update after missing a target.

**Baseline AI-ish output**

While we did not fully achieve our planned growth target this quarter, we made meaningful progress across product, sales, and customer success, and remain confident in our ability to execute against our strategic roadmap.

**Humanized output**

We missed the quarter's growth target. The main issue was conversion after trial, especially in accounts where setup required customer data cleanup. Product shipped the import checklist late, and sales kept pushing deals into trial before that gap was fixed. This month we are moving two engineers onto activation and pausing outbound into the healthcare segment until the setup path is cleaner.

**Score**

Meaning 4, Template reduction 5, Rhythm 5, Specificity 5, Audience fit 5, Ethics 5.

**Penalty gate**

Score 100 / 100, threshold 95. Findings: none.

**Notes**

Keeps the miss visible and names the operational fix without glossy reassurance.

### Case 29

**Prompt**

Make this changelog entry more useful for users.

**Baseline AI-ish output**

We have optimized the dashboard experience with enhanced filtering capabilities, improved performance, and resolved multiple issues to provide a smoother and more efficient workflow for all users.

**Humanized output**

Dashboard filters now remember your last view, so you can come back to the same region, owner, and status without setting them again. Large tables also load faster on first open. We fixed the bug where exported CSV files sometimes dropped the status column.

**Score**

Meaning 5, Template reduction 5, Rhythm 5, Specificity 5, Audience fit 5, Ethics 5.

**Penalty gate**

Score 100 / 100, threshold 95. Findings: none.

**Notes**

Names the user-visible changes and one specific fix.

### Case 30

**Prompt**

Polish this professional bio without making it sound like a resume template.

**Baseline AI-ish output**

I am a strategic, innovative, and collaborative product leader with a proven track record of driving cross-functional alignment, delivering scalable solutions, and creating value through technology-enabled transformation.

**Humanized output**

I build B2B product teams around messy operational workflows. Most of my work has been in support tools, internal automation, and the handoff between product, design, and implementation. I care most about products that make repeated work easier to see and easier to finish.

**Score**

Meaning 4, Template reduction 5, Rhythm 5, Specificity 5, Audience fit 5, Ethics 5.

**Penalty gate**

Score 100 / 100, threshold 95. Findings: none.

**Notes**

Replaces broad leadership claims with domain, work type, and product preference.

### Case 31

**Prompt**

Rewrite this support reply in friendly, plain English.

**Baseline AI-ish output**

We apologize for the inconvenience you are experiencing. Please be assured that our team is actively investigating this matter and will provide further updates as soon as possible.

**Humanized output**

I checked your account and the export is failing at the file generation step. We are re-running it now and should have a new file ready within 30 minutes. I will send the download link in this thread once it finishes.

**Score**

Meaning 4, Template reduction 5, Rhythm 5, Specificity 5, Audience fit 5, Ethics 5.

**Penalty gate**

Score 100 / 100, threshold 95. Findings: none.

**Notes**

Turns empty assurance into status, timing, and next action.

### Case 32

**Prompt**

Polish this bilingual product tagline for an AI note-taking tool.

**Baseline AI-ish output**

AI 驱动的智能会议纪要助手 that empowers teams to unlock productivity, capture every insight, and build a seamless collaboration ecosystem.

**Humanized output**

AI meeting notes for teams that need decisions, owners, and follow-ups in one place. 开完会不用再翻录音找谁负责什么。

**Score**

Meaning 4, Template reduction 5, Rhythm 5, Specificity 5, Audience fit 5, Ethics 5.

**Penalty gate**

Score 100 / 100, threshold 95. Findings: none.

**Notes**

Keeps the bilingual format but makes the benefit concrete.

### Case 33

**Prompt**

Make this abstract paragraph less inflated while keeping an academic tone.

**Baseline AI-ish output**

This study provides a comprehensive and innovative exploration of how digital platforms fundamentally transform organizational knowledge flows and generate significant implications for future research and managerial practice.

**Humanized output**

This study examines how digital platforms change the way teams document, search for, and reuse internal knowledge. Its main contribution is a process-level account of where knowledge flow slows down and which platform features make reuse easier to observe.

**Score**

Meaning 5, Template reduction 5, Rhythm 5, Specificity 5, Audience fit 5, Ethics 5.

**Penalty gate**

Score 100 / 100, threshold 95. Findings: none.

**Notes**

Keeps the academic register while narrowing the contribution.

### Case 34

**Prompt**

Make this meeting follow-up sound less stiff.

**Baseline AI-ish output**

Thank you for the productive discussion today. As aligned during the meeting, we will move forward with the proposed implementation plan and coordinate with relevant stakeholders to ensure timely execution.

**Humanized output**

Good to speak today. I will send the revised rollout plan by Thursday morning, including the migration steps and owner list. Once you confirm the support window, we can lock the launch date and share it with the customer success team.

**Score**

Meaning 4, Template reduction 5, Rhythm 5, Specificity 5, Audience fit 5, Ethics 5.

**Penalty gate**

Score 100 / 100, threshold 95. Findings: none.

**Notes**

Replaces meeting boilerplate with deliverable, timing, and dependency.

### Case 35

**Prompt**

Rewrite this fundraising memo sentence in sharper investor language.

**Baseline AI-ish output**

Our company is positioned at the intersection of AI, workflow automation, and enterprise productivity, creating a unique opportunity to capture significant market share in a rapidly evolving landscape.

**Humanized output**

The wedge is customer support teams that still move escalation context across tickets, calls, and spreadsheets. Our product starts with escalation review, where managers already feel the time cost and where the first 20 customers are using the workflow every week.

**Score**

Meaning 4, Template reduction 5, Rhythm 5, Specificity 5, Audience fit 5, Ethics 5.

**Penalty gate**

Score 100 / 100, threshold 95. Findings: none.

**Notes**

Moves from category positioning to wedge, buyer pain, and proof.

### Case 36

**Prompt**

Turn this roadmap slide into a clearer product slide.

**Baseline AI-ish output**

Q3 roadmap: enhance onboarding, strengthen analytics, improve collaboration, optimize mobile experience, and continue building scalable infrastructure to support future growth.

**Humanized output**

**Q3 roadmap should reduce setup time first**

1. Onboarding gets the first two sprints because new teams still need too much help importing data.
2. Analytics comes next, focused on activation and weekly usage. The full reporting suite stays outside this quarter.
3. Mobile improvements stay limited to approval review and status checks.
4. Infrastructure work continues in the background where it protects launch reliability.

**Score**

Meaning 5, Template reduction 5, Rhythm 5, Specificity 5, Audience fit 5, Ethics 5.

**Penalty gate**

Score 100 / 100, threshold 95. Findings: none.

**Notes**

Adds sequencing and tradeoffs while preserving all roadmap areas.

### Case 37

**Prompt**

Rewrite this board update slide for clarity.

**Baseline AI-ish output**

Highlights: revenue continued to grow; challenges: sales cycle lengthened; opportunities: new vertical expansion; next steps: accelerate GTM execution and strengthen product differentiation.

**Humanized output**

**Revenue is still growing, but sales cycles are stretching**

- New pipeline is coming from the same core buyer, so vertical expansion can wait until conversion is steadier.
- The near-term watch item is cycle length by deal size.
- GTM work this month should focus on cleaner qualification and sharper proof for the current segment.

**Score**

Meaning 4, Template reduction 5, Rhythm 5, Specificity 4, Audience fit 5, Ethics 5.

**Penalty gate**

Score 100 / 100, threshold 95. Findings: none.

**Notes**

Turns a template slide into a board-level readout and next focus.

### Case 38

**Prompt**

Rewrite this PRD opening so engineering can act on it.

**Baseline AI-ish output**

To improve user engagement and drive long-term retention, we propose building a personalized notification system that can deliver the right information to the right user at the right time.

**Humanized output**

Users miss follow-up tasks after a meeting because the app only stores notes and does not surface pending owners. The first version should send one daily digest for tasks due in the next 48 hours. Scope is limited to tasks created from meeting notes, with email as the only delivery channel.

**Score**

Meaning 4, Template reduction 5, Rhythm 5, Specificity 5, Audience fit 5, Ethics 5.

**Penalty gate**

Score 100 / 100, threshold 95. Findings: none.

**Notes**

Defines problem, trigger, channel, and first scope.

### Case 39

**Prompt**

De-template this OKR review paragraph.

**Baseline AI-ish output**

This quarter, the team made strong progress toward our objectives, achieved meaningful improvements in key results, and identified several opportunities for continued optimization in the next cycle.

**Humanized output**

The team improved activation from 38 percent to 46 percent, mainly after we simplified setup for invited teammates. Retention did not move much, and interviews point to a handoff gap after the first project. Next cycle should focus on the second-week experience rather than adding another acquisition channel.

**Score**

Meaning 4, Template reduction 5, Rhythm 5, Specificity 5, Audience fit 5, Ethics 5.

**Penalty gate**

Score 100 / 100, threshold 95. Findings: none.

**Notes**

Adds result, miss, evidence, and next-cycle focus.

### Case 40

**Prompt**

Make this sales deck page less generic.

**Baseline AI-ish output**

Our solution helps enterprises streamline workflows, improve collaboration, reduce costs, and unlock data-driven insights through an integrated platform designed for modern teams.

**Humanized output**

**For support leaders managing escalations across tools**

Before, a manager checks the ticket, call notes, Slack thread, and spreadsheet before deciding what happened. With this workflow, the escalation summary, owner, deadline, and customer status sit on one page. The first use case is weekly escalation review.

**Score**

Meaning 4, Template reduction 5, Rhythm 5, Specificity 5, Audience fit 5, Ethics 5.

**Penalty gate**

Score 100 / 100, threshold 95. Findings: none.

**Notes**

Narrows the buyer and shows a concrete before/after workflow.

### Case 41

**Prompt**

Rewrite this research memo summary in a less AI-ish way.

**Baseline AI-ish output**

The market demonstrates substantial growth potential, supported by favorable policy trends, expanding customer demand, and continuous technological innovation, creating attractive opportunities for leading companies.

**Humanized output**

The setup is worth tracking, but the current evidence is still early. Policy support has improved project approvals, and demand is visible in tender volume. The next check is whether leading suppliers convert those tenders into signed orders with delivery schedules. Valuation should stay tied to confirmed backlog rather than market-size language.

**Score**

Meaning 4, Template reduction 5, Rhythm 5, Specificity 5, Audience fit 5, Ethics 5.

**Penalty gate**

Score 100 / 100, threshold 95. Findings: none.

**Notes**

Moves from broad opportunity language to evidence and valuation discipline.

### Case 42

**Prompt**

Rewrite this onboarding document opening for new employees.

**Baseline AI-ish output**

Welcome to the company. This document is designed to help you quickly understand our culture, workflows, tools, and collaboration practices so that you can integrate into the team efficiently.

**Humanized output**

Welcome. Your first week will be easier if you start with three things in this order. Set up the core tools, read the team operating notes, then book short intro calls with your manager and project buddy. This guide is meant to help you find the right documents and avoid asking the same setup questions twice.

**Score**

Meaning 5, Template reduction 5, Rhythm 5, Specificity 5, Audience fit 5, Ethics 5.

**Penalty gate**

Score 100 / 100, threshold 95. Findings: none.

**Notes**

Gives new hires an actionable first-week sequence.

### Case 43

**Prompt**

De-template this pricing proposal paragraph.

**Baseline AI-ish output**

Our pricing model is designed to provide flexible, scalable, and cost-effective options for organizations of all sizes, ensuring that every customer can select the plan that best meets their evolving business needs.

**Humanized output**

Pricing should follow the rollout path. Start with the team plan if fewer than 30 people need access and usage is still concentrated in one department. Move to the enterprise plan when SSO, audit logs, or cross-department reporting becomes part of the buying requirement. That keeps the first contract smaller and leaves room to expand after adoption is visible.

**Score**

Meaning 4, Template reduction 5, Rhythm 5, Specificity 5, Audience fit 5, Ethics 5.

**Penalty gate**

Score 100 / 100, threshold 95. Findings: none.

**Notes**

Turns abstract pricing flexibility into decision guidance.

### Case 44

**Prompt**

Humanize this workshop recap.

**Baseline AI-ish output**

The workshop generated valuable insights across customer needs, product opportunities, and future innovation directions. Participants actively contributed ideas and aligned on several strategic priorities for follow-up execution.

**Humanized output**

The workshop produced two concrete outputs. We agreed that onboarding friction is the first customer problem to tackle, and we collected 14 examples of where setup breaks. The open question is whether the fix belongs in product, implementation, or both. Priya will turn the notes into a one-page decision memo by Friday.

**Score**

Meaning 5, Template reduction 5, Rhythm 5, Specificity 5, Audience fit 5, Ethics 5.

**Penalty gate**

Score 100 / 100, threshold 95. Findings: none.

**Notes**

Captures decisions, open question, owner, and artifact.

### Case 45

**Prompt**

Make this restaurant hero image prompt less generic.

**Baseline AI-ish output**

Beautiful modern restaurant interior, warm cinematic lighting, elegant tables, cozy atmosphere, premium dining experience, ultra-realistic, 8K, highly detailed, award-winning photography.

**Humanized output**

Wide hero photo for a neighborhood restaurant website. Camera at seated eye level near a two-person table, with the bar and open kitchen softly visible in the back. Early evening window light, warm pendant lamps, linen napkins, water glasses with slight reflections, one server crossing the frame. Leave the upper-left area calm for headline text.

**Score**

Meaning 5, Template reduction 5, Rhythm 5, Specificity 5, Audience fit 5, Ethics 5.

**Penalty gate**

Score 100 / 100, threshold 95. Findings: none.

**Notes**

Replaces quality tags with use case, camera height, scene details, and text-safe space.

### Case 46

**Prompt**

Rewrite this mobile app onboarding illustration prompt as art direction.

**Baseline AI-ish output**

Friendly futuristic app onboarding illustration showing people using AI productivity tools, clean modern style, gradient background, floating cards, 3D icons, delightful and engaging.

**Humanized output**

Onboarding illustration for the first screen of a task-planning app. Show one person reviewing a short task list on a phone while a laptop nearby shows simple calendar blocks. Flat editorial style, soft off-white background, small blue and green accents, clear empty space at the top for app copy. Keep UI shapes simple and unreadable.

**Score**

Meaning 5, Template reduction 5, Rhythm 5, Specificity 5, Audience fit 5, Ethics 5.

**Penalty gate**

Score 100 / 100, threshold 95. Findings: none.

**Notes**

Defines screen purpose, subject action, style, palette, and text handling.

### Case 47

**Prompt**

De-AI this children's book cover prompt.

**Baseline AI-ish output**

Magical whimsical children's book cover with a brave little girl exploring a dreamy forest full of glowing creatures, enchanting atmosphere, vibrant colors, masterpiece, highly detailed, fantasy style.

**Humanized output**

Children's book cover for ages 6 to 8. A girl in a yellow raincoat stands at the edge of a damp forest path, holding a small red lunchbox. Fireflies gather near a hollow tree, but the scene stays gentle rather than scary. Leave the top quarter clear for title lettering and the lower-right corner open for author name.

**Score**

Meaning 5, Template reduction 5, Rhythm 5, Specificity 5, Audience fit 5, Ethics 5.

**Penalty gate**

Score 100 / 100, threshold 95. Findings: none.

**Notes**

Adds audience, cover layout, focal character, props, and mood.

### Case 48

**Prompt**

Make this ecommerce lifestyle image prompt more realistic.

**Baseline AI-ish output**

Stunning lifestyle photo of a premium ceramic desk lamp in a beautiful minimalist home office, soft cinematic lighting, elegant decor, hyper-realistic, luxury aesthetic, trending design.

**Humanized output**

Lifestyle product photo for a ceramic desk lamp. Place the lamp on a walnut desk beside a closed notebook, a pencil, and a half-full coffee cup. Morning light from a window on the right, matte ceramic texture, visible power cord tucked behind the base, neutral wall, modest home office setting.

**Score**

Meaning 5, Template reduction 5, Rhythm 5, Specificity 5, Audience fit 5, Ethics 5.

**Penalty gate**

Score 100 / 100, threshold 95. Findings: none.

**Notes**

Makes the product scale, material, setting, and everyday context visible.

### Case 49

**Prompt**

Rewrite this conference keynote background prompt.

**Baseline AI-ish output**

Futuristic AI conference stage background with glowing network lines, abstract data waves, blue purple gradient, high-tech atmosphere, epic cinematic lighting, ultra-detailed.

**Humanized output**

Wide keynote background for a 16:9 stage screen. Use a dark neutral base with a slow field of thin data lines moving diagonally across the right side. Keep the center-left area quiet for speaker silhouette and title overlay. Low contrast, no readable text, no bright shapes near the podium area.

**Score**

Meaning 5, Template reduction 5, Rhythm 5, Specificity 5, Audience fit 5, Ethics 5.

**Penalty gate**

Score 100 / 100, threshold 95. Findings: none.

**Notes**

Translates generic tech atmosphere into stage-safe composition and projection constraints.

### Case 50

**Prompt**

Turn this science explainer image prompt into clear visual direction.

**Baseline AI-ish output**

Beautiful detailed illustration of cells communicating through molecular signals, glowing particles, vibrant colors, futuristic biomedical visualization, 8K, masterpiece, highly detailed, educational.

**Humanized output**

Educational figure for a high-school biology explainer. Show three cells arranged left to right, with small messenger molecules moving from the first cell to receptors on the second. Use a clean cutaway style, muted teal and coral accents, and leave blank space under each cell for labels added later. Keep the biology simplified and readable.

**Score**

Meaning 5, Template reduction 5, Rhythm 5, Specificity 5, Audience fit 5, Ethics 5.

**Penalty gate**

Score 100 / 100, threshold 95. Findings: none.

**Notes**

Specifies audience, diagram structure, visual hierarchy, and label space.

## Aggregate Assessment

Final pass rate: 50 of 50 cases meet the rubric passing bar.

## Penalty Gate Result

Threshold: 95.

Forbidden-structure counts across accepted humanized outputs:

- Forced Chinese contrast: 0
- Problem-not-in frame: 0
- Negative-first opening: 0
- Broad English negative contrast: 0
- Trailing not-frame: 0
- Not-alone contrast: 0
- Colon-led label explanation: 0
- Quoted framing label: 0
- Plus-stack shorthand: 0

All accepted humanized outputs scored at least 95. Any candidate below the threshold must be revised and scored again before delivery.

Average strengths:

- Template reduction: consistently strong across all categories.
- Natural rhythm: strongest in Chinese social/client writing and English email use cases.
- Specificity: strong after Iteration 6 because PPT and image prompt references force concrete actions, while the penalty gate now blocks broad contrast and label-like sentence structures before output is accepted.

Remaining limitations:

- If source text lacks real facts, the skill must either ask for details or clearly mark inserted details as placeholders.
- For regulated, academic, legal, medical, or investment content, meaning preservation and source fidelity matter more than natural style.
- The skill improves prompt and copy quality. It should not be positioned as an AI-detection bypass tool.
