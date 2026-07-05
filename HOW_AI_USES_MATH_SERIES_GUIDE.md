# How AI Uses Math Series Guide

This guide is for the dedicated math-in-AI series inside "What AI Can Do".

Related planning docs:

- `HOW_AI_USES_MATH_SERIES_PLAN.md`
- `HOW_AI_USES_MATH_IMAGE_PREREQUISITES.md`
- `HOW_AI_USES_MATH_LESSON_CORE_TEMPLATE.md`

The intent of this series is technical applied understanding:

```text
Students already study the math. The lesson shows how that math is used inside AI.
```

This is different from a motivation series, curiosity series, or hook-first Shorts series. Those can exist separately, but this series should optimize for correctness, clarity, and mechanism.

## Audience

Primary learner:

- 11th/12th standard or high-school students
- already familiar with the school math topic
- may know formulas or textbook definitions
- does not yet know where the concept appears in AI

Assume the learner can follow simple numbers, graphs, coordinates, functions, vectors, matrices, and probability ideas, but do not assume college-level machine learning.

## Series Promise

Each episode should answer:

```text
Where does this school math concept appear in AI, and what job does it do there?
```

The lesson should not only say that a topic is "important for AI". It should show the role of the concept in a real AI mechanism.

## Single Lesson Core, Many Renderers

Each episode should have one stable lesson core before any renderer-specific work starts.

The lesson core contains:

- school concept
- AI use
- mechanism
- mini example
- memory anchor
- quick check
- renderer-agnostic scene flow

Then create separate renderer adaptations from that same core:

- image-only post or carousel
- micro-lesson video
- classroom presentation
- interactive demo
- local-language version

This keeps future improvements small. If the concept or example changes, update the lesson core first, then refresh the affected renderers.

Do not let video-specific details become the source of truth. A Runway prompt, image frame, or voiceover line may adapt the lesson, but it should not redefine the lesson.

Use `HOW_AI_USES_MATH_LESSON_CORE_TEMPLATE.md` for new episodes.

## Image-Only First Rule

For this series, create the image-only/self-contained visual story before video-first source frames.

Reason:

- Image-only cards prove whether the concept is understandable without voiceover, motion, or captions.
- Image-only cards must feel like a lesson, not a random slideshow. The sequence has to introduce its own topic, purpose, and example inside the cards.
- Image-only cards must be generated as complete native educational compositions. The text should be designed into the image, not pasted on top as a generic overlay.
- Video-first frames are intentionally sparse, so they can hide weak teaching ideas until animation is attempted.
- A strong image-only sequence can be simplified into video-first frames later.

Default renderer order:

```text
lesson core -> scene adequacy gate -> image-only visual story -> image-only QA -> video-first source frames -> image-to-video
```

Only skip the image-only pass when the user explicitly asks for a video-only experiment.

## Scene Adequacy Before Prompts

Do not treat image prompts as the beginning of the lesson design process. Before renderer-specific prompt writing, the lesson must prove that its scenes are adequate for the technical idea.

The scene adequacy review checks:

- whether the selected number of scenes is enough for the mechanism
- whether each scene has a single learning job
- whether the chain shows the missing causal bridges
- whether the mini example remains concrete instead of becoming generic
- whether the learner can explain what changed and why the next step follows
- whether the scene sequence creates a false sense of completion

For a difficult or newly created topic, run:

```powershell
python tools/openai_scene_adequacy.py `
  --source-module modules/visual-ai-concepts/<lesson>.source.md `
  --prompt-pack assets/image-prompts/<lesson>-image-story.md `
  --renderer image-story `
  --out assets/reviews/<lesson>-scene-adequacy.md `
  --json-out assets/reviews/<lesson>-scene-adequacy.json
