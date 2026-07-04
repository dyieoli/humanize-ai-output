# English And Bilingual Patterns

Use this reference when English or bilingual output sounds inflated, translation-like, too symmetrical, or generically professional.

## Patterns

| Pattern | Symptoms | Better move |
|---|---|---|
| Prompt-shaped opening | "In today's fast-paced world", "As technology continues to evolve" | Open with the specific situation, result, problem, or ask |
| AI stock vocabulary | delve, tapestry, robust, seamless, leverage, unlock, transformative | Use plain verbs and domain nouns |
| Corporate fog | "drive alignment across stakeholders to enable scalable outcomes" | Name who decides, what changes, and what happens next |
| Overbalanced prose | not only X but also Y, both A and B, repeated parallel pairs | Use one direct sentence unless the contrast matters |
| Excessive politeness | "I hope this email finds you well... kindly inquire..." | Make the relationship and ask specific |
| Translationese | realize transformation, build a closed-loop ecosystem, carry out optimization | Rewrite idiomatically in the target language |
| Bilingual label stuffing | Chinese phrase followed by English phrase after every term | Define once, then use the audience-native term |
| Register mismatch | Startup slang mixed with formal investor language | Pick a stable speaker and setting |
| Over-compressed polish | Every sentence is crisp, executive, and final | Use editor-like connective phrasing with concrete subjects and next actions. |
| Too-neat framing | The rewrite sounds like a perfect memo headline rather than a person revising a sentence | Use softer affirmative pivots: current focus, next step, concrete subject, and decision. |
| Negative-first contrast | Opens by rejecting a phrase before stating the useful claim | Start with the positive claim. Use negative contrast only when naming a specific rejected option matters. |
| Trailing not-frame | Adds a broad tail such as `, not model capability alone` | Name the useful claim directly and remove vague contrast tails. |
| Not-alone contrast | Uses `not X alone` to sound nuanced | State the actual advantage, dependency, or risk without the balancing phrase. |
| Quoted framing labels | Uses quoted concepts as the main explanation, such as a quoted slogan or label | Remove quote wrappers and write the claim directly. |
| Colon-led explanation | Uses `claim: explanation` repeatedly | Split into normal sentences or use a dash only when the label is a real field. |

## Penalty Gate

Humanized output must pass a second correction pass before it is shown.

- Start from 100 points. Passing threshold is 95.
- Count broad negative contrasts, trailing `, not...` frames, `not...alone`, quoted framing labels, colon-led explanation, and `X + Y + Z` shorthand.
- A sentence like `Our current advantage is customer workflow depth, not model capability alone.` should fail the candidate because the useful point is already clear without the tail.
- If the score is below 95, revise and rerun until it passes.

## Stock Phrase Replacements

- leverage -> use, apply, build on
- unlock -> create, open up, make possible
- robust -> reliable, tested, durable, mature
- seamless -> smooth, low-friction, integrated
- transformative -> material, significant, new, high-impact
- long-term value -> margin, retention, cash flow, speed, adoption, or another real metric

## Direct English Moves

Use these when a result is technically clean but still feels AI-polished:

- Replace a quoted or negative-first frame with a direct claim.
- Replace colon-led question framing with "Next step we should focus on whether..."
- Replace broad contrast with a positive next action.
- Replace `not model capability alone` with a direct sentence such as "Customer workflow depth is the current advantage."
- Replace too-clean thesis wording with "The useful signal now is..."
- Replace abstract adoption wording with "getting internal tools actually adopted" when the tone allows it.
- Replace tentative timing wording with "Even if the date is still moving..."
- Replace abstract efficiency claims with "instead of chasing context across tools."
- Replace product-site abstraction by naming the user, object, and outcome directly.

These are small human edits, not slang. Use them only when they fit the audience.

## Bilingual Guidance

When polishing bilingual copy:

1. Decide the dominant language.
2. Keep domain terms in the language the intended audience uses.
3. Define technical terms once if needed.
4. Avoid translating slogans word-by-word.
5. Preserve legally or commercially sensitive terms exactly.

## Examples

Before:

> I am a passionate and results-driven professional with rich experience in AI product innovation, 致力于通过技术赋能业务增长 and creating impactful solutions.

After:

> I build AI product workflows for teams that need less manual review and faster handoffs. My recent work sits between product strategy, prompt design, and internal tool adoption.

What changed:

- Removed inflated self-description.
- Smoothed the Chinese-English mix.
- Named the work and audience.

## Final Check

- Meaning preservation comes before elegance.
- Do not add metrics, customers, credentials, or human experience that the source did not support.
- Check the 95-point penalty gate after rewriting. Keep revising if broad negative contrast, trailing not-frames, or colon-led explanation remain.
- Keep rhythm varied: one short sentence can carry more authority than three polished clauses.
