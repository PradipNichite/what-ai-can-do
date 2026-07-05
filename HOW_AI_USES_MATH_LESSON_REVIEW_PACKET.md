# How AI Uses Math Lesson Review Packet

This packet is for reviewing the whole series in one pass before creating or refreshing images.

Series guide: `HOW_AI_USES_MATH_SERIES_GUIDE.md`
Series plan: `HOW_AI_USES_MATH_SERIES_PLAN.md`
Lesson core template: `HOW_AI_USES_MATH_LESSON_CORE_TEMPLATE.md`
Image prerequisites: `HOW_AI_USES_MATH_IMAGE_PREREQUISITES.md`

## Review Goal

Approve or edit:

- episode sequence
- lesson titles
- technical mechanism for each topic
- mini examples
- visual teaching direction
- renderer priority
- whether existing videos/images should be reused or refreshed

After approval, create individual lesson-core files and image prerequisite sheets in bulk.

## Series Learning Arc

The recommended arc is:

```text
represent information -> compare information -> transform input to output -> handle uncertainty -> learn patterns -> combine signals -> improve from error -> model relationships
```

This keeps the early lessons concrete, then moves toward learning and training.

## Episode 0: Series Intro - How AI Uses Math

Status: planned

One-line learning promise: Students will see the map of how school math appears inside AI systems.

School concept: math topics as a connected toolkit, not isolated chapters.

AI use: representing data, comparing items, making predictions, handling uncertainty, learning from mistakes.

Mechanism:

```text
real-world input -> numbers/structures -> comparison/scoring/update -> AI output
```

Mini example:

```text
photo -> matrix
sentence -> vector
input -> function -> output score
wrong prediction -> error curve -> update direction
```

Memory anchor: AI uses math to represent, compare, predict, and learn.

Misunderstandings to avoid:

- Do not claim one formula explains all AI.
- Do not make the intro motivational only.
- Do not overload the intro with every technical detail.

Renderer-agnostic scene flow:

| Step | Teaching job | Core visual idea | Technical truth |
|---|---|---|---|
| 1 | Set series purpose | student opens math notebook beside tablet | same school math can appear in AI |
| 2 | Representation | image breaks into matrix grid | images can be represented as pixel values |
| 3 | Similarity | words become vector dots | embeddings support similarity comparison |
| 4 | Prediction | function box maps input to output score | models transform inputs into outputs |
| 5 | Uncertainty | probability bars show possible answers | many outputs are scored by likelihood |
| 6 | Learning | error curve and slope appear | training reduces error using direction information |
| 7 | Series map | four words: represent, compare, predict, learn | these are recurring math jobs in AI |

Video notes: make it map-like, 30-45 seconds, no hype.

Image-only notes: can become a carousel cover plus map card.

Image prerequisites: must show multiple math mechanisms, not a generic "math is useful" poster.

Approval notes: decide whether this intro is produced before the next concept lesson.

## Episode 1: Matrices - How AI Sees Images as Numbers

Status: existing video draft

Existing assets:

- `modules/visual-ai-concepts/matrices-how-images-become-numbers.source.md`
- `assets/image-prompts/matrices-images-become-numbers-video-first.md`
- `assets/images/matrices-images-become-numbers-video-first/`
- `outputs/video-renders/matrices-images-become-numbers-micro-lesson-v1-en.mp4`

One-line learning promise: Students will understand that an image can be represented as a grid of numbers.

School concept: matrix as rows and columns.

AI use: image input, pixel data, computer vision.

Mechanism:

```text
photo -> pixels -> brightness/RGB numbers -> matrix/grid -> pattern scan
```

Mini example:

```text
Small grayscale patch:
[[20, 22, 25],
 [80, 85, 88],
 [200, 205, 210]]
```

The numbers represent pixel brightness. Similar number patterns can form edges, shapes, or regions.

Memory anchor: An image is a grid of numbers.

Misunderstandings to avoid:

- AI does not see images like human eyes.
- A matrix is not only a textbook table; it can store real pixel values.
- One matrix can represent grayscale; color usually needs multiple channels.

Renderer-agnostic scene flow:

