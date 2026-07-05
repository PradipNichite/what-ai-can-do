# Existing Progress To Channel Reuse Plan

This document explains how to use the work already created in this project for the YouTube channel without restarting from scratch.

## Core Principle

Do not treat existing work as final channel content automatically.

Treat it as:

```text
concept research + lesson cores + prototype assets + renderer experiments
```

The next job is not to recreate everything. The next job is to consolidate, QA, and package the strongest existing work into the new channel pipeline.

## What Already Exists

The project already has major progress across the first "Class 9-12 Math Inside AI" playlist.

### Existing Concept Sources

Located in:

```text
modules/visual-ai-concepts/
```

Existing relevant concepts:

- `how-ai-uses-math-series-intro.source.md`
- `matrices-how-images-become-numbers.source.md`
- `vectors-how-ai-compares-meaning.source.md`
- `probability-how-ai-handles-uncertainty.source.md`
- `statistics-how-ai-learns-patterns-from-data.source.md`
- `functions-how-ai-turns-input-into-output.source.md`
- `linear-equations-how-ai-combines-signals.source.md`
- `derivatives-how-ai-learns-from-mistakes.source.md`
- `how-chatgpt-sees-images.md`

These should become the canonical lesson cores or be linked from the new `concepts/` layer.

### Existing Prompt Packs

Located in:

```text
assets/image-prompts/
```

Existing video-first prompt packs:

- `how-ai-uses-math-series-intro-video-first.md`
- `matrices-images-become-numbers-video-first.md`
- `vectors-how-ai-compares-meaning-video-first.md`
- `vectors-how-ai-compares-meaning-video-first-v2.md`
- `vectors-how-ai-compares-meaning-video-first-v3.md`
- `probability-how-ai-handles-uncertainty-video-first.md`
- `statistics-how-ai-learns-patterns-from-data-video-first.md`
- `functions-how-ai-turns-input-into-output-video-first.md`
- `linear-equations-how-ai-combines-signals-video-first.md`

Existing image-story style prompt packs:

- `derivatives-ai-learning-story.md`
- `student-ai-study-story.md`
- `customer-support-mobile-story.md`

These show the important distinction between video-first frames and image-only share cards.

### Existing Generated Image Folders

Located in:

```text
assets/images/
```

Relevant first-playlist image folders include:

- `how-ai-uses-math-series-intro-video-first/`
- `matrices-images-become-numbers-video-first/`
- `matrices-how-ai-sees-images-as-numbers-style-b-refresh/`
- `vectors-how-ai-compares-meaning-video-first/`
- `vectors-how-ai-compares-meaning-video-first-v2/`
- `vectors-how-ai-compares-meaning-video-first-v3/`
- `vectors-how-ai-compares-meaning-style-b-refresh/`
- `probability-how-ai-handles-uncertainty-video-first/`
- `probability-how-ai-handles-uncertainty-style-b-refresh/`
- `statistics-how-ai-learns-patterns-from-data-video-first/`
- `functions-how-ai-turns-input-into-output-video-first/`
- `linear-equations-how-ai-combines-signals-video-first/`
- `derivatives-how-ai-knows-which-way-to-improve-style-b-refresh/`
- `derivatives-ai-learning-native-story/`

These are not all equally ready. Some are prototypes, some are refreshed style tests, some are video-first source frames.

### Existing Motion / Video Work

Located in:

```text
outputs/runway-clips/
outputs/video-manifests/
outputs/video-scripts/
outputs/video-renders/
```

Notable progress:

- Matrices has Runway clips, manifest, script/render assets, and a rendered MP4.
- Derivatives has multiple rendered MP4 versions and script versions.
- Vectors has multiple script versions, image prompts, manifests, and Runway clip folders.
- Student AI Study has many renderer experiments that are useful as pipeline learning, but it is not part of the first math playlist.

## How To Reuse Existing Work

Use existing work in four ways:

1. **Lesson core reuse**
   - Keep the source modules as canonical concept explanations.
   - Do not rewrite them unless the concept is wrong or unclear.

2. **Prompt reuse**
   - Reuse strong prompt packs as starting points.
   - Mark old prompts as `prototype`, `video-first`, or `image-story`.
   - Do not send old image-story cards directly to image-to-video unless they pass the video-first QA rules.

3. **Asset reuse**
   - Reuse generated frames only if they match the current channel style, are mobile-readable, and fit the intended renderer.
   - Some frames should be used as reference rather than final assets.

4. **Pipeline learning reuse**
   - Keep lessons learned from Student AI Study, Derivatives, and Matrices about motion, voiceover timing, and text-heavy frames.
   - These experiments reduce future waste.

## Register Existing Work Into `concepts/`

Create a concept folder for each first-playlist topic.

Recommended first batch:

```text
concepts/
  class-9-12-math-inside-ai/
    001-why-ai-needs-class-9-12-math/
    002-images-become-matrices/
    003-meaning-becomes-vectors/
    004-ai-gives-scores-not-certainty/
    005-data-becomes-patterns/
    006-a-model-is-a-function/
    007-signals-combine-into-a-score/
    008-slope-tells-ai-how-to-improve/
    009-distance-helps-ai-compare-things/
    010-connections-become-recommendations/
```

For each concept, create:

```text
concept.md
renderer-plan.md
file-map.md
status.md
```

The concept folders should point to existing files instead of copying everything.

## Current Concept Reuse Map

| Concept | Existing source | Existing prompts/images | Existing motion/render | Reuse action |
|---|---|---|---|---|
| Why AI Needs Class 9-12 Math | yes | yes | partial/unknown | QA intro frames and create Short metadata |
| Images Become Matrices | yes | yes | yes, rendered MP4 exists | Review final render, decide refresh vs publish candidate |
| Meaning Becomes Vectors | yes | yes, multiple versions | yes, Runway/scripts exist | Choose best version, avoid version confusion |
| AI Gives Scores, Not Certainty | yes | yes | no clear final render | Image QA, then motion generation if approved |
| Data Becomes Patterns | yes | yes | no clear final render | Image QA, then decide Short vs image-story |
| A Model Is A Function | yes | yes | no clear final render | QA contact sheet, create motion prompts |
| Signals Combine Into A Score | yes | yes | no clear final render | QA generated frames, then motion |
| Slope Tells AI How To Improve | yes | multiple versions | yes, rendered MP4 exists | Treat old render as prototype; use refresh notes |
| Distance Helps AI Compare Things | partly covered in Vectors | partly in Vectors | partly in Vectors | Decide if separate Short or inside vectors |
| Connections Become Recommendations | likely missing | likely missing | missing | Create new concept core |

## What Not To Do

Do not:

- rename or move all existing media immediately
- regenerate all images just because the structure changed
- treat every existing rendered MP4 as publish-ready
- mix video-first frames and image-only cards without labeling them
- create image-to-video clips before image QA
- lose older versions without noting why they were superseded

## Classification Needed

Each existing asset set should be labeled as one of:

```text
final-candidate
prototype-reference
needs-refresh
image-story-only
video-first-source
deprecated
```

Examples:

- `matrices-images-become-numbers-video-first/`: likely `final-candidate` or `needs-light-QA`
- `derivatives-ai-learning-native-story/`: `prototype-reference` / `image-story-like`
- `derivatives-how-ai-knows-which-way-to-improve-style-b-refresh/`: likely `refresh-candidate`
- `vectors-how-ai-compares-meaning-video-first-v3/`: likely strongest current vector candidate
- `student-ai-study-*`: `pipeline-reference`, not first playlist

## Recommended Next Steps

### Step 1: Create The Concept Registry

Create `concepts/class-9-12-math-inside-ai/` with 10 concept folders.

For each concept, add `file-map.md` that links existing source, prompts, images, manifests, scripts, and renders.

This makes existing progress visible.

### Step 2: Make A Launch Readiness Board

Create one board that tracks:

```text
concept
renderer
source core
scene plan
image prompt
image QA
motion QA
voiceover
assembly
final QA
publish status
```

This board should decide whether the first month is launch-safe.

### Step 3: Audit Existing Assets Before Spending More

For each of the first 8 concepts:

- open the contact sheet
- inspect mobile readability
- check technical accuracy
- check current visual style consistency
- decide: use, refresh, or park

### Step 4: Convert Strong Concepts Into Renderer Plans

For each concept, decide which renderers matter now:

- YouTube Short: P0
- Image-only share story: P1
- YouTube Community post: P1
- Long-form video: P2
- Article: P3

Do not create all renderers for every concept immediately.

### Step 5: Build The First Launch Batch

The first launch batch should probably use the strongest existing work:

1. Intro / Why AI Needs Class 9-12 Math
2. Matrices
3. Vectors
4. Probability
5. Functions
6. Statistics
7. Linear Equations
8. Derivatives refresh or prototype

Then create or finish:

9. Distance / Similarity
10. Graphs / Recommendations

## Practical Recommendation

Use the next working session to create the `concepts/` registry and file maps.

Do not generate any new images or videos until:

```text
existing assets are registered
best versions are chosen
launch gaps are visible
```

This will save money because we will know which concepts truly need new assets and which can be reused or lightly refreshed.

## Bottom Line

The existing work is not wasted. It is the foundation.

But it needs to be converted from:

```text
scattered production artifacts
```

into:

```text
a launch-ready concept and renderer pipeline
```

That is the bridge between the project so far and a sustainable YouTube channel.