```

If this returns `needs-revision`, change the lesson core or scene flow first. Prompt edits and regeneration should come after the missing scene or causal bridge is fixed.

## Intent Before Format

Choose the video style from the intent.

For this series, the intent is:

- applied math understanding
- technically correct explanation
- visible mechanism
- one small example the learner can reason through
- retention of the concept-to-AI connection

This means:

- use micro-lessons by default
- avoid social-media hook language
- avoid motivational framing as the main point
- avoid curiosity-only openings that do not teach
- use calm teaching voice and clear visual progression

Other series may have different intent:

- motivation: why math matters for future careers
- curiosity: surprising facts about AI
- awareness: one quick idea for broad audiences
- practical use: how to use AI tools in daily work

Do not mix those intents into this series unless the episode explicitly asks for that treatment.

## Required Episode Fields

Every topic in this series must define:

- `school_concept`: the familiar school math idea
- `ai_use`: where the idea appears in AI
- `mechanism`: what the concept does in the AI system
- `mini_example`: one simple technically correct example
- `visual_sequence`: how the mechanism will be shown on screen
- `memory_anchor`: one accurate sentence to remember
- `quick_check`: one question that tests understanding
- `renderer_adaptation_notes`: what changes across video, image-only, presentation, and interactive versions

Example:

```text
Topic: Vectors: how AI compares meaning
School concept: vector as a list of numbers with direction and distance
AI use: embeddings for search and recommendations
Mechanism: text is converted into vectors; similar meanings are close or point in similar directions
Mini example: "cheap phone" and "budget mobile" get nearby vectors
Memory anchor: Similar meaning means nearby vectors.
```

## Preferred Episode Structure

Use 6-8 compact scenes:

1. Learning objective: school concept -> AI use
2. Familiar school version
3. Concrete AI example
4. Numeric or visual representation
5. Mechanism: transformation, comparison, scoring, or update
6. Where AI uses it
7. Memory anchor
8. Quick check or recap

The first scene can create curiosity, but its main job is to orient the learner.

Self-contained opening requirement:

- The first scene/card must include the lesson title or clear topic name.
- It must say what the student will learn, not only show an object or diagram.
- It must connect the school concept to the AI use in plain language.
- It must introduce the concrete example if the rest of the lesson depends on one.
- A viewer who sees only the first card should know why the next cards exist.
- The opener must be composed like a native lesson card, using generated poster typography, tablet/notebook UI, callouts, arrows, or sticky-note elements. Avoid text that looks pasted onto an unrelated image.

Preferred opening:

```text
In this lesson, you will see how <school concept> is used in AI to <AI use>.
```

Avoid:

```text
AI can do something amazing...
You won't believe how AI...
Here is the secret behind AI...
```

## Technical Accuracy Rules

For every episode:

- use simple explanations, but do not make false statements
- distinguish analogy from mechanism
- include one real mechanism step, not only a metaphor
- use small numbers where they help understanding
- avoid saying AI "understands" unless the mechanism is shown as representation, comparison, scoring, or prediction
- avoid implying one math concept explains the whole AI system
- avoid formulas unless they serve the learning goal

Good:

```text
The model does not store the word meaning directly. It stores numbers that place related meanings near each other in vector space.
```

Weak:

```text
AI understands words just like humans do.
```

## Visual Rules

Use the established warm student/tablet style from the matrices and vectors lessons, but do not let style replace teaching value.

Each frame must show one technical job:

- transformation: image -> pixels -> numbers
- comparison: vectors close vs far
- scoring: class probabilities or output scores
- representation: input becomes a vector, grid, graph, or feature list
- optimization: error measured, slope found, small update made

Avoid frames whose only teaching value is:

- student looking at a glowing tablet
- generic AI icons
- decorative formulas
- beautiful but vague charts
- labels that explain the concept while the image itself does not
- large generic text pasted over an otherwise unrelated background

Native image-story text rule:

- Generate the full card with ChatGPT/image generation as one designed image.
- Text should appear as part of the educational scene: notebook writing, tablet interface, diagram labels, speech bubbles, sticky notes, poster typography, arrows, or mini-cards.
- Do not use post-production overlays as the main teaching layer unless the task explicitly calls for manual graphic design.
- Reject cards where the text could be removed and the image would become an unrelated stock-style scene.

Each frame should answer:

```text
If the video paused here, what technical step is visible?
```

## Topic Map

Recommended sequence:

| Order | Topic | School Concept | AI Use | Mechanism Focus |
|---|---|---|---|---|
| 0 | Series Intro | math topics as a toolkit | representation, prediction, learning | map the series |
| 1 | Matrices | rows, columns, grids | images and data batches | pixels become number grids |
| 2 | Vectors | lists, direction, distance | embeddings and search | meaning becomes nearby vectors |
| 3 | Functions | input -> rule -> output | models | inputs become output scores |
| 4 | Probability | chance, likelihood | prediction confidence | outcomes receive probability scores |
| 5 | Statistics | mean, spread, trends | learning from data | patterns are estimated from examples |
| 6 | Linear Equations | variables and weighted sums | scoring from features | features times weights become a score |
| 7 | Derivatives | slope/rate of change | learning direction | slope tells update direction |
| 8 | Gradient Descent | repeated small steps | model training | reduce loss step by step |
| 9 | Graphs | nodes and edges | relationships | connected data supports recommendations |
| 10 | Coordinates | points and distance | embedding maps | distance represents similarity |
| 11 | Logic | true/false conditions | decision rules | conditions route decisions |

Use `HOW_AI_USES_MATH_SERIES_PLAN.md` as the source of truth for current ordering, status, and batch planning.

## Readiness Gates

Do not call a topic ready for review unless it has the appropriate artifact for that stage.

For source review:

- lesson core exists or source module follows the lesson-core structure
- source module exists
- school concept, AI use, mechanism, mini example are written
- renderer adaptation notes exist if the topic will be reused across formats
- scene adequacy has been checked for new or technically difficult lessons

For visual review:

- image prerequisites exist
- scene adequacy passed or the exception is documented
- image-only prompt pack exists
- image-only story cards exist
- image-only contact sheet exists
- the first card or opening scene self-identifies the lesson and explains the school concept -> AI use promise
- text is integrated into the generated image composition, not pasted on as a generic caption overlay
- the cards make sense without voiceover, motion, or external captions
- each frame has a technical teaching job

For video review:

- approved image-only concept exists, or a deliberate exception is documented
- video-first prompt pack exists
- video-first source images exist
- preview or final render exists
- verification contact sheet exists
- motion or animatic has been checked for teaching value

Prompt packs alone are not visual drafts. Video-first images alone are not concept proof. Image-only cards prove the teaching idea; video clips prove the motion adaptation.

## Voice And Captions

Voice:

- calm Indian-English educator tone
- direct and precise
- no hype
- no dramatic punchline dependency

Captions:

- sparse
- use for key terms, memory anchor, or quick check
- do not repeat every spoken sentence

## Episode Quality Checklist

Before moving forward, check:

- Does the episode start from the school concept?
- Does it show the AI application clearly?
- Is the mechanism visible, not just narrated?
- Is the mini example technically correct?
- Would an 11th/12th student learn where this math is used?
- Are we avoiding motivational or curiosity-series language?
- Do the visuals match the existing series style?
- Do the visuals carry technical knowledge, not only mood?
