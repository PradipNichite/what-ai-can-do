# Graphs: How AI Understands Relationships - Native Story V2

Series: How AI Uses Math
Source module: `modules/visual-ai-concepts/graphs-how-ai-understands-relationships.source.md`
Output image folder: `assets/images/graphs-how-ai-understands-relationships-native-story-v2-openai/`
Renderer: image-only native mobile story cards

This is a separate renderer prompt pack because the earlier graph image-story prompts produced too many clean slide/infographic cards. This V2 prompt pack follows the native story style of:

- `assets/image-prompts/student-ai-study-story.md`
- `assets/image-prompts/derivatives-ai-learning-story.md`

## Native Story Direction

Use image generation to create the full educational composition. Do not treat the image as a background and the text as a later overlay. Text should be part of the scene through tablet UI, notebook prompts, sticky notes, arrows, labels, callouts, and mini cards.

The card should feel like one complete designed educational poster, where illustration, diagram, and text are generated together, not a separate caption pasted on top.

Text must be integrated through tablet UI, notebook panels, poster typography, sticky notes, arrows, labels, callouts, or mini-cards.

## Character And Style Lock

Use the same kind of visual world as the best native story examples:

- warm modern Indian educational illustration
- 9:16 mobile story aesthetic
- recurring Indian high-school learner at a wooden study desk
- green/teal school shirt, dark hair, expressive curious face
- warm desk lamp, open notebook, pen cup, books, sticky notes, plant
- tablet or phone as the main teaching surface
- text integrated inside the scene, not a clean slide template
- diagrams live on the tablet/notebook, with arrows and labels connected to objects
- no blank corporate infographic background
- no generic PPT card
- no separate caption block pasted over the image

Core mechanism:

```text
separate items -> nodes -> edges -> graph -> connected neighbors -> path -> recommendation
```

Memory anchor:

```text
Graphs are math for connected things.
```

## Cards

### Card 1 - Lesson Opener

Teaching job: introduce the lesson, school concept, AI use, and concrete recommendation example in one self-contained native story card.

Prompt:

```text
Use case: illustration-story
Asset type: 9:16 native educational story card, frame 1 of 8
Primary request: Create a polished vertical mobile story card for Indian 11th/12th standard students titled "Graphs: How AI understands relationships". The card must feel like a complete designed educational poster where illustration, tablet diagram, notebook notes, sticky notes, and text are generated together, not a separate caption overlay.
Scene/backdrop: Warm Indian student study desk at home. A recurring Indian high-school learner in a green/teal shirt sits at a wooden desk with a tablet, open notebook, pen cup, books, sticky notes, and warm lamp. The tablet shows separate video/topic cards: AI basics, machine learning, coding tutorial, study tips, cricket, music.
Subject: Indian high-school learner, tablet with video/topic cards, notebook showing tiny node-and-edge doodle, sticky note with recommendation task.
Style/medium: warm modern educational illustration, high quality Instagram/WhatsApp story aesthetic, expressive, clear, hand-drawn poster typography mixed with tablet UI, not corporate stock, not flat PPT.
Composition/framing: 9:16 portrait. Student and tablet occupy the middle. Integrate the title as large friendly poster typography near the top, the learning promise as a notebook callout, and the example as a sticky note attached near the tablet.
Text to render verbatim, exactly:
"Graphs: How AI understands relationships"
"Nodes + edges connect video topics."
"Example: recommend the next study video"
Constraints: no lines between video cards yet; keep items separate; render all text clearly and exactly; no extra text; no logos; no watermark; no generic caption panel; text must feel native to the scene through poster title, notebook callout, and sticky note; mobile readable.
```

### Card 2 - Items Become Nodes

Teaching job: show each video/topic item becoming a node.

Prompt:

```text
Use case: illustration-story
Asset type: 9:16 native educational story card, frame 2 of 8
Primary request: Create a polished mobile story card showing how separate video/topic items become graph nodes. Keep the same warm Indian study-desk world and recurring learner style as card 1.
Scene/backdrop: Same learner at the wooden study desk. Tablet is large in the foreground. The tablet shows video/topic cards gently transforming into colorful circular nodes. Notebook beside the tablet has a simple hand-drawn note.
Subject: Tablet UI transformation from video cards to large circular nodes, student watching curiously, pen and sticky notes around the tablet.
Style/medium: warm modern educational illustration, high quality mobile story aesthetic, integrated tablet UI and notebook notes, not a clean infographic slide.
Composition/framing: 9:16 portrait. Big tablet in lower/middle area; student face visible behind it. Use arrows from video cards to nodes and one magnified node callout.
Text to render verbatim, exactly:
"Each item becomes a node."
"AI basics"
"machine learning"
"coding tutorial"
"study tips"
"cricket"
"music"
"node"
Constraints: use only the listed video/topic labels from the opener; do not introduce unrelated labels such as climate, plant life, atoms, history, geography, or school subjects; do not show edges yet; nodes must be large enough for mobile; text appears as tablet label and notebook callout; no extra text; no logos; no watermark; no blank PPT background.
```

### Card 3 - Relationships Become Edges

Teaching job: show relationships becoming edges.

Prompt:

```text
Use case: illustration-story
Asset type: 9:16 native educational story card, frame 3 of 8
Primary request: Create a polished native story card showing relationship lines added between related video/topic nodes. Keep the same warm desk, learner, tablet, and story-card composition.
Scene/backdrop: Same learner leans toward the tablet with an aha expression. The tablet shows the nodes from the previous card. Clean glowing edges are drawn between related nodes: AI basics to machine learning, machine learning to coding tutorial, and study tips to study topic. Cricket and music remain dim and separate.
Subject: Tablet graph UI, hand-drawn arrows, edge labels, learner noticing the connections.
Style/medium: warm modern educational illustration, high quality WhatsApp/Instagram story aesthetic, integrated text, not flat infographic.
Composition/framing: 9:16 portrait. The tablet fills the lower half, learner and desk objects fill the upper/middle. Integrate the headline as a sticky note or notebook banner, not a floating poster block.
Text to render verbatim, exactly:
"Relationships become edges."
"edge"
"related"
Constraints: edges must explain chosen relationships, not random decoration; avoid tangled network; keep labels large; no extra text; no logos; no watermark; no generic caption panel.
```

### Card 4 - Nodes Plus Edges Form A Graph

Teaching job: show nodes plus edges forming a graph/network.

Prompt:

```text
Use case: illustration-story
Asset type: 9:16 native educational story card, frame 4 of 8
Primary request: Create a polished native educational story card showing that nodes plus edges form a graph. It must stay in the same warm Indian study-desk/tablet story world.
Scene/backdrop: Same learner at desk, notebook open with a small graph doodle, tablet showing a compact readable network. The learner points at the tablet with a pencil.
Subject: Tablet network with 8 to 10 large circular nodes connected by clean edges, grouped into learning/AI, study/math, and entertainment clusters.
Style/medium: warm modern educational illustration, story-card aesthetic, friendly educational poster typography integrated with tablet and notebook surfaces.
Composition/framing: 9:16 portrait. Tablet is the main visual surface; notebook callout beside it explains the idea. Include desk lamp warmth and familiar objects for continuity.
Text to render verbatim, exactly:
"Nodes + edges form a graph."
"graph"
Constraints: no dense network; no tiny labels; graph must be understandable on a phone; text must be on tablet/notebook elements, not a generic title overlay; no extra text; no logos; no watermark.
```

### Card 5 - Connected Neighbors Are Related

Teaching job: show connected neighbors as related recommendation candidates.

Prompt:

```text
Use case: illustration-story
Asset type: 9:16 native educational story card, frame 5 of 8
Primary request: Create a polished native story card showing that connected neighbor nodes are related. This card must not become a plain infographic; keep the warm desk/tablet/learner story composition.
Scene/backdrop: Same Indian learner at the wooden desk. Tablet is angled toward the viewer. A watched "AI basics" node is highlighted on the tablet. Two connected neighbor nodes, "machine learning" and "coding tutorial", are linked with clear edges and marked related. Far nodes like cricket and music are dimmed.
Subject: Tablet graph UI with watched node, connected neighbor nodes, dim far nodes, student using a pencil or finger to follow the links.
Style/medium: warm modern educational illustration, high quality mobile story aesthetic, expressive, native integrated text, no clean corporate slide.
Composition/framing: 9:16 portrait. Learner, tablet, notebook, sticky notes, and graph UI all visible. Put the main sentence as a handwritten notebook banner or tablet top bar. Put "related" labels attached to the actual edges.
Text to render verbatim, exactly:
"Connected neighbors are related."
"AI basics"
"machine learning"
"coding tutorial"
"related"
Constraints: visible edges must explain relatedness; do not rely only on glow; keep graph sparse and readable; preserve warm study-desk/tablet context; no blank white infographic card; no extra text; no logos; no watermark.
```

