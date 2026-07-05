# Channel Folder Structure And Asset System

This document defines how to organize the YouTube channel pipeline without breaking the existing project structure.

Important update:

The YouTube channel should not become the master structure for all content. The master creative unit should be a concept/story with multiple renderers. See `MULTI_RENDERER_CONTENT_STRUCTURE.md` for the fuller model.

## Current Project Pattern

The project already has a useful production structure:

```text
modules/visual-ai-concepts/
assets/image-prompts/
assets/images/
outputs/video-manifests/
outputs/video-scripts/
outputs/runway-clips/
tools/
research/youtube-channel/
```

Existing examples:

- source module: `modules/visual-ai-concepts/matrices-how-images-become-numbers.source.md`
- prompt pack: `assets/image-prompts/matrices-images-become-numbers-video-first.md`
- generated frames: `assets/images/matrices-images-become-numbers-video-first/`
- Runway clips: `outputs/runway-clips/matrices-images-become-numbers-runway-clips/`
- manifests: `outputs/video-manifests/matrices-images-become-numbers-*.json`
- scripts: `outputs/video-scripts/matrices-images-become-numbers-*.md`

This pattern is good because tools can easily find assets by type.

## Problem To Solve

For a YouTube channel pipeline, asset-type folders are not enough.

We also need to answer quickly:

- What playlist is this video part of?
- What is the current stage?
- Which videos are launch-ready?
- Which videos are waiting for scene plans?
- Which videos already have approved images?
- Which prompts created the final assets?
- Which files belong to this one video?
- What should be worked on next?

So we should not replace the current structure. We should add a channel control layer.

## Recommended Model

Use a hybrid structure:

```text
Existing folders = production asset storage
New concepts folder = one concept, many renderers, status, and file maps
New channel folder = YouTube playlist, packaging, and publishing schedule
```

Do not duplicate large media files unless there is a strong reason.

Instead, the channel video folder should contain:

- learning core
- scene plan
- QA notes
- metadata
- links to source assets
- status
- next action
- final selected asset references

## Recommended New Folder

Create:

```text
concepts/
```

for cross-platform concept management.

Also create:

```text
channel/
```

Inside it:

```text
channel/
  README.md
  channel-board.md
  brand/
  playlists/
  videos/
  templates/
```

Purpose:

```text
concepts/ is the operating layer for concept production.
channel/ is the operating layer for YouTube publishing.
```

Neither should replace `modules/`, `assets/`, or `outputs/`.

## Full Recommended Structure

```text
channel/
  README.md
  channel-board.md
  brand/
    channel-name-description.md
    watermark-guide.md
    visual-style.md
    upload-defaults.md
  playlists/
    01-class-9-12-math-inside-ai/
      playlist.md
      launch-plan.md
      video-order.md
      status-board.md
  videos/
    001-why-ai-needs-class-9-12-math/
      video.md
      learning-core.md
      scene-plan.md
      image-prompts.md
      image-qa.md
      motion-prompts.md
      motion-qa.md
      voiceover-script.md
      assembly-notes.md
      upload-metadata.md
      file-map.md
    002-images-become-matrices/
      ...
  templates/
    video.md
    learning-core.md
    scene-plan.md
    image-qa.md
    motion-qa.md
    upload-metadata.md
```

## Why A Separate `channel/` Folder Helps

The current repo is broader than the YouTube channel. It includes articles, modules, research, tools, business examples, student examples, Marathi localization, and experiments.

The channel needs a simpler production cockpit.

The `channel/` folder should answer:

```text
What are we publishing, when, and what is blocking it?
```

The existing folders answer:

```text
Where are the reusable source modules, prompts, images, clips, scripts, and manifests?
```

Both are needed.

## Per-Video Folder Rule

Every video should have one channel folder, even if its assets live elsewhere.

Example:

```text
channel/videos/002-images-become-matrices/
```

This folder is the memory bank for the video.

It should include:

```text
video.md
learning-core.md
scene-plan.md
image-prompts.md
image-qa.md
motion-prompts.md
motion-qa.md
voiceover-script.md
assembly-notes.md
upload-metadata.md
file-map.md
```

## `video.md`

This is the one-page status summary.

Template:

```md
# 002 - Images Become Matrices

Status: scene-plan-ready
Playlist: Class 9-12 Math Inside AI
Format: Short
Target length: 35-45 seconds
Publish order: 2

School concept: Matrices
AI mechanism: Image representation / computer vision
Memory sentence: Images become number grids.

Current blocker: Image prompts not finalized.
Next action: Create source-frame prompt pack.

Canonical files:
- Source module:
- Image prompt pack:
- Image folder:
- Runway folder:
- Manifest:
- Script:
- Export:
```

## `file-map.md`

This file prevents asset confusion.

It should link the channel video folder to the existing production asset folders.

Example:

```md
# File Map

Source module:
- `modules/visual-ai-concepts/matrices-how-images-become-numbers.source.md`

Image prompts:
- `assets/image-prompts/matrices-images-become-numbers-video-first.md`

Images:
- `assets/images/matrices-images-become-numbers-video-first/`

Runway clips:
- `outputs/runway-clips/matrices-images-become-numbers-runway-clips/`

Video manifests:
- `outputs/video-manifests/matrices-images-become-numbers-micro-lesson-v1.en.json`

Video scripts:
- `outputs/video-scripts/matrices-images-become-numbers-script-versions.md`
```

