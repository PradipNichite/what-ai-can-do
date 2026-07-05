# Graphs Source Frame Review Notes

Status: visual-draft
Pipeline stage: 05 Visual Draft

Source module: `modules/visual-ai-concepts/graphs-how-ai-understands-relationships.source.md`
Prompt pack: `assets/image-prompts/graphs-how-ai-understands-relationships-video-first.md`
Contact sheet: `assets/images/graphs-how-ai-understands-relationships-video-first/graphs-video-first-source-contact-sheet.jpg`

## Review

This set fits the current Direction B math-series style: realistic warm study desk, Indian 11th/12th standard learner, teal/green shirt, wooden desk, lamp, notebook, books, plant, and tablet as the main technical surface.

The teaching sequence is clear:

```text
separate video items -> nodes -> edges -> graph -> nearby connected nodes -> path -> knowledge graph -> connected recommendation
```

Strong frames:

- Frame 1: clean separate video/topic cards with no network yet.
- Frame 4: compact readable graph with clustered nodes, not an unreadable web.
- Frame 5: nearby connected nodes are visibly related through edges.
- Frame 6: highlighted path strongly explains the suggestion.
- Frame 8: quick check shows a connected candidate versus a disconnected candidate.

Risks:

- Frame 2 already shows some connecting lines, so it slightly blurs the node-before-edge distinction. It still works because the circular nodes are large and the `node` label is readable.
- Frame 3 includes a few generated micro-labels inside the tablet UI. They are not central to the lesson, but final video should avoid letting them morph or distract.
- The graph is readable overall, but future regenerations should keep the node count near 8-10 and avoid adding extra decorative lines.
- The recommendation must stay explained by visible connections and path lighting, not only by glow.

Recommendation:

Good visual draft for technical review. For final Runway generation, use locked or low-motion prompts on frames with labels (`node`, `edge`, `path`) and avoid zooming into frame 3's small generated UI text. If doing a refinement pass, the highest-value improvement would be regenerating frame 2 with no edges yet.
