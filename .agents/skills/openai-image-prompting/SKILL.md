---
name: openai-image-prompting
description: Use when creating, revising, or productizing OpenAI GPT Image prompts for generated educational visuals, image-only story cards, style-reference workflows, character consistency, text-in-image reliability, or cost/quality experiments.
---

# OpenAI Image Prompting

Use this with `image-story-gate` for educational story cards.

Source reference:

- OpenAI Cookbook: `https://developers.openai.com/cookbook/examples/multimodal/image-gen-models-prompting-guide`

## Prompt Shape

Use a stable, skimmable structure:

```text
Use case:
Asset type:
Primary request:
Scene/backdrop:
Subject:
Technical visual:
Style/medium:
Composition/framing:
Text to render verbatim, exactly:
Constraints:
```

For complex prompt packs, keep this order because it maps cleanly to OpenAI's recommended pattern: goal, scene, subject, key details, constraints.

## Native Educational Cards

For this repo, always adapt GPT Image prompting into native generated compositions:

- Put diagrams on tablet, phone, notebook, sticky notes, classroom poster surfaces, labels, arrows, callouts, or mini-cards.
- Demand one complete designed educational poster, not a background plus pasted caption.
- Quote every required text string.
- Say `no extra text` unless intentionally allowing helpful micro-labels.
- Name what must remain readable at mobile size.

## Character Consistency

For one lesson, prefer this generation order:

1. Generate or select a strong opener as the character anchor.
2. Use the opener image as the primary reference for later frames.
3. Generate later frames with the same learner, outfit, desk, lighting, camera angle family, and illustration style.
4. Keep external references for the opener or for repair only; avoid resending many style references to every card unless quality drops.

When using references, describe their role explicitly:

```text
Use the attached references for visual style, composition grammar, character continuity, warm Indian study-desk atmosphere, and native integrated text treatment. Do not copy their topic.
```

## Text Reliability

For exact in-image text:

- Put each string in quotes.
- Use short strings.
- Assign each string to a surface: tablet title, notebook note, sticky note, edge label, button, score card.
- Avoid long paragraphs.
- Ask for large contrast and mobile readability.
- Regenerate only the failing frame when the rest of the sequence works.

## Cost Ladder

Use the cheapest setting that answers the current question:

- Prompt/style debugging: one or two cards, `gpt-image-1-mini` or `gpt-image-2`, `quality=low`.
- Full lesson draft: `gpt-image-2`, `quality=low`, anchor-after-first references.
- Final lesson: `gpt-image-2`, `quality=medium`, after QA passes at draft quality.

Use `single-request-lesson` only as an experiment. It may save repeated reference-image input, but it can weaken per-frame control, retries, QA, and LangSmith filtering.

## Image-Only To Video-First Conversion

Treat image-only cards and video source frames as sibling renderers:

- Image-only card: self-contained, enough native text to teach when paused.
- Video source frame: lower text, one clear action, one motion target, voiceover carries explanation.

When converting an accepted image-only lesson to video-first:

1. Keep the same character anchor and study-desk world.
2. Preserve the visible mechanism, not the full text.
3. Move explanation from image text into voiceover.
4. Use icons, bars, meters, arrows, dots, scan lines, highlights, and hand motion.
5. For every frame, define the motion target before generating.

Paired generation can be tested for one scene at a time. Use strict pair separation:

```text
Output 1: IMAGE_ONLY_STORY_CARD
Output 2: VIDEO_SOURCE_FRAME
```

The prompt must protect both outputs:

- Tell the model not to treat them as two variations of the same poster.
- For `IMAGE_ONLY_STORY_CARD`, require self-contained explanation, native integrated text, exact requested text, and enough context to work without voiceover.
- For `VIDEO_SOURCE_FRAME`, require sparse text, one motion target, and no copied poster explanation from the image-only card.
- Preserve shared character, environment, style, and technical numbers.

Use paired generation for experiments or selected technical scenes. It can work for both formats when the prompt has separate acceptance criteria for each output. Do not make it the default final renderer until visual QA confirms both outputs are as strong as standalone generation across several lessons.

## QA Loop

After generation:

1. Build a contact sheet from actual frame files only.
2. Inspect pixels with vision QA.
3. Compare against the image-story gate.
4. Repair the smallest failing unit: prompt string, one frame, or reference strategy.
5. Preserve successful patterns in prompt packs, scripts, or this skill.
