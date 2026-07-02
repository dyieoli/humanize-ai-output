# Evaluation Prompts

These fixtures cover the four core capability areas. Baseline outputs are intentionally AI-ish so the skill has clear failure modes to correct.

## Chinese writing naturalization

### Case 1

Prompt: 把这段项目周报改得更像真人写的，适合发给老板。

Baseline AI-ish output: 本周我们围绕核心目标持续推进相关工作，其中登录模块已经完成后端联调，数据看板口径仍待财务确认，支付回调也需要风控规则进一步明确。如果周三前相关事项无法确认，测试包可能顺延一天。下一步我们将通过多方协同和高效沟通，持续优化执行路径，确保项目稳步推进。

Expected improvement: concrete progress, risks, owner, deadline, fewer empty phrases.

### Case 2

Prompt: 把这段小红书文案改得自然一点，不要像 AI。

Baseline AI-ish output: 今天想和大家分享一个非常重要的观点：自律不是压抑自己，而是成就更好的自己。以前我会把晚上安排得非常充实，包括运动、读书和复盘，但往往坚持三天就失败。后来我改成洗完澡只看 10 页书，只要坚持下去，就一定会遇见更优秀的自己。

Expected improvement: less motivational cliche, more lived-in detail, lighter rhythm.

### Case 3

Prompt: 改写这段客户道歉回复，要真诚但不过度卑微。

Baseline AI-ish output: 非常抱歉订单状态没有及时同步，导致客服看到的信息滞后，也让您多等了。我们对此高度重视，将在今天 18:00 前给您更新处理结果；如果需要补发或退款，我们将按您的选择处理。我们将立即进行内部复盘，并持续优化服务流程，感谢您的理解与支持。

Expected improvement: name the issue, action, compensation or next step, deadline.

### Case 4

Prompt: 把这段中文分析改得更像投资研究员写的。

Baseline AI-ish output: 该公司具备较强的发展潜力，未来有望受益于行业趋势。目前需要重点关注试点订单能否进入批量交付、放量后毛利率能否维持，以及后续公告是否只有合作框架而缺少交付节奏和收入确认。同时也需要关注大客户议价、替代供应商进入、政策变化和业绩兑现等风险。

Expected improvement: concrete thesis, evidence type, deciding variables, risk trigger.

## English and bilingual polish

### Case 5

Prompt: Rewrite this investor update in crisp, natural English.

Baseline AI-ish output: We are pleased to share that our team shipped the beta to 12 design partners this month and made significant progress across multiple dimensions. The review workflow has received positive feedback, while admin controls remain a key blocker for wider rollout. Going forward, July will be focused on activation and retention as we continue to execute with discipline to create long-term value.

Expected improvement: concrete milestones, metrics, risks, ask, founder-like voice.

### Case 6

Prompt: Polish this bilingual LinkedIn intro without making it sound inflated.

Baseline AI-ish output: I am a passionate and results-driven professional with rich experience in AI product innovation, prompt design, product strategy, and internal tool adoption, 致力于帮助团队减少人工审核、加快协作交接 and creating impactful solutions.

Expected improvement: remove resume cliches, smooth language mix, clarify work and audience.

### Case 7

Prompt: Make this English email warmer and less robotic.

Baseline AI-ish output: Dear Sarah, I hope this email finds you well. I am writing to follow up on the rollout plan we discussed last week and kindly inquire whether there are any timing updates from your side, as this will help us decide whether to hold the engineering slot for next sprint.

Expected improvement: shorter opening, specific context, clear ask, less excessive politeness.

### Case 8

Prompt: Improve this Chinese-to-English translation for a product website.

Baseline AI-ish output: Our platform helps enterprise operations teams realize intelligent transformation by bringing scattered approvals, files, and status updates into a unified closed-loop digital ecosystem, thereby improving operational efficiency and reducing time spent chasing context.

Expected improvement: plain product value, clear user, use case, and outcome.