| Step | Teaching job | Core visual idea | Technical truth |
|---|---|---|---|
| 1 | Learning objective | photo beside matrix grid | images can become matrices |
| 2 | Familiar concept | notebook shows rows and columns | matrices organize values by position |
| 3 | AI example | tablet shows photo recognition | AI image systems use pixel data |
| 4 | Representation | zoom into pixels | a digital image is made of pixels |
| 5 | Mechanism | pixel brightness becomes numbers | pixel values can be numeric |
| 6 | Color | RGB layers appear | color images often use channels |
| 7 | Application | scan line detects edge/shape pattern | models look for patterns in grids |
| 8 | Quick check | small grid asks bright/dark region | higher value usually means brighter in grayscale |

Video notes: existing video can stay as series episode draft.

Image-only notes: needs slightly more embedded labels than video version.

Image prerequisites: existing images already show core mechanism; review only if refreshing style/clarity.

Approval notes: approve existing draft or request v2 refresh.

## Episode 2: Vectors - How AI Compares Meaning

Status: preferred visual direction exists

Existing assets:

- `modules/visual-ai-concepts/vectors-how-ai-compares-meaning.source.md`
- `assets/image-prompts/vectors-how-ai-compares-meaning-video-first-v3.md`
- `assets/images/vectors-how-ai-compares-meaning-video-first-v3/`
- `outputs/video-renders/vectors-how-ai-compares-meaning-micro-lesson-v3-en.mp4`

One-line learning promise: Students will understand that AI can compare meaning by converting items into vectors and comparing distance or direction.

School concept: vector as a list of numbers with magnitude, direction, and distance.

AI use: embeddings, semantic search, recommendations.

Mechanism:

```text
text/query/item -> embedding vector -> point or arrow in vector space -> similarity comparison -> nearest result
```

Mini example:

```text
"cheap phone" -> [0.80, -0.10, 0.55]
"budget mobile" -> [0.78, -0.08, 0.52]
"banana recipe" -> [-0.30, 0.91, 0.12]
```

The first two vectors are closer, so the meanings are treated as more related.

Memory anchor: Similar meaning means nearby vectors.

Misunderstandings to avoid:

- AI is not matching only exact words.
- A vector dimension is not always a human-readable feature.
- Nearby vectors mean model-estimated similarity, not guaranteed truth.

Renderer-agnostic scene flow:

| Step | Teaching job | Core visual idea | Technical truth |
|---|---|---|---|
| 1 | Learning objective | two different phrases connect to similar vectors | meaning can be compared numerically |
| 2 | Familiar concept | vector arrow/list in notebook | vectors can be lists or directions |
| 3 | AI example | semantic search query on tablet | search can use meaning similarity |
| 4 | Representation | sentence becomes vector chips | embeddings represent text with numbers |
| 5 | Mechanism | points show near vs far | distance/angle can compare vectors |
| 6 | Application | nearest result is selected | retrieval uses nearby vectors |
| 7 | Recommendation | related lesson/product card glows | recommendations can use similarity |
| 8 | Quick check | car/vehicle vs car/banana | related meanings should be closer |

Video notes: v3 is preferred because it shows vector chips, distance, angle, and ranking.

Image-only notes: include labels for "near", "far", "similar" if needed.

Image prerequisites: existing v3 images likely pass; review the actual contact sheet with ChatGPT vision before final video.

Approval notes: approve v3 direction or request final polish.

## Episode 3: Functions - How AI Turns Input Into Output

Status: needs source module and images

One-line learning promise: Students will understand an AI model as a learned function that maps input numbers to output scores.

School concept: function as input -> rule -> output, such as `y = f(x)`.

AI use: model prediction for images, text, recommendations, classification.

Mechanism:

```text
input object -> input numbers -> learned function/model -> transformed numbers -> output scores
```

Mini example:

```text
input features for a small image/object:
[fur=1, pointy_ears=1, wheels=0]

model outputs:
cat: 0.82
dog: 0.14
car: 0.04
```

The model function transforms input numbers into scores for possible outputs.

Memory anchor: An AI model is a function learned from data.

Misunderstandings to avoid:

- Do not imply the function is a simple one-line school formula.
- Do not say AI directly understands raw images/text before numeric representation.
- Do not make the model a black box with no visible transformation.

Renderer-agnostic scene flow:

