# Agent System Overview

This file explains the local Codex setup for this project: agent instructions, skills, hooks, and where to look before changing them.

## Agent Start Instructions

There is no `agent.start.md` file in this repository.

The active repo-level agent instruction file is:

```text
AGENTS.md
```

It currently contains three mandatory rule groups:

- Explore then productize: use Codex/ChatGPT built-in capabilities for first-time discovery, then turn approved repeatable workflows into product assets such as scripts, skills, hooks, templates, or pipeline docs.
- Documentation hygiene: search existing docs first, update the smallest canonical file, and avoid scattered process notes.
- Image-only educational stories: read `IMAGE_STORY_GATE.md` before creating or reviewing image-only stories, and run the verifier after editing image-story prompt packs or review notes.
- Non-negotiable visual standard: image-only lesson cards must be self-contained native educational cards, not background images with pasted caption blocks.

For fresh project orientation, use:

```text
NEW_SESSION_START_NOTE.md
```

That file points new sessions to the pipeline board, content pipeline, backlog structure, and the selected topic or episode.

## Local Skills In Use

The project currently has two local skills:

```text
.agents/skills/image-story-gate/SKILL.md
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

### `visual-qa-validator`

Purpose:

- Applies when reviewing generated visual assets, contact sheets, image-story cards, video-first source frames, rendered lesson frames, or candidate skill-base examples.
- Requires ChatGPT vision inspection of actual rendered images/contact sheets before making visual quality claims.
- Requires visual inspection against the intended renderer: image-only story, video-first source frame, style reference, lesson-core reference, or skill-base example.
- Produces evidence-backed verdicts such as `pass`, `pass-with-caveats`, `needs-revision`, `reject`, or `reference-only`.

This skill does not generate new visuals. It validates whether existing visuals are readable, coherent, and suitable for their intended next step. The verdict must come from ChatGPT vision inspection.

## Hook In Use

The project currently has one Codex hook config:

```text
.codex/hooks.json
```

It runs on the Codex `Stop` event:

```powershell
python tools/verify_image_story_gate.py --changed
```

What it does:

- Checks changed image-story prompt packs and review notes.
- Fails if required gate language is missing.
- Prevents a session from quietly accepting image-story work without the required opener/native-composition/review checks.

What it does not do:

- It does not judge artwork quality by itself.
- It does not inspect pixels or generated images.
- It does not enforce every project rule.
- It only checks changed image-story prompt/review Markdown files that match the verifier's patterns.

## Verifier Script

The hook uses:

```text
tools/verify_image_story_gate.py
```

The script checks changed files such as:

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
tools/verify_image_story_gate.py = textual image-story gate checker, not visual QA
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
