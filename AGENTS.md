# Project Agent Rules

These rules are mandatory for this repository.

## No-Guessing Preflight

Before doing visual, video, QA, hook, skill, pipeline, API, or environment-variable work, inspect the current repository state instead of relying on memory:

1. Read `AGENT_SYSTEM_OVERVIEW.md`.
2. Read the relevant local skill under `.agents/skills/`.
3. For API keys or environment variables, read `.env.example` and search the consuming script with `rg` before saying a key is missing or choosing a variable name.
4. If the overview conflicts with the filesystem, hooks, or current git status, trust the live repository state and update the overview as part of the work.
5. Do not present a visual/video artifact as a candidate, accepted, visual-QA, or publish-ready until the relevant gate has passed and the actual pixels/contact sheet/video frames were inspected.

QA is a kill-switch before presentation, not a checklist to justify work after it is already made.

A `pass-with-caveats` verdict is not a pass. Do not use it to promote an artifact, present a candidate, move a pipeline stage, start video generation, or mark anything accepted/publish-ready. Convert the caveats into fixes, repair the lesson/scene/visual, and rerun the relevant QA until the result is a clean `pass`, `needs-revision`, `reject`, or `reference-only`.

## Explore Then Productize

This project uses two modes together:

1. `Exploration mode`: use Codex and ChatGPT built-in capabilities freely to brainstorm, inspect, generate, compare, and learn what works.
2. `Product mode`: once a pattern, workflow, visual standard, prompt structure, QA rubric, or artifact shape is approved, convert it into reusable code, scripts, skills, hooks, templates, or documented pipeline steps.

Do not leave a repeated successful workflow as chat-only knowledge. Preserve it as a product asset.

Do not force every first attempt into code. First discover the shape of the work with Codex; then productize the parts that are valuable and repeatable.

## Documentation Hygiene

Before creating any new Markdown instruction, guide, session note, or process file:

1. Search existing docs with `rg` or `Get-ChildItem`.
2. Prefer updating the smallest existing canonical file.
3. Create a new Markdown file only when it has a distinct lifecycle, owner, or output artifact.
4. If a new file is created, link it from the relevant canonical file and state why it could not be merged.

Do not scatter process rules across many notes. Put hard rules in `AGENTS.md`, gates/checklists in the smallest relevant gate file, and long background material only where it is truly needed.

## Image-Only Educational Stories

Before creating or reviewing any image-only educational story, read `IMAGE_STORY_GATE.md`.

Do not generate story images until the prompt pack satisfies that gate.

Do not accept, reject, or classify visual quality from filenames, local scripts, metadata, or pixel statistics alone. Inspect the actual generated images/contact sheet with ChatGPT vision capability before making any visual QA verdict.

After creating or editing an image-story prompt pack or review note, run:

```powershell
python tools/verify_image_story_gate.py --changed
```

If the gate fails, do not call the image story accepted, complete, visual-draft, visual-qa, or publish-ready.

## Non-Negotiable Visual Standard

Image-only lesson cards must be self-contained native educational cards.

- The opener must identify the lesson, learning promise, school concept, AI use, and concrete example/task.
- Text must be generated as part of the image composition: tablet UI, notebook panels, poster typography, sticky notes, speech bubbles, arrows, labels, or callouts.
- Do not make a background image and paste a generic caption/headline block over it.

## Video Style Gate

Before creating, editing, assembling, reviewing, or presenting any How AI Uses Math video short, video-first frame set, or programmatic animation candidate, use the project `video-style-gate` skill and run:

```powershell
python tools/verify_video_style_gate.py --changed
```

Production video shorts must use ElevenLabs voiceover, image-to-video clips for motion, and Creatomate API assembly. Local still-image assembly is allowed only as a private timing/debug preview, not as a deliverable or comparison candidate.

Before calling a video a candidate, verify it is a complete lesson: opener, school concept, AI use, concrete example, mechanism chain, and memory anchor or quick check. Motion architecture cannot compensate for a missing lesson shape.

Lesson adequacy can be judged from the scene table, source images, contact sheets, or sampled frames before motion is polished. If a cold student could not explain what is shown, what changed, why it changed, and why the next scene follows, revise the lesson flow instead of improving render settings.

Animation must enhance a specific technical moment inside the currently approved visual reference for that lesson. It must not replace the lesson with flat tutorial/PPT cards, generic caption panels, or a newly invented style. Motion verification is not visual QA; inspect actual contact sheets or sampled frames before any pass/candidate claim.

## Media API Contracts

Before calling or modifying Runway, Creatomate, ElevenLabs, tmpfiles, or OpenAI media pipeline code, use the project `media-api-contracts` skill.

Do not guess API request fields or environment variable names. Use the existing wrapper scripts and provider reference files as the contract memory. After repeated API failures, update the relevant skill reference, wrapper, or verifier before ending the work.

Run:

```powershell
python tools/verify_media_api_contracts.py
```
