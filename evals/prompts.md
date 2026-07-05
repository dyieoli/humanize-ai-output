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

## Expanded coverage cases

### Case 17

Prompt: 把这段团队通知改得自然一点，适合发在项目群里。

Baseline AI-ish output: 各位同事，为了进一步提升项目协同效率，确保本周版本发布目标顺利达成，请大家积极配合相关工作安排。测试同学需尽快完成回归验证，研发同学需及时修复问题，产品同学需持续跟进需求闭环。

Expected improvement: concrete owners, timing, group-message tone, fewer generic coordination phrases.

### Case 18

Prompt: 把这段产品更新说明改得像真实产品经理写的。

Baseline AI-ish output: 本次版本升级围绕用户体验优化和功能完善展开，新增消息筛选能力，优化列表加载速度，并修复若干已知问题，致力于为用户带来更加高效、稳定、便捷的使用体验。

Expected improvement: specific change list, user-visible impact, plain wording.

### Case 19

Prompt: 改写这段创始人公开说明，要克制、可信。

Baseline AI-ish output: 对于近期发货延迟给用户造成的不便，我们深表歉意。我们高度重视每一位用户的体验，将持续优化供应链管理能力，提升履约效率，以更加负责任的态度回馈广大用户的信任。

Expected improvement: acknowledge delay, give concrete reason and deadline, avoid PR language.

### Case 20

Prompt: 把这段学习心得改得更像个人记录。

Baseline AI-ish output: 学习英语的关键不是短期突击，而是建立长期坚持的习惯。通过每天背单词、听听力和进行口语练习，可以逐步提升综合语言能力，实现自我成长。

Expected improvement: lived-in detail, less slogan, direct affirmative style.

### Case 21

Prompt: 把这段投研风险提示改得更像内部备忘录。

Baseline AI-ish output: 该标的虽然具备较强成长性，但仍需警惕多重风险因素，包括下游需求波动、原材料价格上涨、客户集中度较高以及行业竞争加剧等因素对公司盈利能力产生的不利影响。

Expected improvement: rank the risks, name the first thing to watch, keep analyst tone.

### Case 22

Prompt: 改写这封候选人拒信，要真诚但不拖沓。

Baseline AI-ish output: 非常感谢您参与本次面试流程。经过综合评估，我们认为您的经历与当前岗位要求仍存在一定差距，因此很遗憾本次无法继续推进。祝您未来职业发展顺利。

Expected improvement: respectful, concise, no vague corporate evaluation tone.

### Case 23

Prompt: 把这段社群活动邀请改得更像人写的。

Baseline AI-ish output: 为了帮助大家更好地了解 AI 工具在个人成长和职场效率提升中的应用价值，我们将举办一次线上分享活动，欢迎大家积极报名参与，共同探索 AI 时代的新机遇。

Expected improvement: concrete topic, time, audience, less event-template wording.

### Case 24

Prompt: 把这段运营 SOP 改得更可执行。

Baseline AI-ish output: 用户反馈需要及时响应并形成闭环，相关负责人应根据问题类型进行分类处理，持续优化用户体验，并通过数据分析不断提升运营效率。

Expected improvement: triage steps, owner, timing, output format.

### Case 25

Prompt: 把这段用户评价改得真实一点，少一点广告感。

Baseline AI-ish output: 这款笔记软件极大提升了我的工作效率，界面简洁美观，功能强大完善，让我在学习和工作中都能获得前所未有的流畅体验，强烈推荐给每一个追求高效的人。

Expected improvement: specific use case, measured praise, natural imperfection.

### Case 26

Prompt: 把这段论文致谢改得自然、得体。

Baseline AI-ish output: 在论文完成过程中，我得到了导师、同学和家人的大力支持与帮助，在此向所有给予我关心、指导和鼓励的人表示最诚挚的感谢。

Expected improvement: specific support, restrained emotion, no template gratitude.

### Case 27

Prompt: Rewrite this renewal email so it sounds like a real account manager.

Baseline AI-ish output: Dear Alex, we are excited to continue partnering with your team and would like to proactively discuss renewal options that can unlock additional value across your organization while ensuring a seamless continuation of service.

