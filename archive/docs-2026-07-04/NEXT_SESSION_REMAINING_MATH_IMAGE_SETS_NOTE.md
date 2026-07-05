# Next Session Note: Remaining Math Image Sets

Use this note as an index for the remaining planned image folders in the `How AI Uses Math` series.

Important: image-only concept-proof cards now come before video-first frames. See:

```text
HOW_AI_USES_MATH_IMAGE_ONLY_GAP_AUDIT.md
```

For parallel work, open one of the self-contained topic notes below in each new session:

```text
NEXT_SESSION_GRADIENT_DESCENT_IMAGE_SET_NOTE.md
NEXT_SESSION_GRAPHS_IMAGE_SET_NOTE.md
NEXT_SESSION_COORDINATES_IMAGE_SET_NOTE.md
NEXT_SESSION_LOGIC_IMAGE_SET_NOTE.md
```

## Goal

Create video-first source-frame image sets for the topics that are in the series plan but do not yet have generated image folders.

## Missing Image Folders

Generate these in the same style as the existing newer math lessons:

1. `Gradient Descent: How AI Learns From Mistakes`
2. `Graphs: How AI Understands Relationships`
3. `Coordinates: How AI Places Ideas In Space`
4. `Logic: How AI Makes Rule-Based Decisions`

## Required Style

Follow the series style decision in:

```text
HOW_AI_USES_MATH_STYLE_DECISION_NOTE.md
```

Use Direction B:

- realistic warm study-desk/tablet technical style
- recurring Indian teenage learner
- teal/green shirt
- wooden desk, lamp, notebook, books
- tablet overlays with readable diagrams, labels, numbers, arrows, and graphs
- clear technical mechanism first
- minimal text per frame
- no vague glowing AI visuals

Match these completed examples:

```text
assets/images/functions-how-ai-turns-input-into-output-video-first/
assets/images/statistics-how-ai-learns-patterns-from-data-video-first/
assets/images/linear-equations-how-ai-combines-signals-video-first/
assets/images/how-ai-uses-math-series-intro-video-first/
```

## Expected Output Folders

Use these folder names unless a better existing slug is already present:

```text
assets/images/gradient-descent-how-ai-learns-from-mistakes-video-first/
assets/images/graphs-how-ai-understands-relationships-video-first/
assets/images/coordinates-how-ai-places-ideas-in-space-video-first/
assets/images/logic-how-ai-makes-rule-based-decisions-video-first/
```

Also archive the prompt packs here:

```text
assets/image-prompts/gradient-descent-how-ai-learns-from-mistakes-video-first.md
assets/image-prompts/graphs-how-ai-understands-relationships-video-first.md
assets/image-prompts/coordinates-how-ai-places-ideas-in-space-video-first.md
assets/image-prompts/logic-how-ai-makes-rule-based-decisions-video-first.md
```

## Production Order

Generate in this order:

1. Gradient Descent
2. Graphs
3. Coordinates
4. Logic

Reason: Gradient Descent is the strongest next lesson because it follows `Linear Equations -> Derivatives -> Gradient Descent`. Graphs is already in the applied math backlog. Coordinates and Logic are optional plan episodes, so generate them after the required arc.

## Topic Mechanism Notes

### 1. Gradient Descent: How AI Learns From Mistakes

Core mechanism:

```text
prediction -> loss/error -> slope/gradient direction -> small update -> lower loss -> repeat
```

Suggested 8-frame sequence:

1. Model predicts, answer is wrong
2. Error/loss is measured
3. Loss curve appears on tablet
4. Slope shows which direction reduces error
5. Small step updates the weight
6. New prediction has lower error
7. Repeated steps move down the curve
8. Quick check: large step can overshoot, small steps learn steadily

### 2. Graphs: How AI Understands Relationships

Core mechanism:

```text
entities -> nodes -> relationships -> edges -> connected paths -> recommendation or answer
```

Suggested 8-frame sequence:

1. Many separate items look unrelated
2. Items become nodes
3. Relationships become edges
4. A small network forms
5. Nearby connected nodes reveal similar interests
6. A path explains a recommendation
7. Knowledge graph connects facts
8. Quick check: graphs are math for connected things

### 3. Coordinates: How AI Places Ideas In Space

Core mechanism:

```text
item -> numbers -> point in space -> distance -> similarity -> cluster
```

Suggested 8-frame sequence:

1. A real item or sentence needs a place in AI memory
2. The item becomes numbers
3. Numbers act like coordinates
4. Point appears on simple x/y space
5. Nearby points mean similar ideas
6. Far points mean different ideas
7. Clusters show groups of related meaning
8. Quick check: coordinates help AI organize ideas in space

### 4. Logic: How AI Makes Rule-Based Decisions

Core mechanism:

```text
condition -> true/false check -> branch -> next rule -> decision
```

Suggested 8-frame sequence:

1. AI system receives a request
2. First condition checks one fact
3. True path and false path split
4. Decision tree grows with simple branches
5. Rules filter unsafe or impossible options
6. Agent chooses next action based on conditions
7. Logic combines with learned scores
8. Quick check: logic helps AI follow rules, not just guess

## Generation Checklist

For each topic:

1. Create or confirm a source module in `modules/visual-ai-concepts/`.
2. Create the prompt pack in `assets/image-prompts/`.
3. Generate 8 source frames in the expected `assets/images/` folder.
4. Create a contact sheet named with the topic slug.
5. Add short review notes in the image folder.
6. Check text readability, math accuracy, and visual consistency against Direction B.
7. Update `PIPELINE_BOARD.md`, `HOW_AI_USES_MATH_SERIES_PLAN.md`, and `PROJECT_STATUS.md` if the production state changes.

## Important Constraint

Do not make these look like generic AI art. Each frame should visibly teach one mechanism step using diagrams that a Class 9-12 student can understand.
