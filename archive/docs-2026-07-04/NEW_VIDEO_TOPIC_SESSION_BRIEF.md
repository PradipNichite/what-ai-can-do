# New Video Topic Session Brief

Use this note when starting a fresh Codex session for one new educational video topic.

The goal is to let a new session create a video like the derivative and matrices lessons without re-explaining the pipeline.

## What To Tell The New Session

Paste this:

```text
We are creating a new bite-sized micro-lesson video for the project "What AI Can Do".

Read `NEW_VIDEO_TOPIC_SESSION_BRIEF.md` first.

If the topic belongs to the math-in-AI series, also read `HOW_AI_USES_MATH_SERIES_GUIDE.md`.
For math-in-AI batch planning, also read `HOW_AI_USES_MATH_SERIES_PLAN.md` and `HOW_AI_USES_MATH_IMAGE_PREREQUISITES.md`.

Use the derivative and matrices lessons as examples:
- Derivatives example: `outputs/video-scripts/derivatives-ai-learning-micro-lesson-v1.md`
- Matrices example: `modules/visual-ai-concepts/matrices-how-images-become-numbers.source.md`
- Matrices prompt pack: `assets/image-prompts/matrices-images-become-numbers-video-first.md`
- Matrices video manifest: `outputs/video-manifests/matrices-images-become-numbers-micro-lesson-v1.en.json`

Create the new topic using the same micro-lesson pipeline:
source module -> video-first prompt pack -> source frames -> Runway clips -> voiceover -> Creatomate render -> verification -> Markdown script version.
```

Then add the new topic idea in one sentence, for example:

```text
Topic: Vectors and how AI compares meaning.
```

For the math-in-AI series, also add the school concept and applied AI use:

```text
Topic: Functions: how AI turns input into output.
School concept: function as input -> rule -> output.
AI use: model input, numeric transformation, output scores.
```

## Core Product Direction

Default format:

- micro-lesson / bite-sized learning
- 35-75 seconds for first drafts
- optimized for understanding and retention, not flashy hooks
- teaching-first opening: state what the learner will understand, not a dramatic hook
- calm Indian-English educator voice
- sparse captions only for signposts and memory anchor

Avoid:

- generic hook-first Short unless explicitly requested
- attention-grabbing phrasing that sounds like social-media bait
- vague "AI magic" openings that do not teach the mechanism
- dense poster cards when the goal is video
- flat white diagram cards that do not match the established video style
- beautiful but generic images that do not teach the technical idea
- too many captions
- equal scene durations without checking voiceover timing
- stretching clips beyond their useful motion

## Math-In-AI Series Direction

For full guidance, read `HOW_AI_USES_MATH_SERIES_GUIDE.md`.
For sequence and batch planning, read `HOW_AI_USES_MATH_SERIES_PLAN.md`.
For image readiness, read `HOW_AI_USES_MATH_IMAGE_PREREQUISITES.md`.

For math topics, think of the series as:

```text
You already study this math in school. Here is how that same idea is used inside AI.
```

Target learner:

- 11th/12th standard or high-school students
- already familiar with the school concept
- curious about where the concept is applied
- needs technical accuracy without college-level overload

Do not frame these as hook-first Shorts. Frame them as small applied-math lessons.

Each math-in-AI topic should include:

- `school_concept`: the familiar math idea, such as vector, matrix, function, probability, graph, derivative
- `ai_use`: the AI behavior it helps explain, such as embeddings, image pixels, model outputs, uncertainty, recommendations, learning updates
- `mechanism`: what actually changes, gets compared, multiplied, scored, optimized, or transformed
- `mini_example`: one concrete, technically correct example with simple numbers or labels
- `visual_sequence`: the visible transformation/comparison that the learner can follow

Preferred opening:

```text
In this lesson, you will see how <school concept> is used in AI to <applied use>.
```

Avoid openings like:

```text
AI can do something amazing...
You won't believe how AI...
Here is the secret behind AI...
```

The first scene may create curiosity, but its job is to set the learning objective clearly.

## Default Visual Style

Before generating new source frames, inspect the current best visual references:

- `assets/images/matrices-images-become-numbers-video-first/`
- `assets/images/vectors-how-ai-compares-meaning-video-first-v2/`

New concept videos should match this established visual language unless the user explicitly asks for a different style:

- warm modern Indian educational illustration
- recurring Indian teenage student at a wooden study desk
- teal/green shirt, dark wavy hair, expressive curious face
- warm desk lamp, notebook, pen, books, small plant, cozy study-room background
- concept shown through tablet/phone overlays, icons, dots, arrows, grids, glow, and visual transformations
- minimal embedded text; voiceover explains the concept
- sparse captions only for signposts and memory anchors

Avoid using mostly flat diagrams on a plain white/cream background for the final video source frames. If a topic needs math visuals, place the diagram inside the consistent tablet/study environment, or use a warm classroom-style visual overlay. Preserve the established style first, then simplify the technical element.