| Step | Teaching job | Core visual idea | Technical truth |
|---|---|---|---|
| 1 | Learning objective | `input -> f -> output` bridges to AI model | models map inputs to outputs |
| 2 | Familiar concept | notebook shows `y = f(x)` | functions connect input and output |
| 3 | AI example | tablet shows image/text entering model | AI tasks start with input data |
| 4 | Representation | input becomes feature/vector chips | models usually work on numbers |
| 5 | Mechanism | numbers pass through learned layers/steps | transformations produce new values |
| 6 | Output | score bars appear | outputs are often numeric scores |
| 7 | Application | highest score becomes prediction | score comparison supports decisions |
| 8 | Quick check | ask which output has highest score | function output is interpreted after scoring |

Video notes: show movement through the function/model, not a static box.

Image-only notes: can include `x -> f(x) -> y` plus one AI example.

Image prerequisites: must show numeric transformation inside/around the model.

Approval notes: likely next new concept lesson after intro.

## Episode 4: Probability - How AI Handles Uncertainty

Status: visual draft

Existing assets:

- `modules/visual-ai-concepts/probability-how-ai-handles-uncertainty.source.md`
- `assets/image-prompts/probability-how-ai-handles-uncertainty-video-first.md`
- `assets/images/probability-how-ai-handles-uncertainty-video-first/`

One-line learning promise: Students will understand that many AI outputs are probability-based predictions, not guaranteed answers.

School concept: probability as likelihood from 0 to 1 or 0% to 100%.

AI use: classification confidence, recommendations, next-word or next-token prediction.

Mechanism:

```text
possible answers -> probability scores -> compare scores -> choose likely answer -> uncertainty if scores are close
```

Mini example:

```text
cat: 0.72
dog: 0.20
car: 0.08
total: 1.00
```

The AI chooses cat because it has the highest probability, not because it is guaranteed true.

Memory anchor: AI predictions are confidence-weighted guesses.

Misunderstandings to avoid:

- High probability is not certainty.
- Low confidence should change how much we trust the output.
- Probabilities depend on the model and input quality.

Renderer-agnostic scene flow:

| Step | Teaching job | Core visual idea | Technical truth |
|---|---|---|---|
| 1 | Learning objective | ambiguous input has several possible answers | AI may estimate, not know |
| 2 | Familiar concept | 0 to 1 probability scale | probability measures likelihood |
| 3 | AI example | cat/dog/car options around image | classification considers alternatives |
| 4 | Representation | probability bars with values | options can get scores |
| 5 | Mechanism | highest bar highlights | top probability is selected |
| 6 | Uncertainty | close bars show low confidence | close scores mean less certainty |
| 7 | Application | recommender/chatbot/classifier panels | many AI systems score possibilities |
| 8 | Quick check | clear winner vs close scores | close top scores are more uncertain |

Video notes: current image set is ready for review, then animatic/video.

Image-only notes: values and labels should be readable without narration.

Image prerequisites: current frame 1 is acceptable after user clarified the earlier flower image confusion.

Approval notes: review the actual contact sheet with ChatGPT vision before Runway generation.

## Episode 5: Statistics - How AI Learns Patterns From Data

Status: needs source module and images

One-line learning promise: Students will understand that AI learns useful patterns by looking across many examples, not by memorizing one example.

School concept: mean, spread, trend, sample, variation.

AI use: datasets, training examples, pattern finding, bias detection.

Mechanism:

```text
many examples -> measurements/features -> pattern estimate -> prediction rule -> check on new example
```

Mini example:

```text
Study hours: 1, 2, 3, 4, 5
Score trend: 45, 52, 61, 68, 76
```

A model can estimate a trend, but real data has variation and exceptions.

Memory anchor: AI learns patterns from many examples, not from one example.

Misunderstandings to avoid:

- Statistics is not only averages.
- More data is not automatically better if it is biased or poor quality.
- A trend is not a guarantee for every individual case.

Renderer-agnostic scene flow:

| Step | Teaching job | Core visual idea | Technical truth |
|---|---|---|---|
| 1 | Learning objective | many dots become pattern | AI learns from examples |
| 2 | Familiar concept | mean/trend/spread in notebook | statistics summarizes data |
| 3 | AI example | many labeled examples feed model | training uses datasets |
| 4 | Representation | examples become data points | features can be plotted/measured |
| 5 | Mechanism | trend line appears through cloud | models estimate patterns |
| 6 | Variation | points do not all sit on line | data has noise/spread |
| 7 | Application | new point gets prediction | learned pattern guides prediction |
| 8 | Quick check | good data vs biased data | poor data can produce poor predictions |

