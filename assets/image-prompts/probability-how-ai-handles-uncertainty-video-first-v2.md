# Probability: How AI Handles Uncertainty - Video-First Prompt Pack v2

Source module: `modules/visual-ai-concepts/probability-how-ai-handles-uncertainty.source.md`
Derived from: `assets/image-prompts/probability-how-ai-handles-uncertainty-image-story.md`
Reference image-story run: `assets/images/experiments/probability-single-request-medium/`

This v2 is optimized for image-to-video source frames. It keeps the same warm native story world as the accepted image-only probability set, but removes poster-style explanation where voiceover can carry the teaching.

## Character / Style Bible

- Same recurring Indian teenage learner, 11th/12th standard
- Dark wavy hair, teal/green shirt, curious expressive face
- Warm wooden study desk, desk lamp, notebook, pen, books, sticky notes, small plant
- Tablet as the main probability surface
- Warm modern Indian educational illustration, cinematic 9:16 mobile source frame
- Use the accepted probability opener or first generated video frame as the character anchor
- Keep text minimal; use bars, scales, score chips, glows, arrows, and meters

## Video-First Rule

Image-only cards explain themselves when paused. These source frames should give Runway a clean motion target:

- one visual action per frame
- 0-1 short heading or only technical numbers
- no long explanatory sentences unless the frame is a recap
- large tablet UI and visible hand/face motion
- no dense labels, no paragraph text, no flat diagram card

## Technical Sequence

```text
possible answers -> probability scale -> score bars -> selected high score -> close scores lower confidence -> real AI panels -> recap chain -> quick check
```

## Frame Teaching Table

| # | Learning job | Visual evidence | Motion role | Risk |
|---|---|---|---|---|
| 1 | AI estimates likely answers | input with cat/dog/car option cards | option cards appear | too much opener text |
| 2 | Probability scale | 0 to 1 scale and pointer | pointer slides | scale becomes a static chart |
| 3 | Scores for options | cat/dog/car bars with values | bars grow | text-heavy poster |
| 4 | Highest score chosen | cat bar glows, chosen card appears | highlight/select | implies certainty |
| 5 | Close scores mean uncertainty | cat/dog bars close, low confidence meter | bars pulse, meter drops | warning symbol overused |
| 6 | Same idea in real AI | three compact AI panels | panels highlight | panels too tiny |
| 7 | Recap chain | input -> scores -> choice | nodes light up | memory text too dense |
| 8 | Quick check | clear winner vs close scores | uncertain card glows | score lists too small |

## Frame 1 - Possible Answers

```text
Use case: scientific-educational
Asset type: 9:16 source frame for image-to-video animation
Primary request: Create frame 1 of a video-first educational short about probability and AI uncertainty.
Scene/backdrop: Warm Indian study room with wooden desk, lamp, notebook, books, sticky notes, and small plant.
Subject: Same recurring Indian teenage learner with dark wavy hair and teal/green shirt, looking at a tablet.
Technical visual: Tablet shows one blurry tabby-cat face input/photo card in the center, with visible cat ears or whiskers, and three large option cards around it: cat, dog, car. None is selected yet. The input must not look like a dog, car, hedgehog, ball, toy, or fuzzy object because later frames make cat the highest score.
Style/medium: warm modern Indian educational illustration, polished cinematic 9:16 mobile frame.
Composition/framing: tablet and learner large, safe lower space for caption overlay, clear foreground/background separation.
Text (verbatim): "cat", "dog", "car"
Motion target for later video: the three option cards appear around the input one by one.
Constraints: minimal text only; no extra text; no logos; no watermark; no flat poster card; keep character and environment consistent; input photo must be visually consistent with a cat prediction.
```

Runway prompt:

```text
The three option cards appear around the tablet input one by one: cat, dog, car.
The student leans in slightly with a curious expression.
Gentle desk parallax and warm lamp glow.
Keep the full vertical frame visible. Keep text unchanged. No new text. No crop.
```

## Frame 2 - Probability Scale