Expected improvement: clear reason for reaching out, timing, next step, less sales language.

### Case 28

Prompt: Rewrite this founder update after missing a target.

Baseline AI-ish output: While we did not fully achieve our planned growth target this quarter, we made meaningful progress across product, sales, and customer success, and remain confident in our ability to execute against our strategic roadmap.

Expected improvement: direct miss, what changed, what is being fixed, no glossy reassurance.

### Case 29

Prompt: Make this changelog entry more useful for users.

Baseline AI-ish output: We have optimized the dashboard experience with enhanced filtering capabilities, improved performance, and resolved multiple issues to provide a smoother and more efficient workflow for all users.

Expected improvement: concrete changes, user action, visible impact.

### Case 30

Prompt: Polish this professional bio without making it sound like a resume template.

Baseline AI-ish output: I am a strategic, innovative, and collaborative product leader with a proven track record of driving cross-functional alignment, delivering scalable solutions, and creating value through technology-enabled transformation.

Expected improvement: specific domain, plain verbs, stable professional voice.

### Case 31

Prompt: Rewrite this support reply in friendly, plain English.

Baseline AI-ish output: We apologize for the inconvenience you are experiencing. Please be assured that our team is actively investigating this matter and will provide further updates as soon as possible.

Expected improvement: state what is happening, give timing, avoid empty assurance.

### Case 32

Prompt: Polish this bilingual product tagline for an AI note-taking tool.

Baseline AI-ish output: AI 驱动的智能会议纪要助手 that empowers teams to unlock productivity, capture every insight, and build a seamless collaboration ecosystem.

Expected improvement: natural bilingual handling, clear user benefit, no stock AI vocabulary.

### Case 33

Prompt: Make this abstract paragraph less inflated while keeping an academic tone.

Baseline AI-ish output: This study provides a comprehensive and innovative exploration of how digital platforms fundamentally transform organizational knowledge flows and generate significant implications for future research and managerial practice.

Expected improvement: precise contribution, restrained claims, academic but readable.

### Case 34

Prompt: Make this meeting follow-up sound less stiff.

Baseline AI-ish output: Thank you for the productive discussion today. As aligned during the meeting, we will move forward with the proposed implementation plan and coordinate with relevant stakeholders to ensure timely execution.

Expected improvement: concrete next steps, owner, timing, less meeting-template language.

### Case 35

Prompt: Rewrite this fundraising memo sentence in sharper investor language.

Baseline AI-ish output: Our company is positioned at the intersection of AI, workflow automation, and enterprise productivity, creating a unique opportunity to capture significant market share in a rapidly evolving landscape.

Expected improvement: name the wedge, customer pain, proof point, no grand positioning.

### Case 36

Prompt: Turn this roadmap slide into a clearer product slide.

Baseline AI-ish output: Q3 roadmap: enhance onboarding, strengthen analytics, improve collaboration, optimize mobile experience, and continue building scalable infrastructure to support future growth.

Expected improvement: sequence, user outcome, tradeoff, fewer equal-weight bullets.

### Case 37

Prompt: Rewrite this board update slide for clarity.

Baseline AI-ish output: Highlights: revenue continued to grow; challenges: sales cycle lengthened; opportunities: new vertical expansion; next steps: accelerate GTM execution and strengthen product differentiation.

Expected improvement: direct headline, numbers placeholders avoided unless given, clear watch item.

### Case 38

Prompt: Rewrite this PRD opening so engineering can act on it.

Baseline AI-ish output: To improve user engagement and drive long-term retention, we propose building a personalized notification system that can deliver the right information to the right user at the right time.

Expected improvement: problem, trigger, user behavior, first scope.

### Case 39

Prompt: De-template this OKR review paragraph.

Baseline AI-ish output: This quarter, the team made strong progress toward our objectives, achieved meaningful improvements in key results, and identified several opportunities for continued optimization in the next cycle.

Expected improvement: real result structure, what moved, what missed, next focus.

### Case 40

Prompt: Make this sales deck page less generic.

Baseline AI-ish output: Our solution helps enterprises streamline workflows, improve collaboration, reduce costs, and unlock data-driven insights through an integrated platform designed for modern teams.

