---
name: visual-qa-validator
description: Use when reviewing generated visual assets, image-story cards, contact sheets, video-first source frames, rendered lesson frames, or candidate base examples in this repository. Requires ChatGPT vision inspection of actual rendered images or sampled video frames, applies project gates, and writes evidence-backed QA verdicts before assets are accepted, used as skill bases, moved to visual-draft/visual-qa/publish-ready, or sent to video generation.
---

# Visual QA Validator

Use this skill to validate visuals with ChatGPT vision capability. Do not generate new assets in this workflow.

Do not make visual QA verdicts from local scripts, metadata, filenames, prompt text, or pixel statistics. The actual rendered image, contact sheet, or sampled video frames must be inspected visually by ChatGPT before any `pass`, `reject`, `accepted`, `visual-draft`, `visual-qa`, `publish-ready`, or `skill base` claim.

## Required Inputs

Identify at least one:

- image folder under `assets/images/`
- contact sheet path
- prompt pack under `assets/image-prompts/`
- review note path
- source module under `modules/visual-ai-concepts/`
- candidate example for skill creation

## Workflow

1. Read the relevant project gates:
   - For image-only stories: `IMAGE_STORY_GATE.md`
   - For visual renderer QA: `VISUAL_QA_CHECKLIST.md`
   - For math-in-AI lessons: `HOW_AI_USES_MATH_SERIES_GUIDE.md`
   - For video-first frames: `VIDEO_FIRST_VISUAL_GUIDE.md`
   - For skill-base example selection: `SKILL_BASE_EXAMPLE_VALIDATION.md`
2. Open the contact sheet, image files, or sampled video frames with ChatGPT vision capability.
3. Inspect the actual rendered pixels. This is the real QA step.
4. Compare the result against the intended renderer:
   - image-only card/story
   - video-first source frame
   - style reference
   - lesson-core/source reference
   - skill-base example
5. Compare the result against the accepted style/reference contact sheet when one exists. For How AI Uses Math videos, this is mandatory before any pass verdict.
6. Write a concise QA note with evidence, caveats, and verdict.
7. Treat caveats as blocking repair work. A `pass-with-caveats` verdict is not a pass and does not authorize promotion, candidate presentation, video generation, or publish-ready movement.
8. Run required repository verifier commands when applicable.

## Visual Inspection Criteria

Use ChatGPT vision to inspect the actual pixels of the rendered image/contact sheet. Then answer:

For every visual set, answer:

- Does the first frame/card orient a new viewer?
- Is the technical mechanism visible, not only implied by captions?
- Is text readable at mobile size?
- Does the text look native to the image composition?
- Is any important text pasted over a background as a generic overlay?
- Does the sequence progress logically?
- Are style, character, lighting, and environment consistent enough for the renderer?
- Are labels/numbers accurate enough for the teaching goal?
- Does the artifact work without external project notes?
- Does it preserve the approved visual language for the lesson or series?
- Would a side-by-side view with the accepted reference make this look like the same series?
- Is any "animation" replacing the visual style instead of enhancing a specific technical moment?

For video-first frames, also answer:

- Is each frame motion-friendly?
- Is there one clear motion target?
- Is text sparse enough to survive image-to-video?
- Would the voiceover carry the explanation without the frame becoming vague?

For image-only stories, also answer all acceptance questions in `IMAGE_STORY_GATE.md`.

## Verdict Labels

Use one of these verdicts:

- `pass`: ready for the intended next step, with no unresolved caveats.
- `pass-with-caveats`: blocked; record the caveats as explicit fixes, address them, then rerun QA. Do not treat it as a pass.
- `needs-revision`: useful direction, but not acceptable yet.
- `reject`: should not be used as a final asset or skill base.
- `reference-only`: useful only for style, mechanism, opener, or failure calibration.

Never call an asset `accepted`, `visual-draft`, `visual-qa`, `publish-ready`, candidate, comparison-ready, or a `skill base` unless the verdict is a clean `pass` for that exact use. `pass-with-caveats` must be converted into `needs-revision`, `reject`, or a clean `pass` after the caveats are fixed and QA is rerun.

For How AI Uses Math video shorts, mark `reject` when a render is technically correct but visually changes the approved style into PPT cards, flat diagram cards, generic tutorial panels, or standalone programmatic animation.

## QA Note Shape

Use this structure:

```md
# <Asset Name> Visual QA

Status: <pass | pass-with-caveats | needs-revision | reject | reference-only>
Intended use: <image-only story | video-first frames | style reference | skill-base example | ...>

## Inputs

- Source:
- Prompt pack:
- Image folder:
- Contact sheet:

## Pixel Health

- Files/images opened with ChatGPT vision:
- Contact sheet inspected:
- Style/reference contact sheet inspected:
- Any obvious blank/corrupt/missing frame seen by vision:
- Caveats:

## Visual Review

- Opener:
- Native composition:
- Mechanism visibility:
- Text readability:
- Sequence:
- Style consistency:

## Verdict

<Clear decision and what may/may not be done next.>
```

## Required Commands

After editing image-story prompt packs or review notes, run this textual gate checker in addition to ChatGPT vision review:

```powershell
python tools/verify_image_story_gate.py --changed
```

If video clips are reviewed, run the video verifier when clips exist. This is not a substitute for visually inspecting sampled frames or preview contact sheets:

```powershell
python tools/verify_video_motion.py <clip-or-folder>
```