## PPT and document de-templating

### Case 9

Prompt: Turn this slide into a sharper executive slide.

Baseline AI-ish output: 背景：行业快速发展；挑战：新进入者正在 6 到 9 个月内压缩功能差距，竞争日益激烈；策略：我们需要依托客户工作流深度持续创新；展望：未来空间广阔，下一阶段应优先提升现有客户留存，再考虑进入新客群。

Expected improvement: claim title, quantified facts, decision implication, fewer generic bullets.

### Case 10

Prompt: Rewrite this strategy document opening so it does not sound like a template.

Baseline AI-ish output: 在当今快速变化的市场环境中，企业面临前所未有的机遇与挑战。过去三个月，销售线索没有减少，但从试用到付费的转化明显变慢，尤其是客户试用后的第一周，使用数据、客户反馈和下一步动作没有形成系统化衔接。为了实现高质量发展，我们需要构建系统化能力。

Expected improvement: actual business situation, named tension, no generic era framing.

### Case 11

Prompt: Humanize this meeting summary for senior stakeholders.

Baseline AI-ish output: 本次会议围绕 MVP 范围、数据口径和上线日期进行了充分讨论，并形成了重要共识：本周只保留登录、导入和基础看板，数据口径由财务最终确认，产品不再自行做临时解释；上线日期尚未确定，取决于周四前能否拿到真实数据样本。后续由产品负责范围变更，财务确认口径，研发评估延期影响。

Expected improvement: decisions, unresolved disagreements, owners, deadlines, tradeoffs.

### Case 12

Prompt: De-template this consulting recommendation slide.

Baseline AI-ish output: 建议从组织、流程、技术、数据四个维度协同发力，围绕重复交接场景明确 owner、统一输入和审核标准、自动化每周重复发生的检查，并以每次交接节省的小时数作为衡量指标。建议先在 30 天内选择一个工作流完成前后耗时统计，打造可持续增长的新引擎。

Expected improvement: actionable sequence, cost, owner, first move, expected impact.

## Image prompt de-AI-styling

### Case 13

Prompt: Make this portrait image prompt less AI-generic.

Baseline AI-ish output: Ultra-realistic cinematic portrait of a 29-year-old hardware founder in a workshop, sleeves rolled up, sitting near prototype parts and a half-open laptop, calm but tired expression, dramatic window lighting, 8K, masterpiece, highly detailed, shallow depth of field.

Expected improvement: photographer-style direction with subject, wardrobe, location, light, mood.

### Case 14

Prompt: De-AI this product render prompt for a premium coffee machine.

Baseline AI-ish output: Futuristic sleek premium home espresso machine with brushed stainless steel body, compact rectangular footprint, tactile black knobs, visible portafilter, small cup tray with a few water marks, placed on a warm stone kitchen counter, luxury aesthetic, award-winning design, hyper-detailed, studio lighting, black background, trending on ArtStation, no logo or text.

Expected improvement: materials, proportions, usage context, surface detail, realistic lighting.

### Case 15

Prompt: Make this travel photo prompt feel less like stock AI art.

Baseline AI-ish output: Beautiful Asian woman in a navy coat walking through a charming European side street in Porto after light rain while checking a folded map, tiled storefronts, wet cobblestones, parked scooter in the foreground, everyday pedestrians in the distance, golden hour, cinematic, vibrant colors, dreamy atmosphere, ultra high resolution.

Expected improvement: believable place details, candid framing, natural posture, imperfect environment.

### Case 16

Prompt: Rewrite this poster prompt so it sounds like art direction.

Baseline AI-ish output: A stunning cyberpunk night-market sci-fi festival poster with layered signs, wet pavement, food stalls, pedestrians, room for title typography in the upper-left area, cyan red and warm white neon lights, futuristic vibes, epic composition, detailed, sharp, 4K, masterpiece, no readable text.

Expected improvement: poster purpose, hierarchy, typography space, color constraints, exclusions.