Expected improvement: specific buyer, workflow, before/after outcome.

### Case 41

Prompt: Rewrite this research memo summary in a less AI-ish way.

Baseline AI-ish output: The market demonstrates substantial growth potential, supported by favorable policy trends, expanding customer demand, and continuous technological innovation, creating attractive opportunities for leading companies.

Expected improvement: decision variables, evidence type, valuation caution.

### Case 42

Prompt: Rewrite this onboarding document opening for new employees.

Baseline AI-ish output: Welcome to the company. This document is designed to help you quickly understand our culture, workflows, tools, and collaboration practices so that you can integrate into the team efficiently.

Expected improvement: useful first-week orientation, concrete next action, warmer voice.

### Case 43

Prompt: De-template this pricing proposal paragraph.

Baseline AI-ish output: Our pricing model is designed to provide flexible, scalable, and cost-effective options for organizations of all sizes, ensuring that every customer can select the plan that best meets their evolving business needs.

Expected improvement: concrete plan logic, tradeoffs, decision guidance.

### Case 44

Prompt: Humanize this workshop recap.

Baseline AI-ish output: The workshop generated valuable insights across customer needs, product opportunities, and future innovation directions. Participants actively contributed ideas and aligned on several strategic priorities for follow-up execution.

Expected improvement: what was decided, what remains open, owner and artifact.

### Case 45

Prompt: Make this restaurant hero image prompt less generic.

Baseline AI-ish output: Beautiful modern restaurant interior, warm cinematic lighting, elegant tables, cozy atmosphere, premium dining experience, ultra-realistic, 8K, highly detailed, award-winning photography.

Expected improvement: real interior details, camera position, light, dining context, no quality tags.

### Case 46

Prompt: Rewrite this mobile app onboarding illustration prompt as art direction.

Baseline AI-ish output: Friendly futuristic app onboarding illustration showing people using AI productivity tools, clean modern style, gradient background, floating cards, 3D icons, delightful and engaging.

Expected improvement: concrete screen purpose, composition, character action, restrained style.

### Case 47

Prompt: De-AI this children's book cover prompt.

Baseline AI-ish output: Magical whimsical children's book cover with a brave little girl exploring a dreamy forest full of glowing creatures, enchanting atmosphere, vibrant colors, masterpiece, highly detailed, fantasy style.

Expected improvement: cover layout, age range, focal character, text-safe space, specific mood.

### Case 48

Prompt: Make this ecommerce lifestyle image prompt more realistic.

Baseline AI-ish output: Stunning lifestyle photo of a premium ceramic desk lamp in a beautiful minimalist home office, soft cinematic lighting, elegant decor, hyper-realistic, luxury aesthetic, trending design.

Expected improvement: product scale, surface, surrounding objects, plausible light.

### Case 49

Prompt: Rewrite this conference keynote background prompt.

Baseline AI-ish output: Futuristic AI conference stage background with glowing network lines, abstract data waves, blue purple gradient, high-tech atmosphere, epic cinematic lighting, ultra-detailed.

Expected improvement: stage use case, readable space, restrained motion background, projection constraints.

### Case 50

Prompt: Turn this science explainer image prompt into clear visual direction.

Baseline AI-ish output: Beautiful detailed illustration of cells communicating through molecular signals, glowing particles, vibrant colors, futuristic biomedical visualization, 8K, masterpiece, highly detailed, educational.

Expected improvement: audience, diagram layout, labeled-space planning, scientific clarity without quality tags.

## Forced Contrast and Formality Stress Cases

### Case 51

Prompt: 把这段科研综述改得更像严肃但可读的研究说明。

Baseline AI-ish output: 基因驱动技术的应用不是单纯的基因编辑效率问题，而是涉及生态系统稳定性、种群动态和跨物种基因流动的系统性风险评估。当前研究普遍认为，需要从分子机制、生态影响和监管框架三个维度协同发力，构建更加完善的生物安全评价体系，为转基因昆虫的田间释放提供科学决策依据。

Expected improvement: remove forced contrast, keep scientific risk dimensions, reduce slogan-like research framing.

### Case 52

