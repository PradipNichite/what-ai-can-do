# Vectors: How AI Compares Meaning

Status: video-interactive
Pipeline stage: 08 Video / Interactive
Type: Granular Episode
Parent topic: Applied Mathematics In AI
Primary format: Micro-lesson video
Next action: Review v2 style-corrected preview before spending Runway credits on all final clips.

## Learning Promise

In this micro-lesson, students learn that AI can compare meaning by turning words or sentences into vectors: lists of numbers that can be compared by distance or direction.

## Target Learner

11th/12th science students, first-year learners, and curious non-technical viewers who have heard about AI search or recommendations but do not yet understand what "meaning as numbers" means.

## Why It Matters

Many useful AI features depend on comparing meaning, not matching exact words. Semantic search can find "budget mobile" when a user types "cheap phone." Recommendation systems can suggest related videos, products, or lessons. Embeddings make this possible by placing similar meanings close together in vector space.

## Core Explanation

A vector is a list of numbers.

For AI, a word, sentence, image, or user preference can be converted into a vector:

```text
"budget mobile" -> [0.82, -0.14, 0.51, 0.07, ...]
```

The individual numbers are not meant to be read like exam marks. Together, they act like coordinates for meaning.

When two meanings are similar, their vectors usually end up close together, or they point in a similar direction. That is why AI can connect:

- `cheap phone`
- `budget mobile`
- `affordable smartphone`

These phrases do not share the same exact words, but they carry related meaning.

This idea is used in:

- semantic search
- recommendations
- document search
- question answering over notes
- matching users, products, lessons, and examples

## Math Glimpse

A vector is a list of numbers.

Similarity can be checked in simple ways:

- distance: closer points are more similar
- direction: vectors pointing in a similar direction are more similar

For this lesson, avoid formulas. Show arrows and nearby points instead.

## Memory Anchor

Similar meaning means nearby vectors.

## Micro-Lesson Flow

1. What you will learn: AI can connect related meaning even with different words.
2. A vector is a list of numbers.
3. Meanings become points in a meaning space.
4. Similar meanings are close or point in similar directions.
5. Semantic search finds the nearest meanings.
6. Recommendations suggest nearby meanings.
7. Recap and quick check.

## Quick Check

Which pair should be closer in meaning space?

```text
"car" + "vehicle"
or
"car" + "banana"
```

Answer: `car` and `vehicle`, because they have related meaning.
