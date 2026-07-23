# New Session Start Note

Use this note when starting a fresh Codex session for this project.

## Latest Handoff: 2026-07-06

Recent session focus: Gradient Descent hybrid video experiment using Runway image-to-video clips, one programmatic technical insert, ElevenLabs Zara voice, and Creatomate assembly.

Critical outcome:

- The current Gradient Descent hybrid videos are failure calibration, not lesson candidates.
- The latest v2 render still feels like disconnected slides and does not reliably teach a student what gradient descent is doing.
- Do not continue by polishing motion, voice, or render settings.
- The lesson flow has now been repaired into a 12-beat gold-standard hybrid source draft and passed structured scene adequacy.
- The next action is to create the gold-standard source-frame/prompt pack from the passed 12-beat flow before generating images, clips, or renders.

Open these first:

```text
assets/reviews/gradient-descent-scene-adequacy.md
assets/reviews/gradient-descent-gold-standard-scene-adequacy.md
outputs/video-scripts/gradient-descent-gold-standard-hybrid-v1.md
outputs/video-scripts/gradient-descent-script-versions.md
outputs/video-renders/verification/gradient-descent-complete-lesson-hybrid-creatomate-v2.visual-qa.md
outputs/video-scripts/gradient-descent-complete-lesson-hybrid-creatomate-v2.md
modules/visual-ai-concepts/gradient-descent-how-ai-learns-from-mistakes.source.md
HOW_AI_USES_MATH_IMAGE_PREREQUISITES.md
tools/media_pipeline/prompts/openai_scene_adequacy.md
```

Next action:

1. Treat the previous scene adequacy `pass-with-caveats` as a false pass for video comprehension.
2. Use the repaired 12-beat source and gold-standard hybrid blueprint as the active draft:
   - W1 current setting
   - prediction
   - loss
   - point on loss curve
   - gradient/uphill direction
   - opposite update
   - W2
   - lower loss
   - repeat decision
3. Use the clean scene adequacy pass to write prompts/source-frame requirements so a cold student can explain, after each scene:
   - what object is being shown
   - what changed
   - why the next scene follows
   - how this connects slope from school graphs to AI training
4. Create new source frames or prompt packs from the passed flow. Do not reuse caveated frames as candidates.

Hard stop:

- Do not generate images, Runway clips, voiceover, or Creatomate renders until the scene adequacy review explicitly passes the cold-student comprehension test.
- Do not treat native-story style, animation, or smooth voice as a substitute for explanation.
- If the lesson still reads as a sequence of slides, mark it `reject` even if the pipeline is technically correct.
- Do not treat `pass-with-caveats` as a pass. Fix the caveats, rerun the relevant scene/visual QA, or mark the artifact `needs-revision`, `reject`, or `reference-only`.
- Judge lesson adequacy from the scenes and source images themselves, not only from motion. If the images cannot teach the lesson sequence, repair the lesson before making more render variants.
- Legacy files and folders with names like `gold-candidates` are not automatically trusted if their QA note says `pass-with-caveats`. Use them as reference or failure calibration only until a clean visual QA pass exists.

## Latest Handoff: 2026-07-05

Recent session focus: full Warm Minimal Tablet Closeup Gradient Descent source-frame pass, OpenAI visual QA, targeted frame repair, and selected Runway smoke testing.

Current visual direction:

- Keep rich self-contained story-card style for image-only lessons.
- Use **Warm Minimal Tablet Closeup** as the provisional default candidate for video-first math/AI source frames.
- Keep **Clean Mechanism First** as fallback for hard technical diagrams.
- Use **Notebook Tutor Sketch** and **Dark AI Dashboard** only as selective insert styles.
- Do not regenerate all existing lessons yet. Gradient Descent now proves the Warm Minimal direction well enough for video-first production with caveats; next prove it on Statistics before promoting it to a stronger series rule.

Key evidence to open first:

```text
VIDEO_STYLE_EXPERIMENT_LOG.md
VIDEO_FIRST_VISUAL_GUIDE.md
assets/images/experiments/gradient-descent-frame4-style-grid-v1/gradient-descent-frame4-style-grid-v1-contact-sheet.jpg
assets/images/experiments/warm-minimal-tablet-keyframe-comparison-v1/current-vs-warm-keyframes-contact-sheet.jpg
assets/images/experiments/warm-minimal-tablet-keyframe-comparison-v1/warm-minimal-tablet-keyframe-comparison-v1-qa.md
outputs/runway-clips/gradient-descent-runway-style-ab-frame4-v1/
assets/image-prompts/gradient-descent-how-ai-learns-from-mistakes-video-first.md
assets/images/gradient-descent-how-ai-learns-from-mistakes-video-first-warm-minimal-v1/gradient-descent-warm-minimal-source-contact-sheet.jpg
assets/images/gradient-descent-how-ai-learns-from-mistakes-video-first-warm-minimal-v1/gradient-descent-warm-minimal-source-frame-review-notes.md
outputs/video-manifests/gradient-descent-warm-minimal-runway-smoke-v1.json
outputs/runway-clips/gradient-descent-warm-minimal-runway-smoke-v1/gradient-descent-warm-minimal-runway-smoke-v1-qa.md
```

Important traces / request IDs:

- Gradient style-grid image generation LangSmith trace: `019f32e9-3f3a-7d70-bf84-07e07d82c71f`
- Gradient style-grid QA OpenAI request ID: `a20a330b-23c4-4daa-a919-01bdaf0204f8`
- Warm Minimal cross-lesson generation LangSmith trace: `019f3316-5c4a-7d83-81eb-a23699daa22e`
- Warm Minimal cross-lesson QA OpenAI request ID: `62aaaf4d-d89b-42f9-974f-3d82397e4de5`
- Full Gradient Warm Minimal source-frame generation LangSmith trace: `019f3336-8a7d-7523-8684-4d7e8e60424f`
- Gradient targeted frames 5-6 repair LangSmith trace: `019f333b-ce2d-74f0-a0ef-8086b81aa445`
- Final Gradient Warm Minimal source-frame QA OpenAI request ID: `5111c65a-8262-43f5-aa0a-511f4efb038a`

