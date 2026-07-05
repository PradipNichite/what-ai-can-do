# How AI Uses Math Image-Only Gap Audit

Last updated: 2026-07-03

## Rule

For the `How AI Uses Math` series, create the image-only/self-contained visual story before video-first source frames.

The image-only version is the concept proof. It should work as a paused Instagram carousel, WhatsApp story, classroom slide sequence, or contact sheet without voiceover, motion, or external captions.

Default order:

```text
lesson core -> image-only prompt pack -> image-only cards/contact sheet -> image-only QA -> video-first prompt pack -> video source frames -> image-to-video
```

## Naming Convention

Use these names for image-only concept-proof assets:

```text
assets/image-prompts/<slug>-image-story.md
assets/images/<slug>-image-story/
assets/images/<slug>-image-story/<slug>-image-story-contact-sheet.jpg
assets/images/<slug>-image-story/<slug>-image-story-review-notes.md
```

Use video-first names only after the image-only concept works:

```text
assets/image-prompts/<slug>-video-first.md
assets/images/<slug>-video-first/
```

## Current Inventory

| Order | Lesson | Current Image-Only Status | Existing Related Assets | Next Action |
|---|---|---|---|---|
| 0 | Series Intro: How AI Uses Math | Missing | Has video-first source frames | Create image-only concept story |
| 1 | Matrices: How AI Sees Images as Numbers | Partial / style-refresh exists | `assets/images/matrices-how-ai-sees-images-as-numbers-style-b-refresh/` | Decide if style-refresh counts; archive image-story prompt pack if accepted |
| 2 | Vectors: How AI Compares Meaning | Partial / style-refresh exists | `assets/images/vectors-how-ai-compares-meaning-style-b-refresh/` | Decide if style-refresh counts; archive image-story prompt pack if accepted |
| 3 | Functions: How AI Turns Input Into Output | Missing | Has video-first source frames | Create image-only concept story |
| 4 | Probability: How AI Handles Uncertainty | Partial / style-refresh exists | `assets/images/probability-how-ai-handles-uncertainty-style-b-refresh/` | Decide if style-refresh counts; archive image-story prompt pack if accepted |
| 5 | Statistics: How AI Learns Patterns From Data | Missing | Has video-first source frames | Create image-only concept story |
| 6 | Linear Equations: How AI Combines Signals | Missing | Has video-first source frames | Create image-only concept story |
| 7 | Derivatives: How AI Knows Which Way To Improve | Exists / older native story | `assets/image-prompts/derivatives-ai-learning-story.md`, `assets/images/derivatives-ai-learning-native-story/` | Review whether it should be refreshed into Direction B |
| 8 | Gradient Descent: How AI Learns From Mistakes | Missing | Has video-first prompt pack/source frames from parallel work | Create image-only concept story before further video work |
| 9 | Graphs: How AI Understands Relationships | Missing | Has video-first prompt pack/source frames from parallel work | Create image-only concept story before further video work |
| 10 | Coordinates: How AI Places Ideas In Space | Missing | No confirmed image set yet | Create source module and image-only concept story |
| 11 | Logic: How AI Makes Rule-Based Decisions | Missing | No confirmed image set yet | Create source module and image-only concept story |

## Highest-Priority Image-Only Work

Start with the lessons that already have video-first assets but no image-only concept proof:

1. `Gradient Descent: How AI Learns From Mistakes`
2. `Graphs: How AI Understands Relationships`
3. `Functions: How AI Turns Input Into Output`
4. `Statistics: How AI Learns Patterns From Data`
5. `Linear Equations: How AI Combines Signals`
6. `Series Intro: How AI Uses Math`

Then handle optional or partial cases:

7. `Coordinates: How AI Places Ideas In Space`
8. `Logic: How AI Makes Rule-Based Decisions`
9. Confirm whether the Matrices, Vectors, and Probability style-refresh sets are strong enough to count as image-only concept proofs.
10. Decide whether Derivatives should stay as the older native story or be refreshed into the newer Direction B image-only style.

## Parallel Session Notes

Use these notes to run the highest-priority image-only work in parallel:

```text
NEXT_SESSION_IMAGE_ONLY_PARALLEL_BATCH_NOTE.md
NEXT_SESSION_IMAGE_ONLY_GRADIENT_DESCENT_NOTE.md
NEXT_SESSION_IMAGE_ONLY_GRAPHS_NOTE.md
NEXT_SESSION_IMAGE_ONLY_FUNCTIONS_NOTE.md
NEXT_SESSION_IMAGE_ONLY_STATISTICS_NOTE.md
NEXT_SESSION_IMAGE_ONLY_LINEAR_EQUATIONS_NOTE.md
NEXT_SESSION_IMAGE_ONLY_SERIES_INTRO_NOTE.md
```

## Image-Only Acceptance Criteria

An image-only story counts as a concept proof only if:

- the first card is a self-contained lesson opener: title/topic, what the learner will understand, school concept, AI use, and the concrete example or task
- generated text is native to the card composition: poster typography, tablet UI, notebook panels, speech bubbles, sticky notes, diagram labels, arrows, or callouts
- the card does not look like text was pasted on top of a separate background image
- each later card is self-contained enough to understand without voiceover
- the contact sheet shows a clear concept progression
- key terms and diagrams are readable on mobile
- the mechanism is visible, not only narrated by text
- the sequence includes a memory anchor or recap
- there is a short QA/review note in the image folder

If a set looks beautiful but only makes sense after reading project notes, animation, or voiceover, it does not count as image-only proof.

Failure pattern to reject:

```text
Card 1 shows an unexplained object or diagram, then later cards begin transforming it.
Card text looks like a generic overlay pasted onto a background.
```

Required pattern:

```text
Card 1 tells the learner what lesson they are in and why the example matters.
The image and text are generated as one designed educational card.
```
