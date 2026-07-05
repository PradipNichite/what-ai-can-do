# Project Agent Rules

These rules are mandatory for this repository.

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
