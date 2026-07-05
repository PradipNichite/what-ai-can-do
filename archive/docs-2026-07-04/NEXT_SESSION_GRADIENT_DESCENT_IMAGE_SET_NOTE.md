# Next Session Note: Gradient Descent Image Set

Use this note as the full handoff for a new parallel Codex session.

## Task

Create the image-only concept-proof set first for:

```text
Gradient Descent: How AI Learns From Mistakes
```

This topic is in `HOW_AI_USES_MATH_SERIES_PLAN.md`. A video-first set may already exist from a parallel session, but the missing priority is now the image-only/self-contained visual story.

## Output Targets

Create or update:

```text
modules/visual-ai-concepts/gradient-descent-how-ai-learns-from-mistakes.source.md
assets/image-prompts/gradient-descent-how-ai-learns-from-mistakes-image-story.md
assets/images/gradient-descent-how-ai-learns-from-mistakes-image-story/
assets/image-prompts/gradient-descent-how-ai-learns-from-mistakes-video-first.md
assets/images/gradient-descent-how-ai-learns-from-mistakes-video-first/
```

First create the image-story folder with 8 self-contained story cards, a contact sheet, and short review notes. Only then derive or revise the video-first assets.

## Existing Context To Read First

```text
HOW_AI_USES_MATH_STYLE_DECISION_NOTE.md
HOW_AI_USES_MATH_SERIES_PLAN.md
VIDEO_FIRST_VISUAL_GUIDE.md
VIDEO_PROMPT_TEMPLATES.md
CHARACTER_CONSISTENCY_GUIDE.md
backlog/ideas/optimization-ai-improves-step-by-step.md
modules/visual-ai-concepts/derivatives-how-ai-learns-from-mistakes.source.md
assets/image-prompts/functions-how-ai-turns-input-into-output-video-first.md
assets/image-prompts/linear-equations-how-ai-combines-signals-video-first.md
```

## Style

Use the current Direction B math-series style:

- realistic warm study-desk/tablet technical style
- recurring Indian 11th/12th standard learner
- dark wavy hair, teal/green shirt, curious focused expression
- wooden desk, lamp, notebook, books, small plant
- tablet as the main technical surface
- readable diagrams and arrows
- minimal embedded text
- no generic glowing AI art

Match these examples:

```text
assets/images/functions-how-ai-turns-input-into-output-video-first/
assets/images/statistics-how-ai-learns-patterns-from-data-video-first/
assets/images/linear-equations-how-ai-combines-signals-video-first/
assets/images/how-ai-uses-math-series-intro-video-first/
```

## Lesson Core

School concept:

```text
Repeated small steps using slope.
```

AI use:

```text
Training a model by reducing loss/error.
```

Mechanism:

```text
prediction -> loss/error -> gradient direction -> small step -> lower loss -> repeat
```

Memory anchor:

```text
Gradient descent is AI taking small downhill steps on an error curve.
```

Keep it distinct from the derivatives lesson. Derivatives explain the direction clue; gradient descent explains the repeated training loop.

## Suggested 8-Card Image-Only Sequence

| # | Scene | Learning job | Visible evidence | Motion role |
|---|---|---|---|---|
| 1 | Wrong prediction | AI starts with a mistake | tablet shows input, prediction chip, correct answer chip | prediction chip appears |
| 2 | Measure loss | error becomes a score | large error gap and simple loss meter | gap lights up |
| 3 | Loss curve | error depends on model setting | curve on tablet with a point high on the slope | curve draws |
| 4 | Gradient direction | slope points toward lower error | tangent/arrow points downhill | arrow draws downhill |
| 5 | Small update | weight changes a little | point moves one short step on curve | point steps |
| 6 | Lower loss | new prediction improves | loss meter shrinks, prediction closer | meter decreases |
| 7 | Repeat | many small steps train model | dotted path descends to valley | dots appear in sequence |
| 8 | Quick check | step size matters | small step path vs overshoot path | overshoot path flashes warning |

## Prompt-Pack Requirements

Create a full image-only prompt pack first with:

- character/style bible
- technical teaching table
- 8 self-contained story-card prompts
- per-frame risk notes

After the image-only cards pass QA, create or revise the video-first prompt pack with 8 source-frame prompts and 8 Runway image-to-video prompts.

Use minimal text. Preferred text labels are short:

```text
loss
small step
lower error
```

Avoid dense formulas. A simple update visual is okay if large and readable:

```text
weight -> weight - small step
```

## Acceptance Criteria

- The image-only sequence clearly shows repeated improvement, not just one derivative slope.
- The cards make sense without voiceover, motion, or external captions.
- The loss curve and downhill steps are visually readable on mobile.
- The point on the curve visibly moves from higher loss to lower loss.
- The learner, desk, lighting, tablet style, and palette match the newer math lessons.
- The contact sheet looks like it belongs beside Functions, Statistics, and Linear Equations.
- Review notes mention any text/math risks before video generation.
