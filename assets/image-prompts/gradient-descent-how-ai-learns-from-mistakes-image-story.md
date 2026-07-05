# Gradient Descent: How AI Learns From Mistakes - Image Story Prompt Pack

Series: How AI Uses Math  
Source module: `modules/visual-ai-concepts/gradient-descent-how-ai-learns-from-mistakes.source.md`  
Output image folder: `assets/images/gradient-descent-how-ai-learns-from-mistakes-image-story/`  
Renderer: image-only/self-contained 9:16 story cards

## Goal

Create a paused visual story that explains gradient descent without voiceover, animation, or external captions.

Self-contained opener requirement:

The first card must not assume the viewer knows the title or project context. It must name the lesson topic, state the learning promise, connect the school concept to the AI use, and introduce the wrong-prediction example used by the rest of the story.

Native generated composition requirement:

Use image generation to create the full educational composition. The card should feel like one complete designed educational poster, where illustration, diagram, and text are generated together, not a separate caption pasted on top. Text should be part of the scene through tablet UI, notebook panels, poster typography, sticky notes, arrows, labels, callout bubbles, and mini cards. Avoid a pasted overlay look.

Core mechanism:

```text
prediction -> loss/error -> gradient direction -> small step -> lower loss -> repeat
```

Memory anchor:

```text
Gradient descent is AI taking small downhill steps on an error curve.
```

## Character / Style Bible

- realistic warm study-desk/tablet technical style
- 9:16 vertical mobile frame
- recurring Indian 11th/12th standard learner with dark wavy hair and teal/green shirt
- wooden study desk, warm desk lamp, notebook, pen, books, small plant
- tablet as the main technical surface
- large readable technical overlays: prediction chips, loss meter, U-shaped loss curve, point marker, slope arrow, dotted descent path
- integrated generated headline/callout text on each card, not external captions or pasted overlay text
- short labels only: `prediction`, `loss`, `slope`, `small step`, `lower error`, `repeat`
- no dense formulas, no backpropagation diagram, no generic glowing AI art, no logos, no watermark

## Image-Only Story Cards

### Card 1 - Mistake Starts Learning

Teaching job: show that training begins when the model prediction is wrong.

Text to embed:

```text
Gradient Descent: How AI Learns From Mistakes
AI lowers error with small downhill steps.
Slope tells which way to move.
prediction: dog
correct: cat
```

Prompt:

```text
Use case: scientific-educational
Asset type: 9:16 self-contained carousel card
Primary request: Create card 1 for "Gradient Descent: How AI Learns From Mistakes". Make it a self-contained opener for Indian 11th/12th standard students: title the lesson, show that school-math slope helps AI training, and introduce the wrong-prediction example used by the rest of the story. Show an Indian high-school learner at a warm study desk looking at a tablet. The tablet shows an animal input card, a model prediction chip, and a correct answer chip that do not match.
Style/medium: realistic warm study-desk/tablet technical style.
Composition/framing: tablet large in foreground; learner visible behind it; title as native poster typography or notebook header; learning promise as a sticky note or notebook callout; mismatch chips on tablet.
Text (verbatim): "Gradient Descent: How AI Learns From Mistakes", "AI lowers error with small downhill steps.", "Slope tells which way to move.", "prediction: dog", "correct: cat".
Constraints: make the mismatch visually obvious; show slope as the school-math idea and training as the AI use; text must be native to tablet/notebook/sticky-note surfaces; keep text large and readable; no extra text; no logos; no watermark.
```

### Card 2 - Mistake Becomes Loss

Teaching job: show that the wrong prediction becomes a measurable error score.

Text to embed:

```text
The mistake becomes a loss score.
loss = how wrong the model is
loss: 8/10
```

Prompt:

```text
Use case: scientific-educational
Asset type: 9:16 self-contained carousel card
Primary request: Create card 2 showing the mismatch becoming a loss score.
Scene/backdrop: same warm Indian study desk and learner.
Technical overlay: tablet shows the same example direction as card 1: the model prediction is dog and the correct answer is cat. Put a "prediction: dog" chip and a "correct: cat" chip separated by a highlighted error gap; the gap feeds into a large score-like loss meter with 0-to-10 tick marks and a clear high marker at 8.
Text (verbatim): "The mistake becomes a loss score.", "loss = how wrong the model is", "loss: 8/10".
Constraints: loss meter must read as a measured score, not a warning decoration or emotion meter; do not reverse the example; keep prediction dog and correct cat; keep labels large; no dense formulas; no extra text.
```

### Card 3 - Loss Curve

Teaching job: show that different model settings create different loss values.

Text to embed:

```text
A model setting sits on a loss curve.
High point = high error
weight setting
```

Prompt:

```text
Use case: scientific-educational
Asset type: 9:16 self-contained carousel card
Primary request: Create card 3 showing one large U-shaped loss curve on the tablet.
Technical overlay: a single large U-shaped loss curve on the tablet. Show a vertical cue labeled "loss" and a simple horizontal cue labeled "weight setting"; place one glowing point high on the right side of the curve so it clearly means this weight setting creates high loss. Keep the curve, point, and two axis cues large enough for mobile.
Text (verbatim): "A model setting sits on a loss curve.", "High point = high error", "loss", "weight setting".
Constraints: keep the two axis cues simple and readable; avoid dense axis numbers; no formulas; no extra labels beyond the listed text.
```

### Card 4 - Slope Gives Direction

Teaching job: separate derivative from gradient descent: slope gives the local direction clue.

Text to embed:

```text
Slope gives the direction clue.
Move downhill to lower error.
gradient: higher loss
move opposite
slope
lower error
```

Prompt:

```text
Use case: scientific-educational
Asset type: 9:16 self-contained carousel card
Primary request: Create card 4 showing the local slope at a point on the loss curve.
Technical overlay: U-shaped loss curve with a point and tangent line. Show two clearly separated cues: a faint uphill cue labeled "gradient: higher loss" and a stronger downhill cue labeled "move opposite" toward "lower error". Keep the tablet diagram simple enough for mobile.
Text (verbatim): "Slope gives the direction clue.", "Move downhill to lower error.", "gradient: higher loss", "move opposite", "slope", "lower error".
Constraints: make the distinction clear: gradient indicates higher loss, gradient descent moves opposite toward lower error; do not let the downhill arrow be labeled as the gradient; no dense formulas.
```

### Card 5 - One Small Update

Teaching job: show one careful update step opposite the gradient.

Text to embed:

```text
Gradient descent takes one small step.
step opposite gradient
new weight =
old weight - small step
small step
```

Prompt:

```text
Use case: scientific-educational
Asset type: 9:16 self-contained carousel card
Primary request: Create card 5 showing one small gradient descent update on the curve.
Technical overlay: old point and nearby new point slightly lower on the curve, connected by a short arrow labeled "step opposite gradient". Put the update rule on one large notebook/tablet note as two stacked lines: "new weight =" and "old weight - small step". It must use exactly one equals sign and one clear minus sign.
Text (verbatim): "Gradient descent takes one small step.", "step opposite gradient", "new weight =", "old weight - small step", "small step".
Constraints: step must be visibly small and opposite the gradient cue; update expression should be large and simple; do not replace the minus sign with a second equals sign; keep the two-line update visually grouped as one rule; no extra formulas.
```

### Card 6 - Lower Error

Teaching job: show that the new setting has lower loss, but not perfect prediction.

Text to embed:

```text
After the step, loss is lower.
The prediction is closer, not perfect.
lower error
loss: 5/10
```

Prompt:

```text
Use case: scientific-educational
Asset type: 9:16 self-contained carousel card
Primary request: Create card 6 showing lower loss after one update.
Technical overlay: one large tablet UI only: smaller loss meter marked "loss: 5/10", prediction/correct chips closer together, and a small curve inset with the point lower than before. Include a small before-to-after cue from "loss: 8/10" to "loss: 5/10". Put the sentence "The prediction is closer, not perfect." as a large notebook or tablet callout. Keep the diagram simple and avoid extra mini-panels.
Text (verbatim): "After the step, loss is lower.", "The prediction is closer, not perfect.", "lower error", "loss: 5/10", "loss: 8/10".
Constraints: do not show perfect prediction after one step; use only the required text; no extra sticky-note explanations; keep text and diagram readable on mobile.
```

### Card 7 - Repeat To Learn

Teaching job: show that gradient descent is repeated updates, not one derivative calculation.

Text to embed:

```text
Training repeats the loop.
small steps lower loss
repeat
```

Prompt:

```text
Use case: scientific-educational
Asset type: 9:16 self-contained carousel card
Primary request: Create card 7 showing repeated gradient descent steps.
Technical overlay: U-shaped loss curve with dotted points and short step arrows descending toward the valley. The curve and ordered dotted path should dominate the tablet; do not add a notebook checklist.
Text (verbatim): "Training repeats the loop.", "small steps lower loss", "repeat".
Constraints: repeated steps must be clearly ordered; path should not look decorative; no extra checklist text; no dense formulas.
```

### Card 8 - Quick Check: Step Size Matters

Teaching job: compare useful small steps with a too-large step that overshoots.

Text to embed:

```text
Quick check: why small steps?
Too large can overshoot the valley.
small step
too far
```

Prompt:

```text
Use case: scientific-educational
Asset type: 9:16 self-contained carousel card
Primary request: Create card 8 as a quick check about step size.
Technical overlay: one U-shaped loss curve with two paths: a smooth small-step dotted path descending into the valley and a second oversized path jumping past the valley and landing higher.
Text (verbatim): "Quick check: why small steps?", "Too large can overshoot the valley.", "small step", "too far".
Constraints: make the two paths easy to compare; avoid scary warning symbols; no extra text.
```

## Production Note

The image-story cards were regenerated as native 9:16 educational images with text integrated into the tablet interface and scene composition. They are not the patched overlay draft.