```text
Use case: scientific-educational
Asset type: 9:16 source frame for image-to-video animation
Primary request: Create frame 2 showing probability as a simple likelihood scale.
Scene/backdrop: Same warm Indian study desk and tablet environment.
Subject: Same recurring learner pointing at the tablet.
Technical visual: Tablet shows a large horizontal scale from 0 to 1 with 0%, 50%, 100% below it. A pointer sits near 0.7.
Style/medium: warm modern Indian educational illustration, crisp mobile-readable tablet UI.
Composition/framing: tablet fills the center; learner hand visible; leave safe caption space.
Text (verbatim): "0", "0.5", "1", "0%", "50%", "100%"
Motion target for later video: the pointer slides from 0 toward about 0.7 and glows softly.
Constraints: no extra text; no logos; no watermark; keep numbers large; avoid dense labels.
```

Runway prompt:

```text
The probability pointer slides smoothly from 0 toward about 0.7.
The glow strengthens as the pointer moves right.
The student's finger follows the scale.
Keep the full vertical frame visible. Keep numbers unchanged. No new text. No crop.
```

## Frame 3 - Score Bars

```text
Use case: scientific-educational
Asset type: 9:16 source frame for image-to-video animation
Primary request: Create frame 3 showing AI assigning probability scores to possible answers.
Scene/backdrop: Same warm study desk and tablet.
Subject: Same learner watches a tablet with a clean bar chart.
Technical visual: Tablet shows three large probability bars. Cat is tallest, dog medium, car shortest. Each bar must include a single large high-contrast mobile-readable text label beside the bar, not tucked at the bottom edge: cat 0.72, dog 0.20, car 0.08.
Style/medium: warm modern Indian educational illustration with crisp readable UI.
Composition/framing: tablet centered and large, learner visible from side, enough margin for subtle camera movement. Fill more of the tablet with the bars and labels; avoid empty margins around the chart.
Text (verbatim): "cat 0.72", "dog 0.20", "car 0.08"
Motion target for later video: bars grow from zero to their final heights.
Constraints: no dense text; no extra text; no logos; no watermark; keep category-score labels large enough after video compression; do not rely only on animal/car icons; avoid poster headline.
```

Runway prompt:

```text
The three probability bars grow from zero to their final heights.
Cat grows tallest, dog medium, car shortest.
The student watches attentively.
Keep the full vertical frame visible. Keep labels and numbers unchanged. No new text. No crop.
```

## Frame 4 - Highest Score

```text
Use case: scientific-educational
Asset type: 9:16 source frame for image-to-video animation
Primary request: Create frame 4 showing AI choosing the highest probability without implying certainty.
Scene/backdrop: Same warm desk and tablet environment.
Subject: Learner points at the tallest probability bar.
Technical visual: Tablet shows the same cat/dog/car bars. The cat bar glows and a selected card appears.
Style/medium: warm modern Indian educational illustration, crisp tablet UI.
Composition/framing: tablet large, selected card easy to see, safe caption area.
Text (verbatim): "cat 0.72", "dog 0.20", "car 0.08", "chosen: cat"
Motion target for later video: cat bar glows, dog and car dim, selected card appears.
Constraints: no extra text; no logos; no watermark; do not add a certainty claim; keep all text readable.
```

Runway prompt:

```text
The cat probability bar glows green and the chosen cat card appears.
Dog and car dim slightly.
The student points at the selected answer.
Keep the full vertical frame visible. Keep labels unchanged. No new text. No crop.
```

## Frame 5 - Uncertainty

```text
Use case: scientific-educational
Asset type: 9:16 source frame for image-to-video animation
Primary request: Create frame 5 showing uncertainty when scores are close.
Scene/backdrop: Same warm study desk and tablet.
Subject: Same learner with a thoughtful uncertain expression.
Technical visual: Tablet shows close probability bars: cat 0.42, dog 0.39, car 0.19. Cat and dog are almost equal. A yellow low-confidence meter sits below.
Style/medium: warm modern Indian educational illustration, clear mobile-readable UI.
Composition/framing: tablet large, close bars visibly similar, student expression visible.
Text (verbatim): "cat 0.42", "dog 0.39", "car 0.19", "low confidence"
Motion target for later video: cat and dog bars pulse together; confidence meter drops or glows yellow.
Constraints: no dense text; no logos; no watermark; keep labels readable; avoid scary warning symbols.
```

