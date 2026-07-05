# OpenAI Visual QA - image-story

Generated: 2026-07-05T12:10:56+00:00
Model: `gpt-5.5`
Response ID: `resp_005ae034a2221f8f006a4a49b8ffc88192850724e9f91d3c6c`
OpenAI request ID: `85958fa0-d9a5-4151-a20e-54c95ab4997b`

## Inputs

- Image folder: `assets/images/gold-candidates/gradient-descent-strict-paired-medium/image-only`
- Contact sheet: `assets/images/gold-candidates/gradient-descent-strict-paired-medium/image-only-contact-sheet.jpg`
- Prompt pack: `assets/image-prompts/gradient-descent-how-ai-learns-from-mistakes-image-story.md`
- Source module: `modules/visual-ai-concepts/gradient-descent-how-ai-learns-from-mistakes.source.md`

Reviewed images:
- `assets\images\gold-candidates\gradient-descent-strict-paired-medium\image-only-contact-sheet.jpg`

## Verdict

- Status: `needs-revision`
- Intended use: `image-story`
- Next action: `regenerate-frame`

Good visual story structure and mostly strong mechanism diagrams, but not ready to accept because frame 5 misrenders the core update formula and frame 2 breaks the dog/cat example continuity. Some later frames also need mobile simplification.

## Gate Evidence

- Opener: `pass` - Frame 1 is self-contained: it clearly names the lesson, “Gradient Descent: How AI Learns From Mistakes,” shows the AI promise about lowering error with small downhill steps, connects slope to movement direction on a notebook graph, and introduces the mismatch example with tablet chips “prediction: dog” and “correct: cat.” The cat image plus dog prediction makes the mistake visually obvious.
- Opener required fix: None
- Native composition: `partial` - Most text is integrated into tablet screens, notebook cards, sticky notes, and poster-style headers within the warm study-desk scene. The recurring learner, tablet, desk lamp, plant, books, and notebook style are consistent. However, several top brush-stroke headline panels feel like repeated poster overlays rather than fully embedded surfaces, and some frames add extra generated mini-notes not in the prompt.
- Native composition required fix: Keep the designed educational-poster look, but reduce repeated generic top-banner treatment where possible and avoid extra small explanatory text that was not requested.
- Overlay risk: `medium` - The tablet diagrams and sticky notes feel native, but the large white brush-stroke headline areas on frames 1, 3, 4, 5, 7, and 8 have a somewhat pasted poster-caption feel. They are visually consistent and not obviously post-production overlays, but they risk reading as a caption layer over the scene rather than part of the desk/tablet environment.
- Mechanism visibility: `partial` - The sequence visibly shows the core mechanism: wrong prediction, loss meter, U-shaped loss curve, slope/tangent direction, a small step, lower loss, repeated steps, and overshoot comparison. Frame 5 has a serious text/technical issue: the update note appears to read “new weight = old weight = small step” instead of the required minus-step update. Frame 2 also flips the animal example relative to frame 1: frame 1 has prediction dog/correct cat, while frame 2 shows prediction cat/correct dog, which breaks example continuity.
- Mechanism required fix: Regenerate or repair frame 5 so the formula clearly reads “new weight = old weight - small step.” Repair frame 2 to preserve the same example direction as frame 1: prediction dog, correct cat, or avoid animal labels if not needed.
- Mobile readability: `partial` - Main headlines and major labels are generally large and readable on the contact sheet: “loss,” “slope,” “lower error,” “small step,” “repeat,” and “too far” are visible. Some small notebook/tablet notes are too dense for mobile, especially frame 6’s small panels and frame 7’s notebook checklist. Frame 5’s formula is not just small but semantically misrendered.
- Mobile readability required fix: Prioritize only the required text on each card. Remove or enlarge tiny extra notes, especially in frames 6 and 7, and fix frame 5’s update expression.

## Frame Notes

### Frame 1

- Status: `pass`
- Evidence: Strong opener. Title, learning promise, slope callout, and mismatch chips are all visible. The learner and warm Indian study-desk/tablet style are clear. The cat image with “prediction: dog” and “correct: cat” introduces the example well.
- Fix: None

### Frame 2

- Status: `needs-revision`
- Evidence: The loss meter is clear and the mistake-to-loss idea is readable. However, the example continuity is reversed: tablet shows “Your prediction” with a cat and “Correct answer” with a dog, conflicting with frame 1’s prediction dog/correct cat example. Main headline and sticky note are readable.
- Fix: Regenerate/repair so the same mismatch continues: prediction dog, correct cat. Keep the loss meter as a score.

### Frame 3

- Status: `pass`
- Evidence: Large U-shaped loss curve is clear, with a high glowing point on the right and a readable callout “High point = high error.” The “loss” axis label is readable and the tablet dominates the frame.
- Fix: None

### Frame 4

- Status: `pass`
- Evidence: Slope/tangent line, point, and downhill arrow toward “lower error” are visible. The card separates the direction clue from the full loop and makes downhill movement clear.
- Fix: None

### Frame 5

- Status: `reject`
- Evidence: The curve, old/new points, and small step arrow are visually good, but the update expression on the notebook appears wrong: it reads like “new weight = old weight = small step” rather than “new weight = old weight - small step.” This is a core technical text failure for the update rule.
- Fix: Regenerate/repair frame 5. The formula must clearly read “new weight = old weight - small step,” with a visible minus sign and no mistaken second equals sign.

### Frame 6

- Status: `needs-revision`
- Evidence: The tablet shows lower loss, closer prediction/correct chips, and a small curve inset. It correctly avoids implying perfection. But the frame is cluttered with multiple small panels and extra notes; some text is too small for mobile.
- Fix: Simplify to the required text only: “After the step, loss is lower.” “The prediction is closer, not perfect.” and “lower error.” Enlarge the loss meter and closer-not-perfect chip comparison.

### Frame 7

- Status: `needs-revision`
- Evidence: Repeated dotted descent steps toward the valley are clear, and “Training repeats the loop,” “small steps lower loss,” and “repeat” are visible. However, the notebook checklist adds dense extra text that will not be readable on a phone and distracts from the simple repeat mechanism.
- Fix: Remove or greatly simplify the notebook checklist. Keep the ordered dotted path, arrows, “repeat,” and “small steps lower loss.”

### Frame 8

- Status: `pass`
- Evidence: The quick check is understandable: green small-step path descends toward the valley while the red oversized path jumps too far and lands higher. “small step,” “too far,” and the overshoot note are readable.
- Fix: None
