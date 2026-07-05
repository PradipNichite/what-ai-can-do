# Coded Skills Proposal

This note summarizes which Codex skills are worth creating from the current project docs and tools.

The strongest candidates are not generic writing skills. They are repeatable production workflows with clear file shapes, quality gates, and local scripts.

Before using existing artifacts as examples, read `SKILL_BASE_EXAMPLE_VALIDATION.md`.
That file records the ChatGPT vision validation pass for candidate base examples. Example suitability must come from visual inspection of the actual rendered assets.

For converting visual generation and review into API-backed product scripts, read `OPENAI_VISUAL_PRODUCTIZATION_PLAN.md`.

## Recommended Skill Set

### 1. `create-ai-math-micro-lesson`

Purpose:
Create a new "How AI Uses Math" lesson from a topic idea, using the repo's math-in-AI teaching rules.

Trigger examples:
- "Create a new math-in-AI lesson on graphs"
- "Make a micro-lesson for probability and AI uncertainty"
- "Use the math series pipeline for functions"

Inputs:
- Topic
- School concept
- AI use
- Optional target length, language, analogy, renderer priority

Outputs:
- `modules/visual-ai-concepts/<slug>.source.md`
- lesson-core fields from `HOW_AI_USES_MATH_LESSON_CORE_TEMPLATE.md`
- renderer-agnostic scene flow
- quick check and memory anchor

References to bundle:
- `HOW_AI_USES_MATH_SERIES_GUIDE.md`
- `HOW_AI_USES_MATH_LESSON_CORE_TEMPLATE.md`
- `HOW_AI_USES_MATH_SERIES_PLAN.md`
- `LEARNING_VIDEO_FORMATS.md`

Coded resources:
- `scripts/new_math_lesson_core.py`: create a correctly named source file from topic metadata.
- `scripts/check_math_lesson_core.py`: validate required fields such as school concept, AI use, mechanism, mini example, memory anchor, quick check, and renderer notes.

Priority: High.

Why:
This is the central repeatable creative workflow. It prevents every new lesson from rediscovering the same structure.

### 2. `build-video-first-prompt-pack`

Purpose:
Convert an approved lesson core into a video-first prompt pack with technical teaching value for each frame.

Trigger examples:
- "Create the video-first prompt pack for this lesson"
- "Turn this source module into image prompts"
- "Make Runway prompts for the probability lesson"

Inputs:
- Source module or lesson core
- Optional visual style override

Outputs:
- `assets/image-prompts/<slug>-video-first.md`
- 6-8 source image prompts
- matching Runway image-to-video prompts
- per-frame fields: learning job, visual evidence, transformation, motion role, risk

References to bundle:
- `VIDEO_FIRST_VISUAL_GUIDE.md`
- `VIDEO_PROMPT_TEMPLATES.md`
- `CHARACTER_CONSISTENCY_GUIDE.md`
- selected examples:
  - `assets/image-prompts/matrices-images-become-numbers-video-first.md`
  - `assets/image-prompts/vectors-how-ai-compares-meaning-video-first-v2.md`

Coded resources:
- `scripts/new_prompt_pack.py`: create a prompt pack skeleton from lesson scene flow.
- `scripts/check_prompt_pack.py`: flag missing Runway prompts, missing motion roles, too many frames without transformations, and missing character/style bible.

Priority: High.

Why:
The docs repeatedly warn against generic pretty frames. A skill can enforce "visible mechanism first" before image generation.

### 3. `assemble-and-verify-micro-video`

Purpose:
Take approved source frames, Runway clips, voiceover, and a manifest through render and verification.

Trigger examples:
- "Render this micro-lesson video"
- "Generate voiceover and assemble the final video"
- "Verify the rendered video for motion and black frames"

Inputs:
- Final video manifest or scene plan
- Voiceover text
- Clip URLs or local clip files

Outputs:
- `outputs/video-manifests/<slug>-micro-lesson-v1.en.json`
- voiceover MP3 under `outputs/video-assets/`
- rendered MP4 under `outputs/video-renders/`
- verification contact sheet and motion report
- Markdown script version under `outputs/video-scripts/`

References to bundle:
- `archive/docs-2026-07-04/NEW_VIDEO_TOPIC_SESSION_BRIEF.md` as historical context only
- `CONTENT_PIPELINE.md`
- `VIDEO_FIRST_VISUAL_GUIDE.md`

Coded resources:
- Existing scripts to bundle or wrap:
  - `tools/generate_elevenlabs_voiceover.py`
  - `tools/generate_scene_voiceovers.py`
  - `tools/generate_runway_clips.py`
  - `tools/render_creatomate_phase1.py`
  - `tools/verify_video_motion.py`
- New helper:
  - `scripts/check_video_artifacts.py`: verify the expected manifest, script, render, contact sheet, and motion report exist.

Priority: High, but after the first two.

Why:
This is the most code-heavy pipeline. It already has scripts, but a skill would give Codex the correct sequence and quality gates.

### 4. `write-video-script-version`

Purpose:
Create or update the human-readable Markdown version of a video manifest.

Trigger examples:
- "Create the Markdown script version for this manifest"
- "Sync the video script notes with the JSON"
- "Make a script versions index"

