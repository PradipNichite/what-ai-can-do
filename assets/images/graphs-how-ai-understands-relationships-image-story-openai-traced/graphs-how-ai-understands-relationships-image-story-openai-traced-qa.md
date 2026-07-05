# OpenAI Visual QA - image-story

Generated: 2026-07-04T12:44:56+00:00
Model: `gpt-5.5`
Response ID: `resp_0a889c175fc96b2b006a4900272e4881a08357f7233436881b`
OpenAI request ID: `45b6fb14-2305-4dfb-b41c-7d2a7f73f912`

## Inputs

- Image folder: `assets\images\graphs-how-ai-understands-relationships-image-story-openai-traced`
- Contact sheet: `assets\images\graphs-how-ai-understands-relationships-image-story-openai-traced\graphs-how-ai-understands-relationships-image-story-openai-traced-contact-sheet.jpg`
- Prompt pack: `assets\image-prompts\graphs-how-ai-understands-relationships-image-story.md`
- Source module: `modules\visual-ai-concepts\graphs-how-ai-understands-relationships.source.md`

Reviewed images:
- `assets\images\graphs-how-ai-understands-relationships-image-story-openai-traced\graphs-how-ai-understands-relationships-image-story-openai-traced-contact-sheet.jpg`

## Verdict

- Status: `needs-revision`
- Intended use: `image-story`
- Next action: `regenerate-frame`

The story teaches the graph mechanism well and the opener is strong, but the set is not fully ready because several cards lose the native warm study-desk composition and some small labels are marginal for mobile. Mechanism visibility passes; composition consistency and overlay/template feel need revision.

## Gate Evidence

- Opener: `pass` - Frame 1 is self-contained: it visibly names the topic as “Graphs: How AI understands relationships,” includes the school/AI bridge “Nodes and edges help AI connect video topics,” and introduces the continuing example with the sticky note “Example: recommend the next study video.” The separate video/topic cards are shown clearly with no connecting lines yet.
- Opener required fix: None
- Native composition: `partial` - Frame 1 integrates text into a notebook page, tablet cards, and sticky note, and Frame 2 uses a tablet diagram with a magnified node label. However, several later cards shift into clean generic infographic layouts with large headline text floating on blank poster space rather than the recurring warm study-desk/tablet scene. Frames 3–8 mostly lose the Indian learner/warm desk continuity; Frames 4–6 especially look like standalone template cards rather than the same native study-tablet lesson world.
- Native composition required fix: Regenerate or revise the weaker frames so the main teaching text and diagrams feel built into the tablet/notebook/sticky-note educational scene, with more consistent warm desk/tablet context across the set.
- Overlay risk: `medium` - The text is generally clean and readable, but multiple frames use large, perfectly flat headline blocks at the top of otherwise minimal infographic cards: e.g., Frame 5 “Connected neighbors are related.”, Frame 6 “A path can explain a recommendation.”, and Frame 8 “Quick check: which recommendation fits?” These do not look like random pasted captions over stock photos, but they do have a template-overlay feel rather than fully embedded tablet/notebook UI text. Frame 1 has low overlay risk because the text is visibly part of physical paper/sticky-note surfaces.
- Mechanism visibility: `pass` - The core sequence is visually understandable: Frame 1 shows separate video/topic items; Frame 2 turns items into circular nodes with a labeled enlarged node; Frame 3 adds selected relationship edges and labels “edge”/“related”; Frame 4 shows a sparse graph; Frame 5 highlights connected neighbors and dims far nodes; Frame 6 shows a sequential path from AI basics to machine learning to coding tutorial with a recommend marker; Frame 7 shows a knowledge graph connecting entity icons; Frame 8 compares a connected coding tutorial recommendation against an unconnected cricket option.
- Mechanism required fix: None for mechanism, though Frame 5 would be stronger if the neighbor nodes were named or more clearly matched to machine learning and coding tutorial.
- Mobile readability: `partial` - Main headlines are readable across the contact sheet, and the key labels “node,” “edge,” “path,” “recommend,” and “knowledge graph” are mostly legible. Some small topic labels inside tablets are likely marginal on a phone, especially in Frames 3 and 8. Frame 5’s slanted “related” labels are small and may be hard to read on mobile. Frame 1’s tablet topic labels are smaller but still supported by clear icons.
- Mobile readability required fix: Increase size/contrast of small mechanism labels in Frames 3, 5, and 8, especially “related” and topic labels inside the tablet UI.

## Frame Notes

### Frame 1

- Status: `pass`
- Evidence: Strong opener. It names the lesson, states the AI/video recommendation purpose, shows separate video cards, and uses notebook/sticky-note/tablet surfaces for text. No edges are visible yet, matching the teaching step.
- Fix: None.

### Frame 2

- Status: `pass`
- Evidence: Clearly communicates that each item becomes a node. The tablet shows colored circular nodes, and one enlarged node is labeled “node.” No relationship edges are shown.
- Fix: None.

### Frame 3

- Status: `needs-revision`
- Evidence: Relationships/edges are visible and the labels “edge” and “related” appear. However, the frame has a duplicated diagram area above and tablet below, making it visually busier than necessary. Some small card labels may be hard on mobile, and the style shifts away from the warm desk/learner continuity.
- Fix: Use one main tablet diagram, enlarge the edge/related labels, and keep the warm study-desk/tablet setting consistent.

### Frame 4

- Status: `needs-revision`
- Evidence: The graph is sparse and readable, and the headline says “Nodes + edges form a graph.” However, there is no separate visible “graph” label other than the word in the headline, and the card looks like a generic clean infographic with no learner/study-desk continuity.
- Fix: Add a small integrated “graph” label near the network and restore some warm tablet/desk context or make it feel more native to the established scene.

### Frame 5

- Status: `needs-revision`
- Evidence: The central watched node, connected neighbors, dim far nodes, and related edges are visible. But the related neighbor nodes are icon-only, so the continuing recommendation example is less clear; the “related” labels are small/rotated and may not read on mobile. The card also lacks the recurring desk/tablet setting.
- Fix: Label or visually identify the connected neighbors as machine learning/coding tutorial candidates, enlarge the “related” labels, and place the graph on the tablet within the study scene.

### Frame 6

- Status: `pass`
- Evidence: The path mechanism is clear: AI basics connects down to machine learning and then coding tutorial, with the path highlighted and “recommend” marking the final node. Unrelated nodes are dimmed.
- Fix: Optional: integrate the headline/path legend into tablet UI or notebook callouts to reduce template-overlay feel.

### Frame 7

- Status: `pass`
- Evidence: The knowledge graph is clear and readable, with entity icons connected by edges and labels for “node,” “edge,” and “knowledge graph.” The tablet-in-hands composition supports the technical surface requirement.
- Fix: None.

### Frame 8

- Status: `pass`
- Evidence: The quick check is understandable: coding tutorial has a visible connected path and check mark, while cricket highlights is dim/unconnected. The prompt text and “path” label are readable.
- Fix: Optional: enlarge the small path label and simplify the duplicated top/bottom choice layout if targeting very small phone screens.
