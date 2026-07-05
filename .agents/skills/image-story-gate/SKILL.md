---
name: image-story-gate
description: Use for any image-only educational story, carousel, visual lesson, or contact-sheet review in this repository. Enforces self-contained lesson openers and native generated text composition before image generation and acceptance.
---

# Image Story Gate Skill

Use this skill before generating or reviewing any image-only educational story in this repository.

## Required Workflow

1. Read `IMAGE_STORY_GATE.md`.
2. Read the selected lesson/source module.
3. Before image generation, ensure the prompt pack explicitly includes:
   - self-contained opener
   - native generated composition
   - no pasted-overlay look
   - integrated text plan
   - mechanism visibility
4. Generate only after the prompt pack passes the gate.
5. Review the contact sheet against the same gate.
6. Run:

   ```powershell
   python tools/verify_image_story_gate.py --changed
   ```

7. If the checker fails, do not mark the story accepted or complete.

## Visual Standard

Cards must feel like complete generated educational posters. Text belongs inside the generated design through tablet UI, notebook panels, poster typography, sticky notes, speech bubbles, labels, arrows, callouts, or mini-cards.

Reject cards that look like a nice background with a generic caption or headline pasted on top.
