---
name: humanize-ai-output
description: Use when polishing AI-generated or AI-assisted Chinese writing, English writing, bilingual copy, presentation/document language, design briefs, or image prompts to reduce stiff, generic, templated, over-polished, translation-like, or obviously AI-shaped output while preserving meaning.
---

# Humanize AI Output

## Goal

Revise AI-assisted output so it feels edited, specific, and audience-aware. Preserve facts, citations, names, numbers, user intent, format constraints, and required terminology.

Use this skill for:

- Chinese text naturalization.
- English and bilingual polish.
- PPT and document de-templating.
- Image prompt de-AI-styling.

Do not claim to bypass AI detection, falsify authorship, fabricate human experience, hide required disclosure, or make unsupported claims.

## Quick Workflow

1. Identify the artifact type: Chinese prose, English prose, bilingual copy, PPT/document, design brief, or image prompt.
2. Extract fixed constraints: facts, numbers, claims, audience, tone, required format, citations, brand terms, and forbidden changes.
3. Create variation before rewriting.
   - If tools are available, run `scripts/style_seed.py --task <chinese|english|bilingual|ppt|document|image>`.
   - If tools are not available, silently choose one variation recipe from `references/variation-recipes.md`.
4. Diagnose the AI-ish patterns.
   - For Chinese, read `references/chinese-style-patterns.md` when the draft has strong contrast phrases like `不是...而是...`, slogan-like wording, or stiff transitions.
   - For English or bilingual text, read `references/english-bilingual-patterns.md` when the draft has corporate fog, translationese, or over-polished rhythm.
   - For slides, documents, and design briefs, read `references/design-and-ppt-patterns.md`.
   - For image prompts, read `references/image-prompt-patterns.md`.
5. Rewrite in passes:
   - Cut generic openings, recap endings, and low-information phrases.
   - Replace forced contrast patterns such as `不是...而是...`, `是...而不是...`, `not only...but also`, and over-balanced pairings unless they clarify a real distinction.
   - Ground claims in concrete subjects, actions, evidence, context, limits, or next steps.
   - Vary sentence length and paragraph weight.
   - Keep enough friction: specific constraints, tradeoffs, real-world detail, and natural imperfection.
   - For Chinese, avoid over-polishing every sentence into crisp model-like judgments. Keep light connective words and natural time adverbs such as `呢`, `总之`, `一来`, `以免`, `现在`, `可能就要`, `那么`, or `一起` when they match the user's voice.
   - For English, prefer direct affirmative claims. Avoid quoted framing labels, `X is not Y, it is Z` structures, and colon-led explanation sentences when a plain sentence works.
   - If using a negative contrast, make the rejected object specific and necessary; otherwise start from the positive claim.
6. Run the final check:
   - Meaning preserved.
   - No invented facts, metrics, personal experience, or source references.
   - No claim that the result is human-written or undetectable.
   - No excessive AI-stock phrases, decorative layout instructions, or adjective-heavy prompts.
   - Output still fits the user's requested format.

## Variation Rules

Always make a deliberate variation choice so repeated use on the same prompt can produce different humanized answers.

Vary at least three of:

- Voice: concise practical, conversational professional, editorial, warm explanatory, sharp executive, loose draft.
- Opening: direct finding, scene detail, problem tension, decision, user pain, or concrete next step.
- Rhythm: short punchy lines, mixed paragraph lengths, one expanded paragraph, or compressed note style.
- Intervention strength: light polish, medium rewrite, heavy restructure.
- Detail strategy: keep spare, add grounded specifics from source, move details into bullets, or turn abstract terms into actions.
- Layout strategy for PPT/document tasks: claim-first slide, decision memo, evidence table, timeline, owner/action log, or before/after contrast.

Do not randomize facts. Randomize style, structure, rhythm, and emphasis.

## Core Heuristics

Prefer direct, natural phrasing over visible rhetorical machinery.

Common AI-ish patterns to reduce:

- Forced contrast: `不是 A, 而是 B`, `是 A, 而不是 B`, `not merely X but Y`.
- Template transitions: first/second/finally in short texts, `综上所述`, `值得注意的是`, `in today's fast-paced world`.
- Abstract filler: empower, unlock, ecosystem, closed loop, transformative, robust, seamless, 赋能, 抓手, 闭环, 生态, 底层逻辑.
- Even rhythm: similar sentence lengths, three tidy bullets everywhere, balanced paragraphs with no priority.
- Fake nuance: `it depends` or `需要综合考虑` without naming the deciding variable.
- Summary-first blandness: broad setup before any real point.
- Excessive completeness: covering benefits, risks, outlook, and conclusion shallowly when the audience needs one judgment.
- Over-polish: every sentence sounds final, symmetrical, and frictionless.
- Layout genericness: three rounded cards, purple gradients, generic icons, equal-weight bullets, fake diagrams.
- Prompt genericness: cinematic, 8K, masterpiece, futuristic, sleek, breathtaking, hyper-detailed without scene, use case, or composition.

Keep contrast structures only when they correct a likely misunderstanding, define a boundary, or make the main idea clearer.

## Task-Specific Moves

### Chinese Text Naturalization

Use lighter connective tissue: `更准确地说`, `重点在于`, `放到实际场景里`, `相比之下`, `问题卡在`, `接下来要看`.

Prefer:

- Specific action over abstract slogan.
- Natural Chinese verbs over translation-like verb-noun stacks.
- One clear judgment over multiple padded caveats.
- Concrete next step over `持续优化`.

### English And Bilingual Polish

Choose one stable register before rewriting: investor update, product copy, email, academic paragraph, internal memo, social post, or website copy.

Prefer:

- Plain verbs over stock AI vocabulary.
- Idiomatic target-language phrasing over literal translation.
- One-time definition of bilingual terms instead of repeated label stuffing.
- Relationship-aware email openings over default politeness.

### PPT And Document De-Templating

Make the content shape drive the layout.

Prefer:

- Claim-first slide titles.
- One dominant takeaway per slide.
- Evidence tables, timelines, decision logs, owner/action grids, or annotated screenshots when they match the content.
- Real metrics with source, baseline, date, and implication.
- Visual hierarchy over equal boxes.

Avoid nested cards, default three-column layouts, generic icons, decorative gradients, fake process diagrams, and slide text that reads like compressed prose.

### Image Prompt De-AI-Styling

Turn quality tags into art direction.

Specify:

- Subject and action.
- Use case and output format.
- Setting, time, light source, material, camera distance, and composition.
- Realistic constraints and natural imperfections.
- Space for text when the image will be used in a poster, slide, or hero.

Avoid asking the image model to render dense text. If text is needed, reserve blank space and add typography later.

## Output Format

If the user asks only for the revised output, return only the revised output.

If the user asks for explanation, include:

- `Humanized version`
- `What changed`
- `Notes / risks`

Keep the explanation short and specific. Mention meaning changes only if they were necessary or requested.

## Resources

- `references/chinese-style-patterns.md`: Chinese AI-ish patterns and rewrites.
- `references/english-bilingual-patterns.md`: English, bilingual, and translationese patterns.
- `references/design-and-ppt-patterns.md`: PPT, document, layout, and design brief de-templating.
- `references/image-prompt-patterns.md`: Image prompt de-AI-styling.
- `references/variation-recipes.md`: Variation recipes for repeated prompts.
- `references/examples.md`: Compact before/after examples.
- `scripts/style_seed.py`: Generates a random style recipe.
- `scripts/ai_tone_lint.py`: Flags common AI-ish patterns in text.