Prompt: 把这段年终个人总结改得自然一点，保留一点正式感。

Baseline AI-ish output: 回顾这一年，我深刻意识到成长不是一蹴而就的过程，而是持续自我迭代的旅程。无论是工作中面临的挑战，还是生活里的起起伏伏，我都努力保持积极的心态，不断突破自己的舒适区。展望新的一年，我将继续脚踏实地，追求更高质量的自我提升。

Expected improvement: less slogan-like self-growth language, natural reflection, formal but personal tone.

### Case 53

Prompt: 把这段产品发布通稿开头改得更像真实发布稿。

Baseline AI-ish output: 在数字化转型加速的今天，企业对于高效协同办公的需求日益增长。我们很高兴地宣布，全新升级的智能办公平台正式上线，致力于通过 AI 赋能打破部门壁垒，实现数据互联互通，为用户带来更加流畅顺畅的协作体验。

Expected improvement: direct launch context, concrete product changes, less generic digital-transformation setup.

### Case 54

Prompt: 把这段会议纪要总结改得更自然，避免强对照套话。

Baseline AI-ish output: 这次会议的核心不是简单地分配任务。这是一次重新梳理团队协作机制的机会。与会人员一致认为，当前的问题并非资源不足，而在于流程节点之间缺乏有效衔接，导致信息传递滞后。

Expected improvement: catch split forced contrast and synonym contrast, state meeting conclusion directly.

### Case 55

Prompt: 把这段读书笔记/书评改得少一点 AI 味。

Baseline AI-ish output: 读完这本书，我最大的感受是，真正的智慧不是知道所有答案，而是学会提出正确的问题。作者用大量生动的案例告诉我们，成长的关键往往藏在那些看似微不足道的日常选择之中，值得每一位读者细细品味。

Expected improvement: less aphoristic contrast, more specific reading impression, restrained praise.

### Case 56

Prompt: 把这段简历自我评价改得更具体、更可信。

Baseline AI-ish output: 本人具备扎实的专业基础和良好的团队协作能力，在过往的工作经历中，始终秉持精益求精的工作态度，善于在压力下保持高效执行力。同时具备较强的学习能力和创新思维，能够快速适应不同的工作环境，为团队创造持续价值。

Expected improvement: replace resume stock phrases with concrete responsibilities and working habits.

### Case 57

Prompt: 把这段公众号推文开头改得自然一点。

Baseline AI-ish output: 你有没有想过，为什么有些人总能在人群中脱颖而出？答案其实很简单：他们不是天赋异禀，而是掌握了正确的方法论。今天这篇文章，我将从三个维度为大家拆解这个问题，希望能给你带来一些启发。

Expected improvement: avoid hook-template contrast and colon answer, open with a direct topic.

### Case 58

Prompt: 把这段网络故障客服道歉话术改得真诚、明确。

Baseline AI-ish output: 非常抱歉给您的使用体验带来不便。我们已高度重视此次网络异常问题，技术团队正在全力排查根本原因，预计将在最短时间内完成修复。后续我们也会持续优化系统稳定性，感谢您一直以来的理解与支持。

Expected improvement: clear apology, next update timing, less empty assurance, no invented root cause.

### Case 59

Prompt: Rewrite this English business email feedback request so it sounds natural and concise.

Baseline AI-ish output: I hope this email finds you well. I wanted to reach out to kindly request your valuable feedback on the proposal we discussed last week. Your insights are not just important to us, but essential in helping us refine our approach and ensure we deliver a solution that truly meets your needs. Looking forward to hearing your thoughts at your earliest convenience.

Expected improvement: shorter email, concrete feedback ask, avoid over-polished broad contrast.

### Case 60

Prompt: 把这段组织效率分析改得自然一点，专门处理“并非...而是...”这类同义强对照。

Baseline AI-ish output: 团队效率低下的根源并非成员能力不足，而是缺乏清晰的责任分工和统一的沟通机制。要解决这个问题，需要综合考虑组织架构、流程设计和工具支持等多个因素，通过系统性的变革实现效率的整体提升。

Expected improvement: catch synonym forced contrast, name the workflow variables, replace broad transformation language with next steps.
