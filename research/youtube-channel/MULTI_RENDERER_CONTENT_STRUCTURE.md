# Multi-Renderer Content Structure

This document updates the folder and pipeline thinking from "YouTube video production" to "one concept, many distribution renderers."

## Core Correction

The project should not be organized around YouTube videos as the primary creative unit.

The primary unit should be:

```text
one concept / one learning story
```

That concept can then become multiple outputs:

- YouTube Short
- long-form YouTube video
- image-only carousel/story
- YouTube Community post
- WhatsApp share pack
- Instagram post or Reel
- article
- classroom slide
- interactive demo
- local-language version

So the production system should be:

```text
Concept core -> renderer adaptations -> platform-specific exports
```

Not:

```text
YouTube video -> leftover assets
```

## Why This Matters

The same topic needs different visuals depending on distribution.

### Image-Only / Carousel / WhatsApp

These assets must be understandable without voiceover.

They usually need:

- more embedded text
- clearer labels
- complete explanation per card
- stronger memory sentence on the image
- self-contained sequence
- share-friendly brand mark

### Video-First Source Frames

These assets are intended to become moving clips.

They usually need:

- less embedded text
- more open space for captions
- one visual action per frame
- clear motion targets
- fewer small labels
- less dense composition
- voiceover/captions carrying explanation

This distinction is already captured in the project research:

```text
Keep carousel cards for sharing.
Generate separate video source frames with less embedded text.
Move narration/captions into audio/subtitle layers.
```

Reference:

```text
research/notes/applied-ai-video-pipeline-techniques.md
```

## Recommended Mental Model

Use this hierarchy:

```text
Concept
  Core lesson
  Renderer adaptations
    Video-first
    Image-only story
    Article
    Community post
    Classroom/presentation
    Interactive/demo
  Platform exports
    YouTube Shorts
    YouTube long-form
    WhatsApp
    Instagram
    LinkedIn
```

## What Existing Structure Already Does Well

The current repo already has the right raw ingredients:

```text
modules/visual-ai-concepts/
assets/image-prompts/
assets/images/
outputs/mobile-stories/
outputs/video-manifests/
outputs/video-scripts/
outputs/runway-clips/
outputs/video-renders/
articles/
```

The `Functions` source module is especially close to the desired model because it includes renderer adaptation notes:

- Video Micro-Lesson
- Image-Only Post
- Presentation / Classroom
- Interactive / Demo

That should become the standard for every concept.

## Problem With A Pure `channel/videos` Structure

A folder like this is useful for YouTube publishing:

```text
channel/videos/002-images-become-matrices/
```

But it can accidentally imply that the YouTube video is the main artifact.

That is too narrow.

The concept should remain the parent. YouTube should be one renderer or distribution output.

## Better Structure

Create a new `content/` or `concepts/` layer for cross-platform concept management.

Recommended:

```text
concepts/
  class-9-12-math-inside-ai/
    001-why-ai-needs-class-9-12-math/
    002-images-become-matrices/
    003-meaning-becomes-vectors/
```

Each concept folder should contain planning and links, not necessarily all heavy assets.

Example:

```text
concepts/
  class-9-12-math-inside-ai/
    002-images-become-matrices/
      concept.md
      lesson-core.md
      renderer-plan.md
      file-map.md
      status.md
      renderers/
        video-short.md
        video-long.md
        image-story.md
        community-post.md
        article.md
        classroom.md
```

## Keep Asset Storage By Type

Do not move all generated media into the concept folder.

Keep:

```text
modules/visual-ai-concepts/
assets/image-prompts/
assets/images/
outputs/mobile-stories/
outputs/video-manifests/
outputs/video-scripts/
outputs/runway-clips/
outputs/video-renders/
articles/
```

Reason:

- existing tools already use these folders
- generated media can become large
- asset-type folders are easier for automation
- one concept may have many renderer variants

The concept folder should link to the canonical files through `file-map.md`.

## Concept Folder Files

### `concept.md`

One-page identity.

```md
# 002 - Images Become Matrices

Series: Class 9-12 Math Inside AI
Concept status: active
Primary concept: Matrices
AI mechanism: Image representation / computer vision
Memory sentence: Images become number grids.

Distribution priority:
1. YouTube Short
2. Image-only story
3. YouTube Community post
4. Article later

Current bottleneck:
Video-first images need QA.
```

