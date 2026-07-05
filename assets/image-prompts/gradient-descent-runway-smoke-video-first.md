# Gradient Descent Runway Smoke Test - Video-First Source Frames

Source module: `modules/visual-ai-concepts/gradient-descent-how-ai-learns-from-mistakes.source.md`
Base video-first pack: `assets/image-prompts/gradient-descent-how-ai-learns-from-mistakes-video-first.md`
Output folders:

- `assets/images/gold-candidates/gradient-descent-runway-smoke-source-v1/` - story-reference attempt, rejected because the opener style reference contaminated mid-lesson frames.
- `assets/images/gold-candidates/gradient-descent-runway-smoke-source-v2/` - clean mechanism-first attempt for A/B comparison.

Purpose: generate only the highest-risk video source frames before spending Runway credits on a full lesson.

Runway A/B smoke test:

- Manifest: `outputs/video-manifests/gradient-descent-runway-style-ab-frame4-v1.json`
- Clips: story-derived frame 4 versus clean mechanism-first frame 4.
- Use this test to compare retention/learning focus before choosing the full-video source-frame mode.

Global smoke-test constraints:

- These are mid-lesson video source frames, not self-contained posters.
- Do not render the lesson title or a large top banner.
- Do not show the dog/cat prediction example in these frames.
- Do not show "prediction: dog" or "correct: cat".
- Tablet must be the main technical surface and must show only the requested mechanism for that frame.
- Keep text sparse, large, and motion-safe.

## Frames

### Frame 4 - Gradient Direction

Learning job: local slope gives a direction clue; gradient descent moves opposite that clue to lower loss.

Runway prompt:

```text
The tangent line and faint higher-loss gradient cue draw first, then the separate opposite downhill arrow draws toward the lower part of the curve. The learner's pointing hand moves slightly. Keep existing text unchanged. No new text. No crop.
```

Prompt:

```text
Use case: scientific-educational
Asset type: 9:16 source frame for image-to-video animation
Primary request: Create frame 4 showing only the gradient direction mechanism on the loss curve. This is a mid-lesson video source frame, not an opener or poster.
Scene/backdrop: same warm Indian study desk, lamp and notebook visible.
Subject: same recurring learner in teal/green shirt, looking focused and pointing gently at the tablet.
Style/medium: realistic warm study-desk/tablet technical style, polished cinematic vertical frame.
Composition/framing: tablet large in foreground with learner hand near the curve. No title banner at the top.
Text (verbatim): "gradient: higher loss", "move opposite", "lower error".
Technical overlay: tablet shows only a large U-shaped loss curve with one point on the slope and a thin tangent line at the point. Add a faint uphill cue labeled "gradient: higher loss" and a separate stronger downhill arrow labeled "move opposite" toward "lower error".
Motion target for later video: tangent/gradient cue draws first, then the opposite downhill arrow draws toward lower error.
Constraints: keep text minimal and readable; no lesson title; no top banner; no dog/cat image; no prediction/correct cards; no sticky-note slogans; no logos; no watermark; no dense formulas; do not label the downhill arrow as the gradient.
```

### Frame 5 - Small Update

Learning job: the model changes its weight by a small amount opposite the gradient.

Runway prompt:

```text
The curve point moves one short step downhill and the small step arrow glows. The update note stays locked and readable. Add only subtle hand motion and tablet glow. No new text. No crop.
```

Prompt:

```text
Use case: scientific-educational
Asset type: 9:16 source frame for image-to-video animation
Primary request: Create frame 5 showing only one small gradient descent update on the loss curve. This is a mid-lesson video source frame, not an opener or poster.
Scene/backdrop: same warm Indian study room, wooden desk, warm lamp, notebook, books, small plant.
Subject: same Indian teenage learner in teal/green shirt, focused expression, hand near tablet.
Style/medium: realistic warm study-desk/tablet technical style, polished 9:16 mobile frame.
Composition/framing: tablet is the main technical surface; learner and desk remain visible. No title banner at the top.
Text (verbatim): "small step", "opposite gradient", "new weight = old weight - small step".
Technical overlay: tablet shows only the loss curve with an old point and a nearby new point slightly lower on the curve; a short step arrow labeled "opposite gradient" connects them. Put the simple update visual "new weight = old weight - small step" as a large readable note on the tablet, not a dense formula.
Motion target for later video: point moves one short step opposite the gradient cue and the step arrow glows.
Constraints: keep both text elements large and readable; no lesson title; no top banner; no dog/cat image; no prediction/correct cards; no sticky-note slogans; no extra text; no logos; no watermark; avoid tiny equation writing; step must be visibly small.
```

### Frame 8 - Quick Check Step Size Matters

Learning job: compare careful small steps with overshooting.

Runway prompt:

```text
The small-step path glows calmly down toward the valley, then the too-far overshoot path flashes once and settles higher on the curve. The learner's pencil hovers as if answering a quick check. Keep all text unchanged. No new text. No crop.
```

Prompt:

```text
Use case: scientific-educational
Asset type: 9:16 source frame for image-to-video animation
Primary request: Create frame 8 as a quick check showing only that step size matters in gradient descent. This is a mid-lesson video source frame, not an opener or poster.
Scene/backdrop: same warm Indian study desk with lamp, notebook, books, small plant.
Subject: same recurring Indian teenage learner in teal/green shirt, holding a pencil over notebook while looking at the tablet.
Style/medium: realistic warm study-desk/tablet technical style, polished cinematic vertical frame.
Composition/framing: tablet and notebook both visible; tablet shows a large comparison diagram. No title banner at the top.
Text (verbatim): "small step", "too far".
Technical overlay: tablet shows only one large U-shaped loss curve with two paths: a smooth small-step dotted path descending toward the valley, and a second oversized path that jumps across the valley and lands higher, labeled "too far"; keep the comparison simple and readable.
Motion target for later video: small-step path glows calmly, then the overshoot path flashes once.
Constraints: keep labels large and readable; no lesson title; no top banner; no dog/cat image; no prediction/correct cards; no sticky-note slogans; no extra text; no logos; no watermark; no dense formulas; avoid scary warning symbols; safe bottom caption area.
```
