# Content Pipeline

This project should be managed as a pipeline, not as a static idea list.

Many topics can exist at different stages at the same time. One idea may only be captured. Another may have a scene flow. Another may have generated images but need QA. Another may be ready for Marathi localization or video.

## Pipeline Stages

| Stage | Meaning | Exit Criteria |
|---|---|---|
| 00 Captured | Idea is recorded but not shaped yet. | Has title, parent topic if relevant, and one-line learning promise. |
| 01 Framed | The audience, purpose, and learning promise are clear. | Has target learner, why it matters, and intended format. |
| 02 Scene Flow | The idea has a visual story structure. | Has 6-8 scene flow for umbrella topics or granular episodes. |
| 03 Source Draft | The explanation is written as a source module. | Has source doc with core explanation and key teaching points. |
| 04 Prompt Pack | Image/video prompts are archived. | Has frame-by-frame prompts in `assets/image-prompts/`. |
| 05 Visual Draft | First visual assets exist. | Has generated or designed images/cards. |
| 06 Visual QA | Visuals are reviewed with ChatGPT vision inspection of the actual rendered images/contact sheets/video frames. | Text, layout, sequence, factual clarity, and localization are checked visually, not inferred from prompts or scripts. |
| 07 Localized | Marathi or other local-language version exists. | Localized copy sounds natural, not dictionary-translated. |
| 08 Video / Interactive | Optional richer renderer exists. | Has storyboard, video, website, or interactive demo. |
| 09 Publish Ready | Asset is ready to share. | Has final reviewed output, prompt archive, QA notes, and clear format. |
| 10 Published / Archived | Asset was shared or intentionally closed. | Has publication link or archival note. |

## Status Labels

Use one of these labels in docs and board tables:

- `captured`
- `framed`
- `scene-flow`
- `source-draft`
- `prompt-pack`
- `visual-draft`
- `visual-qa`
- `localized`
- `video-interactive`
- `publish-ready`
- `published`
- `archived`

## Content Item Types

| Type | Description |
|---|---|
| Umbrella Topic | A broad map that can itself become a post/story. |
| Granular Episode | A focused concept, workflow, example, or career explanation. |
| Lesson Core | Stable renderer-agnostic explanation used by multiple outputs. |
| Renderer | A specific output format such as Markdown, 9:16 story, Marathi story, video, PDF, or interactive demo. |

## Metadata Block

Use this at the top of new topic and episode docs:

```md
Status: scene-flow
Pipeline stage: 02 Scene Flow
Type: Umbrella Topic
Parent topic: ...
Primary format: 9:16 mobile visual story
Next action: ...
```

For math-in-AI topics, also include:

```md
Target learner: 11th/12th standard or high-school students
School concept: ...
AI use: ...
Mechanism focus: transformation | comparison | scoring | optimization | representation
Series guide: HOW_AI_USES_MATH_SERIES_GUIDE.md
```

## Movement Rules

- A topic can move forward without waiting for other topics.
- An umbrella topic and its child episodes can be in different stages.
- For new educational concepts, create the image-only/self-contained visual story before video-first source frames unless the user explicitly overrides this for a specific session.
- `IMAGE_STORY_GATE.md` is the authority for image-only story opener, native-text, overlay-failure, and acceptance rules. Do not duplicate that gate in new notes.
- Do not create image-to-video source frames as the first visual format unless the user explicitly overrides this for a specific session.
- Do not move an item to `visual-draft` unless prompts or visual direction are preserved.
- For math-in-AI topics, `visual-draft` should normally mean image-only story cards exist first. Video-first frames are a later renderer adaptation.
- Do not move an educational image story, video, slide deck, or interactive renderer to `visual-draft`, `visual-qa`, or `publish-ready` if it only works after reading project notes. It must orient a new viewer inside the artifact itself.
- Do not move an item to `publish-ready` unless QA notes exist.
- Marathi/local-language versions are not literal translation tasks; they are separate renderer work.
- Keep the lesson core separate from renderer outputs. Improve the core first when the concept changes, then update each affected renderer.
- Every generated video manifest JSON should have a matching human-readable Markdown script/version file under `outputs/video-scripts/`.
- Keep JSON as the machine-readable render source and Markdown as the review/comparison source.
- For math-in-AI topics, do not mark an item as `source-draft` unless it explains the school concept, the AI use, and the actual mechanism connecting them.

## Video Script Versioning

For every video version, maintain both:

```text
outputs/video-manifests/<asset-version>.json
outputs/video-scripts/<asset-version>.md
```

The Markdown script should include:

- purpose of this version
- linked manifest JSON
- linked voiceover file
- linked rendered video when available
- learning design fields when available
- full voiceover script
- scene timing table
- review notes

If there are multiple versions of one episode, also keep an index file:

```text
outputs/video-scripts/<episode>-script-versions.md
```

## Weekly Working Pattern

1. Capture new ideas quickly.
2. Choose 1-3 items to move forward.
3. Convert selected items into scene flows.
4. Generate or design image-only/self-contained visual story drafts first.
5. Review the image-only contact sheet with ChatGPT vision as a critic before making video frames.
6. Convert approved image-only concepts into video-first source frames only after the concept works while paused.
7. Localize only after the English/story structure is clear.
8. Preserve prompts, assets, QA notes, and next action before pausing.
