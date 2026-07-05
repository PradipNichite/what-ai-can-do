# How AI Uses Math Series Plan

This is the working sequence for the dedicated "How AI Uses Math" micro-lesson series.

Series guide: `HOW_AI_USES_MATH_SERIES_GUIDE.md`
Lesson core template: `HOW_AI_USES_MATH_LESSON_CORE_TEMPLATE.md`
Review packet: `HOW_AI_USES_MATH_LESSON_REVIEW_PACKET.md`

## Series Intent

This series is not a motivation series and not a curiosity-first Shorts series.

The intent is:

- technically correct applied math understanding
- 11th/12th standard learner level
- familiar school concept first
- AI mechanism second
- one concrete example per episode
- visuals that show technical work, not only mood

## Approval Flow

Do this in batches:

1. Approve the series sequence.
2. Create or update the shared lesson core for each episode.
3. Approve the lesson-level technical brief for each episode.
4. Create renderer adaptation notes.
5. Create image prerequisite sheets.
6. Create image-only/self-contained prompt packs.
7. Generate image-only story cards and contact sheets.
8. Review image-only contact sheets as the concept proof.
9. Create video-first prompt packs only after the image-only concept works.
10. Generate video-first source images in batches.
11. Generate video clips only after video-source visual approval.

Do not generate images before the lesson brief and image prerequisites exist.

The shared lesson core is the source of truth. Renderer outputs should adapt it, not replace it.

Image-only comes before video-first by default. Video-first frames are an adaptation, not the first concept test.

## Recommended Sequence

### 0. Series Intro: How AI Uses Math

Purpose: set the map for the series.

School concept: many school math topics work together.

AI use: representation, comparison, prediction, uncertainty, and learning.

Mechanism focus: math gives AI ways to represent information as numbers, compare those numbers, score possible outputs, and improve from error.

Reason for position: this intro tells students what kind of series they are watching. It should be short and map-like, not motivational.

Status: visual draft.

Assets:

- source module: `modules/visual-ai-concepts/how-ai-uses-math-series-intro.source.md`
- prompt pack: `assets/image-prompts/how-ai-uses-math-series-intro-video-first.md`
- source frames: `assets/images/how-ai-uses-math-series-intro-video-first/`
- contact sheet: `assets/images/how-ai-uses-math-series-intro-video-first/how-ai-uses-math-intro-source-contact-sheet.jpg`

### 1. Matrices: How AI Sees Images as Numbers

School concept: rows, columns, grids.

AI use: images and numeric data.

Mechanism focus: image -> pixels -> brightness or RGB values -> matrix/grid -> pattern scan.

Reason for position: most concrete visual entry point. Students can see how an image becomes numbers.

Existing assets:

- source module: `modules/visual-ai-concepts/matrices-how-images-become-numbers.source.md`
- prompt pack: `assets/image-prompts/matrices-images-become-numbers-video-first.md`
- source frames: `assets/images/matrices-images-become-numbers-video-first/`
- rendered video: `outputs/video-renders/matrices-images-become-numbers-micro-lesson-v1-en.mp4`

Status: existing video draft.

### 2. Vectors: How AI Compares Meaning

School concept: list of numbers, direction, distance.

AI use: embeddings, semantic search, recommendations.

Mechanism focus: text/query -> embedding vector -> point in meaning space -> distance/angle comparison -> nearest result.

Reason for position: follows matrices naturally because both are numeric representations. Vectors introduce similarity.

Existing assets:

- source module: `modules/visual-ai-concepts/vectors-how-ai-compares-meaning.source.md`
- preferred prompt pack: `assets/image-prompts/vectors-how-ai-compares-meaning-video-first-v3.md`
- preferred source frames: `assets/images/vectors-how-ai-compares-meaning-video-first-v3/`
- preview video: `outputs/video-renders/vectors-how-ai-compares-meaning-micro-lesson-v3-en.mp4`

Status: preferred visual direction exists.

### 3. Functions: How AI Turns Input Into Output

School concept: function as input -> rule -> output.

AI use: AI model as a learned function.

Mechanism focus: input numbers -> model/function -> transformed numbers -> output scores.

Reason for position: bridges representation to prediction. After matrices and vectors show inputs as numbers, functions explain what the model does with those numbers.

Status: needs source module and images.

### 4. Probability: How AI Handles Uncertainty

School concept: chance, likelihood, values from 0 to 1 or 0% to 100%.

AI use: classification confidence, recommendations, next-token choices.

Mechanism focus: possible outputs -> probability scores -> highest score selected -> close scores mean uncertainty.

Reason for position: after functions produce output scores, probability explains how AI handles likely answers.

Existing assets:

- source module: `modules/visual-ai-concepts/probability-how-ai-handles-uncertainty.source.md`
- prompt pack: `assets/image-prompts/probability-how-ai-handles-uncertainty-video-first.md`
- source frames: `assets/images/probability-how-ai-handles-uncertainty-video-first/`

Status: visual draft with local preview.

Preview assets:

- local preview GIF: `assets/images/probability-how-ai-handles-uncertainty-video-first/probability-preview-animatic.gif`
- dense preview sheet: `assets/images/probability-how-ai-handles-uncertainty-video-first/probability-preview-dense-sheet.jpg`

### 5. Statistics: How AI Learns Patterns From Data

School concept: mean, spread, trends, examples.

AI use: learning from many data points.

Mechanism focus: many examples -> pattern estimate -> variation/noise -> better or biased predictions depending on data.

Reason for position: after single prediction and probability, move to many examples and patterns.

Status: visual draft.

Assets:

- source module: `modules/visual-ai-concepts/statistics-how-ai-learns-patterns-from-data.source.md`
- prompt pack: `assets/image-prompts/statistics-how-ai-learns-patterns-from-data-video-first.md`
- source frames: `assets/images/statistics-how-ai-learns-patterns-from-data-video-first/`
- contact sheet: `assets/images/statistics-how-ai-learns-patterns-from-data-video-first/statistics-video-first-source-contact-sheet.jpg`

### 6. Linear Equations: How AI Combines Signals

School concept: weighted sum, equation with variables.

AI use: simple model score, neuron-like weighted inputs.

Mechanism focus: features x weights -> weighted sum -> score.

Reason for position: gives a simple mechanism for how a model can combine inputs before introducing learning updates.

Status: visual draft.

Assets:

- source module: `modules/visual-ai-concepts/linear-equations-how-ai-combines-signals.source.md`
- prompt pack: `assets/image-prompts/linear-equations-how-ai-combines-signals-video-first.md`
- source frames: `assets/images/linear-equations-how-ai-combines-signals-video-first/`
- contact sheet: `assets/images/linear-equations-how-ai-combines-signals-video-first/linear-equations-video-first-source-contact-sheet.jpg`

### 7. Derivatives: How AI Knows Which Way To Improve

School concept: slope/rate of change at a point.

AI use: learning direction during training.

Mechanism focus: error curve -> tangent slope -> changing a weight changes error -> move opposite the slope.

Reason for position: derivative makes more sense after students know that a model makes scores and can be wrong.

Existing assets:

- source module: `modules/visual-ai-concepts/derivatives-how-ai-learns-from-mistakes.source.md`
- image set: `assets/images/derivatives-ai-learning-native-story/`
- rendered video: `outputs/video-renders/derivatives-ai-learning-micro-lesson-v1-en.mp4`

Status: existing video draft; refresh decision written.

Decision note:

- `assets/images/derivatives-ai-learning-native-story/derivatives-refresh-decision.md`

### 8. Gradient Descent: How AI Learns From Mistakes

School concept: repeated small steps using slope.

AI use: model training and loss reduction.

Mechanism focus: prediction -> loss -> gradient direction -> small step -> repeat until loss reduces.

Reason for position: uses derivatives repeatedly. Should come after derivatives, not before.

Status: needs source module and images.

### 9. Graphs: How AI Understands Relationships

School concept: nodes and edges.

AI use: recommendations, knowledge graphs, social networks, connected data.

Mechanism focus: entities become nodes, relationships become edges, nearby/connected nodes support suggestions.

Reason for position: separate branch of math representation. Can come earlier, but works well after the core prediction/learning arc.

Status: needs source module and images.

### 10. Coordinates: How AI Places Ideas In Space

School concept: points, axes, distance.

AI use: embedding spaces and clusters.

Mechanism focus: items become points; distance shows similarity; clusters show related groups.

Reason for position: optional reinforcement episode. It can either support vectors earlier or come later as a visual deepening.

Status: optional.

### 11. Logic: How AI Makes Rule-Based Decisions

School concept: true/false, conditions, if-then reasoning.

AI use: decision trees, filters, agents, safety rules.

Mechanism focus: condition checks route a decision path.

Reason for position: optional because it is less central to neural model training but useful for AI systems and agents.

Status: optional.

## Recommended First Production Batch

Batch A should include:

1. Series Intro
2. Functions
3. Probability refinement if needed
4. Statistics

Why this batch:

- matrices already exists
- vectors preferred direction already exists
- functions is the missing bridge
- probability already has images and can be reviewed/refined
- statistics naturally follows probability

## Existing Lessons And Placement

The derivative video remains part of this series, but it should be presented later in the sequence.

Reason:

- derivatives explain improvement direction
- improvement direction needs prior ideas: model output, prediction error, loss/probability/score
- after functions and probability, derivatives feel useful instead of isolated

If reusing the current derivative video, label it as an existing draft. If making the series visually consistent, create a refreshed video-first image set before final publication.

## Approval Needed Before Image Generation

Approve or edit:

- `HOW_AI_USES_MATH_LESSON_REVIEW_PACKET.md`
- episode sequence
- episode titles
- included/optional topics
- whether derivative should be reused as-is or refreshed
- whether Batch A should start with intro + functions + statistics
- shared lesson core for each selected episode
- renderer priority, with image-only first as the default

After approval, generate image prerequisites and image-only prompt packs in bulk for the selected batch.
