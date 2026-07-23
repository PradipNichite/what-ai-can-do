# Media Pipeline Tools

This folder contains the production scripts for the visual/video pipeline.
The old `tools/*.py` entrypoints are compatibility wrappers that call into this
folder, so existing commands still work.

## Folder Map

- `openai_visual_qa.py` - OpenAI vision review for actual images/contact sheets.
- `openai_visual_models.py` - Pydantic structured-output schema for QA verdicts.
- `openai_scene_adequacy.py` - structured scene-flow review before image prompts.
- `openai_image_story_generate.py` - parallel OpenAI image-story generation.
- `openai_image_story_pipeline.py` - one-command generation, contact sheet, and QA under one LangSmith trace.
- `openai_dual_format_experiment.py` - paired image-only/video-first generation experiments.
- `build_contact_sheet.py` - contact sheet creation for image folders.
- `pipeline_tracing.py` - LangSmith trace helpers with shared metadata/tags.
- `prompts/openai_visual_qa.md` - reviewable prompt instructions for visual QA.
- `generate_runway_clips.py` - Runway image-to-video task creation and polling.
- `render_creatomate_phase1.py` - Creatomate assembly/render submission.
- `generate_elevenlabs_voiceover.py` - ElevenLabs voiceover generation.
- `upload_tmpfiles.py` - public URL helper for source frames, Runway clips, and voiceover assets.
- `generate_elevenlabs_sfx.py` - ElevenLabs sound-effect generation.
- `generate_scene_voiceovers.py` - per-scene voiceover helper.
- `build_smart_video_manifest.py` - scene plan to Creatomate manifest.
- `verify_video_motion.py` - video-frame sampling and motion/contact-sheet checks.
- `verify_video_style_gate.py` - static guardrail that prevents programmatic animation from replacing approved shorts style or bypassing visual QA.
- `verify_image_story_gate.py` - textual image-story gate checker used by hooks.
- `verify_media_api_contracts.py` - static guardrail that keeps env names, API request fields, provider endpoints, and wrapper-script contracts aligned with `.agents/skills/media-api-contracts/`.
- `generate_marathi_captioned_story.py` - local captioned-story renderer.
- `build_knowledge_viewer.py` - local knowledge-viewer builder.
- `classify_scene_motion_strategy.py` - scene-level motion/router classifier for shorts video.
- `render_programmatic_animation.py` - deterministic code-driven educational animation renderer.
- `prompts/openai_scene_adequacy.md` - reviewable prompt instructions for pre-image scene adequacy.

## Keys And Local Environment

Put secrets in your shell environment or in a repo-root `.env` file:

```text
OPENAI_API_KEY=...
RUNWAYML_API_SECRET=...
CREATOMATE_API_KEY=...
ELEVENLABS_API_KEY=...
```

Production video shorts use:

```text
source frames -> image-to-video clips -> ElevenLabs voice -> Creatomate assembly
```

Local still-image assembly is only a timing/debug preview and should not be
presented as a comparison candidate or final deliverable.

Optional OpenAI settings:

```text
OPENAI_IMAGE_MODEL=gpt-image-2
OPENAI_IMAGE_AGENT_MODEL=gpt-5.5
OPENAI_VISION_QA_MODEL=gpt-5.5
OPENAI_MAX_PARALLEL_IMAGES=3
OPENAI_MAX_PARALLEL_QA=2
OPENAI_REQUEST_TIMEOUT_SECONDS=180
OPENAI_IMAGE_REFERENCE_STRATEGY=anchor-after-first
OPENAI_IMAGE_CHARACTER_ANCHOR_CARD=1
OPENAI_IMAGE_OUTPUT_COMPRESSION=
```

Optional LangSmith tracing:

```text
LANGSMITH_TRACING=true
LANGSMITH_API_KEY=...
LANGSMITH_PROJECT=what-ai-can-do-media-pipeline
```

The repo `.gitignore` excludes `.env`. Do not commit secrets.

## Structured Output

OpenAI calls use the official OpenAI Python SDK wrapped with LangSmith:

```python
from langsmith.wrappers import wrap_openai
client = wrap_openai(OpenAI())
```

Image generation uses the Responses API `image_generation` tool so the OpenAI
call is auto-traced by LangSmith as an OpenAI call, not hand-written as a custom
log span. The image tool model is `OPENAI_IMAGE_MODEL`; the Responses model that
invokes the tool is `OPENAI_IMAGE_AGENT_MODEL`.

