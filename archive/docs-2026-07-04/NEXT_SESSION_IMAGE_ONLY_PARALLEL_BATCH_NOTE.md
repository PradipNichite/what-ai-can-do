# Next Session Batch: Image-Only Concept Proofs

Use this as the index for parallel sessions that create image-only/self-contained visual stories for existing `How AI Uses Math` lessons.

## Rule

Do not start with video-first source frames.

For each lesson, create the image-only concept-proof format first:

```text
lesson core -> image-only prompt pack -> image-only story cards -> contact sheet -> review notes
```

The image-only cards must make sense without voiceover, motion, or external captions. This is how we test whether the concept is powerful before spending time on image-to-video.

## Recommended Parallel Sessions

Run 6 sessions, one per lesson:

| Session | Lesson | Start Note |
|---|---|---|
| A | Gradient Descent: How AI Learns From Mistakes | `NEXT_SESSION_IMAGE_ONLY_GRADIENT_DESCENT_NOTE.md` |
| B | Graphs: How AI Understands Relationships | `NEXT_SESSION_IMAGE_ONLY_GRAPHS_NOTE.md` |
| C | Functions: How AI Turns Input Into Output | `NEXT_SESSION_IMAGE_ONLY_FUNCTIONS_NOTE.md` |
| D | Statistics: How AI Learns Patterns From Data | `NEXT_SESSION_IMAGE_ONLY_STATISTICS_NOTE.md` |
| E | Linear Equations: How AI Combines Signals | `NEXT_SESSION_IMAGE_ONLY_LINEAR_EQUATIONS_NOTE.md` |
| F | Series Intro: How AI Uses Math | `NEXT_SESSION_IMAGE_ONLY_SERIES_INTRO_NOTE.md` |

## Why These Six

These lessons already have lesson cores and/or video-first assets, but they do not yet have a confirmed image-only concept-proof story in the current pipeline.

Do not include Coordinates and Logic in this batch. They are separate optional lessons and may still need source modules or first-pass lesson shaping.

## Shared Output Naming

Each session should create:

```text
assets/image-prompts/<slug>-image-story.md
assets/images/<slug>-image-story/
assets/images/<slug>-image-story/<slug>-image-story-contact-sheet.jpg
assets/images/<slug>-image-story/<slug>-image-story-review-notes.md
```

## Shared Style

Follow:

```text
HOW_AI_USES_MATH_STYLE_DECISION_NOTE.md
HOW_AI_USES_MATH_SERIES_GUIDE.md
CONTENT_PIPELINE.md
```

Use Direction B:

- realistic warm study-desk/tablet technical style
- recurring Indian 11th/12th standard learner
- dark wavy hair, teal/green shirt
- wooden desk, lamp, notebook, books, small plant
- readable diagrams, labels, arrows, numbers, and callouts
- self-contained educational cards, not sparse animation source frames
- technical mechanism visible on every card

## Shared Acceptance Criteria

Each image-only story counts only if:

- each card can be understood without voiceover
- the contact sheet shows clear concept progression
- text is readable on mobile
- diagrams and labels are not overcrowded
- the mechanism is visible, not only described
- the last card includes a memory anchor or quick check
- review notes identify any weak card before video adaptation