## Technical Teaching Value Gate

Do not judge source frames only by whether they look good as images. A frame must also be useful as a video teaching moment.

Before generating images, define for each scene:

- `learning_job`: what technical idea this frame teaches
- `visual_evidence`: what the viewer can see that proves the idea
- `transformation`: what changes on screen, such as photo -> pixels -> numbers
- `motion_role`: what Runway should animate to guide attention
- `voiceover_dependency`: what the image leaves for narration to explain

Good technical visual sequence:

```text
photo -> pixel zoom -> brightness numbers -> matrix grid -> RGB layers -> AI scan
```

Weak technical visual sequence:

```text
student looking at tablet -> generic glowing icons -> generic cards -> recap
```

For abstract topics like vectors, make the mechanism visible:

```text
sentence/query -> vector number chips -> point in meaning space -> nearby cluster -> distance/angle comparison -> nearest result -> recommendation
```

Each source frame should answer: "If the video paused here, what technical step is the learner seeing?" If the answer is only "student looking at a nice UI," revise before Runway.

## First Files To Open

Open these before creating a new topic:

1. `LEARNING_VIDEO_FORMATS.md`
2. `VIDEO_FIRST_VISUAL_GUIDE.md`
3. `VIDEO_PROMPT_TEMPLATES.md`
4. `CONTENT_PIPELINE.md`
5. `SHORTS_CREATION_LEARNING_TIMELINE.md`

For math-in-AI topics, also open:

1. `HOW_AI_USES_MATH_SERIES_GUIDE.md`
2. `HOW_AI_USES_MATH_SERIES_PLAN.md`
3. `HOW_AI_USES_MATH_IMAGE_PREREQUISITES.md`

Then open the two examples:

1. `outputs/video-scripts/derivatives-ai-learning-micro-lesson-v1.md`
2. `modules/visual-ai-concepts/matrices-how-images-become-numbers.source.md`
3. `assets/image-prompts/matrices-images-become-numbers-video-first.md`
4. `outputs/video-scripts/derivatives-ai-learning-script-versions.md`

Also inspect the best source-frame references before image generation:

1. `assets/images/matrices-images-become-numbers-video-first/`
2. `assets/images/vectors-how-ai-compares-meaning-video-first-v2/`
3. `assets/image-prompts/vectors-how-ai-compares-meaning-video-first-v2.md`

## Reference Examples

### Derivatives Lesson

Use this as the example of evolving from short-form video into a micro-lesson:

- Script version: `outputs/video-scripts/derivatives-ai-learning-micro-lesson-v1.md`
- Manifest: `outputs/video-manifests/derivatives-ai-learning-micro-lesson-v1.en.json`
- Rendered video: `outputs/video-renders/derivatives-ai-learning-micro-lesson-v1-en.mp4`

Learning from derivatives:

- One continuous voiceover is better than disconnected scene voiceovers.
- Lesson signposts help: what you will learn, why it matters, concept, recap.
- Technical poster cards can feel static; video-first frames are better.
- Memory anchor: one sentence repeated clearly.

### Matrices Lesson

Use this as the cleaner video-first example:

- Source module: `modules/visual-ai-concepts/matrices-how-images-become-numbers.source.md`
- Prompt pack: `assets/image-prompts/matrices-images-become-numbers-video-first.md`
- Source frames: `assets/images/matrices-images-become-numbers-video-first/`
- Manifest: `outputs/video-manifests/matrices-images-become-numbers-micro-lesson-v1.en.json`
- Rendered video: `outputs/video-renders/matrices-images-become-numbers-micro-lesson-v1-en.mp4`

Learning from matrices:

- Start video-first, not poster-first.
- Use minimal embedded text.
- Put explanation in voiceover and sparse captions.
- Use visual transformations: photo -> pixels -> numbers -> matrix -> AI scan.
- Keep the warm student/tablet/study-desk style consistent across new concept lessons.
- Technical diagrams should appear as tablet overlays or classroom-style visual elements, not isolated flat poster cards.
- The images work because each one shows a concrete technical step, not only a nice student scene.

### Vectors Lesson

Use this as the example of correcting visual-style drift:

- v1 script: `outputs/video-scripts/vectors-how-ai-compares-meaning-micro-lesson-v1.md`
- v2 script: `outputs/video-scripts/vectors-how-ai-compares-meaning-micro-lesson-v2.md`
- v2 prompt pack: `assets/image-prompts/vectors-how-ai-compares-meaning-video-first-v2.md`
- v2 source frames: `assets/images/vectors-how-ai-compares-meaning-video-first-v2/`

Learning from vectors:

- v1 was rejected because it used flat diagram cards and did not match the earlier visual style.
- v2 corrected the direction by using the same warm student/tablet environment as matrices.
- v2 improved style, but still needs stronger technical visual content before final production.
- For abstract topics, show the concept as tablet overlays: icons, dots, arrows, clusters, and glows.
- Make the technical sequence explicit: text/query becomes vector numbers, vectors become points, points are compared by distance or angle, nearest points become search/recommendation results.
- Do not rely on readable labels to make the concept understandable.

