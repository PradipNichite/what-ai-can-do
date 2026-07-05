# Gradient Descent: How AI Learns From Mistakes - Video-First Prompt Pack

These prompts are for Warm Minimal Tablet Closeup source frames intended for image-to-video clips. They are not self-contained image-story cards. The voiceover should carry the full explanation while each frame gives the video model one clean technical action to animate.

Series: How AI Uses Math
Source module: `modules/visual-ai-concepts/gradient-descent-how-ai-learns-from-mistakes.source.md`
Style version: Warm Minimal Tablet Closeup v1
Output image folder: `assets/images/gradient-descent-how-ai-learns-from-mistakes-video-first-warm-minimal-v1/`

## Character / Style Bible

Recurring learner:

- Indian 11th/12th standard student, curious and focused
- dark wavy hair, teal/green shirt or visible teal/green sleeve
- warm wooden study desk, soft desk lamp, notebook edge, pencil, books, small plant
- tablet as the dominant technical surface, filling about 70-80 percent of the 9:16 frame
- human context through hand, sleeve, pencil, partial face, or soft background presence

Visual rules:

- Warm minimalist tablet closeup, polished educational illustration, cinematic but uncluttered.
- One technical action per frame.
- Keep embedded text sparse, large, and native to the tablet UI.
- Prefer graph marks, meters, chips, dots, arrows, and glow states over explanatory paragraphs.
- Leave safe margins for subtle camera movement and caption overlays.
- Avoid title banners, dense formulas, generic glowing AI art, logos, watermarks, flat slide cards, and pasted caption blocks.
- Do not label the downhill update arrow as the gradient. The gradient cue points toward higher loss; the update moves opposite.

## Technical Teaching Table

| # | Scene | Learning job | Visible evidence | Transformation / comparison | Motion role | Risk |
|---|---|---|---|---|---|---|
| 1 | Opener bridge | AI improves by reducing mistakes | compact chain: wrong prediction icon -> loss meter -> loss curve -> small step | mistake -> loss -> update | chain lights left to right | too sparse without voiceover |
| 2 | Measure loss | error becomes a score | mismatch gap feeds large `loss: 8/10` meter | gap -> numeric loss | gap pulse fills meter | loss looks like emotion, not score |
| 3 | Loss curve | loss depends on weight setting | big U-shaped curve, high point, axis cues | weight setting -> loss value | curve draws, point lands | curve too tiny on mobile |
| 4 | Gradient direction | gradient points to higher loss, update moves opposite | tangent/uphill cue plus separate downhill arrow | local slope -> opposite direction | gradient cue first, update arrow second | implies gradient itself points downhill |
| 5 | Small update | model changes weight by one small step | old point, nearby lower new point, short step arrow | old weight -> new weight | point moves short distance | step looks too large |
| 6 | Lower loss | one update can reduce error without becoming perfect | smaller meter `loss: 5/10`, closer prediction chip | high loss -> lower loss | meter shrinks, chip slides closer | implies perfect prediction |
| 7 | Repeat loop | training repeats many small updates | dotted path descends toward valley, loss meter levels shrink | repeated updates -> lower loss | dots appear in order | dots look decorative |
| 8 | Step-size check | careful small steps beat oversized jumps | small-step path vs too-far overshoot path | careful update vs overshoot | small path glows, overshoot flashes | comparison becomes cluttered |

## Frame 1 - Opener Bridge

Learning job: AI training improves by turning a mistake into loss, then taking a small step toward lower loss.

Visual evidence: tablet shows a compact visual chain: wrong prediction icon, loss meter, loss curve, small downhill step.

Transformation: mistake -> loss -> small update.

Motion role: chain lights up left to right and the small step arrow pulses.

Risk: the frame can become too abstract unless the chain clearly includes mistake, loss, curve, and step.

Source image prompt:

```text
Use case: scientific-educational
Asset type: 9:16 source frame for image-to-video animation
Primary request: Create frame 1 of a Warm Minimal Tablet Closeup micro-lesson about "Gradient Descent: How AI Learns From Mistakes".
Scene/backdrop: warm wooden study desk with soft lamp glow, notebook edge, pencil, books, small plant, and a tablet held close to the viewer.
Subject: Indian 11th/12th standard learner; teal/green sleeve and focused pointing hand visible near the tablet; partial face may appear softly in the background but the tablet is the hero.
Style/medium: warm minimalist tablet closeup, polished modern Indian educational illustration, cinematic 9:16 mobile frame, uncluttered and motion-safe.
Composition/framing: tablet fills about 75 percent of the frame; desk context stays subtle; leave safe bottom margin for captions.
Text (verbatim): "mistake", "loss", "small step".
Technical overlay: tablet shows a compact left-to-right chain: wrong prediction icon -> vertical loss meter -> U-shaped loss curve -> short green downhill step arrow. The chain must imply AI improves by reducing error.
Motion target for later video: chain lights up left to right and the small step arrow pulses once.
Constraints: no lesson title, no dog/cat words, no extra text, no dense formulas, no logos, no watermark, keep labels large and native to the tablet UI, do not make a flat slide card.
```

Runway prompt:

```text
The tablet chain lights up from mistake icon to loss meter to loss curve to small step arrow.
The learner's pointing hand moves slightly and the small step arrow pulses once.
Keep the full vertical frame visible.
Keep existing text unchanged and readable.
No new text. No crop.
```

## Frame 2 - Measure Loss

Learning job: a wrong prediction becomes a numeric loss score.

Visual evidence: mismatch gap feeds into a high loss meter labeled `loss: 8/10`.

Transformation: prediction-target gap -> numeric loss score.

Motion role: gap glows and fills the meter upward.

Risk: the meter must read as a score, not a warning decoration.

Source image prompt:

```text
Use case: scientific-educational
Asset type: 9:16 source frame for image-to-video animation
Primary request: Create frame 2 showing a model mistake becoming a loss score.
Scene/backdrop: close-up tablet on warm wooden study desk with lamp glow, notebook edge, pencil, and subtle books/plant context.
Subject: same recurring Indian teenage learner; teal/green sleeve and hand near the tablet; tablet is dominant.
Style/medium: warm minimalist tablet closeup, polished educational illustration, cinematic 9:16 frame.
Composition/framing: tablet fills most of frame; simple UI elements large enough for phone viewing; safe margins for slight camera motion.
Text (verbatim): "prediction", "correct", "loss: 8/10".
Technical overlay: tablet shows two icon chips that do not match: one prediction chip and one correct-answer chip. A highlighted gap between them feeds into a large vertical loss meter labeled "loss: 8/10", filled high on a simple 0-to-10 scale without clutter.
Motion target for later video: mismatch gap glows, then a pulse flows into the loss meter and fills it upward.
Constraints: no dog/cat words, no extra text, no logos, no watermark, no dense formulas, avoid angry warning graphics, keep the score label large and readable.
```

Runway prompt:

```text
The mismatch gap glows, then a soft pulse flows into the loss meter as it fills upward.
The learner's hand hovers near the meter with a small pointing motion.
Keep the full vertical frame visible.
Keep existing text unchanged and readable.
No new text. No crop.
```

## Frame 3 - Loss Curve

Learning job: different weight settings can create different loss values.

Visual evidence: large U-shaped curve with one point high on the slope and clear loss/weight-setting cues.

Transformation: weight setting -> loss value.

Motion role: curve draws and the high point lands on the slope.

Risk: axis labels or curve may become too small after video motion.

Source image prompt:

```text
Use case: scientific-educational
Asset type: 9:16 source frame for image-to-video animation
Primary request: Create frame 3 showing a one-weight loss curve.
Scene/backdrop: close tablet on warm study desk with notebook edge, pencil, and soft lamp glow.
Subject: same recurring Indian teenage learner; only teal/green sleeve, hand, or soft partial face needed; tablet mechanism is dominant.
Style/medium: warm minimalist tablet closeup, premium mobile educational illustration, clean graph, soft paper-and-lamp warmth.
Composition/framing: tablet fills about 75 percent of the vertical frame; graph is large and centered with safe margins.
Text (verbatim): "loss", "weight setting".
Technical overlay: tablet shows one large clean U-shaped loss curve with a single glowing point high on the right slope. Add a simple vertical cue labeled "loss" and horizontal cue labeled "weight setting". No axis numbers.
Motion target for later video: loss curve draws from left to right, then the high point pops into place.
Constraints: no extra text, no formulas, no logos, no watermark, keep graph and labels large, do not make the tablet look like a generic presentation slide.
```

Runway prompt:

```text
The loss curve draws smoothly across the tablet and the high point pops onto the slope with a soft glow.
The learner's hand remains steady near the graph.
Keep the full vertical frame visible.
Keep existing text unchanged and readable.
No new text. No crop.
```

## Frame 4 - Gradient Direction

Learning job: the gradient points toward higher loss, so gradient descent moves opposite toward lower error.

Visual evidence: tangent/uphill gradient cue and separate downhill opposite-update arrow from the same point.

Transformation: local slope clue -> opposite update direction.

Motion role: tangent/gradient cue appears first, then the opposite arrow draws toward lower error.

Risk: the frame fails if the downhill arrow is labeled as the gradient.

Source image prompt:

```text
Use case: scientific-educational
Asset type: 9:16 source frame for image-to-video animation
Primary request: Create frame 4 showing that the gradient points toward higher loss and the update moves opposite toward lower error.
Scene/backdrop: close-up tablet on warm study desk, pencil and notebook edge visible, soft lamp glow.
Subject: same recurring Indian teenage learner; teal/green sleeve and pointing hand near the graph; no full character required.
Style/medium: warm minimalist tablet closeup, premium mobile explainer illustration, clean graph, warm human desk context.
Composition/framing: tablet fills most of the frame; graph is large and readable with safe margins for video motion.
Text (verbatim): "gradient: higher loss", "move opposite", "lower error".
Technical overlay: tablet shows one large U-shaped loss curve with a point on the slope. A thin red/orange tangent or uphill cue at the point is labeled "gradient: higher loss". A separate green arrow starts at the same point and is labeled "move opposite", ending near "lower error" toward the valley.
Motion target for later video: tangent cue appears first, then the opposite update arrow draws toward lower error.
Constraints: no lesson title, no extra text, no formulas, no logos, no watermark, do not label the downhill arrow as the gradient, keep labels high contrast and larger than in the style-grid experiment.
```

Runway prompt:

```text
The tangent and higher-loss gradient cue draw first, then the separate move-opposite arrow draws toward lower error.
The learner's pointing hand moves slightly without covering the labels.
Keep the full vertical frame visible.
Keep existing text unchanged and readable.
No new text. No crop.
```

## Frame 5 - Small Update

Learning job: the model changes its weight by one small step opposite the gradient.

Visual evidence: old point, nearby new lower point, and a thick short green arrow directly connecting them.

Transformation: old weight setting -> nearby new weight setting.

Motion role: old point moves one short distance along the arrow and the step arrow glows.

Risk: if the point jumps far, the later step-size lesson becomes confusing.

Source image prompt:

```text
Use case: scientific-educational
Asset type: 9:16 source frame for image-to-video animation
Primary request: Create frame 5 showing one small gradient descent update.
Scene/backdrop: tablet closeup on warm wooden study desk with notebook edge, pencil, and soft lamp glow.
Subject: same recurring Indian teenage learner; teal/green sleeve and hand resting near the tablet.
Style/medium: warm minimalist tablet closeup, polished 9:16 educational illustration, uncluttered and motion-safe.
Composition/framing: tablet is the main technical surface; curve and old/new points are large; safe bottom margin for captions.
Text (verbatim): "small step", "opposite gradient".
Technical overlay: tablet shows the same U-shaped loss curve with two large colored points: old point higher on the slope and new point nearby slightly lower. A thick short green arrow must directly connect old point to new point, starting at the old point and ending at the new point. Place the label "opposite gradient" beside the arrow, not floating in the center of the graph. A small native tablet chip reads "small step". Do not include a full formula.
Motion target for later video: old point moves one short step along the visible arrow to the nearby lower point and the arrow glows.
Constraints: no extra text, no formulas, no logos, no watermark, the connecting arrow must be clearly visible on mobile, step must be visibly small, do not show the point jumping across the valley.
```