Most useful next action:

1. Create/update the full Warm Minimal Tablet Closeup video-first prompt pack for **Statistics**.
2. Generate all Statistics video source frames with OpenAI SDK, one LangSmith trace for the lesson.
3. Build contact sheet and run `tools/openai_visual_qa.py` in `video-first` mode.
4. If QA passes, send only the highest-risk Statistics frames to Runway first.
5. For future Gradient assembly, use the accepted source frames and the locked-arrow Runway prompt pattern for frame 5.

Known caveats:

- Vectors should not be fully regenerated until prompts add clearer distance/nearest-neighbor cues.
- Warm Minimal frames are video-first; they require voiceover/motion and are not replacements for image-only self-contained story cards.
- Existing richer image-only Gradient and Statistics candidates are still useful gold examples for static cards.
- In Runway, do not ask a graph point to travel along the curve unless the motion must be broad; for small updates, keep points fixed and pulse the short arrow.

## Project Goal

This is not a single article or one-off image project. Treat it as a multi-format content production pipeline.

The goal is to take educational/career/AI-awareness ideas through stages until they become publishable visual knowledge assets: 9:16 mobile stories, Marathi versions, videos, PDFs, interactive demos, or other native formats.

## First Files To Open

1. `PIPELINE_BOARD.md`
2. `CONTENT_PIPELINE.md`
3. `BACKLOG_STRUCTURE.md`
4. The selected topic or episode doc under `backlog/topics/` or `backlog/ideas/`

For math-in-AI series work, open:

```text
HOW_AI_USES_MATH_SERIES_GUIDE.md
HOW_AI_USES_MATH_SERIES_PLAN.md
HOW_AI_USES_MATH_IMAGE_PREREQUISITES.md
VIDEO_FIRST_VISUAL_GUIDE.md
```

Use specific `NEXT_SESSION_*` notes only if they are intentionally restored from the archive for a short handoff.

## Operating Model

Ideas can be at different stages at the same time.

Do not treat the backlog as a flat list. There are two levels:

- Umbrella Topic: broad map that can itself become a post/story.
- Granular Episode: focused concept, workflow, example, or career story.

Both levels can become publishable assets.

## Pipeline Stages

Use the stage definitions in `CONTENT_PIPELINE.md`.

Common stages:

- `00 Captured`
- `01 Framed`
- `02 Scene Flow`
- `03 Source Draft`
- `04 Prompt Pack`
- `05 Visual Draft`
- `06 Visual QA`
- `07 Localized`
- `08 Video / Interactive`
- `09 Publish Ready`

## How To Start A New Work Session

1. Open `PIPELINE_BOARD.md`.
2. Pick one item from the board.
3. Open its topic/episode doc.
4. Confirm:
   - current stage
   - next action
   - primary format
   - parent topic
5. Move only that item forward by one clear stage.
6. Preserve all prompts, assets, QA notes, and next action before stopping.

## If The User Says "Pick One"

Good default options:

1. `Derivatives: How AI Learns From Mistakes`
   - Current stage: `06 Visual QA`
   - Best next action: review math-glimpse card and create Marathi version.

2. `Student AI Learning`
   - Current stage: `02 Scene Flow`
   - Best next action: turn the umbrella topic into a 9:16 carousel/post.

3. `Careers That Did Not Look Serious 10 Years Ago`
   - Current stage: `02 Scene Flow`
   - Best next action: create prompt pack for visual story.

4. `Biology But Not Doctor`
   - Current stage: `01 Framed`
   - Best next action: create a relatable 9:16 scene flow.

## Content Style Reminder

The user does not want blog-style explanation converted into images.

Preferred style:

- visual-first
- scene-by-scene
- mobile-native
- short captions
- strong narrative progression
- native to each format
- enough technical truth where relevant

For Marathi, write natural spoken Marathi with familiar English technical words preserved when people actually use them.

## Visual Workflow Reminder

Before generating or reviewing image-only educational story cards, open `IMAGE_STORY_GATE.md`.

Default workflow:

1. Start with image-only/self-contained story cards unless the user explicitly asks to skip them.
2. Store prompts in `assets/image-prompts/`.
3. Generate image-only story assets and a contact sheet.
4. Review the actual contact sheet with ChatGPT vision against `IMAGE_STORY_GATE.md` and `VISUAL_QA_CHECKLIST.md`.
5. Only after the image-only concept works, derive video-first source frames with less text and clearer motion targets.
6. For Marathi/Devanagari, verify joined letters and rendering carefully.
7. Record QA notes in the relevant asset folder or `research/notes/`.

## Image-Only First Rule

For new educational concepts, especially the `How AI Uses Math` series, the first visual format must be an image-only/self-contained visual story. Video-first frames are useful for animation, but they are too sparse to prove whether the concept is powerful. The image-only story is the concept test.

Use this order:

```text
lesson core -> image-only prompt pack -> image-only cards/contact sheet -> visual QA -> video-first prompt pack -> video source frames -> image-to-video
```

## Before Ending A Session

Always update:

- `PIPELINE_BOARD.md`
- selected topic/episode doc
- prompt archive if prompts were created
- QA note if visuals were reviewed
- `PROJECT_STATUS.md` if direction or next steps changed

Then commit only the relevant files. Do not include unrelated untracked video-pipeline files unless the user explicitly asks.
