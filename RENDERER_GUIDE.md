# Renderer Guide

The project should produce knowledge assets, not only articles.

Each topic should have a stable explanation underneath it, but every output format should feel native to its medium.

## Single Source, Many Renderers

A module source should define:

- Core learner question.
- Familiar real-life situation.
- Human workflow.
- AI capability.
- Required access, tools, or data.
- Limits and human judgment.
- Try-it-yourself activity.
- Local context.
- Sources.

From that source, create renderers:

| Renderer | Native Form | What To Avoid |
|---|---|---|
| Markdown explanation | Guided written lesson | Giant generic blog article |
| Desktop visual explanation | Wide diagrams, classroom cards | Shrinking mobile layouts |
| Mobile 9:16 story | Swipeable frames, one idea per card | Paragraph-heavy slides |
| Image-only version | Comic or visual sequence | Depending on narration |
| Presentation | 5-10 teachable slides | Copying Markdown headings |
| Video storyboard | Scene beats, camera, voiceover | Reading the article aloud |
| Animated video | Motion, transitions, reveals | Static slides with voice |
| Interactive website | Click, reveal, compare, simulate | Static document page |
| Printable PDF | Worksheet, handout, checklist | Tiny screenshots |
| Local language | Natural localized explanation | Literal translation |

## Mobile-First 9:16 Story

This should feel like Instagram Stories, WhatsApp Status, or YouTube Community cards.

Rules:

- One idea per frame.
- Use 9:16 portrait.
- Use large visual actions.
- Use very little text, or short captions when context is needed.
- Let each frame create the next question.
- Prefer characters, emotion, icons, arrows, and repeated objects.
- Design for phone viewing first.

Example frame flow for customer support:

1. Customer's order has not arrived.
2. Customer contacts support.
3. Support asks for Order ID or Mobile Number.
4. Support opens the company System.
5. Support finds the Order.
6. Support reads delivery status.
7. Support explains it to the customer.
8. AI follows the same workflow when connected to tools.
9. Human takes over for refund, damaged item, or angry customer.

## Captioned Mobile Renderer

Captions are allowed when they help the viewer understand the story without external context.

Rules:

- Keep captions short.
- Put captions inside the image for sharing contexts like WhatsApp Status.
- Use natural language, not textbook wording.
- Preserve familiar technical words in English for local-language versions when that is how people speak.
- Do not turn each frame into a paragraph.

## Native Integrated Visual Renderer

When image generation can produce accurate text, prefer native integrated story cards over manual caption overlays.

Use text as part of the visual composition:

- phone UI,
- chat bubbles,
- sticky notes,
- notebook writing,
- mini cards,
- arrows and labels,
- comparison blocks.

This is especially useful for social/mobile education because the viewer experiences one designed card, not an image plus a caption pasted underneath.

Still run visual QA. Generated text can be excellent, but every frame must be reviewed.

## Image-Only Renderer

The image-only version should almost work without narration.

Use:

- Facial expressions.
- Phone screens with symbolic UI.
- Arrows.
- Locked/unlocked systems.
- Database icons.
- Tool icons.
- Human handover gestures.
- Before/after contrast.

Avoid:

- Long captions.
- Dense labels.
- Explaining the concept in text after every image.

## Renderer Review Questions

Before finalizing a renderer, ask:

- Does this feel native to the medium?
- Could someone understand the main idea quickly?
- Is there too much reading?
- Does each frame or section reveal only one idea?
- Does the format work for the intended device?
- Is the Indian context visible without feeling forced?
- Has the rendered output passed visual QA, including text rendering in local scripts?

See `VISUAL_QA_CHECKLIST.md` before marking any visual renderer complete.
