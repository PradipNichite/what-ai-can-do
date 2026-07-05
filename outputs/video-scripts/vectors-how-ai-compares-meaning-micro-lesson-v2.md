# Vectors: How AI Compares Meaning - Micro-Lesson v2

Status: video-interactive
Pipeline stage: 08 Video / Interactive
Type: Renderer
Parent topic: Vectors: How AI Compares Meaning
Format: micro-lesson
Language: en-IN

## Purpose

Visual style correction after v1 drifted into flat diagram cards. This version matches the matrices lesson style more closely: warm Indian student study setting, tablet-based educational overlays, minimal embedded text, and clearer visual metaphors.

## Files

- Source module: `modules/visual-ai-concepts/vectors-how-ai-compares-meaning.source.md`
- Source frames: `assets/images/vectors-how-ai-compares-meaning-video-first-v2/`
- Prompt pack: `assets/image-prompts/vectors-how-ai-compares-meaning-video-first-v2.md`
- Source contact sheet: `assets/images/vectors-how-ai-compares-meaning-video-first-v2/vectors-video-first-v2-source-contact-sheet.jpg`
- Runway clips manifest: `outputs/video-manifests/vectors-how-ai-compares-meaning-v2-runway-clips.json`
- Manifest JSON: `outputs/video-manifests/vectors-how-ai-compares-meaning-micro-lesson-v2.en.json`
- Voiceover MP3: `outputs/video-assets/vectors-how-ai-compares-meaning-micro-lesson-v1-en.voiceover.mp3`
- Rendered preview video: `outputs/video-renders/vectors-how-ai-compares-meaning-micro-lesson-v2-en.mp4`
- Verification contact sheet: `outputs/video-renders/verification/vectors-how-ai-compares-meaning-micro-lesson-v2-en.contact-sheet.jpg`
- Verification dense sheet: `outputs/video-renders/verification/vectors-how-ai-compares-meaning-micro-lesson-v2-en.dense-sheet.jpg`
- Motion report: `outputs/video-renders/verification/vectors-how-ai-compares-meaning-micro-lesson-v2-en.motion-report.json`

## Learning Design

- `format`: micro-lesson
- `learning_goal`: Understand that AI can compare meaning by turning text into vectors and checking which vectors are close or point in similar directions.
- `why_it_matters`: This explains semantic search, recommendations, embeddings, and retrieval over notes or documents.
- `memory_anchor`: Similar meaning means nearby vectors.
- `quick_check`: Which pair should be closer: car and vehicle, or car and banana?
- `cognitive_load`: medium

## Voiceover Script

In this micro lesson, you will learn how AI compares meaning with vectors. AI can find related meaning even when words differ. A vector is a list of numbers. A sentence becomes a point in meaning space. Similar meanings land close, or point in similar directions. So affordable smartphone can match cheap phone or budget mobile. This powers semantic search, recommendations, and embeddings. Remember: similar meaning means nearby vectors. Quick check: car and vehicle, or car and banana?

## Scene Timing

| # | Scene ID | Duration | Caption |
|---|---|---:|---|
| 1 | `01-related-meaning-search` | 5.0s | What you will learn |
| 2 | `02-sentence-to-vector` | 5.0s | Vector = list of numbers |
| 3 | `03-meaning-space-clusters` | 5.0s |  |
| 4 | `04-vector-direction-angle` | 5.0s | Close or similar direction |
| 5 | `05-semantic-search-nearest` | 5.0s |  |
| 6 | `06-recommendation-nearby` | 5.0s |  |
| 7 | `07-recap-meaning-vectors` | 5.0s | Similar meaning = nearby vectors |
| 8 | `08-final-recap-brief` | 1.4s |  |

## Review Notes

- v2 prioritizes consistency with the matrices visual language over the flat v1 diagram style.
- Frames avoid readable embedded text wherever possible so Runway does not warp labels.
- Rendered preview uses local gentle pan/zoom because Runway credits ran out after the first two v2 clips.
- Verification: 12-sample motion report passed visually with no blank frames; black-ratio metric is inflated by dark desk/hair/lamp content rather than true black borders. Dense half-second sheet shows no blank tail.
