# Project Status

Last updated: 2026-06-29

## Current Direction

This project is becoming a multi-format knowledge asset system, not a Markdown-only course.

Each topic should start from a single source explanation, then produce native renderers:

- Markdown explanation
- Desktop visual explanation
- Mobile-first 9:16 visual story
- Image-only visual sequence
- Presentation
- Video storyboard
- Animated video
- Interactive website
- Printable PDF
- Natural local-language versions

The strongest direction so far is mobile-first visual storytelling with generated images where text, illustration, arrows, symbols, and scene progression are integrated into the image itself.

## Important Product Decisions

- Do not make the output feel like a blog converted into images.
- Use 9:16 story cards for WhatsApp Status, Instagram Stories, YouTube Community posts, and mobile-first education.
- Captions are allowed, but they should be short and native to the card.
- Generated text inside images is allowed and useful, but every image needs visual QA.
- Marathi localization should sound like natural spoken Marathi, not textbook translation.
- Familiar technical words should remain in English when Marathi speakers naturally use them: AI, Agent, Order, Mobile Number, System, Tool, Prompt, Dashboard, API, Database, etc.
- Educational examples should be student-first and curiosity-building, not random business automation examples.
- Applied mathematics can become its own series, especially concepts students learn in 11th/12th standard and later see in AI, engineering, or data science.

## Completed / Preserved Work

### Customer Support AI Agent

Status: Prototype complete across multiple renderer styles.

Assets:

- Markdown explanation
- Desktop visual journey
- Mobile 9:16 story
- Marathi mobile story
- Captioning pipeline and Marathi rendering QA notes

Important files:

- `modules/business/ai-customer-support-agent.source.md`
- `modules/business/ai-customer-support-agent.md`
- `outputs/mobile-stories/ai-customer-support-agent.md`
- `outputs/mobile-stories/ai-customer-support-agent.mr.md`
- `assets/image-prompts/customer-support-mobile-story.md`
- `assets/images/customer-support-mobile-story/`
- `assets/images/customer-support-mobile-story-mr/`

### How Students Can Use AI To Study Better

Status: Stronger student-first example created.

This became the first better example after moving away from generic business automation.

Important files:

- `modules/education/how-students-can-use-ai-to-study-better.source.md`
- `outputs/mobile-stories/how-students-can-use-ai-to-study-better.md`
- `assets/image-prompts/student-ai-study-story.md`
- `assets/images/student-ai-study-native-story/`
- `research/notes/student-ai-study-native-story-qa.md`

### Derivatives: How AI Learns From Mistakes

Status: Current flagship applied-math prototype.

This module now includes both intuition and a small technical glimpse. It should not merely say "derivatives help AI correct mistakes"; it should show the learner how slope, error, weight, and a small update step connect.

Important files:

- `modules/visual-ai-concepts/derivatives-how-ai-learns-from-mistakes.source.md`
- `outputs/mobile-stories/derivatives-how-ai-learns-from-mistakes.md`
- `assets/image-prompts/derivatives-ai-learning-story.md`
- `assets/images/derivatives-ai-learning-native-story/`
- `research/notes/derivatives-ai-learning-native-story-qa.md`

Current frame count: 8

Key technical frames:

- `02-derivative-at-a-point.png`: tangent slope, tiny step, tiny change.
- `04-derivative-reduces-error.png`: error curve and slope direction.
- `05-the-math-glimpse.png`: `slope = Delta error / Delta weight` and `new weight = old weight - small step x slope`.

## Asset Inventory

Current image folders:

- `assets/images/customer-support-journey/`: 5 images
- `assets/images/customer-support-mobile-story/`: 7 images
- `assets/images/customer-support-mobile-story-mr/`: 7 images
- `assets/images/student-ai-study-native-story/`: 5 images
- `assets/images/derivatives-ai-learning-native-story/`: 8 images

Prompt archives:

- `assets/image-prompts/ai-customer-support-agent-infographic.md`
- `assets/image-prompts/customer-support-visual-journey.md`
- `assets/image-prompts/customer-support-mobile-story.md`
- `assets/image-prompts/student-ai-study-story.md`
- `assets/image-prompts/derivatives-ai-learning-story.md`

## Workflow Learnings

### Image Text QA

Generated text can be strong, especially for English educational cards, but it must be reviewed manually.

For Marathi and Devanagari text, local PIL rendering failed because complex joined letters did not shape correctly. The current safer path is browser/HTML rendering for Marathi overlays, or native image generation followed by manual visual review.

Use:

- `VISUAL_QA_CHECKLIST.md`
- `research/notes/*-qa.md`

### Prompt Preservation

Every generated visual story should have a prompt archive in `assets/image-prompts/`.

The prompt archive should include:

- Frame number
- Intended renderer
- Exact text to render
- Style and composition
- Constraints
- QA notes

### Localization

English should be finalized first, then Marathi should be written naturally.

Marathi should preserve familiar English technical terms and adapt examples for Indian/Maharashtra context where useful.

Use:

- `LOCALIZATION_GUIDE_MARATHI.md`

## Video Pipeline Research

The API-first video generation research has been preserved here:

- `research/notes/api-first-video-generation-pipeline-research.md`

Current recommendation:

- Use still-card animation for most scenes.
- Use image-to-video only for selected high-value moments.
- Assemble final 9:16 videos through a cloud renderer such as Shotstack or Creatomate.

## Recommended Starting Point Tomorrow

Start with the derivatives module.

Recommended next steps:

1. Review the 8-frame derivative story on a phone-sized viewport.
2. Decide whether `05-the-math-glimpse.png` should be regenerated with a cleaner formula area and less decorative UI.
3. Create a Marathi version of the derivative story in natural spoken Marathi.
4. Create a video storyboard version of the derivative story.
5. Decide the next applied-math topic for the series.

Good next applied-math topics:

- Matrices: how images and AI data become grids of numbers.
- Probability: how AI expresses uncertainty.
- Vectors: how AI compares meaning and similarity.
- Functions: how inputs become outputs.
- Optimization: how AI improves step by step.

## Git Snapshot

Latest meaningful content commit before pause:

- `50015d9 Add derivative technical intuition frames`

Pause snapshot commit should preserve this status file and the video pipeline research note.