Video notes: motion should show dots accumulating and trend emerging.

Image-only notes: include enough labels for mean/trend/spread.

Image prerequisites: must show multiple examples, not a single chart decoration.

Approval notes: good Batch A candidate after Functions.

## Episode 6: Linear Equations - How AI Combines Signals

Status: needs source module and images

One-line learning promise: Students will understand how an AI model can combine several input signals using weights to produce a score.

School concept: linear equation and weighted sum.

AI use: simple scoring models, neuron-like weighted inputs, feature importance.

Mechanism:

```text
features -> multiply by weights -> add results -> score
```

Mini example:

```text
score = 0.6 * fur + 0.3 * ears - 0.8 * wheels

For [fur=1, ears=1, wheels=0]:
score = 0.6 + 0.3 - 0 = 0.9
```

Weights decide how strongly each signal affects the score.

Memory anchor: Weights tell AI how much each signal matters.

Misunderstandings to avoid:

- A weighted sum is not the whole neural network.
- A high weight does not always mean a human-friendly reason.
- This is a simplified mechanism, not full model behavior.

Renderer-agnostic scene flow:

| Step | Teaching job | Core visual idea | Technical truth |
|---|---|---|---|
| 1 | Learning objective | features flow into equation | models combine signals |
| 2 | Familiar concept | `y = ax + b` or weighted sum | equations combine variables |
| 3 | AI example | object has feature chips | inputs can be represented as features |
| 4 | Representation | each feature gets weight | weights scale feature impact |
| 5 | Mechanism | multiply then add | weighted sum creates a score |
| 6 | Change effect | one weight slider changes score | weight changes affect output |
| 7 | Application | score feeds classification/recommendation | scores support decisions |
| 8 | Quick check | which feature matters more? | larger weight usually has stronger effect |

Video notes: animate feature chips multiplying by weights and joining as score.

Image-only notes: show one readable equation and one worked mini example.

Image prerequisites: must keep equation simple and readable.

Approval notes: place before derivatives to prepare for "changing a weight changes error".

## Episode 7: Derivatives - How AI Knows Which Way To Improve

Status: existing video draft; may need refresh

Existing assets:

- `modules/visual-ai-concepts/derivatives-how-ai-learns-from-mistakes.source.md`
- `assets/images/derivatives-ai-learning-native-story/`
- `outputs/video-renders/derivatives-ai-learning-micro-lesson-v1-en.mp4`

One-line learning promise: Students will understand that derivatives give AI a direction clue for reducing error.

School concept: derivative as slope or rate of change at a point.

AI use: training direction, gradients, reducing loss/error.

Mechanism:

```text
weight changes a little -> error changes -> slope tells direction -> update goes opposite slope
```

Mini example:

```text
slope = change in error / change in weight

If increasing the weight makes error go up,
take a small step in the opposite direction.
```

Memory anchor: Derivative tells AI which way to adjust.

Misunderstandings to avoid:

- Do not start with differentiation rules.
- Do not imply the derivative alone trains the model.
- Do not hide the error curve; the learner needs to see what slope is about.

Renderer-agnostic scene flow:

| Step | Teaching job | Core visual idea | Technical truth |
|---|---|---|---|
| 1 | Learning objective | error curve and slope arrow | derivative helps reduce error |
| 2 | Familiar concept | tangent line on curve | derivative is local slope |
| 3 | AI example | prediction compared to correct answer | training measures error |
| 4 | Representation | error plotted against weight | error can be viewed as a function of a parameter |
| 5 | Mechanism | slope shows error increases/decreases | derivative gives direction information |
| 6 | Update | small step opposite slope | training adjusts against error increase |
| 7 | Application | repeated corrections improve model | learning uses many updates |
| 8 | Quick check | if slope is positive, which way? | move opposite the positive direction |

Video notes: current derivative video is useful, but style may need refresh to match warm tablet series.

Image-only notes: can support a little more formula text.

Image prerequisites: must show tangent slope, not only "mistake and correction".

Approval notes: decide reuse vs refresh.

## Episode 8: Gradient Descent - How AI Learns From Mistakes

Status: needs source module and images

