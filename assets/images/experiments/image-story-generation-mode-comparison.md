# Image Story Generation Mode Comparison

Date: 2026-07-04

Purpose: compare `anchor-after-first` against `single-request-lesson` for image-only native educational stories.

OpenAI prompting source used:

- https://developers.openai.com/cookbook/examples/multimodal/image-gen-models-prompting-guide

## Pipeline Modes

`anchor-after-first`

- Generate card 1 with external style references.
- Use generated card 1 as the character/style anchor for cards 2-8.
- Generate cards 2-8 concurrently.
- Best for per-card retries, LangSmith filtering, and controlled repair.

`single-request-lesson`

- Send all frame prompts in one Responses API request.
- Ask the model to return one separate image per frame.
- Best tested for style/character continuity and reducing repeated reference-image inputs.
- Risk: long runtime, large LangSmith payload, less direct per-frame retry.

## Results

| Lesson | Mode | Output folder | Trace ID | Frames returned | QA status | QA next action |
|---|---|---|---|---:|---|---|
| Gradient Descent | anchor-after-first | `assets/images/experiments/gradient-descent-anchor-after-first-medium` | `019f2da7-3d6d-7ac0-a58b-058d7f3d341f` | 8 | `needs-revision` | `regenerate-frame` |
| Gradient Descent | single-request-lesson | `assets/images/experiments/gradient-descent-single-request-medium-retry` | `019f2db5-63f4-7a31-af76-92e1a0f13531` | 8 | `needs-revision` | `regenerate-frame` |
| Probability | anchor-after-first | `assets/images/experiments/probability-anchor-after-first-medium` | `019f2dbe-9dbd-7b80-aaab-1cfd242a5883` | 8 | `pass-with-caveats` | `accept` |
| Probability | single-request-lesson | `assets/images/experiments/probability-single-request-medium` | `019f2dc3-9924-7962-a398-d987da5ba82f` | 8 | `pass-with-caveats` | `accept` |

Comparison sheets:

- `assets/images/experiments/gradient-descent-mode-comparison.jpg`
- `assets/images/experiments/probability-mode-comparison.jpg`

## Visual Findings

Gradient Descent:

- Both modes failed for the same core reason: card 1 was not a self-contained opener. It showed the dog/cat mistake example but did not name Gradient Descent or connect slope/downhill steps to AI training.
- `single-request-lesson` had better same-character continuity. `anchor-after-first` drifted into a boy character in several frames.
- The right fix is prompt repair for card 1 before judging the mode as failed.

Probability:

- Both modes passed with caveats.
- `anchor-after-first` had slightly cleaner exact UI compliance in some frames.
- `single-request-lesson` had strong character/style continuity and returned all 8 separate frames.
- `single-request-lesson` triggered a LangSmith multipart ingest warning because the single OpenAI run payload was about 26.7 MB, above the 20 MB limit. This makes the mode risky for trace completeness unless we reduce payload size or avoid storing large image outputs in one trace.

## Recommendation

Default production mode should remain `anchor-after-first` because it keeps per-card retries, parallelism, and LangSmith filtering clean.

Keep `single-request-lesson` as an explicit experiment flag because it can improve character continuity and reduce repeated reference-image inputs. Before using it at scale, add safeguards:

- warn when the combined run payload is likely to exceed LangSmith limits
- prefer `jpeg` or `webp` for experiment runs if tracing payload size matters
- require QA to confirm `image_outputs_received == expected_frame_count`
- compare against `anchor-after-first` before accepting it as the default

## Prompt Refinement To Carry Forward

- Use the OpenAI cookbook prompt order: goal, scene, subject, details, constraints.
- Quote exact in-image text.
- Name the physical surface for every text string.
- Keep the opener self-contained: title, learning promise, school concept, AI use, and concrete example.
- For one lesson, keep a same-character strategy explicit in the prompt and generation mode.
- Repair the smallest failing unit: one frame, not the whole set, when the sequence is otherwise good.
