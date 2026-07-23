# How AI Uses Math Image Prerequisites

This checklist must be completed before generating images for any "How AI Uses Math" micro-lesson.

Image generation should not start from only a title. It should start from an approved lesson brief and a visible technical sequence.

The approved lesson core is the source of truth. Image prompts are renderer-specific adaptations.

## Required Inputs Before Images

Each episode needs:

- approved shared lesson core or source module
- approved title
- `school_concept`
- `ai_use`
- `mechanism`
- `mini_example`
- `memory_anchor`
- `quick_check`
- 6-8 scene flow
- technical teaching table
- visual continuity notes
- image prompt pack path
- output image folder path

## Scene Adequacy Gate

Before writing or approving image prompts, review whether the scene flow itself is enough to teach the concept.

This gate exists because image generation starts too late in the process. A polished set of cards can still fail if the selected scenes skip a causal bridge, hide the real mechanism, or create a false sense that the learner understood something technical.

The scene flow must answer:

- Is 6-8 scenes enough for this specific concept, or should the lesson add, merge, split, or reorder scenes?
- Does each scene have one technical learning job?
- Can the learner identify what is represented, computed, compared, scored, or updated?
- Does the sequence include the causal bridge from one step to the next?
- Does the mini example stay concrete across the sequence?
- Are the school concept, AI use, mechanism, memory anchor, and quick check all supported by scenes?
- Would the scene still teach if it were only a rough sketch, before style and image quality?
- Cold-student test: after each scene, can a learner with no project context say what object is being shown, what changed, why it changed, and why the next scene follows?

Reject or revise the scene flow when it has the right vocabulary but still reads like disconnected slides. Visual style, animation, smooth voiceover, and API assembly do not compensate for missing causal explanation.

If the scene flow fails this gate, revise the source module or scene table before changing image prompts.

Only a clean scene adequacy `pass` can unlock image prompts or video-first frames. Treat `pass-with-caveats` as a false pass: convert every caveat into a scene-level repair, revise the lesson core or scene table, and rerun the adequacy review before generation. A caveat about lesson comprehension, causal flow, or concrete mechanism is not documentation debt; it is the next work item.

Use the structured checker when a lesson is new, technically difficult, or has produced shallow visuals:

```powershell
python tools/openai_scene_adequacy.py `
  --source-module modules/visual-ai-concepts/<lesson>.source.md `
  --prompt-pack assets/image-prompts/<lesson>-image-story.md `
  --renderer image-story `
  --out assets/reviews/<lesson>-scene-adequacy.md `
  --json-out assets/reviews/<lesson>-scene-adequacy.json
