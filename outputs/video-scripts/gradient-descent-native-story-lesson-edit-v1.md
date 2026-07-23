# Gradient Descent Native Story Lesson Edit v1

Purpose: recover the earlier full native educational story style for a complete Gradient Descent short. This replaces the rejected cropped tablet-closeup direction for comparison.

Manifest JSON: `outputs/video-manifests/gradient-descent-native-story-lesson-edit-v1.json`

Source frames: `assets/images/gold-candidates/gradient-descent-scene-gated-full-v3/`

Accepted source-frame QA: `assets/images/gold-candidates/gradient-descent-scene-gated-full-v3/gradient-descent-scene-gated-full-v3-qa.md`

Style reference contact sheet: `assets/images/gold-candidates/gradient-descent-scene-gated-full-v3/gradient-descent-scene-gated-full-v3-contact-sheet.jpg`

Local preview video: `outputs/video-renders/gradient-descent-native-story-lesson-edit-v1.mp4`

Production assembly manifest: `outputs/video-manifests/gradient-descent-native-story-runway-creatomate-v1.en.json`

Runway image-to-video manifest: `outputs/video-manifests/gradient-descent-native-story-runway-clips-v1.json`

ElevenLabs voiceover MP3: `outputs/video-assets/gradient-descent-native-story-lesson-edit-v1.voiceover.mp3`

Creatomate cloud render: https://f002.backblazeb2.com/file/creatomate-c8xg3hsxdu/dfde867e-46e7-4315-a531-9f077786b06d.mp4

Visual QA: `outputs/video-renders/verification/gradient-descent-native-story-runway-creatomate-v1-en.visual-qa.md`

## Render Commands

```powershell
python tools/generate_elevenlabs_voiceover.py `
  --manifest outputs/video-manifests/gradient-descent-native-story-lesson-edit-v1.json

python tools/generate_runway_clips.py `
  --manifest outputs/video-manifests/gradient-descent-native-story-runway-clips-v1.json `
  --all --submit --wait

python tools/render_creatomate_phase1.py `
  --manifest outputs/video-manifests/gradient-descent-native-story-runway-creatomate-v1.en.json `
  --style clean --submit --wait
```

## Lesson Flow

| # | Scene | Duration | Teaching job |
|---|---|---:|---|
| 1 | mistake starts learning | 4.4s | wrong prediction starts the learning loop |
| 2 | mistake becomes loss | 4.2s | mistake becomes a loss score |
| 3 | loss curve | 4.0s | loss depends on model setting |
| 4 | slope gives direction | 4.7s | gradient points to higher loss; update moves opposite |
| 5 | one small update | 4.3s | one small update changes the weight |
| 6 | lower error | 4.1s | loss becomes lower but not perfect |
| 7 | repeat to learn | 4.4s | training repeats many small steps |
| 8 | step size matters | 4.5s | too-large steps can overshoot |

## Voiceover

Gradient descent is how AI learns from mistakes. First, the model predicts dog, but the correct answer is cat. That mistake becomes a loss score. The loss curve shows which model settings create high or low error. The slope points toward higher loss, so gradient descent moves the opposite way. One small step changes the weight. The loss becomes lower, but not perfect. Then training repeats: check the loss, take another small step, and keep improving. But if the step is too large, it can overshoot. Remember: gradient descent means repeated careful steps toward lower error.

## Notes

- This edit uses the older full native-story gold candidate, not the rejected close-cropped tablet style.
- Production output must use Runway image-to-video clips and Creatomate API assembly. The local still-image preview is not a deliverable.
- Code-controlled animation should only be added later as a small technical enhancement if it preserves this full composition.
- Voiceover is generated through ElevenLabs, not local Windows TTS.