`openai_visual_qa.py` uses the OpenAI Python SDK parse path:

```python
client.responses.parse(..., text_format=VisualQAVerdict)
```

`VisualQAVerdict` is a Pydantic model in `openai_visual_models.py`. Pydantic is
the source of truth; the SDK turns it into the strict structured-output schema
used by OpenAI and returns `response.output_parsed`.

`openai_scene_adequacy.py` uses the same SDK parse path with
`SceneAdequacyVerdict`. This is the upstream gate: it checks whether the scene
sequence can teach the technical concept before image-generation cost is spent.

## Commands

Review a lesson's scene flow before image generation:

```powershell
python tools/openai_scene_adequacy.py `
  --source-module modules/visual-ai-concepts/gradient-descent-how-ai-learns-from-mistakes.source.md `
  --prompt-pack assets/image-prompts/gradient-descent-how-ai-learns-from-mistakes-image-story.md `
  --renderer image-story `
  --topic "Gradient Descent: how AI learns from mistakes" `
  --out assets/reviews/gradient-descent-scene-adequacy.md `
  --json-out assets/reviews/gradient-descent-scene-adequacy.json
```

Run QA on the graphs image-story contact sheet:

```powershell
python tools/openai_visual_qa.py `
  --image-folder assets/images/graphs-how-ai-understands-relationships-image-story `
  --contact-sheet assets/images/graphs-how-ai-understands-relationships-image-story/graphs-how-ai-understands-relationships-image-story-contact-sheet.jpg `
  --prompt-pack assets/image-prompts/graphs-how-ai-understands-relationships-image-story.md `
  --source-module modules/visual-ai-concepts/graphs-how-ai-understands-relationships.source.md `
  --mode image-story `
  --out assets/images/graphs-how-ai-understands-relationships-image-story/graphs-how-ai-understands-relationships-image-story-openai-qa.md `
  --json-out assets/images/graphs-how-ai-understands-relationships-image-story/graphs-how-ai-understands-relationships-image-story-openai-qa.json
```

Generate image-story cards concurrently:

```powershell
python tools/openai_image_story_generate.py `
  --prompt-pack assets/image-prompts/graphs-how-ai-understands-relationships-image-story.md `
  --out-dir assets/images/graphs-how-ai-understands-relationships-image-story-openai `
  --parallel 4 `
  --quality medium
```

Run generation, contact sheet, and QA under one LangSmith parent trace:

```powershell
python tools/openai_image_story_pipeline.py `
  --prompt-pack assets/image-prompts/graphs-how-ai-understands-relationships-image-story.md `
  --source-module modules/visual-ai-concepts/graphs-how-ai-understands-relationships.source.md `
  --out-dir assets/images/graphs-how-ai-understands-relationships-image-story-openai-traced `
  --parallel 3
```

For a targeted repair/test run, add `--only-card 5`.

## Cost And Character Strategy

The default production strategy is `anchor-after-first`:

1. Generate card 1 first using the external style references.
2. Use the generated card 1 as the character/style anchor for cards 2-N.
3. Generate cards 2-N concurrently.

This reduces repeated reference-image inputs and improves within-lesson
character consistency. Use these flags to override it:

```powershell
--reference-strategy anchor-after-first
--character-anchor-card 1
```

Other strategies:

- `all-cards` - sends the external style references to every card request.
  Highest reference pressure, higher input-image cost.
- `single-request-lesson` - asks one OpenAI Responses request to produce all
  lesson frames as separate image outputs. Useful for experiments and may
  improve character continuity, but can be slower, harder to repair per frame,
  and can create very large LangSmith payloads.
- `none` - sends no style references. Cheapest, but only safe when prompts are
  already strongly style-locked.

Recommended cost ladder:

- Draft: `--image-model gpt-image-1-mini --quality low`, one or two target
  cards only, usually `--only-card 1` and the most technical card.
- Review: `--image-model gpt-image-2 --quality low`, full lesson with QA.
- Final: `--image-model gpt-image-2 --quality medium`, only after the prompt
  pack and character anchor are working.

Use `jpeg` or `webp` plus `--output-compression` when smaller files or faster
transfer matter. Keep `png` for visual QA baselines if compression artifacts
would make text review harder.

Run a whole lesson as one request only when comparing strategies:

```powershell
python tools/openai_image_story_pipeline.py `
  --prompt-pack assets/image-prompts/probability-how-ai-handles-uncertainty-image-story.md `
  --source-module modules/visual-ai-concepts/probability-how-ai-handles-uncertainty.source.md `
  --out-dir assets/images/experiments/probability-single-request-medium `
  --reference-strategy single-request-lesson `
  --quality medium
```

