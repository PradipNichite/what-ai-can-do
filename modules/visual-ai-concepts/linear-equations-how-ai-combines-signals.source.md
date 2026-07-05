# Linear Equations: How AI Combines Signals

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
Next action: Review source-frame contact sheet before video generation.

## Lesson Identity

Title: Linear Equations: How AI Combines Signals

Short title: Linear Equations In AI

Episode order: 6

One-line learning promise: Students will understand how an AI model can combine input signals using weights to produce a score.

Memory anchor: Weights tell AI how much each signal matters.

## School Math Concept

Students may know equations such as:

```text
y = ax + b
```

This episode extends that idea to a weighted sum with multiple input signals.

## AI Application

Where this appears in AI:

- simple scoring models
- feature-based classifiers
- neuron-like weighted inputs
- recommendation scores

## Mechanism

```text
features -> multiply by weights -> add results -> score
```

## Mini Example

```text
score = 0.6 * fur + 0.3 * ears - 0.8 * wheels

For [fur=1, ears=1, wheels=0]:
score = 0.6 + 0.3 - 0 = 0.9
```

## Misunderstandings To Avoid

- A weighted sum is not the whole neural network.
- A high weight does not always mean a human-friendly reason.
- This is a simplified mechanism, not full model behavior.

## Renderer-Agnostic Scene Flow

| Step | Teaching job | Core visual idea | Must be technically true |
|---|---|---|---|
| 1 | Learning objective | features flow into equation | models combine signals |
| 2 | Familiar concept | `y = ax + b` or weighted sum | equations combine variables |
| 3 | AI example | object has feature chips | inputs can be features |
| 4 | Representation | each feature gets weight | weights scale feature impact |
| 5 | Mechanism | multiply then add | weighted sum creates a score |
| 6 | Change effect | one weight slider changes score | weight changes affect output |
| 7 | Application | score feeds classifier | scores support decisions |
| 8 | Quick check | which feature matters more? | larger weight usually has stronger effect |

## Quick Check

Question: If `fur` has weight `0.6` and `wheels` has weight `-0.8`, which signal strongly pushes away from an animal prediction?

Correct answer: wheels

Why: the negative weight reduces the animal-like score.