Runway prompt:

```text
Keep both colored points fixed in place; do not move the points around the curve.
Only the short green arrow between the two points pulses softly.
The learner's hand shifts subtly beside the tablet.
Keep the full vertical frame visible.
Keep existing text unchanged and readable.
No new text. No crop.
```

## Frame 6 - Lower Loss

Learning job: after one update, the model can reduce loss without becoming perfect.

Visual evidence: loss meter shrinks from high state to `loss: 5/10`; prediction chip and correct chip use the same visual language as frame 2, now closer together but still separated by a small remaining gap.

Transformation: high loss -> lower loss.

Motion role: meter decreases and prediction chip slides closer while a small remaining gap stays visible.

Risk: the visual must not imply a perfect answer after one step.

Source image prompt:

```text
Use case: scientific-educational
Asset type: 9:16 source frame for image-to-video animation
Primary request: Create frame 6 showing lower loss after one small update.
Scene/backdrop: close tablet on warm study desk with notebook, pencil, and lamp glow.
Subject: same recurring Indian teenage learner; teal/green sleeve and soft partial face or hand context.
Style/medium: warm minimalist tablet closeup, polished mobile educational illustration, cinematic but uncluttered.
Composition/framing: tablet fills most of frame; loss meter and prediction chips are large; safe margins for motion.
Text (verbatim): "loss: 5/10", "lower error".
Technical overlay: tablet shows a smaller loss meter labeled "loss: 5/10". Reuse the same two-card comparison language from frame 2: one chip labeled "prediction" and one chip labeled "correct". Put the chips closer together than frame 2, but keep a clear small remaining gap between them so improvement is partial, not perfect. Include a tiny curve inset with the point slightly lower than before.
Motion target for later video: loss meter shrinks and the prediction chip slides closer to the correct chip while the small remaining gap stays visible.
Constraints: no extra text, no logos, no watermark, no dense formulas, do not use a single checkmark as the answer, do not show perfect prediction, keep labels readable.
```

Runway prompt:

```text
The loss meter shrinks to the lower level and the prediction chip slides closer to the correct chip without fully matching it.
The learner gives a small aha hand gesture near the tablet.
Keep the full vertical frame visible.
Keep existing text unchanged and readable.
No new text. No crop.
```

## Frame 7 - Repeat Loop

Learning job: training means repeating small updates many times.

Visual evidence: dotted path steps down the loss curve while a compact loss meter shows lower levels.

Transformation: repeated updates -> lower loss.

Motion role: dots appear in sequence and the loss meter levels shrink.

Risk: dotted points must look like ordered updates, not decoration.

Source image prompt:

```text
Use case: scientific-educational
Asset type: 9:16 source frame for image-to-video animation
Primary request: Create frame 7 showing repeated small gradient descent updates reducing loss.
Scene/backdrop: tablet close on warm desk, notebook and pencil visible, learner hand resting nearby.
Subject: same recurring Indian teenage learner; teal/green sleeve or hand context only; tablet mechanism dominates.
Style/medium: warm minimalist tablet closeup, clean educational illustration with soft glow, 9:16 mobile source frame.
Composition/framing: tablet fills most of frame; dotted path and loss meter are large enough for mobile.
Text (verbatim): "repeat", "lower loss".
Technical overlay: tablet shows a U-shaped loss curve with a dotted path of four small points stepping downhill toward the valley. Beside the curve, a compact loss meter shows stacked ghost levels shrinking from high to lower. The final point is near lower loss but not exactly perfect.
Motion target for later video: dotted points light up in order and the loss meter shrinks level by level.
Constraints: no extra text, no dense formulas, no logos, no watermark, no perfect-answer implication, make the ordered step sequence unmistakable.
```