Inputs:
- Manifest JSON
- Voiceover file path
- Render path, if available
- Review notes

Outputs:
- `outputs/video-scripts/<asset-version>.md`
- optional `<episode>-script-versions.md` index

References to bundle:
- `CONTENT_PIPELINE.md`
- existing script examples from `outputs/video-scripts/`

Coded resources:
- `scripts/manifest_to_script_md.py`: parse JSON and generate the Markdown script version with purpose, files, learning design, full voiceover, scene timing, and review notes.
- `scripts/check_manifest_script_sync.py`: compare scene IDs, durations, captions, and voiceover text between JSON and Markdown.

Priority: Medium-high.

Why:
The repo explicitly requires JSON plus Markdown for every video version. This is deterministic and ideal for code.

### 5. `localize-marathi-visual-story`

Purpose:
Create natural Marathi versions of mobile stories or video captions, preserving meaning and local context.

Trigger examples:
- "Create a Marathi version of this story"
- "Localize this lesson for Maharashtra students"
- "Review Marathi captions for naturalness"

Inputs:
- English story/script/source module
- Target audience
- Optional dialect or formality notes

Outputs:
- Marathi story/script files, usually under `outputs/mobile-stories/` or renderer-specific paths
- QA notes for visual text rendering

References to bundle:
- `LOCALIZATION_GUIDE_MARATHI.md`
- `VISUAL_QA_CHECKLIST.md`
- representative Marathi outputs

Coded resources:
- `scripts/extract_visual_copy.py`: extract captions/card text from Markdown or JSON for localization review.
- `scripts/check_marathi_common_terms.py`: flag common terms that should usually stay familiar, transliterated, or not be over-translated.

Priority: Medium.

Why:
The language judgment is human-like, but extraction and QA support can be coded.

### 6. `visual-qa-validator`

Status: implemented locally at `.agents/skills/visual-qa-validator/`.

Purpose:
Review source frames, prompt packs, contact sheets, or rendered videos against the project's educational visual standards.

Trigger examples:
- "Review these frames"
- "Does this contact sheet pass the style gate?"
- "Check whether the video teaches the mechanism"

Inputs:
- Prompt pack, contact sheet, image directory, video, or motion report

Outputs:
- pass/revise decision
- frame-by-frame issues
- recommended next action
- status label such as `pass`, `rerender-visual`, `rerender-text`, or `needs-human-review`

References to bundle:
- `VIDEO_FIRST_VISUAL_GUIDE.md`
- `VISUAL_QA_CHECKLIST.md`
- `CHARACTER_CONSISTENCY_GUIDE.md`

Coded resources:
- Existing script:
  - `tools/verify_video_motion.py`
- New helper:
  - `scripts/make_image_contact_sheet.py`: create contact sheets from frame folders.
  - `scripts/check_frame_sequence.py`: verify numbered frames, expected count, contact sheet presence, and review note presence.

Priority: Medium.

Why:
This is a strong QA skill. It must use ChatGPT vision inspection for the verdict and may use deterministic artifact checks only as supporting diagnostics.

### 7. `manage-content-pipeline-board`

Purpose:
Keep topic files and `PIPELINE_BOARD.md` consistent with the project pipeline.

Trigger examples:
- "Move this topic to prompt-pack"
- "Update the pipeline board"
- "Show what is ready for visual QA"

Inputs:
- Topic slug or title
- New status/stage
- Next action

Outputs:
- updated metadata block in topic/episode files
- updated `PIPELINE_BOARD.md`
- optional missing-artifact report

References to bundle:
- `CONTENT_PIPELINE.md`
- `BACKLOG_STRUCTURE.md`
- `PIPELINE_BOARD.md`

Coded resources:
- `scripts/check_pipeline_status.py`: scan Markdown metadata and list mismatches against allowed labels/stages.
- `scripts/topic_inventory.py`: output a CSV/JSON table of topics, stages, types, next actions, and missing artifacts.

Priority: Medium.

Why:
This keeps production memory clean as the backlog grows.

## Build Order

1. `create-ai-math-micro-lesson`
2. `build-video-first-prompt-pack`
3. `write-video-script-version`
4. `assemble-and-verify-micro-video`
5. `review-visual-teaching-value`
6. `localize-marathi-visual-story`
7. `manage-content-pipeline-board`

## First Implementation Recommendation

Start with two skills:

1. `create-ai-math-micro-lesson`
2. `build-video-first-prompt-pack`

These cover the highest-leverage creative decisions before expensive image/video generation happens. They can share references but stay separate because one produces the stable lesson core, while the other adapts that core into video-first visual production.

After those are working, add `write-video-script-version` because it is small, deterministic, and will clean up the JSON/Markdown sync requirement.

## Skill Design Notes

- Keep `SKILL.md` lean and procedural.
- Put long project docs into `references/`.
- Put deterministic file creation and validation into `scripts/`.
- Do not create one giant "What AI Can Do" skill. The workflows trigger differently and should stay modular.
- Prefer scripts for validation, skeleton generation, contact sheets, manifest-to-Markdown conversion, and artifact inventory.
- Keep subjective educational judgment in the skill instructions, supported by checklists.
