# Gradient Descent Complete Lesson Hybrid Creatomate v2

Purpose: rebuild the hybrid architecture as a complete lesson, not a motion demo. The animation remains a small technical insert inside the approved native-story style.

Manifest JSON: `outputs/video-manifests/gradient-descent-complete-lesson-hybrid-creatomate-v2.en.json`

Creatomate cloud render: https://f002.backblazeb2.com/file/creatomate-c8xg3hsxdu/4ac20d82-42e0-4a89-85fb-1fc682944d12.mp4

Local QA copy: `outputs/video-renders/gradient-descent-complete-lesson-hybrid-creatomate-v2-en.mp4`

Visual QA: `outputs/video-renders/verification/gradient-descent-complete-lesson-hybrid-creatomate-v2.visual-qa.md`

Style reference contact sheet: `assets/images/gold-candidates/gradient-descent-scene-gated-full-v3/gradient-descent-scene-gated-full-v3-contact-sheet.jpg`

Accepted style reference QA: `assets/images/gold-candidates/gradient-descent-scene-gated-full-v3/gradient-descent-scene-gated-full-v3-qa.md`

Programmatic insert spec: `outputs/video-manifests/gradient-descent-native-story-programmatic-insert-v1.json`

ElevenLabs voice: `Zara - Soft and Serene Indian Voice` (`ADd2WEtjmwokqUr0Y5Ad`)

## Minimum Lesson Gate

- School concept: slope on a graph.
- AI use: training a model by reducing prediction error.
- Concrete example: a tiny model predicts dog when the correct answer is cat.
- Mechanism chain: prediction -> loss -> loss curve -> slope/gradient -> opposite small step -> repeat.
- Memory anchor: measure loss, read the slope, step carefully.
- Quick check: why not one huge jump?

## Voiceover

In this lesson, slope from school graphs becomes a tool for AI training. Our tiny model predicts dog, but the answer is cat, so we measure the mistake as loss. On the loss curve, some weight settings create high loss and some lower loss. The slope tells which direction makes loss rise, so gradient descent steps the opposite way. One small update lowers the loss. Then AI repeats: measure loss, read the slope, step carefully. Quick check: why not one huge jump? Because it can overshoot the low-loss valley.

## Motion Mix

| Scene | Learning beat | Motion source |
|---|---|---|
| 1 | opener: school slope helps AI training reduce error | Runway image-to-video |
| 2 | concrete example: dog/cat mistake becomes loss | Runway image-to-video |
| 3 | representation: settings map to high or low loss | Runway image-to-video |
| 4 | school concept bridge: slope tells which way loss rises | Runway image-to-video |
| 5 | exact small update opposite the slope | programmatic technical insert |
| 6 | loss lowers but is not perfect | Runway image-to-video |
| 7 | measure, read slope, step, repeat | Runway image-to-video |
| 8 | quick check: one huge jump can overshoot | Runway image-to-video |

## Production Commands

```powershell
python tools/generate_elevenlabs_voiceover.py `
  --manifest outputs/video-manifests/gradient-descent-complete-lesson-hybrid-creatomate-v2.en.json

python tools/upload_tmpfiles.py `
  outputs/video-assets/gradient-descent-complete-lesson-hybrid-v2.voiceover.mp3 `
  --json-out outputs/video-manifests/gradient-descent-complete-lesson-hybrid-v2.voiceover.uploaded-url.json

python tools/render_creatomate_phase1.py `
  --manifest outputs/video-manifests/gradient-descent-complete-lesson-hybrid-creatomate-v2.en.json `
  --style clean --submit --wait
```

## Review Notes

- This version fixes lesson shape before judging animation.
- It reuses the existing Runway clips and the style-preserving programmatic insert.
- Visual QA status: needs-revision, because the reused Runway loss-score scene retains text/number drift and the Creatomate render is preview-scale.