### Card 6 - Path Explains Recommendation

Teaching job: show a highlighted path explaining a recommendation.

Prompt:

```text
Use case: illustration-story
Asset type: 9:16 native educational story card, frame 6 of 8
Primary request: Create a polished native story card showing how a graph path can explain a recommendation. Keep the same learner and warm desk/tablet visual world.
Scene/backdrop: Same learner at desk, tablet large in foreground. On tablet, a highlighted path runs from AI basics to machine learning to coding tutorial. The final coding tutorial node is marked as the recommendation. Unrelated nodes are dim.
Subject: Tablet graph path, recommendation label, learner following the path with finger, notebook note beside the tablet.
Style/medium: warm modern educational illustration, mobile story card aesthetic, integrated arrows and labels, not a standalone flowchart slide.
Composition/framing: 9:16 portrait. Use the tablet as the technical surface and a sticky-note takeaway below it.
Text to render verbatim, exactly:
"A path can explain a recommendation."
"AI basics"
"machine learning"
"coding tutorial"
"path"
"recommend"
Constraints: path must be sequential and readable; no random arrows; no dense network; labels must attach to actual path and recommendation; no extra text; no logos; no watermark.
```

### Card 7 - Knowledge Graphs Connect Facts

Teaching job: broaden graphs from videos to connected facts.

Prompt:

```text
Use case: illustration-story
Asset type: 9:16 native educational story card, frame 7 of 8
Primary request: Create a polished native story card showing that graphs can connect facts too. Keep the same warm educational story style.
Scene/backdrop: Same study desk. The learner holds or looks at a tablet showing a simple knowledge graph. Notebook beside the tablet has tiny doodles of person, place, concept, book, and video icons.
Subject: Tablet knowledge graph with large entity nodes and clean edges. Icons for person, place, concept, video, and book. One node label and one edge label.
Style/medium: warm modern educational illustration, high quality mobile story aesthetic, integrated text, not a flat diagram slide.
Composition/framing: 9:16 portrait. Tablet centered, hands visible, warm desk objects around it. Main title appears as friendly poster typography integrated into the scene.
Text to render verbatim, exactly:
"Graphs can connect facts too."
"knowledge graph"
"node"
"edge"
Constraints: avoid dense concept-map text; use icons and very short labels; keep mobile readable; no extra text; no logos; no watermark; no generic caption panel.
```

### Card 8 - Quick Check

Teaching job: test that the connected recommendation is better justified than an unconnected one.

Prompt:

```text
Use case: illustration-story
Asset type: 9:16 native educational story card, frame 8 of 8
Primary request: Create a polished final quick-check mobile story card. It should feel like the same warm native story world, with the learner choosing between two recommendation cards.
Scene/backdrop: Same learner at desk with tablet and notebook. Tablet shows watched "AI basics" connected by a visible path to "coding tutorial". Two choice cards sit below: coding tutorial with check mark, cricket highlights dimmed/unconnected.
Subject: Tablet quick-check UI, visible path, two recommendation choices, student thinking and pointing.
Style/medium: warm modern educational illustration, high quality Instagram/WhatsApp story aesthetic, integrated quiz UI, not a generic quiz slide.
Composition/framing: 9:16 portrait. Main question at top as tablet/notebook heading. Graph path in middle. Two choice cards at bottom with visual evidence.
Text to render verbatim, exactly:
"Quick check: which recommendation fits?"
"Choose the one with a path."
"AI basics"
"coding tutorial"
"cricket highlights"
"path"
Constraints: connected recommendation must be visibly justified by path; unconnected cricket choice should be dim; keep text readable; no extra text; no logos; no watermark; no generic caption panel.
```

## Acceptance Standard

The set can only be accepted if actual generated images show:

- self-contained opener
- native generated composition
- no pasted-overlay look
- integrated text plan
- mechanism visibility
- mobile readability
- recurring warm desk/tablet story style similar to the student AI study and derivatives native-story examples