One-line learning promise: Students will understand training as repeated small steps that reduce loss.

School concept: repeated steps using slope/direction; builds from derivatives.

AI use: optimization during model training.

Mechanism:

```text
prediction -> loss/error -> gradient direction -> small step opposite gradient -> lower loss -> repeat
```

Mini example:

```text
step 1 loss: 8.0
step 2 loss: 5.1
step 3 loss: 3.2
step 4 loss: 2.4
```

The model improves by repeatedly adjusting parameters to reduce loss.

Memory anchor: Gradient descent is small steps toward lower error.

Misunderstandings to avoid:

- Downhill analogy is not enough; show loss and gradient.
- Gradient descent may not always find the perfect/global minimum.
- Step size matters; too large can overshoot.

Renderer-agnostic scene flow:

| Step | Teaching job | Core visual idea | Technical truth |
|---|---|---|---|
| 1 | Learning objective | point on loss curve moves lower | training reduces loss |
| 2 | Familiar concept | slope/downhill direction | slope suggests direction of change |
| 3 | AI example | wrong prediction creates loss | loss measures error |
| 4 | Representation | loss curve/surface appears | loss depends on parameters |
| 5 | Mechanism | gradient arrow shows steep increase | move opposite gradient to reduce loss |
| 6 | Step size | small step vs too-large step | learning rate affects update |
| 7 | Repeat | loss values decrease over steps | training repeats many updates |
| 8 | Quick check | which step is safer? | small controlled step is usually safer |

Video notes: motion is central; point should visibly step down the curve.

Image-only notes: show before/after loss table plus curve.

Image prerequisites: must show loss values changing, not only a person walking downhill.

Approval notes: comes directly after derivatives.

## Episode 9: Graphs - How AI Understands Relationships

Status: needs source module and images

One-line learning promise: Students will understand how graphs represent relationships between people, products, ideas, or facts.

School concept: graph as nodes and edges.

AI use: recommendations, knowledge graphs, social networks, connected data, retrieval paths.

Mechanism:

```text
entities -> nodes
relationships -> edges
nearby/connected nodes -> suggested item or related fact
```

Mini example:

```text
Student -> likes -> vectors lesson
Vectors lesson -> related to -> embeddings
Embeddings -> used in -> semantic search
```

The graph helps find connected concepts or recommendations.

Memory anchor: Graphs help AI use relationships, not only individual items.

Misunderstandings to avoid:

- This graph is not the same as a line graph.
- A connection suggests relationship, not automatic truth.
- Graph-based AI still depends on data quality.

Renderer-agnostic scene flow:

| Step | Teaching job | Core visual idea | Technical truth |
|---|---|---|---|
| 1 | Learning objective | connected nodes on tablet | graphs model relationships |
| 2 | Familiar concept | nodes and edges in notebook | graph has vertices and connections |
| 3 | AI example | recommendation network | recommendations can use connections |
| 4 | Representation | people/items become nodes | entities can be graph nodes |
| 5 | Mechanism | shared neighbor/path highlights | graph structure reveals related items |
| 6 | Application | recommended lesson/product appears | connectedness can support suggestions |
| 7 | Knowledge graph | fact triples connect | facts can be represented as relations |
| 8 | Quick check | which item is closer in graph? | fewer/stronger connections often mean closer relation |

Video notes: animate path highlighting through connected nodes.

Image-only notes: label nodes and edge verbs clearly.

Image prerequisites: must avoid decorative network background; show a real relationship path.

Approval notes: can be moved earlier if recommendation examples become a priority.

## Episode 10: Coordinates - How AI Places Ideas In Space

Status: optional reinforcement lesson

One-line learning promise: Students will understand that AI can place items as points in a space where distance can represent similarity.

School concept: coordinate plane, axes, points, distance.

AI use: embedding visualization, clustering, similarity maps.

Mechanism:

```text
item -> numbers -> point in space -> distance/clusters -> similarity judgment
```

Mini example:

```text
phone: (2.1, 1.8)
mobile: (2.3, 1.7)
banana: (-1.4, 3.2)
```

Phone and mobile are closer in this simplified map.

Memory anchor: In AI maps, nearby points often mean similar items.

Misunderstandings to avoid:

- Real embeddings can have hundreds or thousands of dimensions, not only 2D.
- Axes may not have simple human labels.
- A 2D map is a simplification for learning.

