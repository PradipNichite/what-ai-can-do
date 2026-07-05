# Graphs Image Story Review Notes

Status: needs-revision
Pipeline stage: 06 Visual QA

Source module: `modules/visual-ai-concepts/graphs-how-ai-understands-relationships.source.md`
Prompt pack: `assets/image-prompts/graphs-how-ai-understands-relationships-image-story.md`
Contact sheet: `assets/images/graphs-how-ai-understands-relationships-image-story/graphs-how-ai-understands-relationships-image-story-contact-sheet.jpg`

## Review

This set follows the Direction B math-series style: warm realistic study desk, Indian 11th/12th standard learner, teal/green shirt, tablet technical overlays, and a small readable graph rather than a dense network.

However, it fails the self-contained lesson-opening gate and the native-card composition gate. The original card 1 starts with `Many items look separate at first.` and separate video cards, but it does not tell a new viewer that this is a lesson about graphs, nodes and edges, or AI recommendations. The regenerated opener also does not meet the project standard because the text feels like a large caption layer over a study-desk image instead of a fully generated educational card where text, diagram, and scene are designed together.

The image-only teaching sequence is clear:

```text
separate video topics -> nodes -> edges -> graph -> related neighbors -> path -> knowledge graph -> quick-check recommendation
```

## Readability Checks

- `node`: readable in card 2, with a large example node and no edges yet.
- `edge`: readable in card 3 and card 7, tied to actual connecting lines.
- `path`: readable in card 6 and card 8, with a visible start-to-end route.
- `recommendation`: card 6 and card 8 explain the recommendation through a visible connected path, not only through glow or a check mark.

## Strong Cards

- Card 1: separate video/topic cards are clean and clearly not connected yet.
- Card 2: node concept is visually isolated before edges appear.
- Card 5: connected neighbor idea is easy to read because far nodes are dimmed.
- Card 6: the recommendation path from watched topic to suggested coding tutorial is visible and sequential.
- Card 8: quick check works as a paused card; the connected coding choice is justified by the path while cricket remains disconnected.

## Risks / Notes

- Required fix: regenerate or replace card 1 using native image generation as a complete educational poster/card. It must include the title/topic, the learning promise, the school concept `nodes and edges`, the AI use `video recommendations`, and the concrete example/task.
- Required style fix: text must be integrated through tablet UI, notebook panels, poster lettering, sticky notes, arrows, labels, or mini cards. Do not use generic text pasted over a background image.
- Some tiny generated labels inside tablet UI are decorative and should not be relied on for teaching.
- Card 4 uses icon-only clusters, which is readable as a graph but does not label every topic. This is acceptable because the teaching job is graph structure, not topic naming.
- Card 7 introduces `knowledge graph` clearly, but should remain a side example; the main lesson should continue to use the video recommendation graph.
- Future regeneration should keep the graph near 8-10 large nodes and avoid adding more relationship lines.

## Verdict

Not accepted as a final image-only concept proof. The node, edge, path, and recommendation logic are readable after the sequence begins, but the opener and text composition do not meet the project standard. Regenerate card 1, and consider regenerating the full set if the contact sheet still feels like captions over images rather than native educational cards.
