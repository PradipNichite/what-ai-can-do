# Probability: How AI Handles Uncertainty

Status: visual-draft
Pipeline stage: 05 Visual Draft
Type: Granular Episode
Parent topic: Applied Mathematics In AI
Primary format: Micro-lesson video
Next action: Review source-frame contact sheet and local preview animatic with ChatGPT vision before Runway generation.

## Learning Promise

In this micro-lesson, students learn that many AI outputs are not guaranteed answers. They are probability-based predictions: estimates of which option is most likely.

## Target Learner

11th/12th science students, first-year learners, and curious non-technical viewers who use AI tools but do not yet understand confidence, uncertainty, and probabilistic prediction.

## Why It Matters

AI systems often make decisions under uncertainty. A classifier may decide whether an image shows a cat, dog, or car. A recommendation system may estimate which video a user will like. A chatbot may choose the next word that is most likely to fit the context.

Understanding probability helps learners avoid a common mistake: treating AI output as certainty. AI can be confident and still be wrong.

## Core Explanation

Probability is a number that describes how likely something is.

It can be written as:

```text
0 to 1
```

or:

```text
0% to 100%
```

For example:

```text
cat: 0.72
dog: 0.20
car: 0.08
```

This means the AI thinks `cat` is the most likely answer, not that it is guaranteed.

AI often compares several possible outputs and chooses the option with the highest probability. When probabilities are close, the AI should be treated as uncertain.

## Math Glimpse

Probability values usually add up to `1` across the main options.

Example:

```text
cat 0.72 + dog 0.20 + car 0.08 = 1.00
```

A higher number means more confidence. A lower number means less confidence.

## Memory Anchor

AI predictions are confidence-weighted guesses.

## Micro-Lesson Flow

1. What you will learn: AI often estimates what is most likely.
2. Why it matters: confidence is not the same as truth.
3. Concrete example: a tablet photo could be cat, dog, or car.
4. Core concept: probability is a number from `0` to `1`.
5. Mechanism: AI assigns probability scores to possible answers.
6. Decision: AI chooses the highest score, but close scores mean uncertainty.
7. AI use: recommendations, classifiers, and chatbots use this idea.
8. Recap and quick check.

## Technical Teaching Table

| # | Scene | Learning job | Visible evidence | Transformation / motion role |
|---|---|---|---|---|
| 1 | Prediction is not certainty | AI estimates likely answers | tablet shows several possible answer cards, not one fixed answer | answer options appear around a question/image |
| 2 | Probability scale | probability ranges from 0 to 1 / 0% to 100% | horizontal scale with 0, 0.5, 1 and pointer moving | pointer slides from unlikely to likely |
| 3 | Option scores | each possible answer gets a score | cat/dog/car bars with numeric probabilities | bars grow to different heights |
| 4 | Highest probability wins | AI chooses the largest score | cat bar glows as the top score | top bar highlights, smaller bars dim |
| 5 | Uncertainty | close probabilities mean less confidence | two bars are close, warning/uncertain marker appears | bars nearly tie, confidence meter drops |
| 6 | Real AI uses | probability powers classification and recommendations | same scoring idea shown for photo, video recommendation, next-word prediction | three mini panels reuse probability bars |
| 7 | Memory anchor | predictions are confidence-weighted guesses | recap chain: input -> probability scores -> chosen output | nodes light up left to right |
| 8 | Quick check | learner identifies uncertainty | two probability sets side by side: clear winner vs close scores | close-score set pulses as uncertain |

## Quick Check

Which AI prediction is more uncertain?

```text
A: cat 0.90, dog 0.07, car 0.03
B: cat 0.42, dog 0.39, car 0.19
```

Answer: `B`, because the top two probabilities are close.
