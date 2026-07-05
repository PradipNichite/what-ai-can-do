# Video-First Visual Guide

This guide defines how visual assets differ across formats.

The key rule:

> A story card should explain itself when paused. A video source frame should give the video model something clean to animate.

## 0. Default Series Visual Style

For new "What AI Can Do" concept micro-lessons, use the established warm Indian student/tablet style unless the user explicitly asks for a different visual direction.

Current best references:

- `assets/images/matrices-images-become-numbers-video-first/`
- `assets/images/vectors-how-ai-compares-meaning-video-first-v2/`

Default look:

- warm modern Indian educational illustration
- Indian teenage student at a wooden study desk
- teal/green shirt, dark wavy hair, expressive curious face
- warm desk lamp, notebook, pen, books, plant, cozy study-room background
- tablet or phone as the main concept surface
- abstract ideas shown as overlays: icons, dots, arrows, grids, clusters, glow, scan lines, transformations
- cinematic but calm educational composition

Avoid visual-style drift:

- Do not make mostly flat white/cream diagram cards for final video source frames.
- Do not switch to a new character, environment, or illustration style without a reason.
- Do not depend on tiny labels or dense text to explain the concept.
- For math-heavy topics, embed the diagram inside the tablet/study environment or use a warm visual overlay.

Use the contact sheet as a style gate. If the new frames do not look like they belong next to the matrices frames, revise before Runway generation.

Style consistency is necessary but not sufficient. The frames must also carry technical teaching value.

## 0.5 Technical Teaching Value

Do not approve frames only because they are beautiful or consistent with the series style. Educational video frames must show the mechanism of the concept.

For every scene, define:

| Field | Question |
|---|---|
| `learning_job` | What does this frame teach? |
| `visual_evidence` | What can the learner see that proves the idea? |
| `transformation` | What changes from before to after? |
| `motion_role` | What should move to guide attention? |
| `risk` | What might look nice but fail to explain? |

Good frame:

```text
Learning job: A sentence becomes a vector.
Visual evidence: phrase/input card visibly transforms into a row of number chips.
Transformation: text/icon input -> ordered numeric vector.
Motion role: pulse moves from input card into number chips.
```

Weak frame:

```text
Learning job: "AI understands meaning."
Visual evidence: student looking at a glowing tablet.
Transformation: none.
Motion role: generic glow.
```

For abstract AI/math concepts, use a visible technical sequence:

- vectors: text/query -> number chips -> meaning-space point -> nearby cluster -> distance/angle -> nearest result
- matrices: photo -> pixels -> brightness numbers -> rows/columns -> RGB layers -> AI scan
- derivatives: mistake/error -> curve -> slope at a point -> downhill direction -> small update
- probability: possible outcomes -> probability scores -> highest score -> uncertainty when scores are close
- functions: input numbers -> model/function -> transformed numbers -> output scores

If a frame cannot explain its technical step without decorative text, redesign the visual metaphor before generating Runway clips.

For math-in-AI lessons, avoid "attention hook" frames that only create surprise. The first frame should establish the school concept and the AI application clearly enough that the lesson direction is obvious.

## 1. Image-Only Story Cards

Image-only story cards are meant for WhatsApp Status, Instagram Stories, carousels, and static sharing.

They can include:

- headline text
- labels and arrows
- chat bubbles
- mini UI panels
- summary equations or formulas
- complete idea inside one frame

Good image-only card:

- one idea per card
- readable without audio
- enough text to understand the concept
- designed as a finished poster
- strong visual hierarchy

Risk when used for video:

- too much text can warp during image-to-video generation
- small labels become unreadable
- dense layouts limit camera movement
- Runway/Kling/Luma may animate the wrong thing
- text preservation fights against motion

## 2. Video Source Frames

Video source frames are not final posters. They are animation inputs.

They should include:

- one clear action
- fewer words
- larger character/action area
- clear foreground and background
- visible hands, phone, notebook, or UI element that can move
- enough safe margin for subtle camera movement
- minimal UI text

Good video source frame:

- works with voiceover
- shows behavior, not the full explanation
- gives the video model a motion target
- avoids tiny text and crowded labels
- preserves the main subject clearly
- shows a visible technical step, not only a mood or reaction

Video source frames should usually have only:

- 0-1 short headline, or
- 1-3 large words, or
- icon-only UI elements

For this project, prefer icon-only or very low-text tablet overlays when the concept is abstract. Let the voiceover explain terms like vector, matrix, derivative, embedding, and semantic search.

### 2.5 Two Approved Source-Frame Modes

Use one of these modes intentionally. Do not mix them inside a lesson unless the difference is part of a deliberate A/B experiment.

**Story-derived mode**

- Keeps the warm student/tablet environment from the image-only cards.
- Preserves the recurring character, desk, lamp, notebook, and visual continuity.
- Works best when the learner's context and emotional story carry part of the lesson.
- Risk: richer scenes can distract from the mechanism or give Runway too many moving targets.

**Clean mechanism-first mode**

