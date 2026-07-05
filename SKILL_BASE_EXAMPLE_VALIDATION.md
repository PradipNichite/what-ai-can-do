# Skill Base Example Validation

Status: first validation pass

Purpose: validate which existing project artifacts are safe to use as bases for creating new Codex skills.

This is a distinct audit artifact, not a process rule. It is separate from `CODED_SKILLS_PROPOSAL.md` because it records evidence from ChatGPT vision inspection and should be refreshed when candidate examples change.

Important correction: visual suitability must be decided by ChatGPT vision inspection of the actual contact sheets/images. Local pixel checks are not accepted as validation evidence for teaching quality, opener quality, native composition, or visual style.

## Validation Method

Rules checked:

- `IMAGE_STORY_GATE.md`
- `HOW_AI_USES_MATH_SERIES_GUIDE.md`
- `VIDEO_FIRST_VISUAL_GUIDE.md`
- `HOW_AI_USES_MATH_IMAGE_PREREQUISITES.md`

ChatGPT vision checks:

- opener self-contained?
- native generated composition?
- pasted-overlay risk?
- mechanism visible?
- mobile readability likely?
- suitable as image-only story base, video-first base, visual-style reference, lesson-core reference, or failure example?

## File Presence Summary

The checked candidates had image folders and contact sheets available for ChatGPT vision inspection.

Most generated frames appear to be review-sized assets rather than a publish-quality guarantee. Final publication should still inspect exported assets visually.

| Candidate | Frames | Contact sheet | Vision-review caveat |
|---|---:|---:|---|
| `gradient-descent-how-ai-learns-from-mistakes-image-story` | 8 | yes | mechanism positive, opener partial |
| `graphs-how-ai-understands-relationships-image-story` | 8 | yes | failure example |
| `derivatives-ai-learning-native-story` | 8 | yes | older style |
| `vectors-how-ai-compares-meaning-video-first-v3` | 7 | yes | video-first, not image-only |
| `matrices-images-become-numbers-video-first` | 7 | yes | video-first, not image-only |
| `probability-how-ai-handles-uncertainty-video-first` | 8 | yes | video-first, not image-only |
| `vectors-how-ai-compares-meaning-style-b-refresh` | 8 | yes | visual reference, not full opener standard |
| `matrices-how-ai-sees-images-as-numbers-style-b-refresh` | 8 | yes | visual reference, not full opener standard |
| `probability-how-ai-handles-uncertainty-style-b-refresh` | 8 | yes | visual reference, not full opener standard |

## Candidate Vision Verdicts

### Gradient Descent Image Story

Files:

- `assets/image-prompts/gradient-descent-how-ai-learns-from-mistakes-image-story.md`
- `assets/images/gradient-descent-how-ai-learns-from-mistakes-image-story/`
- `assets/images/gradient-descent-how-ai-learns-from-mistakes-image-story/gradient-descent-how-ai-learns-from-mistakes-image-story-review-notes.md`

Visual verdict:

- Mechanism visibility: strong.
- Native tablet-centered composition: strong.
- Sequence coherence: strong.
- Opener under current strict gate: partial. Card 1 introduces the wrong-prediction task, but does not fully name the lesson, school concept, AI use, and learning promise.

Skill-base verdict:

- Use as: mechanism-sequence positive example for `build-image-story-prompt-pack`.
- Do not use as: perfect opener example.
- Required note for skill creation: copy the mechanism progression, but require a stronger card 1 than this example has.

### Graphs Image Story

Files:

- `assets/image-prompts/graphs-how-ai-understands-relationships-image-story.md`
- `assets/images/graphs-how-ai-understands-relationships-image-story/`
- `assets/images/graphs-how-ai-understands-relationships-image-story/graphs-how-ai-understands-relationships-image-story-review-notes.md`

Visual verdict:

- Mechanism visibility after card 2: strong enough.
- Opener: fails current gate.
- Native composition: fails/at risk because headline text feels like a large overlay on a study-desk scene.
- Existing review note already marks it `needs-revision`.

Skill-base verdict:

- Use as: negative example for `review-image-story-contact-sheet`.
- Do not use as: positive base for image-story generation.
- Required note for skill creation: this is the failure pattern for "mechanism later is not enough if the opener fails."

### Derivatives Native Story

Files:

- `assets/image-prompts/derivatives-ai-learning-story.md`
- `assets/images/derivatives-ai-learning-native-story/`
- `assets/images/derivatives-ai-learning-native-story/derivative-source-contact-sheet.jpg`
- `assets/images/derivatives-ai-learning-native-story/derivatives-refresh-decision.md`

Visual verdict:

- Opener: strong and self-contained at the topic level.
- Technical teaching: strong.
- Current style match: weak/dated compared with the newer warm tablet Direction B style.
- Video-first suitability: weak because it is poster-heavy and dense.

Skill-base verdict:

- Use as: lesson-structure and opener-density reference.
- Do not use as: current visual-style reference or video-first prompt base.
- Required note for skill creation: preserve the explicit learning opener, but use newer Direction B visual style.

### Vectors Video-First V3

Files:

- `assets/image-prompts/vectors-how-ai-compares-meaning-video-first-v3.md`
- `assets/images/vectors-how-ai-compares-meaning-video-first-v3/`

Visual verdict:

- Video-first mechanism visibility: strong.
- Style consistency: strong.
- Image-only self-contained standard: not applicable; it assumes voiceover and sparse frame text.

Skill-base verdict:

- Use as: positive base for `build-video-first-prompt-pack`.
- Do not use as: image-story prompt-pack base.
- Required note for skill creation: preserve per-frame visual evidence, low text, and motion-friendly layout.

### Matrices Video-First

Files:

- `assets/image-prompts/matrices-images-become-numbers-video-first.md`
- `assets/images/matrices-images-become-numbers-video-first/`

Visual verdict:

- Mechanism progression: strong: phone photo -> pixels -> brightness numbers -> matrix -> RGB -> scan -> recap.
- Video-first layout: strong.
- Image-only opener: insufficient under current gate.

Skill-base verdict:

- Use as: positive video-first mechanism sequence.
- Do not use as: complete image-story example.

### Probability Video-First

Files:

- `assets/image-prompts/probability-how-ai-handles-uncertainty-video-first.md`
- `assets/images/probability-how-ai-handles-uncertainty-video-first/`
- `assets/images/probability-how-ai-handles-uncertainty-video-first/probability-source-frame-review-notes.md`

Visual verdict:

- Mechanism progression: strong: possible answers -> probability scale -> scores -> chosen answer -> close-score uncertainty -> AI systems -> recap -> quick check.
- Video-first style: strong.
- Frame 6 and 7 are text-dense/small, matching the existing review caveats.
- Image-only opener: insufficient under current gate.

Skill-base verdict:

- Use as: positive video-first base with explicit caveats.
- Do not use as: image-story base.

### Direction B Style Refresh Sets

Files:

- `assets/images/vectors-how-ai-compares-meaning-style-b-refresh/`
- `assets/images/matrices-how-ai-sees-images-as-numbers-style-b-refresh/`
- `assets/images/probability-how-ai-handles-uncertainty-style-b-refresh/`

Visual verdict:

- Strong current visual language: warm desk, tablet-centered technical UI, compact mechanism panels.
- Good mobile-readable technical objects.
- Not sufficient as full image-story gate examples because card 1 generally starts with the example/mechanism rather than a complete lesson opener.

Skill-base verdict:

- Use as: current visual-style references.
- Do not use as: accepted image-story examples unless paired with a stronger opener requirement.

## Recommended Base Set By Skill

### `create-ai-math-micro-lesson`

Use canonical docs first, not visual assets:

- `HOW_AI_USES_MATH_SERIES_GUIDE.md`
- `HOW_AI_USES_MATH_LESSON_CORE_TEMPLATE.md`
- `HOW_AI_USES_MATH_SERIES_PLAN.md`
- `HOW_AI_USES_MATH_IMAGE_PREREQUISITES.md`

Use source modules only after a field-level review for required lesson-core fields:

- `modules/visual-ai-concepts/probability-how-ai-handles-uncertainty.source.md`
- `modules/visual-ai-concepts/vectors-how-ai-compares-meaning.source.md`
- `modules/visual-ai-concepts/gradient-descent-how-ai-learns-from-mistakes.source.md`

Do not call these source modules "best examples" until field-level validation is done.

### `build-image-story-prompt-pack`

No current artifact should be treated as a perfect positive base.

Use a composite base:

- Derivatives for self-contained opener density.
- Gradient Descent for mechanism sequence and native tablet composition.
- Direction B refresh sets for current visual style.
- Graphs as the explicit failure case to avoid.

The skill must state that the new prompt pack should improve on the examples by satisfying all opener fields in `IMAGE_STORY_GATE.md`.

### `review-image-story-contact-sheet`

Use:

- Gradient Descent as a mostly positive review with caveats.
- Graphs as a negative review.

The review skill should be calibrated to reject Graphs-like failures even when later mechanism cards are strong.

### `build-video-first-prompt-pack`

Use:

- Vectors video-first v3 as the strongest style/mechanism base.
- Matrices video-first as a clean transformation-sequence base.
- Probability video-first as a scoring/uncertainty base with text-density caveats.

Do not use image-only stories as video-first bases except as conceptual references.

## Final Position

The examples are not all "best examples."

Validated use should be more precise:

- Positive for video-first: Vectors v3, Matrices, Probability.
- Positive for mechanism-rich image-story composition: Gradient Descent, with opener caveat.
- Positive for explicit opener structure: Derivatives, with old-style caveat.
- Negative calibration example: Graphs.
- Current visual-style reference: Direction B refresh sets.

No image-only example currently qualifies as a perfect gold-standard base under the strict current gate.
