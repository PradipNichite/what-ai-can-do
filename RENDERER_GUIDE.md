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

For reusable lesson series, keep a renderer-agnostic lesson core. The core should not contain video-only timing, image-generation wording, or platform-specific design decisions. Those belong in renderer files.

When improving a lesson, update in this order:

1. Lesson core or source module.
2. Renderer adaptation notes.
3. Image prompts, video scripts, slide copy, or interactive copy.
4. Generated assets and QA notes.

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
| Programmatic technical animation | Code-controlled graphs, arrows, points, counters, and simulations | Asking image-to-video to preserve precise math or text-heavy diagrams |
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

Still run visual QA with ChatGPT vision inspection of the rendered frames. Generated text can be excellent, but every frame must be visually reviewed.

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

## Motion Strategy Classifier

Before generating clips for a shorts video, classify each scene's motion job.
The classifier should decide:

- whether the scene needs animation at all
- whether precise code-controlled animation is required
- whether image-to-video is the better fit for human, camera, or environmental motion
- whether a hybrid overlay is needed because generated context and exact technical labels both matter
- which backend/provider fields should be stored for later comparison

Current local command:

```powershell
python tools/classify_scene_motion_strategy.py `
  --source-module modules/visual-ai-concepts/gradient-descent-how-ai-learns-from-mistakes.source.md `
  --out outputs/video-manifests/gradient-descent-motion-strategy-v1.json `
  --md-out outputs/video-scripts/gradient-descent-motion-strategy-v1.md
```

The resulting JSON is the machine-readable routing source. The matching
Markdown file is the human review surface. Downstream manifests should carry the
classification forward instead of burying the decision inside prompts.

## Programmatic Technical Animation

Use programmatic animation when the motion itself teaches the mechanism.

Programmatic animation must not replace an approved visual style. For the
How AI Uses Math shorts, preserve the specific style reference selected for the
lesson. For Gradient Descent, the current recovery direction is the full
native-story gold candidate, not the rejected close-cropped tablet experiment.
A standalone flat graph/card render is a failed direction unless the approved
renderer for that lesson is explicitly a flat diagram.

Best fits:

- graph points moving along a curve
- vectors changing direction or distance
- matrices transforming pixels into numbers
- probability bars, meters, and thresholds changing over time
- search/ranking/scoring flows where numbers update
- algorithm steps that must stay readable and repeatable

Rules:

- Keep the concept source in the lesson core.
- Store machine-readable animation specs under `outputs/video-manifests/`.
- Store the human-readable timing/review note under `outputs/video-scripts/`.
- Render MP4s under `outputs/video-renders/`.
- Include `renderer_strategy` and `animation_backend` fields in each manifest so experiments can switch implementations without rewriting lesson intent.
- Run `python tools/verify_video_motion.py <video> --samples 12` after rendering.
- Production shorts use ElevenLabs voiceover, image-to-video clips for motion, and Creatomate API assembly. Local still-image assembly is only a timing/debug preview.
- Use image-to-video for human/cinematic motion and production video motion. Use programmatic animation only for precise technical inserts when image-to-video would warp math or labels.
- Do not call motion verification a visual QA pass. Inspect the rendered contact sheet against `VISUAL_QA_CHECKLIST.md`, the series guide, and the accepted source-frame QA before using any clip as a candidate.
- If a programmatic render looks like a PPT/tutorial card while the accepted style is a native story scene, mark it `reject` even if the math is correct.

Backend options to keep swappable:

| Backend | Status | Best Use |
|---|---|---|
| `pillow` | implemented local prototype | Fast deterministic proof of graphs, arrows, counters, and simple 2D mechanisms |
| `motion-canvas` | target candidate | TypeScript procedural educational animation with strong preview/audio workflow |
| `revideo` | target candidate | Motion Canvas-style templates with API rendering and dynamic inputs |
| `remotion` | target candidate | React-based video apps, captions, media composition, and scalable rendering |
| `manim` | specialist fallback | Math-heavy graph/LaTeX scenes when Python/Manim primitives are the cleanest fit |

Do not hard-code one renderer as the permanent answer. Choose a default for speed, but keep the manifest fields stable enough to compare backends on the same learning beat.

Current local prototype:

```powershell
python tools/render_programmatic_animation.py `
  --spec outputs/video-manifests/gradient-descent-programmatic-animation-v1.json `
  --backend auto `
  --out outputs/video-renders/gradient-descent-programmatic-animation-v1.mp4 `
  --poster outputs/video-renders/gradient-descent-programmatic-animation-v1-poster.png `
  --report outputs/video-renders/gradient-descent-programmatic-animation-v1.render-report.json
```

## Renderer Review Questions

Before finalizing a renderer, ask:

- Does this feel native to the medium?
- Could someone understand the main idea quickly?
- Is there too much reading?
- Does each frame or section reveal only one idea?
- Does the format work for the intended device?
- Is the Indian context visible without feeling forced?
- Has the rendered output passed ChatGPT vision QA, including visible text rendering in the actual image?

See `VISUAL_QA_CHECKLIST.md` before marking any visual renderer complete.
