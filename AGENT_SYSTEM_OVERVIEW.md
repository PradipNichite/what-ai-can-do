# Agent System Overview

This file explains the local Codex setup for this project: agent instructions, skills, hooks, and where to look before changing them.

## Agent Start Instructions

There is no `agent.start.md` file in this repository.

The active repo-level agent instruction file is:

```text
AGENTS.md
```

It currently contains these mandatory rule groups:

- No-guessing preflight: inspect this overview, the relevant local skill, and live repository state before visual/video/QA/hook/skill/pipeline/API/env work. For API keys, read `.env.example` and search the consuming script before naming or rejecting an env var. If docs conflict with the filesystem, update the docs.
- Explore then productize: use Codex/ChatGPT built-in capabilities for first-time discovery, then turn approved repeatable workflows into product assets such as scripts, skills, hooks, templates, or pipeline docs.
- Documentation hygiene: search existing docs first, update the smallest canonical file, and avoid scattered process notes.
- Image-only educational stories: read `IMAGE_STORY_GATE.md` before creating or reviewing image-only stories, and run the verifier after editing image-story prompt packs or review notes.
- Non-negotiable visual standard: image-only lesson cards must be self-contained native educational cards, not background images with pasted caption blocks.
- Video style gate: use the `video-style-gate` skill and video verifier before creating, editing, assembling, reviewing, or presenting How AI Uses Math video work.
- Media API contracts: use `media-api-contracts` before calling or modifying Runway, Creatomate, ElevenLabs, tmpfiles, or OpenAI media pipeline API code.

For fresh project orientation, use:

```text
NEW_SESSION_START_NOTE.md
```

That file points new sessions to the pipeline board, content pipeline, backlog structure, and the selected topic or episode.

## Local Skills In Use

The project currently has five local skills:

```text
.agents/skills/image-story-gate/SKILL.md
.agents/skills/media-api-contracts/SKILL.md
.agents/skills/openai-image-prompting/SKILL.md
.agents/skills/video-style-gate/SKILL.md
.agents/skills/visual-qa-validator/SKILL.md
```

### `image-story-gate`

Purpose:

- Applies to image-only educational stories, carousel cards, visual lessons, and contact-sheet reviews.
- Forces the agent to read `IMAGE_STORY_GATE.md`.
- Requires self-contained openers, native generated composition, no pasted-overlay look, integrated text, and visible mechanism evidence before image generation or acceptance.
- Requires running:

```powershell
python tools/verify_image_story_gate.py --changed
```

This skill is for workflow routing and judgment. It tells Codex when and how to apply the image-story gate.

### `media-api-contracts`

Purpose:

- Applies before calling, debugging, or modifying media pipeline APIs.
- Records the repo's known-good env var names, endpoint paths, headers, payload field names, manifest shapes, output files, and dry-run steps for Runway, Creatomate, ElevenLabs, tmpfiles, and OpenAI media tooling.
- Forces API work to start from `.env.example`, the consuming wrapper script, and the relevant provider reference instead of guessed parameters.
- Enforces the production media path: approved source frames, image-to-video clips, ElevenLabs voiceover, and Creatomate API assembly.
- Treats local still-image assembly as timing/debug only, not as a deliverable or comparison candidate.
- Requires running:

```powershell
python tools/verify_media_api_contracts.py
```

This skill is the productized memory for API lessons and failures.

### `openai-image-prompting`

Purpose:

- Applies when creating, revising, or productizing OpenAI GPT Image prompts for educational visuals.
- Defines the stable prompt shape, native educational card requirements, character consistency strategy, text reliability rules, and cost ladder.
- Explains how to convert accepted image-only cards into lower-text video-first source frames without losing the visible mechanism.

Use this with `image-story-gate` for image-only story cards.

### `video-style-gate`

Purpose:

- Applies before creating, editing, assembling, reviewing, or presenting How AI Uses Math video shorts, video-first frames, programmatic animation clips, or rendered lesson videos.
- Protects the currently approved lesson style reference. For Gradient Descent, the current preferred recovery direction is the native-story gold candidate unless the user explicitly selects a different reference.
- Blocks flat PPT/tutorial cards, standalone graph cards, generic caption panels, and programmatic animations that replace the accepted style.
- Requires production video shorts to use ElevenLabs voiceover, image-to-video clips, and Creatomate API assembly. Local still-image assembly is only a timing/debug preview.
- Requires actual contact-sheet/frame inspection and running:

```powershell
python tools/verify_video_style_gate.py --changed
```

For Gradient Descent, the current accepted style references are named in `.agents/skills/video-style-gate/SKILL.md`.

### `visual-qa-validator`

Purpose:

- Applies when reviewing generated visual assets, contact sheets, image-story cards, video-first source frames, rendered lesson frames, or candidate skill-base examples.
- Requires ChatGPT vision inspection of actual rendered images/contact sheets before making visual quality claims.
- Requires visual inspection against the intended renderer: image-only story, video-first source frame, style reference, lesson-core reference, or skill-base example.
- Produces evidence-backed verdicts such as `pass`, `pass-with-caveats`, `needs-revision`, `reject`, or `reference-only`.
- Treats `pass-with-caveats` as a blocking result, not a pass; caveats must be repaired and QA rerun before promotion.

This skill does not generate new visuals. It validates whether existing visuals are readable, coherent, and suitable for their intended next step. The verdict must come from ChatGPT vision inspection.

## Hook In Use

The project currently has one Codex hook config:

```text
.codex/hooks.json
```

It runs on the Codex `Stop` event:

```powershell
python tools/verify_agent_system.py
python tools/verify_image_story_gate.py --changed
python tools/verify_media_api_contracts.py
python tools/verify_video_style_gate.py --changed
python tools/verify_visual_qa_verdicts.py --changed
```

