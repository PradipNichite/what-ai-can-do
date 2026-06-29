# Content Pipeline

This project should be managed as a pipeline, not as a static idea list.

Many topics can exist at different stages at the same time. One idea may only be captured. Another may have a scene flow. Another may have generated images but need QA. Another may be ready for Marathi localization or video.

## Pipeline Stages

| Stage | Meaning | Exit Criteria |
|---|---|---|
| 00 Captured | Idea is recorded but not shaped yet. | Has title, parent topic if relevant, and one-line hook. |
| 01 Framed | The audience, purpose, and learning promise are clear. | Has target learner, why it matters, and intended format. |
| 02 Scene Flow | The idea has a visual story structure. | Has 6-8 scene flow for umbrella topics or granular episodes. |
| 03 Source Draft | The explanation is written as a source module. | Has source doc with core explanation and key teaching points. |
| 04 Prompt Pack | Image/video prompts are archived. | Has frame-by-frame prompts in `assets/image-prompts/`. |
| 05 Visual Draft | First visual assets exist. | Has generated or designed images/cards. |
| 06 Visual QA | Visuals are being reviewed. | Text, layout, sequence, factual clarity, and localization are checked. |
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

## Movement Rules

- A topic can move forward without waiting for other topics.
- An umbrella topic and its child episodes can be in different stages.
- Do not move an item to `visual-draft` unless prompts or visual direction are preserved.
- Do not move an item to `publish-ready` unless QA notes exist.
- Marathi/local-language versions are not literal translation tasks; they are separate renderer work.

## Weekly Working Pattern

1. Capture new ideas quickly.
2. Choose 1-3 items to move forward.
3. Convert selected items into scene flows.
4. Generate or design visual drafts.
5. Review visuals as a critic.
6. Localize only after the English/story structure is clear.
7. Preserve prompts, assets, QA notes, and next action before pausing.
