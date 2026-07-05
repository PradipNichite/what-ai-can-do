# Probability Dual-Format Paired Experiment

Date: 2026-07-04

Purpose: test whether one OpenAI request can generate both renderer variants for the same scene:

1. image-only story card
2. video-first source frame

Prompt packs:

- Image-only: `assets/image-prompts/probability-how-ai-handles-uncertainty-image-story.md`
- Video-first v1 used for run: `assets/image-prompts/probability-how-ai-handles-uncertainty-video-first.md`
- Video-first v2 created after review: `assets/image-prompts/probability-how-ai-handles-uncertainty-video-first-v2.md`

Run:

```powershell
python tools/openai_dual_format_experiment.py `
  --image-prompt-pack assets/image-prompts/probability-how-ai-handles-uncertainty-image-story.md `
  --video-prompt-pack assets/image-prompts/probability-how-ai-handles-uncertainty-video-first.md `
  --out-dir assets/images/experiments/probability-dual-format-paired-frames `
  --only-frame 3 `
  --only-frame 5 `
  --quality low `
  --timeout 600 `
  --style-reference assets/images/experiments/probability-single-request-medium/01-lesson-opener.png
```

Trace ID: `019f2dd1-9180-7c73-883e-87726df3ef5b`

## Outputs

- `image-only-contact-sheet.jpg`
- `video-first-contact-sheet.jpg`
- `paired-format-comparison.jpg`

Frame results:

| Frame | Outputs requested | Outputs received | Image-only path | Video-first path |
|---|---:|---:|---|---|
| 3 | 2 | 2 | `image-only/03-scores-for-options.png` | `video-first/03-scores-for-options-video.png` |
| 5 | 2 | 2 | `image-only/05-close-scores-mean-uncertainty.png` | `video-first/05-close-scores-mean-uncertainty-video.png` |

## Visual Review

The paired request successfully returned two separate images for each tested frame.

The video-first outputs are the stronger result:

- same learner and desk world
- lower text density
- clear motion targets: bars growing, close bars pulsing, confidence meter dropping
- enough clean space for image-to-video movement

The image-only outputs are acceptable low-quality drafts but weaker than the standalone accepted probability image-only set:

- they are less self-contained
- they have less explanatory structure
- the paired prompt appears to pull the image-only output toward the simpler video-first style

## Follow-Up: Strict Pair Separation

The first paired prompt was too loose. It described the image-only output and the video-first output, but it did not strongly prevent the low-text video constraints from influencing the image-only card.

A stricter paired prompt was added to `tools/media_pipeline/openai_dual_format_experiment.py` and rerun with the video-first v2 pack:

```powershell
python tools/openai_dual_format_experiment.py `
  --image-prompt-pack assets/image-prompts/probability-how-ai-handles-uncertainty-image-story.md `
  --video-prompt-pack assets/image-prompts/probability-how-ai-handles-uncertainty-video-first-v2.md `
  --out-dir assets/images/experiments/probability-dual-format-paired-frames-v2-strict `
  --only-frame 3 `
  --only-frame 5 `
  --quality low `
  --timeout 600 `
  --style-reference assets/images/experiments/probability-single-request-medium/01-lesson-opener.png
```

Strict run trace ID: `019f3123-3279-7e80-bf57-6b3e1ef3896e`

Comparison sheet:

- `assets/images/experiments/probability-dual-format-strict-vs-v1-comparison.jpg`

Strict prompt result:

- The image-only output improved: explanatory text remained integrated on notebook/sticky-note surfaces, and the card was more self-contained.
- The video-first output stayed clean: lower text, large chart/meter surfaces, and clear motion targets.
- The model did return two valid separate outputs for each tested scene.

## Decision

Use paired generation as a serious experiment path, not merely a weak draft path. The better conclusion is: paired generation can work for both formats when the prompt explicitly protects each renderer's job.

Do not make it the default final production path yet, because we have only tested selected probability frames. But do keep improving and testing it.

Recommended production flow:

1. Generate or approve the image-only lesson first.
2. Create a video-first v2 prompt pack that removes dense explanation and keeps one motion target per scene.
3. Use the accepted image-only opener or best frame as the character/style reference.
4. Generate video-first source frames separately or with paired generation for selected technical scenes.
5. For selected scenes, test strict paired generation and compare against standalone generation.
6. Send only visually approved low-text frames to Runway.

## Prompt Learning

- The image-only and video-first prompts must explicitly preserve their different jobs.
- The video prompt should say what will move.
- The image-only prompt should retain enough integrated text to explain itself when paused.
- Paired generation can improve character consistency.
- The distinction between renderer formats must be enforced in the prompt with separate acceptance criteria for each output.