Runway prompt:

```text
The cat and dog bars pulse together because their scores are close.
The confidence meter drops and glows yellow.
The student looks thoughtful and uncertain.
Keep the full vertical frame visible. Keep labels unchanged. No new text. No crop.
```

## Frame 6 - Real AI Panels

```text
Use case: scientific-educational
Asset type: 9:16 source frame for image-to-video animation
Primary request: Create frame 6 showing the same probability idea in different AI systems.
Scene/backdrop: Same warm study desk and tablet.
Subject: Learner watches three large mini panels on the tablet.
Technical visual: Tablet has three large icon-first panels: image AI, recommendation, chatbot. Each panel uses two or three thick probability bars and one highlighted likely option; the chatbot panel must also show visible probability bars, not only chat bubbles.
Style/medium: warm modern Indian educational illustration, crisp UI.
Composition/framing: tablet fills center; the three panels occupy most of the tablet height with little decorative spacing; labels are large enough for phone viewing; internal bars are thick and visible; avoid crowded text.
Text (verbatim): "image AI", "recommendation", "chatbot"
Motion target for later video: mini panels highlight one by one.
Constraints: minimal text only; no logos; no watermark; no dense numbers; use icons and bars more than words; do not make the panel labels or internal bars tiny.
```

Runway prompt:

```text
The three tablet panels highlight one by one: image AI, recommendation, chatbot.
Tiny probability bars in each panel glow briefly.
The student nods with understanding.
Keep the full vertical frame visible. Keep labels unchanged. No new text. No crop.
```

## Frame 7 - Recap Chain

```text
Use case: scientific-educational
Asset type: 9:16 source frame for image-to-video animation
Primary request: Create frame 7 as a low-text recap of probability in AI prediction.
Scene/backdrop: Same warm study desk and tablet environment.
Subject: Student smiles with an aha expression.
Technical visual: Tablet shows a clear visual chain: input icon -> probability bars -> chosen answer icon. Notebook has a short anchor note.
Style/medium: warm modern Indian educational illustration, polished and mobile-readable.
Composition/framing: recap chain large, memory note readable, safe bottom caption area.
Text (verbatim): "input", "scores", "choice", "confidence-weighted guess"
Motion target for later video: chain nodes light up left to right; memory note glows softly.
Constraints: no extra text; no logos; no watermark; keep text sparse and readable.
```

Runway prompt:

```text
The recap chain lights up from input to scores to choice.
The memory note glows softly.
The student smiles with an aha expression.
Keep the full vertical frame visible. Keep all text readable and unchanged. No new text. No crop.
```

## Frame 8 - Quick Check

```text
Use case: scientific-educational
Asset type: 9:16 source frame for image-to-video animation
Primary request: Create frame 8 as a quick check about uncertainty.
Scene/backdrop: Same warm study desk and tablet.
Subject: Learner compares two side-by-side score cards on the tablet.
Technical visual: Card A has one clear tall winner bar. Card B has two close top bars and a yellow uncertainty glow. Learner points to B.
Style/medium: warm modern Indian educational illustration, clean readable UI.
Composition/framing: two cards large, student visible, safe caption space.
Text (verbatim): "A", "B", "0.90", "0.42", "0.39"
Motion target for later video: Card B pulses gently and the uncertainty glow appears.
Constraints: no extra text; no logos; no watermark; keep numbers readable; let voiceover explain the full answer.
```

Runway prompt:

```text
The two score cards appear side by side.
Card B pulses gently and the yellow uncertainty glow appears because the top scores are close.
The student thinks, then points to B.
Keep the full vertical frame visible. Keep numbers unchanged. No new text. No crop.
```