## Required Output For Each New Video Topic

For a new topic, create or update these artifacts.

### 1. Source Module

Path:

```text
modules/visual-ai-concepts/<topic-slug>.source.md
```

Must include:

- status / pipeline stage metadata
- learning promise
- school concept and AI use for math-in-AI topics
- target learner
- why it matters
- core explanation
- memory anchor
- micro-lesson flow
- quick check

### 2. Video-First Prompt Pack

Path:

```text
assets/image-prompts/<topic-slug>-video-first.md
```

Must include:

- character / style bible
- 6-8 source image prompts
- matching Runway image-to-video prompt for each frame
- minimal embedded text
- clear motion target per frame
- explicit instruction to match the established matrices/vectors-v2 warm student/tablet visual style
- technical teaching value for each frame: learning job, visible evidence, transformation, and motion role

### 3. Source Frames

Path:

```text
assets/images/<topic-slug>-video-first/
```

Must include:

- numbered PNG frames
- source contact sheet
- quick review note explaining what technical step each frame teaches
- rough preview/animatic when possible, because still images alone are not enough to judge video teaching quality

### 4. Runway Clip Manifest

Path:

```text
outputs/video-manifests/<topic-slug>-runway-clips.json
```

Must include:

- image URLs
- motion prompts
- `ratio`: `720:1280`
- `model`: `gen4_turbo`
- `duration`: `5`

### 5. Final Video Manifest

Path:

```text
outputs/video-manifests/<topic-slug>-micro-lesson-v1.en.json
```

Must include:

- `learning_design`
- `voiceover.text`
- scene IDs and durations
- sparse captions only where useful

### 6. Markdown Script Version

Path:

```text
outputs/video-scripts/<topic-slug>-micro-lesson-v1.md
```

Must include:

- purpose
- linked manifest JSON
- linked voiceover MP3
- linked rendered video when available
- learning design fields
- full voiceover script
- scene timing table
- review notes

If multiple versions exist, also create:

```text
outputs/video-scripts/<topic-slug>-script-versions.md
```

### 7. Final Render And Verification

Required paths:

```text
outputs/video-renders/<topic-slug>-micro-lesson-v1-en.mp4
outputs/video-renders/verification/<topic-slug>-micro-lesson-v1-en.contact-sheet.jpg
outputs/video-renders/verification/<topic-slug>-micro-lesson-v1-en.motion-report.json
```

Also create a dense timestamp sheet when checking for pauses/blanks:

```text
outputs/video-renders/verification/<topic-slug>-micro-lesson-v1-en.dense-sheet.jpg
```

## Preferred Micro-Lesson Structure

Use 6-8 scenes:

1. Learning objective: school concept -> AI use
2. Familiar school version
3. Concrete AI example
4. Numeric or visual representation
5. Mechanism: transformation, comparison, scoring, or update
6. Where AI uses it
7. Memory anchor
8. Quick check or recap

## Voiceover Rules

- Use one continuous voiceover by default.
- Use Indian-English female voice unless asked otherwise.
- Preferred ElevenLabs voice ID:

```text
ADd2WEtjmwokqUr0Y5Ad
```

- Generate voiceover before final timing.
- Measure actual MP3 duration.
- Adjust scene durations to audio.
- Do not stretch low-motion clips too long.

## Verification Rules

Before final answer, run:

```powershell
python tools\verify_video_motion.py outputs\video-renders\<video>.mp4 --samples 12
```

Inspect:

- contact sheet
- black-border ratio
- motion score
- dense timestamp sheet if needed
- whether the video teaches a visible technical sequence, not only shows nice related imagery

Reject or revise when:

- there are true blank/black frames
- text/numbers are unreadable
- important content is cropped
- the video feels paused for too long
- captions fight with the source image
- the visuals do not make the core mechanism understandable
- a frame's only role is decorative atmosphere or a generic student reaction

## Services And Tools

Current working services:

- ElevenLabs for voiceover
- Runway image-to-video
- Creatomate final assembly

Current local scripts:

- `tools/generate_elevenlabs_voiceover.py`
- `tools/generate_runway_clips.py`
- `tools/render_creatomate_phase1.py`
- `tools/verify_video_motion.py`

Important implementation notes:

- Runway ratio used successfully: `720:1280`
- Runway model used successfully: `gen4_turbo`
- Creatomate final render uses manifest JSON.
- Temporary upload hosting has been `tmpfiles.org`; this is acceptable for prototypes but not final product storage.

## What The New Session Needs From The User

Only one thing is required:

```text
Topic: <new lesson topic>
```

Helpful but optional:

- target learner
- desired length
- language
- any must-use analogy
- whether to create video-first images or use existing assets

If the user gives only a topic, proceed with reasonable defaults.
