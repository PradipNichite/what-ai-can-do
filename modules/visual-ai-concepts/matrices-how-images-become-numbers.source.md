# Matrices: How Images Become Numbers

Status: prompt-pack
Pipeline stage: 04 Prompt Pack
Type: Granular Episode
Parent topic: Applied Mathematics In AI
Primary format: Micro-lesson video
Next action: Confirm or create the image-only concept-proof story before further video-first work.

## Learning Promise

In this micro-lesson, students learn that a digital image can be represented as rows and columns of numbers, and that this is one reason matrices matter in AI and computer vision.

## Target Learner

11th/12th science students and first-year learners who have seen matrices as exam tables but do not yet connect them to real systems.

## Why It Matters

Matrices feel abstract until students see that every digital photo is already grid-like. Computers and AI systems do not start by "seeing" like humans. They work with numbers: pixel brightness, color channels, and patterns across grids.

## Core Explanation

A digital image is made of small squares called pixels.

For a grayscale image, each pixel can be stored as one number:

- `0` can mean black.
- `255` can mean white.
- numbers in between mean different brightness levels.

So a small black-and-white image can become a matrix:

```text
[
  [20, 40, 80],
  [30, 120, 200],
  [10, 90, 255]
]
```

Each row and column keeps the pixel position.

Color images usually use more than one matrix. A simple way to think about it:

- one matrix for red
- one matrix for green
- one matrix for blue

Together, these number grids describe the image.

AI can then look for patterns in those numbers: edges, shapes, textures, and objects.

## Memory Anchor

An image is not magic to a computer. It is a grid of numbers.

## Micro-Lesson Flow

1. What you will learn: images can become matrices.
2. Why it matters: AI uses numbers to understand pictures.
3. A student takes a photo.
4. The photo zooms into pixels.
5. Pixel brightness becomes numbers.
6. The grid becomes a matrix.
7. Color images use multiple matrices/channels.
8. AI scans the number grids for patterns.
9. Recap: matrices help computers see.

## Quick Check

If a grayscale photo is `100 x 100` pixels, how many numbers are in its brightness matrix?

Answer: `10,000`.
