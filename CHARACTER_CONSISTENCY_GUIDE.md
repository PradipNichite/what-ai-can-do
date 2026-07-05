# Character Consistency Guide

This guide defines how to keep recurring characters stable across generated story images and videos.

## Character Bible Template

Use this for every recurring character:

```text
Character name: <internal name>
Role: <student / teacher / parent / shopkeeper / support agent>
Age range: <approximate age>
Context: <Indian school student, Maharashtra urban home, etc.>
Face: <round/oval face, expressive eyes, etc.>
Hair: <style, color, tied/loose>
Clothing: <same outfit and colors>
Personality: <curious, focused, friendly>
Expression range: <confused, aha, confident>
Recurring objects: <phone, textbook, notebook, pencil>
Environment: <same study desk, warm home lighting>
Do not change: <hair, outfit, age, overall face, environment>
```

## Student Character Bible

Use this as the default for new concept micro-lessons unless the topic requires a different learner.

```text
Character name: Concept Learner
Role: Indian school student
Age range: teenage student, 11th/12th standard
Context: Indian home study desk, school learning setting
Face: expressive, curious, friendly, youthful
Hair: dark/black wavy hair
Clothing: teal or green shirt, simple student outfit
Personality: curious, thoughtful, willing to learn
Expression range: curious, attentive, aha, focused, confident
Recurring objects: tablet or smartphone, notebook, pen/pencil, books, small plant
Environment: warm wooden study desk, desk lamp, cozy study-room background
Do not change: age, teal/green outfit, dark hair, warm study desk environment
```

## Prompt Pattern For Consistency

Include this block in every image prompt:

```text
Subject: Same recurring Indian school student from this series: teenage learner, dark wavy hair, teal/green shirt, curious expressive face.
Environment: Same warm wooden study desk with desk lamp, notebook, pen, books, small plant, and tablet or smartphone.
Consistency constraints: keep age, hairstyle, outfit, face style, and study desk environment consistent across frames.
```

## Default Concept-Video Style Prompt Block

Use this block for new video-first source frames in this project:

```text
Style/medium: warm modern Indian educational illustration, polished cinematic 9:16 mobile frame, consistent with the matrices and vectors-v2 lessons.
Scene/backdrop: cozy Indian study room with wooden desk, warm desk lamp, notebook, pen, books, small plant, and tablet/phone as the concept surface.
Subject: same recurring Indian teenage learner with dark wavy hair, teal/green shirt, curious expressive face.
Concept visualization: show the abstract idea through tablet overlays, icons, dots, arrows, grids, clusters, scan lines, glow, or visual transformations.
Text constraints: minimal embedded text only; prefer icons and visual structure; no dense labels or poster-like explanation.
Avoid: flat white diagram card, unrelated environment, changed character style, logos, watermark, tiny unreadable text.
```

## Style Reference Assets

Inspect these before generating a new concept-video frame set:

- `assets/images/matrices-images-become-numbers-video-first/`
- `assets/images/vectors-how-ai-compares-meaning-video-first-v2/`

The contact sheet should look like it belongs in the same series as these references. If it does not, revise the prompts before creating Runway clips.

## What Breaks Consistency

Avoid:

- changing outfit color
- changing hairstyle
- switching from child to older teen/adult
- changing gender presentation
- changing illustration style between frames
- switching from desk scene to unrelated location without reason
- asking for too many new props in every scene
- extreme camera angles that hide the character

## Consistency Workflow

1. Generate or choose one anchor frame.
2. Use that frame as the visual reference when possible.
3. Repeat the character bible in every prompt.
4. Generate a contact sheet of all frames.
5. Reject frames where the character drifts too much.
6. Only send approved source frames to image-to-video.

## Contact Sheet Check

Check:

- same age?
- same hair?
- same outfit?
- same face style?
- same environment?
- same phone/textbook/notebook motif?
- expressions vary naturally without changing identity?

For product use, store the accepted anchor image and character bible together.