### `lesson-core.md`

Renderer-agnostic explanation.

Can either be:

- a short local summary, or
- a pointer to `modules/visual-ai-concepts/<topic>.source.md`

Preferred:

Keep the detailed canonical source in `modules/visual-ai-concepts/` and reference it here.

### `renderer-plan.md`

Defines which outputs are worth creating.

```md
# Renderer Plan

| Renderer | Purpose | Status | Priority |
|---|---|---|---|
| YouTube Short | discovery | image-qa | P0 |
| Image-only story | share pack | not-started | P1 |
| Long-form video | trust | learning-core | P2 |
| Article | SEO/depth | parked | P3 |
```

### `file-map.md`

Links all related files.

```md
# File Map

Canonical source:
- `modules/visual-ai-concepts/matrices-how-images-become-numbers.source.md`

Video-first prompt pack:
- `assets/image-prompts/matrices-images-become-numbers-video-first.md`

Video-first source frames:
- `assets/images/matrices-images-become-numbers-video-first/`

Image-only story prompt pack:
- pending

Image-only story output:
- pending

Runway clips:
- `outputs/runway-clips/matrices-images-become-numbers-runway-clips/`

Video manifests:
- `outputs/video-manifests/matrices-images-become-numbers-*.json`

Video scripts:
- `outputs/video-scripts/matrices-images-become-numbers-*.md`
```

### `status.md`

Tracks stage by renderer, not only by concept.

```md
# Status

| Renderer | Core | Scene Plan | Prompts | Assets | QA | Assembly | Export | Publish |
|---|---|---|---|---|---|---|---|---|
| YouTube Short | done | done | done | done | pending | pending | pending | pending |
| Image-only story | done | pending | pending | pending | pending | n/a | pending | pending |
| Article | done | n/a | n/a | n/a | pending | n/a | draft | pending |
```

## Renderer-Specific Assets

Use clear naming for prompt packs and image folders.

### Video-First

```text
assets/image-prompts/<slug>-video-first.md
assets/images/<slug>-video-first/
outputs/runway-clips/<slug>-runway-clips/
outputs/video-manifests/<slug>-short-v1.en.json
outputs/video-renders/<slug>-short-v1.en.mp4
```

### Image-Only Story / Carousel

```text
assets/image-prompts/<slug>-image-story.md
assets/images/<slug>-image-story/
outputs/mobile-stories/<slug>.md
outputs/share-packs/<slug>/
```

### Article

```text
articles/<slug>.md
```

### Community Post

```text
outputs/community-posts/<slug>.md
```

### Classroom

```text
outputs/classroom/<slug>/
```

## Distribution Layer

The YouTube channel still needs a launch board, but it should reference concepts.

Use:

```text
channel/
  channel-board.md
  playlists/
    01-class-9-12-math-inside-ai/
      playlist.md
      video-order.md
      launch-plan.md
```

But `channel/videos/` should either be avoided or kept lightweight.

Better:

```text
channel/playlists/01-class-9-12-math-inside-ai/video-order.md
```

with rows pointing to:

```text
concepts/class-9-12-math-inside-ai/002-images-become-matrices/
```

This keeps YouTube as a distribution plan, not the master content structure.

## Revised Recommendation

Use three layers:

```text
research/ = strategy and decisions
concepts/ = one concept, many renderers, status, file map
channel/ = YouTube packaging, playlists, upload schedule
```

Keep the existing production folders:

```text
modules/ = canonical source explanations
assets/ = prompts and generated images
outputs/ = rendered artifacts and manifests
articles/ = written article outputs
tools/ = automation scripts
```

## Practical First Move

Create `concepts/class-9-12-math-inside-ai/` and register the first 10 concepts there.

Do not move media.

For each concept, create:

```text
concept.md
renderer-plan.md
file-map.md
status.md
```

Then create `channel/playlists/01-class-9-12-math-inside-ai/` as the YouTube launch view that points back to those concepts.

## Updated Bottom Line

The correct production unit is not:

```text
video
```

It is:

```text
concept story
```

The concept story can produce video-first frames, image-only share cards, articles, classroom materials, and YouTube uploads as separate renderer adaptations.
