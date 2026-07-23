# Gradient Descent Hybrid Runway + Programmatic Creatomate v1

Purpose: show the combined production pattern: image-to-video for story/cinematic scenes, code-controlled animation for one precise technical beat, ElevenLabs voiceover, and Creatomate API assembly.

Manifest JSON: `outputs/video-manifests/gradient-descent-hybrid-runway-programmatic-creatomate-v1.en.json`

Creatomate cloud render: https://f002.backblazeb2.com/file/creatomate-c8xg3hsxdu/3247ce26-d547-43ba-a75e-53b20774f9c0.mp4

Visual QA: `outputs/video-renders/verification/gradient-descent-hybrid-runway-programmatic-creatomate-v1-en.visual-qa.md`

Style reference contact sheet: `assets/images/gold-candidates/gradient-descent-scene-gated-full-v3/gradient-descent-scene-gated-full-v3-contact-sheet.jpg`

Accepted style reference QA: `assets/images/gold-candidates/gradient-descent-scene-gated-full-v3/gradient-descent-scene-gated-full-v3-qa.md`

Programmatic insert spec: `outputs/video-manifests/gradient-descent-native-story-programmatic-insert-v1.json`

ElevenLabs voiceover: `outputs/video-assets/gradient-descent-native-story-lesson-edit-v1.voiceover.mp3`

## Motion Mix

| Scene | Learning beat | Motion source |
|---|---|---|
| 1 | wrong prediction starts learning | Runway image-to-video |
| 2 | mistake becomes loss score | Runway image-to-video |
| 3 | loss curve appears | Runway image-to-video |
| 4 | slope gives direction | Runway image-to-video |
| 5 | one small update | programmatic technical insert |
| 6 | lower error after update | Runway image-to-video |
| 7 | repeat to learn | Runway image-to-video |
| 8 | step-size quick check | Runway image-to-video |

## Production Commands

```powershell
python tools/render_native_story_programmatic_insert.py `
  --spec outputs/video-manifests/gradient-descent-native-story-programmatic-insert-v1.json `
  --out outputs/video-renders/gradient-descent-native-story-programmatic-insert-v1.mp4

python tools/upload_tmpfiles.py `
  outputs/video-renders/gradient-descent-native-story-programmatic-insert-v1.mp4 `
  --json-out outputs/video-manifests/gradient-descent-native-story-programmatic-insert-v1.uploaded-url.json

python tools/render_creatomate_phase1.py `
  --manifest outputs/video-manifests/gradient-descent-hybrid-runway-programmatic-creatomate-v1.en.json `
  --style clean --submit --wait
```

## Notes

- This is not a local still-image assembly.
- Scenes 1-4 and 6-8 are image-to-video clips.
- Scene 5 is the code-controlled insert, because the old-to-new point movement and labels are precision-sensitive.
- Creatomate is the assembly layer, and ElevenLabs is the voice path.
