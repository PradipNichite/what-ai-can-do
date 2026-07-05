# OpenAI Visual Productization Plan

Status: implementation handoff

Purpose: convert the current Codex-assisted visual workflow into reusable Python tools that use the user's OpenAI API key for image generation and AI vision review.

This plan follows the repo rule:

```text
first-time idea or uncertain workflow -> explore with Codex/ChatGPT capabilities
approved repeatable workflow -> productize as code, API script, skill, hook, template, or canonical doc
```

## Product Goal

Build a scriptable visual production layer for this project:

```text
lesson core
-> prompt pack
-> OpenAI image generation
-> saved images + metadata
-> OpenAI vision QA
-> structured verdict
-> repair plan / regenerate / accept
-> optional video-first adaptation
-> existing Runway / voiceover / Creatomate pipeline
```

No UI is required now. The product surface is Python CLI tools that Codex can call repeatedly.

## Existing Assets To Reuse

Canonical docs:

- `AGENTS.md`
- `IMAGE_STORY_GATE.md`
- `VISUAL_QA_CHECKLIST.md`
- `CONTENT_PIPELINE.md`
- `HOW_AI_USES_MATH_SERIES_GUIDE.md`
- `HOW_AI_USES_MATH_IMAGE_PREREQUISITES.md`
- `VIDEO_FIRST_VISUAL_GUIDE.md`
- `VIDEO_PROMPT_TEMPLATES.md`
- `SKILL_BASE_EXAMPLE_VALIDATION.md`

Prompt archives:

- `assets/image-prompts/*-image-story.md`
- `assets/image-prompts/*-video-first.md`

Existing generated assets:

- `assets/images/*`

Existing video/product scripts:

- `tools/generate_runway_clips.py`
- `tools/generate_elevenlabs_voiceover.py`
- `tools/generate_scene_voiceovers.py`
- `tools/render_creatomate_phase1.py`
- `tools/build_smart_video_manifest.py`
- `tools/verify_video_motion.py`
- `tools/verify_image_story_gate.py`

The new OpenAI scripts should not replace the existing video pipeline. They should add the missing generation/review layer before image-to-video.

## Environment Contract

Required:

```text
OPENAI_API_KEY
```

Recommended optional variables:

```text
OPENAI_IMAGE_MODEL
OPENAI_VISION_QA_MODEL
OPENAI_MAX_PARALLEL_IMAGES
OPENAI_MAX_PARALLEL_QA
OPENAI_REQUEST_TIMEOUT_SECONDS
```

Do not commit `.env` files or secrets.

The scripts should read environment variables and allow CLI overrides.

## New Tool Set

### 1. `tools/openai_image_story_generate.py`

Purpose:

Generate image-only educational story cards from an approved prompt pack.

Inputs:

```text
--prompt-pack assets/image-prompts/<slug>-image-story.md
--out-dir assets/images/<slug>-image-story-openai/
--model <optional image model>
--parallel <N>
--dry-run
```

Responsibilities:

- Parse frame/card prompts from the prompt pack.
- Check that prompt pack includes required `IMAGE_STORY_GATE.md` language before generation.
- Generate each card through OpenAI image generation API.
- Run cards in parallel with a configurable concurrency limit.
- Save each generated image using stable ordered names:

```text
01-<short-card-name>.png
02-<short-card-name>.png
...
```

- Save per-card metadata:

```text
assets/images/<slug>-image-story-openai/metadata/01.json
```

Metadata should include:

- source prompt pack path
- card number
- prompt text
- model
- size / quality / output format
- request timestamp
- output path
- API response id if available
- seed or deterministic inputs if available
- retry count

Outputs:

- generated cards
- `generation-run.json`
- contact sheet
- optional machine-readable card index

### 2. `tools/openai_visual_qa.py`

Purpose:

Use OpenAI vision to review actual rendered images/contact sheets and produce a structured QA verdict.

Inputs:

```text
--image-folder assets/images/<slug>/
--contact-sheet assets/images/<slug>/<contact-sheet>.jpg
--prompt-pack assets/image-prompts/<slug>.md
--source-module modules/visual-ai-concepts/<slug>.source.md
--mode image-story | video-first | style-reference | skill-base
--out assets/images/<slug>/<slug>-openai-qa.md
--json-out assets/images/<slug>/<slug>-openai-qa.json
```

Responsibilities:

- Send actual image files or contact sheet to OpenAI vision model.
- Apply the correct rubric:
  - image-only story: `IMAGE_STORY_GATE.md`
  - general visual QA: `VISUAL_QA_CHECKLIST.md`
  - math-in-AI: `HOW_AI_USES_MATH_SERIES_GUIDE.md`
  - video-first: `VIDEO_FIRST_VISUAL_GUIDE.md`
  - skill-base example: `SKILL_BASE_EXAMPLE_VALIDATION.md`
- Return structured JSON:

```json
{
  "status": "pass | pass-with-caveats | needs-revision | reject | reference-only",
  "intended_use": "image-story",
  "opener": {
    "status": "pass | fail | partial",
    "evidence": "...",
    "required_fix": "..."
  },
  "native_composition": {
    "status": "pass | fail | partial",
    "evidence": "...",
    "required_fix": "..."
  },
  "overlay_risk": {
    "status": "low | medium | high",
    "evidence": "..."
  },
  "mechanism_visibility": {
    "status": "pass | fail | partial",
    "evidence": "...",
    "required_fix": "..."
  },
  "mobile_readability": {
    "status": "pass | fail | partial",
    "evidence": "...",
    "required_fix": "..."
  },
  "frame_notes": [
    {
      "frame": 1,
      "status": "pass | needs-revision | reject",
      "evidence": "...",
      "fix": "..."
    }
  ],
  "verdict": "...",
  "next_action": "accept | regenerate-frame | regenerate-set | revise-prompt-pack | use-as-reference-only"
}
```

Outputs:

- Markdown QA note
- JSON QA result
- optional repair prompt pack fragment

Hard rule:

The verdict must come from OpenAI vision analysis of actual rendered images, not prompt text alone.

### 3. `tools/openai_repair_prompt_pack.py`

Purpose:

Convert QA failures into targeted regeneration prompts.

Inputs:

```text
--qa-json assets/images/<slug>/<slug>-openai-qa.json
--prompt-pack assets/image-prompts/<slug>.md
--out assets/image-prompts/<slug>-repair-pass-01.md
```

Responsibilities:

- Read failed frames from QA JSON.
- Preserve accepted frames.
- Write targeted regeneration prompts only for failed frames.
- Include exact failure evidence from QA.
- Keep required gate language.

### 4. `tools/build_contact_sheet.py`

Purpose:

Create contact sheets for any generated image folder.

Inputs:

```text
--image-folder assets/images/<slug>/
--out assets/images/<slug>/<slug>-contact-sheet.jpg
--columns 4
```

Responsibilities:

- Make visual review easier.
- Preserve frame order.
- Add small file/frame labels.

This is a utility only. It does not approve visual quality.

### 5. `tools/openai_visual_pipeline.py`

Purpose:

Run the full productized visual loop.

Inputs:

```text
--prompt-pack assets/image-prompts/<slug>-image-story.md
--source-module modules/visual-ai-concepts/<slug>.source.md
--out-dir assets/images/<slug>-image-story-openai/
--mode image-story
--parallel-images 4
--parallel-qa 2
--max-repair-rounds 2
```

Flow:

```text
validate prompt pack
-> generate images in parallel
-> build contact sheet
-> OpenAI vision QA
-> if pass: write accepted review note
-> if fail: create repair prompt pack
-> optionally regenerate failed frames
-> repeat until pass or max repair rounds reached
```

Outputs:

- generated images
- contact sheet
- generation metadata
- QA JSON
- QA Markdown
- repair prompt pack if needed
- final status file:

```text
assets/images/<slug>/pipeline-status.json
```

## Data And Folder Conventions

For image-only stories:

```text
assets/image-prompts/<slug>-image-story.md
assets/images/<slug>-image-story-openai/
assets/images/<slug>-image-story-openai/01-*.png
assets/images/<slug>-image-story-openai/<slug>-contact-sheet.jpg
assets/images/<slug>-image-story-openai/<slug>-openai-qa.md
assets/images/<slug>-image-story-openai/<slug>-openai-qa.json
assets/images/<slug>-image-story-openai/generation-run.json
assets/images/<slug>-image-story-openai/pipeline-status.json
```

For video-first frames:

```text
assets/image-prompts/<slug>-video-first.md
assets/images/<slug>-video-first-openai/
assets/images/<slug>-video-first-openai/<slug>-source-contact-sheet.jpg
assets/images/<slug>-video-first-openai/<slug>-openai-qa.md
assets/images/<slug>-video-first-openai/<slug>-openai-qa.json
```

Do not overwrite existing hand-generated or Codex-generated image folders. Use `-openai` suffix until the new pipeline is trusted.