## Playlist Folder

Each playlist should have one folder.

Example:

```text
channel/playlists/01-class-9-12-math-inside-ai/
```

Files:

```text
playlist.md
launch-plan.md
video-order.md
status-board.md
```

### `playlist.md`

Defines the promise and boundaries.

```md
# Class 9-12 Math Inside AI

Audience:
Indian Class 9-12, higher secondary, junior college, and early college learners.

Promise:
Each video shows one Class 9-12 math concept inside one real AI mechanism.

Includes:
matrices, vectors, functions, probability, statistics, derivatives, linear equations, graphs, optimization.

Excludes:
exam solving, full derivations, coding tutorials, AI news.
```

### `video-order.md`

Tracks publish sequence.

```md
| Order | Video ID | Title | Format | Status | Notes |
|---|---|---|---|---|---|
| 1 | 001 | Why AI Needs Class 9-12 Math | Short | scene-plan-ready | series opener |
| 2 | 002 | Images Become Matrices | Short | image-prompts-ready | existing assets available |
```

### `status-board.md`

Tracks pipeline stage.

```md
| Video | Learning Core | Scene Plan | Image QA | Motion QA | Voiceover | Assembly | Final QA | Scheduled |
|---|---|---|---|---|---|---|---|---|
| 001 | done | done | pending | pending | pending | pending | pending | pending |
```

## Existing Folders Should Stay

Keep these folders as they are:

```text
modules/visual-ai-concepts/
assets/image-prompts/
assets/images/
outputs/video-manifests/
outputs/video-scripts/
outputs/runway-clips/
tools/
```

Reason:

- existing scripts likely depend on this structure
- assets are already organized by production type
- generated media can become heavy
- media should not be duplicated into every channel folder

## Naming Convention

Use stable IDs for channel videos:

```text
001-why-ai-needs-class-9-12-math
002-images-become-matrices
003-meaning-becomes-vectors
004-ai-gives-scores-not-certainty
```

Use descriptive slugs for asset folders:

```text
matrices-images-become-numbers-video-first
vectors-how-ai-compares-meaning-video-first-v3
```

The channel folder can use the simple publishing title, while asset folders can preserve the production/version naming.

## Do Not Put Everything In One Video Folder

Avoid this:

```text
channel/videos/002-images-become-matrices/assets/images/
channel/videos/002-images-become-matrices/assets/motion/
channel/videos/002-images-become-matrices/outputs/
```

Why:

- duplicates existing `assets/` and `outputs/`
- makes tools harder to reuse
- creates confusion about which asset is canonical
- heavy media can make the channel folder messy

Use references instead.

## When To Copy Assets Into Channel Folder

Only copy final lightweight review assets if useful:

- final thumbnail
- final contact sheet
- final export link or small proof image
- final metadata

Do not copy all raw generated images and Runway clips.

## First Playlist Status From Existing Assets

The repo already appears to have strong progress on the first playlist.

Existing or partially existing topics include:

- How AI Uses Math series intro
- Matrices / images become numbers
- Vectors / meaning comparison
- Probability / uncertainty
- Statistics / pattern learning
- Functions / input-output
- Linear equations / signals to score
- Derivatives / improvement direction

Likely missing or less developed:

- distance / similarity
- graphs / recommendations
- optimization / reducing error as its own topic

So the first playlist should not start from zero. It should consolidate existing work into the new channel layer.

## Migration Plan

Do this in phases.

### Phase 1: Add Control Layer

Create:

```text
channel/
channel/channel-board.md
channel/playlists/01-class-9-12-math-inside-ai/
channel/videos/
channel/templates/
```

No media movement yet.

### Phase 2: Register Existing Videos

Create video folders for existing topics:

```text
001-why-ai-needs-class-9-12-math
002-images-become-matrices
003-meaning-becomes-vectors
004-ai-gives-scores-not-certainty
005-data-becomes-patterns
006-a-model-is-a-function
007-slope-tells-ai-how-to-improve
008-signals-combine-into-a-score
```

For each, add:

- `video.md`
- `file-map.md`
- current status
- next action

### Phase 3: Fill Missing Pipeline Docs

For each registered video, add only the missing docs:

- if source exists, do not rewrite it
- if prompt pack exists, link it
- if image QA exists, link or summarize it
- if motion outputs exist, link them

### Phase 4: Launch Readiness Board

Create a board that answers:

```text
Can we launch with 10 finished Shorts?
```

Track:

- finished
- assembly-ready
- voiceover-ready
- images-approved
- scene-plan-ready
- learning-core-ready

## Recommendation

Do maintain a different structure for the YouTube channel, but only as an operating layer.

Do not move the existing production assets into that layer.

Best approach:

```text
channel/ = planning, playlist order, status, per-video memory
modules/ = canonical lesson explanations
assets/ = prompts and generated images
outputs/ = manifests, clips, scripts, renders
research/ = strategy and decisions
tools/ = automation scripts
```

This gives the channel enough structure to operate for months while keeping the current production pipeline intact.
