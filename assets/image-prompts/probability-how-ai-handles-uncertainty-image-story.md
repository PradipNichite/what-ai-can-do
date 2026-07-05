# Probability: How AI Handles Uncertainty - Native Image Story

Series: How AI Uses Math
Source module: `modules/visual-ai-concepts/probability-how-ai-handles-uncertainty.source.md`
Output image folder: `assets/images/probability-how-ai-handles-uncertainty-image-story/`
Renderer: image-only native mobile story cards

## Native Story Direction

Use image generation to create the full educational composition. The card should feel like one complete designed educational poster, where illustration, diagram, and text are generated together, not a separate caption pasted on top.

Text must be integrated through tablet UI, notebook panels, poster typography, sticky notes, arrows, labels, callouts, or mini-cards.

## Character And Style Lock

- warm modern Indian educational illustration
- 9:16 mobile story aesthetic
- recurring Indian 11th/12th standard learner with dark wavy hair
- green/teal school shirt
- warm wooden study desk, desk lamp, notebook, books, sticky notes, pen cup, small plant
- tablet as the main technical surface
- probability bars, confidence meters, scales, answer cards, and quick-check panels live on the tablet/notebook
- no isolated flat diagram cards
- no generic PPT card
- no pasted caption block

Core mechanism:

```text
input -> possible answers -> probability scores -> highest score -> uncertainty when scores are close -> real AI uses -> quick check
```

Memory anchor:

```text
AI predictions are confidence-weighted guesses.
```

## Cards

### Card 1 - Lesson Opener

Teaching job: introduce probability, uncertainty, AI prediction, and the cat/dog/car example in one self-contained card.

Prompt:

```text
Use case: scientific-educational
Asset type: 9:16 native educational story card, frame 1 of 8
Primary request: Create a polished vertical mobile story card for Indian 11th/12th standard students titled "Probability: How AI handles uncertainty". The card must feel like a complete designed educational poster where illustration, tablet UI, notebook notes, sticky notes, and text are generated together, not a separate caption overlay.
Scene/backdrop: Warm Indian student study desk at home. A recurring Indian high-school learner in a green/teal shirt sits at a wooden desk with a tablet, notebook, pen cup, books, sticky notes, small plant, and warm desk lamp.
Subject: Tablet shows one photo/input card with three possible answer cards around it: cat, dog, car. None is guaranteed yet.
Technical visual: Notebook has a tiny probability scale from 0 to 1 and a sticky note introduces the concrete task.
Style/medium: warm modern Indian educational illustration, high quality Instagram/WhatsApp story aesthetic, expressive, clear, hand-drawn poster typography mixed with crisp tablet UI, not corporate stock, not flat PPT.
Composition/framing: 9:16 portrait. Student and tablet occupy the middle. Integrate the title as large friendly poster typography near the top, the learning promise as a notebook callout, and the example as a sticky note attached near the tablet.
Text to render verbatim, exactly:
"Probability: How AI handles uncertainty"
"AI estimates what is most likely."
"Example: cat, dog, or car?"
Constraints: render all text clearly and exactly; no extra text; no logos; no watermark; no generic caption panel; text must feel native to the scene through poster title, notebook callout, sticky note, and tablet UI; mobile readable.
```

### Card 2 - Probability Scale

Teaching job: show probability as a number from 0 to 1 and 0% to 100%.

Prompt:

```text
Use case: scientific-educational
Asset type: 9:16 native educational story card, frame 2 of 8
Primary request: Create a polished native story card showing probability as a scale. Keep the same warm Indian study-desk world and recurring learner style as card 1.
Scene/backdrop: Same learner at the wooden study desk, pointing at a tablet.
Subject: Tablet shows a large horizontal probability scale from 0 to 1, with 0%, 50%, and 100% below it. A pointer sits near 0.7 with a soft confidence glow.
Technical visual: Notebook beside tablet has a simple handwritten note connecting higher probability to stronger confidence.
Style/medium: warm modern educational illustration, high quality mobile story aesthetic, integrated tablet UI and notebook notes, not a clean infographic slide.
Composition/framing: 9:16 portrait. Big tablet in lower/middle area; student face and pointing hand visible behind it.
Text to render verbatim, exactly:
"Probability is a likelihood score."
"0"
"0.5"
"1"
"0%"
"50%"
"100%"
Constraints: scale and numbers must be large enough for mobile; no extra text; no logos; no watermark; no blank PPT background.
```