Renderer-agnostic scene flow:

| Step | Teaching job | Core visual idea | Technical truth |
|---|---|---|---|
| 1 | Learning objective | points on coordinate plane become AI map | coordinates can place ideas |
| 2 | Familiar concept | x-y plane in notebook | points have positions |
| 3 | AI example | items appear as dots | embeddings can be visualized as points |
| 4 | Representation | item becomes coordinate/vector | numbers define position |
| 5 | Mechanism | distances are measured | distance can indicate similarity |
| 6 | Clusters | related dots group together | similar items can cluster |
| 7 | Application | search/recommendation uses nearby point | nearest neighbors can be retrieved |
| 8 | Quick check | choose closer point | closer point is more similar in the map |

Video notes: point movement and distance lines should be clear.

Image-only notes: include a simple 2D coordinate example.

Image prerequisites: must state/signal that 2D is simplified.

Approval notes: optional because vectors already covers much of this; useful if students need more spatial intuition.

## Episode 11: Logic - How AI Makes Rule-Based Decisions

Status: optional

One-line learning promise: Students will understand how conditions and true/false checks help AI systems route decisions.

School concept: logic, conditions, true/false, if-then rules.

AI use: decision trees, filters, tool routing, agent rules, safety checks.

Mechanism:

```text
input -> condition check -> branch -> next check/action -> decision
```

Mini example:

```text
If confidence < 0.50 -> ask human
If confidence >= 0.50 and risk is low -> suggest answer
If risk is high -> require approval
```

Logic helps control when an AI system should act, ask, or stop.

Memory anchor: Logic helps AI systems choose a path.

Misunderstandings to avoid:

- Logic rules are not the same as neural-network learning.
- Rule-based decisions can be brittle if rules are incomplete.
- AI systems often combine learned scores with explicit rules.

Renderer-agnostic scene flow:

| Step | Teaching job | Core visual idea | Technical truth |
|---|---|---|---|
| 1 | Learning objective | decision path on tablet | logic routes actions |
| 2 | Familiar concept | true/false condition in notebook | conditions split paths |
| 3 | AI example | AI assistant decides answer vs ask human | systems use rules around model outputs |
| 4 | Representation | input gets confidence/risk values | decisions can use scores and flags |
| 5 | Mechanism | if-then branches light up | conditions select paths |
| 6 | Application | safety/tool-routing panel | agents and tools need decision rules |
| 7 | Human approval | high-risk branch stops | some actions need human control |
| 8 | Quick check | choose correct branch | rule determines next action |

Video notes: animate branching decision path.

Image-only notes: use clean flowchart, not dense truth tables.

Image prerequisites: must show logic as routing/control, not claim it is the whole AI model.

Approval notes: optional; useful bridge to AI agents later.

## Cross-Series Renderer Plan

For every approved lesson, create one shared lesson core and then adapt it into:

| Renderer | Purpose | Notes |
|---|---|---|
| Video micro-lesson | teach with voice and motion | fewer embedded words, strong technical motion |
| Image-only post | teach without audio | more labels, readable technical sequence |
| Classroom slides | teacher explanation | more explicit diagrams and questions |
| Interactive demo | learner manipulates concept | sliders, points, scores, steps where useful |

## Proposed Production Batches

### Batch A: Fill the Current Gap

1. Series Intro
2. Functions
3. Statistics
4. Probability review/refinement

Reason: matrices and vectors already exist; functions is the missing bridge; probability already has source images; statistics naturally follows.

### Batch B: Training Arc

1. Linear Equations
2. Derivatives refresh decision
3. Gradient Descent

Reason: weighted sums lead into changing weights; derivatives explain direction; gradient descent explains repeated updates.

### Batch C: Relationship Arc

1. Graphs
2. Coordinates, if not folded into vectors
3. Logic, if preparing for agents/tools series

Reason: these support recommendations, retrieval, and AI systems beyond pure model training.

## Review Checklist

Before image work starts, confirm:

- Is the sequence approved?
- Are any titles too vague or misleading?
- Are the mini examples technically safe?
- Should optional lessons stay in this series or move to another series?
- Should derivatives be reused as-is or refreshed?
- Is Batch A approved for bulk lesson-core and image-prerequisite creation?