## Parallelism Plan

Generation:

- Run multiple image requests concurrently.
- Default concurrency should be conservative, for example 3 or 4.
- CLI should allow higher or lower concurrency.
- Each card should be independently retryable.

QA:

- QA can happen at two levels:
  - contact-sheet review for sequence-level verdict
  - per-frame review for detailed repair
- Start with one contact-sheet QA call.
- Use per-frame QA only when contact-sheet QA fails or text/readability is uncertain.

Batch mode:

- Add later after single-topic flow works.
- It should process many prompt packs asynchronously.
- It should write one summary table:

```text
outputs/visual-pipeline-runs/<date-run-id>/summary.md
```

## Product Acceptance Rules

An image-story output can be accepted only when:

- `tools/verify_image_story_gate.py --changed` passes for changed prompt/review Markdown.
- OpenAI vision QA returns `pass` or explicitly approved `pass-with-caveats`.
- The QA Markdown records evidence for opener, native composition, overlay risk, readability, and mechanism visibility.
- The generated image folder contains metadata and contact sheet.

A video-first source set can be sent to Runway only when:

- OpenAI vision QA says the frame set is suitable for video-first use.
- Each frame has a visible technical job.
- Text is sparse enough for image-to-video.
- Motion targets are clear in the prompt pack.

## Implementation Phases

### Phase 1: API QA First

Build first:

- `tools/openai_visual_qa.py`
- JSON schema for QA output
- Markdown QA writer

Why first:

- We already have many generated images.
- QA can validate existing examples immediately.
- It proves the review layer before spending image-generation credits.

Test target:

```text
assets/images/graphs-how-ai-understands-relationships-image-story/
```

Expected result:

```text
needs-revision
```

because the opener/native-card composition fails.

### Phase 2: Contact Sheet Utility

Build:

- `tools/build_contact_sheet.py`

Why:

- API vision QA needs a stable visual input.
- Existing folders are inconsistent.

### Phase 3: OpenAI Image Generation

Build:

- `tools/openai_image_story_generate.py`

Start with:

```text
assets/image-prompts/graphs-how-ai-understands-relationships-image-story.md
```

Goal:

- regenerate card 1 or a full corrected set through OpenAI image generation.

### Phase 4: Repair Loop

Build:

- `tools/openai_repair_prompt_pack.py`
- failed-frame regeneration flow

Goal:

- QA failure becomes targeted regeneration, not manual guessing.

### Phase 5: One-Command Pipeline

Build:

- `tools/openai_visual_pipeline.py`

Goal:

```text
prompt pack -> images -> contact sheet -> OpenAI QA -> repair or accept
```

### Phase 6: Integrate With Existing Video Pipeline

Connect accepted video-first frames to:

- `tools/generate_runway_clips.py`
- `tools/generate_elevenlabs_voiceover.py`
- `tools/render_creatomate_phase1.py`
- `tools/verify_video_motion.py`

Do not rewrite existing video tools until the OpenAI visual layer is stable.

## First Fresh Session Brief

Start a fresh session with this task:

```text
Read AGENTS.md, AGENT_SYSTEM_OVERVIEW.md, OPENAI_VISUAL_PRODUCTIZATION_PLAN.md, IMAGE_STORY_GATE.md, and VISUAL_QA_CHECKLIST.md.

Implement Phase 1 of OPENAI_VISUAL_PRODUCTIZATION_PLAN.md:
- create tools/openai_visual_qa.py
- use OPENAI_API_KEY from environment
- accept an image folder/contact sheet and prompt/source context
- call OpenAI vision through the Responses API
- produce structured JSON and Markdown QA
- test on assets/images/graphs-how-ai-understands-relationships-image-story/
- do not generate new images yet
```

## Guardrails

- Do not commit API keys.
- Do not approve visual quality without OpenAI/ChatGPT vision on actual rendered images.
- Do not let local scripts replace visual judgment.
- Do not overwrite existing asset folders during early implementation.
- Keep Codex exploration available for first-time creative work.
- Productize only repeatable flows that have a clear artifact contract.

## Open Questions For Implementation

Resolve during Phase 1:

- Which exact OpenAI model should be default for visual QA?
- Which exact OpenAI image model should be default for generation?
- Should QA send a contact sheet, individual images, or both?
- What maximum contact-sheet size is safe for API review?
- Should generated images be stored as PNG by default?
- Should retry logic be per-card, per-set, or both?

These should be answered from current official OpenAI docs during implementation, not from memory.
