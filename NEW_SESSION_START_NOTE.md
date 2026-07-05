# New Session Start Note

Use this note when starting a fresh Codex session for this project.

## Latest Handoff: 2026-07-05

Recent session focus: OpenAI image generation pipeline, LangSmith tracing, image-only lesson quality, video-first source-frame style, and early Runway smoke testing.

Current visual direction:

- Keep rich self-contained story-card style for image-only lessons.
- Use **Warm Minimal Tablet Closeup** as the provisional default candidate for video-first math/AI source frames.
- Keep **Clean Mechanism First** as fallback for hard technical diagrams.
- Use **Notebook Tutor Sketch** and **Dark AI Dashboard** only as selective insert styles.
- Do not regenerate all existing lessons yet. First prove the new video-first style on full Gradient Descent and Statistics source-frame packs plus selected Runway clips.

Key evidence to open first:

```text
VIDEO_STYLE_EXPERIMENT_LOG.md
VIDEO_FIRST_VISUAL_GUIDE.md
assets/images/experiments/gradient-descent-frame4-style-grid-v1/gradient-descent-frame4-style-grid-v1-contact-sheet.jpg
assets/images/experiments/warm-minimal-tablet-keyframe-comparison-v1/current-vs-warm-keyframes-contact-sheet.jpg
assets/images/experiments/warm-minimal-tablet-keyframe-comparison-v1/warm-minimal-tablet-keyframe-comparison-v1-qa.md
outputs/runway-clips/gradient-descent-runway-style-ab-frame4-v1/
```

Important traces / request IDs:

- Gradient style-grid image generation LangSmith trace: `019f32e9-3f3a-7d70-bf84-07e07d82c71f`
- Gradient style-grid QA OpenAI request ID: `a20a330b-23c4-4daa-a919-01bdaf0204f8`
- Warm Minimal cross-lesson generation LangSmith trace: `019f3316-5c4a-7d83-81eb-a23699daa22e`
- Warm Minimal cross-lesson QA OpenAI request ID: `62aaaf4d-d89b-42f9-974f-3d82397e4de5`

Most useful next action:

1. Create a full Warm Minimal Tablet Closeup video-first prompt pack for **Gradient Descent**.
2. Generate all Gradient video source frames with OpenAI SDK, one LangSmith trace for the lesson.
3. Build contact sheet and run `tools/openai_visual_qa.py` in `video-first` mode.
4. If QA passes, send only the highest-risk frames to Runway first: gradient direction, small update, repeat/step-size.
5. After Gradient is proven, repeat for **Statistics**.

Known caveats:

- Vectors should not be fully regenerated until prompts add clearer distance/nearest-neighbor cues.
- Warm Minimal frames are video-first; they require voiceover/motion and are not replacements for image-only self-contained story cards.
- Existing richer image-only Gradient and Statistics candidates are still useful gold examples for static cards.

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