```

## Renderer Separation

Before images, decide what image set is being generated:

- video-first source frames
- image-only post/carousel frames
- classroom slide visuals
- interactive demo assets

Do not reuse one image set for every renderer by default.

Video-first images should:

- have fewer words
- give the video model a clear motion target
- preserve safe margins
- rely on voiceover for some explanation

Image-only posts should:

- work without narration
- include enough embedded text to explain the step
- preserve readable labels and arrows
- feel complete when swiped or viewed as a carousel

Both must come from the same lesson core.

## Technical Teaching Table Template

Use this table before writing image prompts:

| # | Scene | Learning job | Visible evidence | Transformation / comparison | Motion role | Risk |
|---|---|---|---|---|---|
| 1 | Learning objective | school concept connects to AI use | notebook/tablet bridge shows both | school idea -> AI use | concept bridge lights up | too generic |
| 2 | Familiar school concept | learner recognizes textbook idea | simple graph/grid/vector/equation | known math shown cleanly | notebook marks highlight | too formula-heavy |
| 3 | AI example | concept appears in real AI task | image/text/recommendation/prediction example | real input enters AI surface | input moves to tablet | looks like generic app |
| 4 | Numeric representation | real-world input becomes numbers | vector chips/matrix grid/features/scores | input -> numbers | chips/grid appear | numbers unreadable |
| 5 | Mechanism | math does its job | compare, score, transform, or update shown | core mechanism visible | arrows/bars/points move | only labels explain it |
| 6 | AI use | connect mechanism to application | search/classification/training/recommendation panel | mechanism -> result | result highlights | application too broad |
| 7 | Memory anchor | one sentence becomes memorable | recap chain or diagram | earlier steps connect | nodes light in order | decorative recap |
| 8 | Quick check | learner tests understanding | two options or small question | compare two cases | correct case pulses | too much text |

## Image Prompt Prerequisites

Before generating any frame, confirm:

- The frame has one clear learning job.
- The technical element is large enough to read on mobile.
- The image would still make sense if paused.
- The frame matches the established warm student/tablet style unless intentionally exempted.
- The prompt describes the exact technical object, not only the mood.
- The prompt avoids dense labels, tiny formulas, and decorative charts.
- The motion target is clear for later image-to-video.

## Default Visual Continuity

Use the existing visual world:

- warm modern Indian educational illustration
- Indian teenage learner
- teal/green shirt
- wooden study desk
- warm desk lamp
- notebook, pen, books, small plant
- tablet as the main technical surface
- overlays for grids, vectors, graphs, bars, arrows, dots, paths, and scores

The learner can appear in every frame, but the tablet/technical overlay must carry the teaching.

## Technical Elements By Topic

### Series Intro

Must show:

- math notebook and tablet connected
- matrix grid
- vector dots
- function box
- probability bars
- error curve/slope

Avoid:

- generic "math is everywhere" poster
- motivational-only scene

### Matrices

Must show:

- image/photo
- pixel zoom
- grid of values
- rows and columns
- RGB or grayscale values
- scan/pattern detection

Avoid:

- matrix as decorative numbers only

### Vectors

Must show:

- phrase/query
- vector number chips
- point or arrow in space
- near vs far comparison
- distance or angle cue
- nearest result/recommendation

Avoid:

- only icons connected by glowing lines

### Functions

Must show:

- familiar `input -> rule -> output`
- AI version: input numbers -> model/function -> output scores
- one concrete input example
- intermediate transformation through layers or steps
- output score table or bars

Avoid:

- black-box box with no visible numeric transformation

### Probability

Must show:

- possible outcomes
- probabilities from 0 to 1 or percentages
- scores that sum to 1 when shown as a set
- highest probability selected
- close scores showing uncertainty

Avoid:

- single answer that looks guaranteed

### Statistics

Must show:

- many examples/data points
- mean or trend line
- spread/variation
- pattern learned from examples
- biased or incomplete data risk if included

Avoid:

- generic bar chart without a learning mechanism

### Linear Equations

Must show:

- features
- weights
- weighted sum
- score
- changing one weight changes the result

Avoid:

- equation-only frame with no AI task

### Derivatives

Must show:

- error curve
- point on curve
- tangent slope
- tiny change in weight/input
- change in error/output
- opposite-direction update

Avoid:

- formal calculus rules as the main visual

### Gradient Descent

Must show:

- loss/error surface or curve
- current point
- gradient/slope direction
- step opposite the gradient
- repeated smaller loss values
- before/after loss comparison

Avoid:

- vague downhill walking analogy without loss/gradient labels

### Graphs

Must show:

- nodes
- edges
- labels or icons for entities
- path or neighborhood
- recommendation/relationship result

Avoid:

- network as decorative background only

## Batch Workflow

For each approved batch:

1. Create or update all source modules.
2. Create prerequisite tables for each episode.
3. Create prompt packs for each episode.
4. Generate source images.
5. Build contact sheets.
6. Write review notes.
7. Only then mark as `visual-draft`.

## Visual Draft Definition

An episode is `visual-draft` only when:

- generated images exist
- source contact sheet exists
- review notes exist
- every frame has a visible technical purpose

Prompt packs without images are `prompt-pack`, not `visual-draft`.
