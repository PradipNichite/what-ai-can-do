# Statistics: How AI Learns Patterns From Data - Image Story Prompt Pack

Series: How AI Uses Math
Source module: `modules/visual-ai-concepts/statistics-how-ai-learns-patterns-from-data.source.md`
Output image folder: `assets/images/statistics-how-ai-learns-patterns-from-data-image-story/`
Renderer: image-only/self-contained 9:16 story cards

## Goal

Create a paused visual story that explains how AI uses statistics to learn patterns from many examples without voiceover, animation, or external captions.

Self-contained opener requirement:

The first card must name the lesson topic, state what the learner will understand, connect the school concept of statistics to AI model training, and introduce the concrete study-hours/score example used by the rest of the story.

Native generated composition requirement:

Use image generation to create the full educational composition. The card should feel like one complete designed educational poster, where illustration, diagram, and text are generated together, not a separate caption pasted on top. Text should be part of the scene through tablet UI, notebook panels, poster typography, sticky notes, arrows, labels, callout bubbles, and mini cards. Avoid a pasted overlay look.

Core mechanism:

```text
many examples -> measurements/features -> pattern estimate -> prediction rule -> check on new example
```

Memory anchor:

```text
AI learns patterns from many examples, not from one example.
```

## Character / Style Bible

- realistic warm study-desk/tablet technical style
- 9:16 vertical mobile frame
- recurring Indian 11th/12th standard learner with dark wavy hair and teal/green shirt
- wooden study desk, warm desk lamp, notebook, pen, books, small plant
- tablet as the main technical surface
- large readable technical overlays: data table, scatterplot, trend line, spread/noise, new example, prediction line, balanced vs narrow data
- integrated generated headline/callout text on each card, not external captions or pasted overlay text
- no dense formulas, no generic glowing AI art, no flat PPT slide, no logos, no watermark

## Image-Only Story Cards

### Card 1 - Lesson Opener

Teaching job: introduce statistics, AI training, and the study-hours/score example in one self-contained card.

Text to embed:

```text
Statistics: How AI Learns Patterns From Data
AI learns from many examples.
Example: study hours -> test score
```

Prompt:

```text
Use case: scientific-educational
Asset type: 9:16 self-contained carousel card
Primary request: Create card 1 for "Statistics: How AI Learns Patterns From Data". Make it a self-contained opener for Indian 11th/12th standard students: title the lesson, show that school statistics helps AI training, and introduce the concrete study-hours-to-test-score example used by the rest of the story.
Scene/backdrop: warm Indian study room with wooden desk, lamp, notebook, books, small plant, and a tablet.
Subject: recurring Indian high-school learner with dark wavy hair and teal/green shirt, looking at a tablet with curiosity.
Technical visual: tablet shows several small student example cards flowing into a simple data table and scatterplot preview.
Style/medium: realistic warm study-desk/tablet technical style, high quality mobile educational story card, native poster typography mixed with crisp tablet UI.
Composition/framing: tablet large in foreground; learner visible behind it; title as native poster typography or notebook header; learning promise as a sticky note; concrete example on the tablet.
Text (verbatim): "Statistics: How AI Learns Patterns From Data", "AI learns from many examples.", "Example: study hours -> test score".
Constraints: opener must explain the school concept to AI use; text must be native to tablet/notebook/sticky-note surfaces; keep text large and readable; no extra text; no logos; no watermark.
```

### Card 2 - Many Examples

Teaching job: show that AI training starts from many examples, not one example.

Text to embed:

```text
One example is not enough.
Many examples reveal a pattern.
```

Prompt:

```text
Use case: scientific-educational
Asset type: 9:16 self-contained carousel card
Primary request: Create card 2 showing why many examples are needed before AI can learn a pattern.
Scene/backdrop: same warm Indian study desk and learner.
Technical overlay: tablet shows one lonely example card on the left dimmed, and a larger group of five example cards on the right highlighted. Each group flows toward a small pattern icon, but only the many-example side forms a clear line.
Text (verbatim): "One example is not enough.", "Many examples reveal a pattern.".
Constraints: make the contrast between one example and many examples obvious; do not imply more data is always good regardless of quality; keep text large; no dense formulas; no extra text.
```

### Card 3 - Data Table

Teaching job: convert the concrete examples into measurements/features.

Text to embed:

```text
Examples become numbers.
hours
score
1 -> 45
2 -> 52
3 -> 61
4 -> 68
5 -> 76
```

Prompt:

```text
Use case: scientific-educational
Asset type: 9:16 self-contained carousel card
Primary request: Create card 3 showing the study-hours examples becoming a clean data table.
Scene/backdrop: same learner at the warm desk, pencil near notebook.
Technical overlay: tablet shows a simple two-column table with headers "hours" and "score", using the exact rows 1 -> 45, 2 -> 52, 3 -> 61, 4 -> 68, 5 -> 76. A few small example cards transform into table rows.
Text (verbatim): "Examples become numbers.", "hours", "score", "1 -> 45", "2 -> 52", "3 -> 61", "4 -> 68", "5 -> 76".
Constraints: table must be readable on mobile; no extra rows; no formulas; no extra text; preserve all numbers exactly.
```

### Card 4 - Points On A Plot

Teaching job: show that examples can be plotted as data points.

Text to embed:

```text
Each example becomes a point.
hours
score
```

Prompt:

```text
Use case: scientific-educational
Asset type: 9:16 self-contained carousel card
Primary request: Create card 4 showing the table rows becoming points on a scatterplot.
Scene/backdrop: same warm Indian study desk and learner.
Technical overlay: tablet shows the same five rows sliding into a scatterplot. The x-axis cue is labeled "hours" and the y-axis cue is labeled "score". Five dots rise from lower-left to upper-right, matching the 1 to 5 hour trend.
Text (verbatim): "Each example becomes a point.", "hours", "score".
Constraints: axes must be simple and readable; dots should clearly trend upward but not sit on a perfect rigid line; no dense axis numbers; no extra text.
```

### Card 5 - Trend Line

Teaching job: show that the model estimates a pattern through many points.

Text to embed:

```text
The model estimates a pattern.
trend line
not memorizing one point
```

Prompt:

```text
Use case: scientific-educational
Asset type: 9:16 self-contained carousel card
Primary request: Create card 5 showing a trend line estimated through the cloud of study-hours and score points.
Scene/backdrop: same learner at the desk, tablet centered.
Technical overlay: tablet shows the five scatterplot points and a clean upward trend line passing through the middle of the point cloud. One individual point should not be singled out as the rule.
Text (verbatim): "The model estimates a pattern.", "trend line", "not memorizing one point".
Constraints: show a real pattern estimate, not a decorative diagonal; line should pass through the data cloud; no equation; no extra text.
```

### Card 6 - Variation Around Pattern

Teaching job: show that real examples vary around the trend, so a trend is not a guarantee.

Text to embed:

```text
Real data has variation.
near the line
not exact
```

Prompt:

```text
Use case: scientific-educational
Asset type: 9:16 self-contained carousel card
Primary request: Create card 6 showing points scattered around the trend line so learners see variation/noise.
Scene/backdrop: same warm study desk and learner.
Technical overlay: tablet shows the trend line with several points close to it and a couple of points visibly above or below it. Use soft highlight rings around off-line points.
Text (verbatim): "Real data has variation.", "near the line", "not exact".
Constraints: do not make all points sit perfectly on the line; do not imply the trend guarantees every individual score; keep diagram sparse and readable; no extra text.
```

### Card 7 - Predict A New Example

Teaching job: show how the learned pattern guides a prediction for a new input.

Text to embed:

```text
New example:
4.5 hours
predicted score: about 72
```

Prompt:

```text
Use case: scientific-educational
Asset type: 9:16 self-contained carousel card
Primary request: Create card 7 showing a new study-hours example mapped to a predicted score using the trend line.
Scene/backdrop: same learner at the warm desk, watching the tablet.
Technical overlay: tablet shows the existing scatterplot and trend line. Add a new highlighted point or vertical guide at 4.5 hours, projecting to the trend line and then across to predicted score about 72.
Text (verbatim): "New example:", "4.5 hours", "predicted score: about 72".
Constraints: make it clear this is an estimate, not a guaranteed exact score; keep projection line readable; no extra formulas; no extra text.
```

### Card 8 - Quick Check

Teaching job: test that the learner understands data quality and biased/narrow data risk.

Text to embed:

```text
Quick check: which data is safer?
A: one narrow group
B: many varied examples
B is safer for learning a general pattern.
```

Prompt:

```text
Use case: scientific-educational
Asset type: 9:16 self-contained carousel card
Primary request: Create card 8 as a quick check about data quality for AI learning.
Scene/backdrop: same learner at desk with tablet and notebook.
Technical overlay: tablet shows two side-by-side dataset cards. A shows a tight narrow cluster from one type of student. B shows many varied points across the range. B is highlighted as the safer choice for learning a general pattern.
Text (verbatim): "Quick check: which data is safer?", "A: one narrow group", "B: many varied examples", "B is safer for learning a general pattern.".
Constraints: make B visibly more varied and representative; do not imply more data is always better if poor quality; no scary warning symbols; no extra text; no logos; no watermark.
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
- visible technical chain from examples to numbers to points to trend line to prediction