### Card 3 - Scores For Options

Teaching job: show AI assigning probability scores to possible answers.

Prompt:

```text
Use case: scientific-educational
Asset type: 9:16 native educational story card, frame 3 of 8
Primary request: Create a polished native story card showing AI assigning probability scores to possible answers. Keep the same learner, desk, tablet, and story-card composition.
Scene/backdrop: Same learner leans toward the tablet with a curious expression.
Subject: Tablet shows three large probability bars for a photo classifier.
Technical visual: Cat bar is tallest, dog medium, car short. Each bar has a readable label and number.
Style/medium: warm modern educational illustration, high quality WhatsApp/Instagram story aesthetic, integrated text, not flat infographic.
Composition/framing: 9:16 portrait. Tablet fills the lower half, learner and desk objects fill the upper/middle. Integrate the headline as a sticky note or notebook banner.
Text to render verbatim, exactly:
"AI gives each option a score."
"cat 0.72"
"dog 0.20"
"car 0.08"
Constraints: bar heights must match the numbers; keep labels large; no extra text; no logos; no watermark; no generic caption panel.
```

### Card 4 - Highest Score Is Chosen

Teaching job: show highest probability selection without implying certainty.

Prompt:

```text
Use case: scientific-educational
Asset type: 9:16 native educational story card, frame 4 of 8
Primary request: Create a polished native educational story card showing that AI often chooses the highest probability. It must stay in the same warm Indian study-desk/tablet story world.
Scene/backdrop: Same learner at desk, tablet showing the same cat/dog/car bars. Learner points at the tallest cat bar with a pencil.
Subject: Tablet UI with cat bar glowing, dog and car dimmed, chosen answer card visible.
Technical visual: Add a small caution note that chosen does not mean guaranteed.
Style/medium: warm modern educational illustration, story-card aesthetic, friendly educational poster typography integrated with tablet and notebook surfaces.
Composition/framing: 9:16 portrait. Tablet is the main visual surface; notebook callout beside it explains the idea.
Text to render verbatim, exactly:
"Highest score gets chosen."
"chosen: cat"
"likely, not guaranteed"
Constraints: do not imply the answer is certain; keep text on tablet/notebook elements, not a generic title overlay; no extra text; no logos; no watermark.
```

### Card 5 - Close Scores Mean Uncertainty

Teaching job: show that close probabilities mean weaker confidence.

Prompt:

```text
Use case: scientific-educational
Asset type: 9:16 native educational story card, frame 5 of 8
Primary request: Create a polished native story card showing uncertainty when scores are close. This card must not become a plain infographic; keep the warm desk/tablet/learner story composition.
Scene/backdrop: Same Indian learner at the wooden desk with a thoughtful uncertain expression. Tablet is angled toward the viewer.
Subject: Tablet shows close cat and dog probability bars, plus a low confidence meter.
Technical visual: Cat 0.42 and dog 0.39 bars are almost the same height. Car 0.19 is lower. Confidence meter is yellow and low.
Style/medium: warm modern educational illustration, high quality mobile story aesthetic, expressive, native integrated text, no clean corporate slide.
Composition/framing: 9:16 portrait. Learner, tablet, notebook, sticky notes, and probability UI all visible. Put the main sentence once, as either a handwritten notebook banner or a tablet top bar, not both.
Text to render verbatim, exactly:
"Close scores mean uncertainty."
"cat 0.42"
"dog 0.39"
"car 0.19"
"low confidence"
Constraints: close bars must visibly look close; render each required phrase exactly once; avoid duplicate uncertainty notes on multiple surfaces; do not use scary warning symbols; keep graph sparse and readable; no extra text; no logos; no watermark.
```

### Card 6 - Same Idea In Real AI

Teaching job: broaden probability from classifiers to recommendations and chatbots.

Prompt:

```text
Use case: scientific-educational
Asset type: 9:16 native educational story card, frame 6 of 8
Primary request: Create a polished native story card showing that probability scores appear in many AI systems. Keep the same learner and warm desk/tablet visual world.
Scene/backdrop: Same learner at desk, tablet large in foreground.
Subject: Tablet has three mini panels: image AI, recommendation, chatbot. Each mini panel shows tiny probability bars.
Technical visual: A single visual rule repeats across all panels: options get scores, then the highest likely option is chosen.
Style/medium: warm modern educational illustration, mobile story card aesthetic, integrated arrows and labels, not a standalone flowchart slide.
Composition/framing: 9:16 portrait. Use the tablet as the technical surface and a sticky-note takeaway below it.
Text to render verbatim, exactly:
"Same idea in real AI."
"image AI"
"recommendation"
"chatbot"
"scores to choice"
Constraints: three panels must be readable but not crowded; render the sticky note as the plain words "scores to choice" with no arrow symbol; no dense numbers; no extra text; no logos; no watermark.
```

### Card 7 - Memory Anchor

Teaching job: summarize the mechanism as a confidence-weighted guess.

Prompt:

```text
Use case: scientific-educational
Asset type: 9:16 native educational story card, frame 7 of 8
Primary request: Create a polished native story card summarizing probability in AI prediction. Keep the same warm educational story style.
Scene/backdrop: Same study desk. The learner smiles with an aha expression while looking at a tablet and notebook.
Subject: Tablet shows a clean chain from input to probability scores to chosen answer. Notebook has the memory anchor written clearly.
Technical visual: Chain nodes connected by arrows, with small probability bars inside the middle node.
Style/medium: warm modern educational illustration, high quality mobile story aesthetic, integrated text, not a flat diagram slide.
Composition/framing: 9:16 portrait. Tablet centered, hands visible, warm desk objects around it. Main anchor appears as friendly notebook typography integrated into the scene.
Text to render verbatim, exactly:
"input"
"probability scores"
"chosen answer"
"AI predictions are confidence-weighted guesses."
Constraints: keep memory anchor readable; avoid dense paragraphs; no extra text; no logos; no watermark; no generic caption panel.
```

### Card 8 - Quick Check

Teaching job: test that the learner can spot uncertainty when top probabilities are close.

Prompt:

```text
Use case: scientific-educational
Asset type: 9:16 native educational story card, frame 8 of 8
Primary request: Create a polished final quick-check mobile story card. It should feel like the same warm native story world, with the learner comparing two probability cards.
Scene/backdrop: Same learner at desk with tablet and notebook.
Subject: Tablet shows two large text-first score cards side by side. Card A has a clear winner. Card B has close top scores and is highlighted as more uncertain.
Technical visual: Put Card A and Card B as large text-first tablet cards. For mobile readability, the score text may wrap into stacked rows, but the exact values must stay clear: A shows cat 0.90, dog 0.07, car 0.03; B shows cat 0.42, dog 0.39, car 0.19. Do not use animal photos, car photos, icon rows, or separate tiny number rows in this frame. Optional simple confidence bars are allowed only if they do not reduce text size. Do not use a checkmark on A; B is the correct "more uncertain" answer.
Style/medium: warm modern educational illustration, high quality Instagram/WhatsApp story aesthetic, integrated quiz UI, not a generic quiz slide.
Composition/framing: 9:16 portrait. Main question at top as tablet/notebook heading. Two choice cards large in the middle. The A and B score values must be the dominant content on the tablet cards in large readable type, not on the notebook and not split into tiny separate icon rows.
Text to render verbatim, exactly:
"Quick check: which is more uncertain?"
"A:"
"cat 0.90"
"dog 0.07"
"car 0.03"
"B:"
"cat 0.42"
"dog 0.39"
"car 0.19"
"B has closer scores."
Constraints: B must be visibly more uncertain because top scores are close; highlight B as the answer; do not put a green checkmark on A; keep the A and B score rows large enough for phone viewing directly on the tablet cards; no animal/car icon rows; no extra text; no logos; no watermark; no generic caption panel.
```

## Acceptance Standard

The set can only be accepted if actual generated images show:

- self-contained opener
- native generated composition
- no pasted-overlay look
- integrated text plan
- mechanism visibility
- mobile readability
- recurring warm desk/tablet story style
- same learner character across one lesson
