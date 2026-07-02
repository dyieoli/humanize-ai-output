# Image Prompt Patterns

Use this reference when an image prompt sounds generic, over-styled, or obviously AI-generated.

## AI-Ish Prompt Symptoms

| Pattern | Symptoms | Better move |
|---|---|---|
| Adjective pileup | ultra-detailed, cinematic, breathtaking, masterpiece, 8K | Specify subject, action, setting, light, composition, and use case |
| Contradictory style stack | minimalist cyberpunk watercolor photorealistic 3D oil painting | Choose one primary style and one secondary modifier |
| Stock-photo perfection | perfect smile, perfect office, vague diversity | Add lived-in details and realistic posture |
| No use-case anchor | Beautiful image, no format or destination | State hero image, slide background, poster, product mockup, editorial spot, icon set |
| Text dependency | Model must render slogans, labels, UI text, dense diagrams | Reserve blank space; add text later |
| SaaS UI literalism | Dashboard prompts ask for readable charts, exact labels, or realistic interface copy | Represent dashboards as chart shapes, table blocks, hierarchy, and empty text-safe areas; add real UI text later |
| Negative prompt laundry list | Long defect list dominates the prompt | Use short exclusions and strengthen positive direction |
| Uncanny lighting | glossy skin, excessive bokeh, overdone rim light | Specify natural light source and restrained post-processing |
| Camera jargon without intent | Random lens, film stock, aperture terms | Use camera terms only when they shape composition |

## Prompt Template

Use this structure when helpful:

```text
Purpose and format:
Subject and action:
Setting:
Composition:
Lighting:
Material / texture:
Mood:
Constraints:
Avoid:
```

## Examples

Before:

> Ultra-realistic cinematic portrait of a young entrepreneur, dramatic lighting, 8K, masterpiece, highly detailed, shallow depth of field.

After:

> Editorial portrait for a founder profile. A 29-year-old hardware founder sits at a cluttered workbench, sleeves rolled up, prototype parts and a half-open laptop nearby. Window light from the left, muted workshop background, 50mm portrait feel, natural skin texture, calm but tired expression, no text.

What changed:

- Replaced quality tags with art direction.
- Added use case, setting, props, composition, and light source.

## Final Check

- Is the image prompt anchored to a use case?
- Does the composition tell the model where the subject sits?
- Are material, light, and setting specific enough?
- Is text handled outside the image model when possible?
- For SaaS or product UI prompts, are dashboards represented as shapes and hierarchy rather than readable text?