Runway prompt:

```text
Dotted points light up one by one down the loss curve while the loss meter shrinks level by level.
The learner's hand stays still enough to keep attention on the tablet.
Keep the full vertical frame visible.
Keep existing text unchanged and readable.
No new text. No crop.
```

## Frame 8 - Step-Size Quick Check

Learning job: small repeated steps are safer than one oversized jump.

Visual evidence: one smooth small-step path descends; a second path jumps across the valley and lands higher.

Transformation: careful update vs overshoot.

Motion role: small-step path glows calmly, then the too-far path flashes once.

Risk: too many labels can make the comparison unreadable.

Source image prompt:

```text
Use case: scientific-educational
Asset type: 9:16 source frame for image-to-video animation
Primary request: Create frame 8 as a quick check showing that step size matters in gradient descent.
Scene/backdrop: warm study desk closeup with tablet as the main surface, notebook and pencil nearby.
Subject: same recurring Indian teenage learner; teal/green sleeve and pencil-holding hand near the tablet.
Style/medium: warm minimalist tablet closeup, polished educational illustration, clean graph and sparse text.
Composition/framing: tablet fills about 75 percent of the frame; two paths are easy to compare; safe margins for video motion.
Text (verbatim): "small step", "too far".
Technical overlay: tablet shows one large U-shaped loss curve with two paths: a smooth small-step dotted path descending toward the valley, and a second oversized path that jumps across the valley and lands higher, labeled "too far". Use a calm green path for small step and a warm orange/red path for too far.
Motion target for later video: small-step path glows calmly, then the too-far overshoot path flashes once and settles higher.
Constraints: no extra text, no formulas, no logos, no watermark, avoid scary warning symbols, keep labels large and readable, do not crop the valley or overshoot landing point.
```

Runway prompt:

```text
The small-step path glows calmly down toward the valley, then the too-far overshoot path flashes once and settles higher on the curve.
The learner's pencil hovers as if answering the quick check.
Keep the full vertical frame visible.
Keep existing text unchanged and readable.
No new text. No crop.
```

## Per-Frame Risk Notes

- Frame 1: Accept only if the chain clearly reads as mistake -> loss -> curve -> step. Reject if it becomes a decorative icon row.
- Frame 2: Reject if `loss: 8/10` is unreadable or the loss meter looks like a generic danger bar.
- Frame 3: Reject if the graph is too small or the `loss` and `weight setting` cues vanish.
- Frame 4: Reject if the downhill arrow is labeled as the gradient or if `gradient: higher loss` is too small for mobile.
- Frame 5: Reject if the update step crosses too far along the curve or if old/new points are unclear.
- Frame 6: Reject if the prediction becomes perfect or if the lower loss score is missing.
- Frame 7: Reject if the dotted path looks like sparkle instead of ordered repeated updates.
- Frame 8: Reject if the overshoot path looks like the correct path or if either landing point is cropped.

## Review Notes To Create After Images

After generation, create:

```text
assets/images/gradient-descent-how-ai-learns-from-mistakes-video-first-warm-minimal-v1/gradient-descent-warm-minimal-source-frame-review-notes.md
assets/images/gradient-descent-how-ai-learns-from-mistakes-video-first-warm-minimal-v1/gradient-descent-warm-minimal-source-contact-sheet.jpg
```

Review for:

- Warm Minimal Tablet Closeup consistency with the accepted style experiment.
- repeated improvement, not just one derivative slope
- visible mistake -> loss -> curve -> gradient direction -> small update -> lower loss -> repeat chain
- readable loss curve and labels on mobile
- tablet-dominant composition with human warmth through hand/sleeve/desk context
- minimal embedded text, no generic poster overlay, no extra labels
- no implication that the model reaches perfection in one step
