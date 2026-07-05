# Functions: How AI Turns Input Into Output

Status: visual-draft
Pipeline stage: 05 Visual Draft
Type: Granular Episode
Parent series: How AI Uses Math
Series guide: ../../HOW_AI_USES_MATH_SERIES_GUIDE.md
Series plan: ../../HOW_AI_USES_MATH_SERIES_PLAN.md
Image prerequisites: ../../HOW_AI_USES_MATH_IMAGE_PREREQUISITES.md
Primary learner: 11th/12th standard students
Primary intent: technically correct applied math understanding
Primary renderer: shared lesson core
Next action: Review source-frame contact sheet for technical clarity and style consistency before Runway generation.

## Lesson Identity

Title: Functions: How AI Turns Input Into Output

Short title: Functions In AI

Episode order: 3

One-line learning promise: Students will understand an AI model as a learned function that maps input numbers to output scores.

Memory anchor: An AI model is a function learned from data.

## School Math Concept

Students have likely studied a function as a rule that maps an input to an output:

```text
y = f(x)
```

They may know terms such as input, output, domain, range, rule, graph, and value of a function.

Minimum prior knowledge:

- a function takes an input
- a rule or process acts on the input
- the function produces an output

What not to teach in this episode:

- formal neural-network architecture
- activation functions in detail
- backpropagation
- proofs or function composition notation beyond a simple visual

## AI Application

Where this appears in AI:

- image classification
- text classification
- recommendations
- speech recognition
- any model that turns data into a prediction

Concrete AI task:

An AI receives an image or text input, converts it into numbers, processes those numbers through a learned model, and produces scores for possible outputs.

Why this math concept is useful:

The function idea helps students see that a model is not magic. It is a learned mapping from input representation to output scores.

## Mechanism

What changes, moves, or gets computed:

```text
input object -> input numbers -> learned function/model -> transformed numbers -> output scores
```

Mechanism explanation in simple words:

In school, a function might take `x = 2` and produce `y = 5`. In AI, the input is usually many numbers, not just one number. These numbers may represent pixels, words, or features. The model applies learned transformations and produces output scores.

Technical accuracy notes:

- AI models usually operate on numeric representations.
- The model can be thought of as a large learned function, but not as one simple handwritten formula.
- Output scores may later be converted into probabilities, but this lesson only needs to show scores.
- The highest score is often used as the predicted class, depending on the task.

Analogy:

The model is like a function machine, but the "rule" is learned from examples.

Where the analogy stops being exact:

Real AI models can have millions or billions of learned parameters, many layers, and complex transformations. They are not simple classroom function machines.

## Mini Example

Example input:

```text
small animal photo
```

Intermediate representation:

```text
[fur=1, pointy_ears=1, wheels=0]
```

Computation/comparison/scoring:

```text
model function processes the input numbers
```

Output:

```text
cat: 0.82
dog: 0.14
car: 0.04
```

What the learner should notice:

The model does not jump directly from image to answer. The input becomes numbers, the learned function transforms those numbers, and the output is a set of scores.

## Misunderstandings To Avoid

- Do not imply the AI function is a simple one-line school formula.
- Do not say AI directly understands raw images or text before numeric representation.
- Do not make the model a black box with no visible transformation.
- Do not say the highest score is always correct.

## Renderer-Agnostic Scene Flow

| Step | Teaching job | Core visual idea | Must be technically true |
|---|---|---|---|
| 1 | Learning objective | `input -> f -> output` bridges to AI model | models map inputs to outputs |
| 2 | Familiar concept | notebook shows `y = f(x)` | functions connect input and output |
| 3 | AI example | tablet shows image/text entering model | AI tasks start with input data |
| 4 | Representation | input becomes feature/vector chips | models usually work on numbers |
| 5 | Mechanism | numbers pass through learned layers/steps | transformations produce new values |
| 6 | Output | score bars appear | outputs are often numeric scores |
| 7 | Application | highest score becomes prediction | score comparison supports decisions |
| 8 | Quick check | ask which output has highest score | output is interpreted after scoring |

## Renderer Adaptation Notes

### Video Micro-Lesson

What needs motion:

- input moves from notebook/tablet into the model
- number chips light up in sequence
- transformation layers pulse one after another
- output score bars grow
- highest score highlights

What voiceover must explain:

- AI models use numbers as input
- a model is like a learned function
- the output is scores, not guaranteed truth

What should be captioned:

- `input -> function -> output`
- `input numbers -> model -> scores`
- memory anchor

What should remain visual only:

- the warm student/study environment
- UI glow and light motion
- secondary examples

### Image-Only Post

What must be understandable without audio:

- school function and AI model are connected
- input becomes numbers
- model produces scores
- highest score becomes the prediction

What text can be embedded:

- short labels: input, function/model, output scores
- one simple score table
- memory anchor

What should be simplified:

- avoid many layers or dense feature vectors

### Presentation / Classroom

What teacher can ask:

- What is the input?
- What is the output?
- Why are the outputs scores instead of one guaranteed answer?

What board diagram works:

```text
x -> f(x) -> y
image/text -> model -> scores
```

What can become a short activity:

Students choose the highest score and explain why high score is not the same as guaranteed truth.

### Interactive / Demo

What learner can manipulate:

- feature values
- model score bars
- selected input example

What changes on screen:

- output scores change as inputs change

What concept becomes clearer:

- a function maps input values to output values

## Quick Check

Question:

If a model outputs these scores, which answer will it usually choose?

```text
cat: 0.18
dog: 0.74
car: 0.08
```

Correct answer:

`dog`

Why:

It has the highest output score.

## Technical Teaching Table

| # | Scene | Learning job | Visible evidence | Transformation / comparison | Motion role | Risk |
|---|---|---|---|---|---|
| 1 | Learning objective | connect school function to AI model | notebook `input -> f -> output`, tablet `input -> model -> scores` | school function -> AI model | bridge line lights up | too generic |
| 2 | Familiar function | show known school concept | `y = f(x)` with input 2 and output 5 | input value -> output value | pencil underline | too formula-heavy |
| 3 | AI input | show real AI task | small animal image enters model panel | real input -> model | input card slides | looks like generic app |
| 4 | Numeric representation | AI needs numbers | input becomes feature chips `[fur, ears, wheels]` | image -> numbers | chips appear | features too literal if not framed as simple example |
| 5 | Learned transformation | model transforms numbers | layered function path with changing number chips | input vector -> hidden values | layers pulse | black-box only |
| 6 | Output scores | model output is numeric | score bars cat/dog/car | transformed numbers -> scores | bars grow | probability confusion |
| 7 | Prediction | highest score selected | cat bar glows and prediction card appears | compare scores -> chosen output | highlight highest | implies guaranteed truth |
| 8 | Quick check | learner interprets scores | dog score highest in score table | compare three scores | correct row pulses | too much text |

## Approval Notes

Approved concept: pending review

Open questions:

- Should this episode use image classification only, or include text as a second example?
- Should the image-only concept story use image classification only, or include text as a second example?

Renderer priority: image-only concept story first, then video-first source images

Image generation allowed: yes for image-only concept-proof draft
