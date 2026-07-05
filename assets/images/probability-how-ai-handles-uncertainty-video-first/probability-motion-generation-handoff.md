# Probability Motion Generation Handoff

Status: approved-for-motion-prep
Date: 2026-07-03

## Decision

Use the existing source frames for the launch-batch Probability Short.

Do not regenerate the full Probability image set before the first motion pass. The frames are visually close enough to the warm study-desk math-series direction and the technical sequence is clear.

## Source Frames

Image base path:

```text
assets/images/probability-how-ai-handles-uncertainty-video-first/
```

Frames:

```text
01-ai-estimates-possible-answers.png
02-probability-scale-0-to-1.png
03-probability-scores-bars.png
04-highest-probability-chosen.png
05-close-scores-uncertainty.png
06-probability-ai-systems.png
07-recap-confidence-weighted-guess.png
08-quick-check-uncertainty.png
```

## Runway Setup Gate

Before submitting to Runway, upload each source frame and create a manifest with real public `image_url` values.

Do not submit from a manifest that contains only local paths.

Recommended manifest path:

```text
outputs/video-manifests/probability-how-ai-handles-uncertainty-runway-clips.json
```

Recommended output directory:

```text
outputs/runway-clips/probability-how-ai-handles-uncertainty-runway-clips/
```

Recommended settings:

```text
model: gen4_turbo
ratio: 720:1280
duration: 5
```

## Clip Prompts

### 01-ai-estimates-possible-answers

```text
The three answer cards appear around the tablet input one by one: cat, dog, car. The student looks curious and leans in slightly. Gentle desk parallax and warm lamp glow. Keep the tablet text readable and unchanged. Keep the full vertical frame visible. No new text. No crop.
```

### 02-probability-scale-0-to-1

```text
The probability pointer slides smoothly from 0 toward about 0.7. The confidence glow grows slightly as the pointer moves right. The student finger follows the scale with a small teaching gesture. Keep numbers readable and unchanged. Keep the full vertical frame visible. No new text. No crop.
```

### 03-probability-scores-bars

```text
The three probability bars grow from zero to their final heights. Cat grows tallest, dog medium, car shortest. The student watches attentively. Keep labels and numbers readable and unchanged. Keep the full vertical frame visible. No new text. No crop.
```

### 04-highest-probability-chosen

```text
The cat probability bar glows green and the chosen cat card brightens. The dog and car bars dim slightly. Student points at the selected answer. Keep labels readable and unchanged. Keep the full vertical frame visible. No new text. No crop.
```

### 05-close-scores-uncertainty

```text
The cat and dog bars pulse together because their scores are close. The confidence meter drops slightly and glows yellow. The student looks thoughtful and uncertain. Keep labels and numbers readable and unchanged. Keep the full vertical frame visible. No new text. No crop.
```

### 06-probability-ai-systems

```text
The three tablet panels highlight one by one: image AI, recommendation, chatbot. Small probability bars in each panel glow briefly. Keep movement gentle because this frame is text-dense. Keep labels readable and unchanged. Keep the full vertical frame visible. No new text. No crop.
```

### 07-recap-confidence-weighted-guess

```text
The recap chain lights up from input to probability scores to chosen answer. The memory sentence glows softly without changing. Use only a very mild push-in so the small text stays readable. Keep the full vertical frame visible. No new text. No crop.
```

### 08-quick-check-uncertainty

```text
The two score cards settle side by side. Card B pulses gently and the uncertainty icon glows to show closer scores. Student thinks, then nods. Keep all numbers readable and unchanged. Keep the full vertical frame visible. No new text. No crop.
```

## Motion QA Checklist

- Text and numbers remain readable on a phone screen.
- No new text appears in generated clips.
- Tablet content does not morph into different labels or scores.
- Frame 6 does not become visually crowded after panel highlights.
- Frame 7 memory sentence remains readable.
- Close scores in frames 5 and 8 still communicate lower confidence.
- Captions do not cover the tablet UI, especially in frames 6 and 7.
- Final motion still supports: `AI does not know for sure. It scores possibilities.`