The Image API `n` parameter is useful for variants, not for eight different
educational story frames with different text and layout requirements. This
pipeline uses the Responses API image-generation tool and asks the model to make
multiple separate tool calls. Treat the result as experimental until QA confirms
that all expected frames were returned and the LangSmith trace ingested cleanly.

## Paired Image-Only And Video-First Experiments

Use `openai_dual_format_experiment.py` when testing whether one request can
produce both renderer variants for the same scene:

```powershell
python tools/openai_dual_format_experiment.py `
  --image-prompt-pack assets/image-prompts/probability-how-ai-handles-uncertainty-image-story.md `
  --video-prompt-pack assets/image-prompts/probability-how-ai-handles-uncertainty-video-first-v2.md `
  --out-dir assets/images/experiments/probability-dual-format-paired-frames `
  --only-frame 3 `
  --only-frame 5 `
  --quality low `
  --style-reference assets/images/experiments/probability-single-request-medium/01-lesson-opener.png
```

The request asks for exactly two separate outputs with strict pair separation:

1. `IMAGE_ONLY_STORY_CARD` - self-contained, text-integrated card.
2. `VIDEO_SOURCE_FRAME` - lower-text source frame with one motion target.

The paired prompt explicitly tells the model these are not two variations of the
same poster. It protects the image-only card from becoming too sparse and
protects the video frame from inheriting dense poster text.

Use this for strategy tests and selected high-value scenes. It can work for both
formats when both outputs have separate acceptance criteria. For final
production, keep comparing against standalone renderer prompt packs until paired
QA is strong across several lessons.

Dry runs do not call OpenAI:

```powershell
python tools/openai_visual_qa.py ... --dry-run
python tools/openai_image_story_generate.py ... --dry-run
```

## Programmatic Technical Animation

Use this lane for precise technical motion where image-to-video would likely
warp labels, curves, or numeric relationships.

Classify a source module before generating clips:

```powershell
python tools/classify_scene_motion_strategy.py `
  --source-module modules/visual-ai-concepts/gradient-descent-how-ai-learns-from-mistakes.source.md `
  --out outputs/video-manifests/gradient-descent-motion-strategy-v1.json `
  --md-out outputs/video-scripts/gradient-descent-motion-strategy-v1.md
```

Attach classifier output to a smart edit manifest when the scene IDs match:

```powershell
python tools/build_smart_video_manifest.py outputs/video-manifests/<plan>.json `
  --motion-strategy outputs/video-manifests/gradient-descent-motion-strategy-v1.json `
  --out outputs/video-manifests/<edit>.json
```

Render the gradient descent prototype:

```powershell
python tools/render_programmatic_animation.py `
  --spec outputs/video-manifests/gradient-descent-programmatic-animation-v1.json `
  --backend auto `
  --out outputs/video-renders/gradient-descent-programmatic-animation-v1.mp4 `
  --poster outputs/video-renders/gradient-descent-programmatic-animation-v1-poster.png `
  --report outputs/video-renders/gradient-descent-programmatic-animation-v1.render-report.json
```

Verify the rendered motion:

```powershell
python tools/verify_video_motion.py outputs/video-renders/gradient-descent-programmatic-animation-v1.mp4 --samples 12
```

The prototype currently implements `animation_backend: "pillow"`. Keep the
backend in the manifest and CLI because later experiments should be able to use
the same lesson spec with backends such as `motion-canvas`, `revideo`,
`remotion`, or `manim` instead of rewriting the lesson plan.

## Parallelism

`openai_image_story_generate.py` parallelizes per-card image requests with
`ThreadPoolExecutor`. Use `--parallel N` or `OPENAI_MAX_PARALLEL_IMAGES`.

Start conservatively, for example `--parallel 3` or `--parallel 4`, then raise
or lower it based on rate limits, latency, and cost comfort.
