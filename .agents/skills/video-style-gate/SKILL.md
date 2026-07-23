---
name: video-style-gate
description: Use before creating, editing, assembling, or reviewing How AI Uses Math video shorts, video-first frames, programmatic animation clips, Remotion/Motion Canvas/Revideo/Manim experiments, or any rendered lesson video. Enforces the current approved lesson style reference, complete lesson intent, API production path, and visual QA before treating animation as a candidate.
---

# Video Style Gate

Use this before any video short work in this repository.

## Non-Negotiables

- Build a complete lesson first; animation is only an enhancement for a specific technical beat.
- Preserve the currently approved lesson style reference unless the user explicitly changes it.
- For production shorts, use ElevenLabs voiceover, image-to-video clips for motion, and Creatomate API assembly. Local still-image assembly is only a private timing/debug preview, not a deliverable.
- Use the preferred smooth Indian-English female ElevenLabs voice for prototypes unless the user explicitly changes it: `Zara - Soft and Serene Indian Voice`, voice ID `ADd2WEtjmwokqUr0Y5Ad`.
- Use one continuous voiceover by default. Separate per-scene clips are allowed only when timing demands it and audio stitching is verified.
- Do not render How AI Uses Math shorts as flat PPT/tutorial cards, standalone graph cards, generic caption panels, or white-background code animations.
- Do not call `verify_video_motion.py` a QA pass. It only checks motion and borders.
- Inspect actual contact sheets or rendered frames with vision before any `pass`, `pass-with-caveats`, candidate, comparison-ready, visual-qa, or publish-ready claim.
- Treat `pass-with-caveats` as a blocking result, not as a pass. Fix the caveats and rerun scene/visual QA before presenting a render as a candidate or moving to the next production step.

## Required Reading

Read the smallest relevant files before acting:

1. `VISUAL_QA_CHECKLIST.md`
2. `HOW_AI_USES_MATH_SERIES_GUIDE.md`
3. The source module for the lesson.
4. The accepted source-frame QA for that lesson, if it exists.

For Gradient Descent, the current recovery style source is the native-story gold candidate:

- `assets/images/gold-candidates/gradient-descent-scene-gated-full-v3/gradient-descent-scene-gated-full-v3-qa.md`
- `assets/images/gold-candidates/gradient-descent-scene-gated-full-v3/gradient-descent-scene-gated-full-v3-contact-sheet.jpg`
- Runway clips should be generated from this set or a QA-approved video-first derivative, then assembled with Creatomate.

The close-cropped Warm Minimal Tablet Closeup direction is rejected for this lesson unless the user explicitly re-approves it.

## Minimum Lesson Gate

A video is not a lesson candidate unless the script and visual sequence satisfy all of these before animation is judged:

- The opening names or clearly frames the lesson.
- The opening connects the school math concept to the AI use in plain language.
- The opening introduces the concrete example or task used by the rest of the video.
- The middle shows the mechanism chain, not just isolated facts or pretty motion.
- The ending gives a memory anchor, quick check, or recap that makes the lesson feel complete.
- The voiceover and visuals feel like one continuous explanation, not a set of unrelated shots.

If a render fails this gate, or only passes with caveats, mark it `reference-only`, `reject`, or `needs-revision`; do not call it comparison-ready just because the motion architecture works.

## Workflow

1. Start from the approved lesson/source-frame style, not from a new renderer.
2. Open the approved reference contact sheet and keep it visible in the review context before judging a new render.
3. Check the minimum lesson gate before classifying motion.
4. Classify motion only after the lesson flow exists.
5. Use programmatic animation only as a small technical insert or overlay that preserves the selected reference style.
6. For production, generate or reuse image-to-video clips, use ElevenLabs audio, and assemble through Creatomate.
7. Write or update a visual QA note from actual pixels, explicitly naming the style/reference contact sheet inspected and the minimum lesson gate verdict.
7. Run:

```powershell
python tools/verify_video_style_gate.py --changed
```

If the gate fails or returns caveats, fix the artifact or mark it `reject` / `needs-revision`. Do not present it as a candidate.

Do not ask the user to approve obvious continuation after a failure. If a render fails the style gate, reject it and continue toward the approved style path.

## Rejection Triggers

Mark `reject` when:

- the video looks like a PPT/tutorial slide deck while the accepted style is native educational story
- programmatic animation replaces the shot style
- a large caption panel carries the lesson instead of native tablet/notebook UI
- a motion report is used as proof of visual quality
- the contact sheet was not inspected visually
- the comparison candidate is assembled from static local images instead of image-to-video clips and Creatomate
- the voice is local TTS instead of ElevenLabs

## Proper Gradient Descent Direction

Use the native-story gold candidate or a QA-approved derivative. The small update frame should preserve the curve, labels, and old/new points while only the short update motion pulses or moves. Any code-controlled animation must preserve the native story composition, not render as a standalone flat graph.
