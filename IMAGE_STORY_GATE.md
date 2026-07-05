# Image Story Gate

This is the mandatory gate for image-only educational story cards.

## Why This Exists

Instruction files and long Markdown notes are not enough. Image stories in this project must be checked against a short, explicit gate before generation and again before acceptance.

## Required Before Image Generation

The prompt pack must explicitly include:

- `Self-contained opener`: card 1 names the lesson/topic, states what the learner will understand, connects the school concept to the AI use, and introduces the concrete example/task.
- `Native generated composition`: the image generator creates the full card, including text and diagram elements, as one designed educational image.
- `No pasted-overlay look`: text is not a generic caption/headline block over a study-desk or background scene.
- `Integrated text plan`: text appears through tablet UI, notebook panels, poster typography, sticky notes, speech bubbles, arrows, labels, callouts, or mini-cards.
- `Mechanism visibility`: each card shows the technical step visually, not only through explanatory text.

## Required Before Acceptance

Inspect the actual generated cards/contact sheet with ChatGPT vision capability. Do not use local scripts, pixel statistics, filenames, or prompt text as a substitute for visual inspection.

The review note must explicitly answer:

- Is the opener self-contained for a viewer who has not read project notes?
- Is the text natively integrated into the generated card design?
- Does any card look like pasted overlay text? If yes, it fails.
- Are the key mechanism labels readable on mobile?
- Is the recommendation/answer/decision explained by visible mechanism evidence, not decoration?

## Automatic Failure Patterns

Reject the set if any of these are true:

- Card 1 starts with an unexplained object, diagram, or transformation.
- The contact sheet feels like a random slideshow until project context is explained externally.
- Text looks like a generic poster overlay pasted onto a background image.
- The image would become an unrelated stock-style scene if the text were removed.
- The mechanism is carried mainly by glow, color, or vibes instead of visible structure.

## Required Language In Prompt Packs

Prompt packs should include language like:

```text
The card should feel like one complete designed educational poster, where illustration, diagram, and text are generated together, not a separate caption pasted on top.
```

```text
Text must be integrated through tablet UI, notebook panels, poster typography, sticky notes, arrows, labels, callouts, or mini-cards.
```

## Required Command

Run this after editing image-story prompt packs or review notes:

```powershell
python tools/verify_image_story_gate.py --changed
```