What it does:

- Checks that this overview mentions all local skills and that hooks run the expected gate scripts.
- Checks changed image-story prompt packs and review notes.
- Fails if required gate language is missing.
- Checks that media API contract references still match the local wrapper scripts.
- Checks changed video manifest/script/visual-QA files for accepted style reference requirements.
- Prevents a session from quietly accepting image-story work without the required opener/native-composition/review checks.
- Prevents a session from quietly presenting programmatic/video work without the required video style gate.
- Prevents changed QA/review notes from treating `pass-with-caveats` or unresolved caveats as a promotion signal.

What it does not do:

- It does not judge artwork quality by itself.
- It does not inspect pixels or generated images.
- It does not enforce every project rule.
- It only checks changed files that match the verifier patterns.

## Git Pre-Commit Hook

Git is configured with:

```text
.githooks/pre-commit
```

The pre-commit hook runs the same five checks:

```powershell
python tools/verify_agent_system.py
python tools/verify_image_story_gate.py --changed
python tools/verify_media_api_contracts.py
python tools/verify_video_style_gate.py --changed
python tools/verify_visual_qa_verdicts.py --changed
```

## Verifier Scripts

The hooks use:

```text
tools/verify_agent_system.py
tools/verify_image_story_gate.py
tools/verify_media_api_contracts.py
tools/verify_video_style_gate.py
tools/verify_visual_qa_verdicts.py
```

`tools/verify_agent_system.py` checks:

- every `.agents/skills/*/SKILL.md` is mentioned in this overview
- Codex Stop hooks include the agent-system, image-story, media-API, video-style, and visual verdict checks
- Git pre-commit includes the same checks
- `AGENTS.md` still contains the mandatory core sections
- `AGENTS.md` states that `pass-with-caveats` is not a pass

`tools/verify_media_api_contracts.py` checks:

- `.env.example` contains the expected local key names
- Runway wrapper still uses `RUNWAYML_API_SECRET`, `/image_to_video`, `promptImage`, `promptText`, and the version header
- Creatomate wrapper still submits `{"source": ...}` to `/v1/renders`
- ElevenLabs wrappers still use `ELEVENLABS_API_KEY`, `xi-api-key`, and expected voiceover fields
- tmpfiles wrapper still converts upload URLs to direct `/dl/` URLs
- this overview mentions the `media-api-contracts` skill and verifier

`tools/verify_image_story_gate.py` checks changed files such as:

- `assets/image-prompts/*image-story*.md`
- `assets/images/*image-story*/*review-notes.md`

It looks for required terms covering:

- self-contained opener
- native generated composition
- complete designed poster/card
- pasted-overlay failure check
- integrated text plan
- mobile readability
- review verdict

`tools/verify_video_style_gate.py` checks changed video manifest/script/QA files such as:

- `outputs/video-manifests/*.json`
- `outputs/video-scripts/*.md`
- `outputs/video-renders/verification/*.visual-qa.md`

It blocks programmatic/video candidates that lack an accepted style reference, a style-preserving animation role, or paired visual QA evidence. For pass verdicts on How AI Uses Math video QA notes, it requires an explicit accepted style/reference comparison and a statement that the style/reference contact sheet was inspected.

`tools/verify_visual_qa_verdicts.py` checks changed review/QA Markdown files for verdict discipline:

- `pass-with-caveats` is not allowed as a promotion status
- clean `pass` notes cannot contain unresolved caveat language
- caveated notes must become repairs, `needs-revision`, `reject`, or `reference-only`

## Planned Skills

Planned but not fully implemented skills are described in:

```text
CODED_SKILLS_PROPOSAL.md
```

The main proposed skills are:

- `create-ai-math-micro-lesson`: create a structured source lesson core for the math-in-AI series.
- `build-video-first-prompt-pack`: convert an approved lesson core into video-first image and Runway prompts.
- Video assembly/verification skill ideas for voiceover, manifests, renders, and motion checks.
- `visual-qa-validator` is implemented locally for ChatGPT vision review of contact sheets and rendered assets.

These are proposals unless a matching folder exists under `.agents/skills/`.

## Quick Mental Model

Use this model:

```text
AGENTS.md = mandatory repo rules
NEW_SESSION_START_NOTE.md = where a new session starts
.agents/skills/* = reusable workflow routing
.codex/hooks.json = automatic checks Codex runs
tools/verify_agent_system.py = stale-doc/hook wiring checker
tools/verify_image_story_gate.py = textual image-story gate checker, not visual QA
tools/verify_media_api_contracts.py = local media API contract checker, not a live API test
tools/verify_video_style_gate.py = textual video style gate checker, not visual QA
tools/verify_visual_qa_verdicts.py = textual verdict-discipline checker, not visual QA
CODED_SKILLS_PROPOSAL.md = future skill roadmap
OPENAI_VISUAL_PRODUCTIZATION_PLAN.md = API-backed generator/reviewer implementation handoff
```

Work style:

```text
first-time idea or uncertain workflow -> explore with Codex/ChatGPT capabilities
approved repeatable workflow -> productize as code, API script, skill, hook, template, or canonical doc
```

## Before Changing The Agent System

1. Update `AGENTS.md` only for hard mandatory rules.
2. Update `IMAGE_STORY_GATE.md` for image-story acceptance rules.
3. Update `.agents/skills/*/SKILL.md` when Codex should route a workflow automatically.
4. Update `.codex/hooks.json` only for automatic checks that should run without being remembered manually.
5. Keep this overview updated when skills or hooks are added, removed, or renamed.
6. Run `python tools/verify_agent_system.py` after changing skills, hooks, or this overview.