- Uses a simpler educational diagram frame with one character or hand, one large technical surface, and very sparse text.
- Works best when the exact graph, vector, matrix, probability table, or transformation is the main learning object.
- Requires voiceover or captions because it is not a self-contained story card.
- Risk: can drift into generic textbook/PPT style if the prompt does not preserve a human learning context and the specific AI task.

When comparing these modes, run a small Runway smoke test on the hardest technical frame before producing a full lesson. Judge preservation of labels, mechanism clarity, motion control, and learning focus from sampled video frames.

Style experiment evidence and current observations are tracked in `VIDEO_STYLE_EXPERIMENT_LOG.md`.

## 3. Example Difference

Image-only card:

```text
Headline: "Give AI context"
Subtext: "Photo + question = better help"
Labels: Class, Topic, Doubt
Arrows from textbook to AI
```

Video source frame:

```text
Text: "Show the page"
Visual: student lifts phone above textbook
Motion target: phone moves, scan glow crosses page, AI icon reacts
Voiceover explains the context
```

## 4. Recommended Video Scene Types

Use compact micro-scenes:

| Scene Type | Visual Role | Motion Target |
|---|---|---|
| Learning Objective | show the school concept and AI use | notebook/tablet concept bridge |
| Problem Setup | show the situation or example | face reaction, phone/tablet glow |
| Demonstration | show the action | hand/phone movement |
| Context | show input quality | bubbles appear, UI pulse |
| Explanation | show simplification | step cards light up |
| Practice | show learner effort | pencil movement, hint card |
| Feedback | show correction | checkmark, correction bubble |
| Verification | show human/textbook check | nodes glow, teacher approval |

## 5. Scene Count

More scenes help only when they are smaller actions.

Bad:

```text
5 dense poster cards, each held for 5 seconds
```

Better:

```text
6-8 compact visual actions, each 3-5 seconds
```

Best for concept learning:

```text
6-8 compact technical transformations, each with one visible idea
```

Recommended educational short:

```text
1. Learning objective
2. Familiar school concept
3. Concrete AI example
4. Numeric/visual representation
5. Mechanism shown on screen
6. AI application
7. Recap or quick check
```

## 6. Character Consistency

Generated-image character consistency is fragile. Treat it as a production constraint.

Use a character bible:

- age and role
- ethnicity/context
- hairstyle
- clothing
- recurring colors
- personality/expression range
- recurring environment
- objects used in each scene

Repeat the character bible in every image prompt.

For this project, start from the default learner bible in `CHARACTER_CONSISTENCY_GUIDE.md` and adapt only when the story truly needs a different character.

For stronger consistency:

- use the same source/reference image when the image tool supports references
- generate first scene as the character anchor
- use image editing/reference-based generation for later frames when possible
- avoid changing camera angle too aggressively
- keep clothing and environment stable
- inspect contact sheets before video generation

## 7. Video Prompting Rules

Image-to-video prompts should focus on motion, not re-describing the whole image.

Good:

```text
Student lifts the phone slightly over the textbook. A soft scan light moves across the page. AI helper reacts with a small nod. Keep all text unchanged. No new text.
```

Bad:

```text
Create an Indian student studying with AI at home with a textbook and phone and explain how AI helps students learn better...
```

For text-heavy frames:

```text
Locked camera. Preserve all text exactly. Add only small character motion and gentle UI glow. No text morphing. No new text.
```

For action-heavy frames:

```text
Student writes in notebook. Pencil moves naturally. Hint card pops on phone. Subtle camera push-in. No new text.
```

## 8. Verification Gates

Before assembly, every generated video clip should be checked for:

- full-frame preservation
- no black frames
- no cropped important content
- text not warped
- character still recognizable
- motion is appropriate for the scene type
- no random extra text
- the clip still shows the intended technical step after animation
- the sequence of clips makes the mechanism easier to understand than the still contact sheet

Use:

```powershell
python tools\verify_video_motion.py path\to\clip.mp4 --samples 6
```

This command is only a diagnostic helper. Do not approve video visuals from motion scores or generated contact sheets alone. Inspect the sampled frames/contact sheet with ChatGPT vision capability before accepting the clip or sequence.

Reject or regenerate clips when:

- text is blanked or morphed
- face/character identity changes too much
- clip is almost static but scene requires action
- important content is cropped
- black-border ratio spikes unexpectedly
- the contact sheet no longer matches the established warm student/tablet visual style
- the clip is visually attractive but technically vague

## 9. Preview / Animatic Gate

Still images alone are not enough to judge whether a lesson will work as a video.

Before treating a frame set as ready, make one of these:

- a quick local animatic with the voiceover and simple pan/zoom
- a rough Runway test of the hardest technical frames
- a dense contact sheet from a preview render

Review the preview for teaching value:

- Does each scene add a new technical step?
- Does the viewer see a transformation, comparison, or mechanism?
- Are there too many generic reaction shots?
- Does the visual sequence work even with sparse captions?
- Is the core idea clearer after watching than after reading the script?

## 10. Product Pipeline Direction

A future product should separate these asset types:

```text
Lesson source
  -> image-only story cards
  -> video source frames
  -> voiceover script
  -> image-to-video clips
  -> final assembled short
```

Do not use one image asset for every output format by default.

Each renderer should have its own prompt strategy.
