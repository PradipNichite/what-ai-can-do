# Gradient Descent Warm Minimal Lesson Edit v1

Purpose: complete Gradient Descent short using the accepted Warm Minimal Tablet Closeup style. Animation is limited to already-QA'd in-tablet Runway motion clips.

Manifest JSON: `outputs/video-manifests/gradient-descent-warm-minimal-lesson-edit-v1.json`

Source frames: `assets/images/gradient-descent-how-ai-learns-from-mistakes-video-first-warm-minimal-v1/`

Accepted source-frame QA: `assets/images/gradient-descent-how-ai-learns-from-mistakes-video-first-warm-minimal-v1/gradient-descent-warm-minimal-source-frame-review-notes.md`

Accepted Runway smoke QA: `outputs/runway-clips/gradient-descent-warm-minimal-runway-smoke-v1/gradient-descent-warm-minimal-runway-smoke-v1-qa.md`

Rendered video: `outputs/video-renders/gradient-descent-warm-minimal-lesson-edit-v1.mp4`

Rendered video with local TTS voiceover: `outputs/video-renders/gradient-descent-warm-minimal-lesson-edit-v1-with-voiceover.mp4`

## Render Command

```powershell
python tools/render_local_video_edit.py `
  --manifest outputs/video-manifests/gradient-descent-warm-minimal-lesson-edit-v1.json `
  --out outputs/video-renders/gradient-descent-warm-minimal-lesson-edit-v1.mp4
```

## Verification Command

```powershell
python tools/verify_video_motion.py outputs/video-renders/gradient-descent-warm-minimal-lesson-edit-v1.mp4 --samples 12
python tools/verify_video_style_gate.py outputs/video-manifests/gradient-descent-warm-minimal-lesson-edit-v1.json outputs/video-scripts/gradient-descent-warm-minimal-lesson-edit-v1.md
```

## Scene Timing

| Scene | Source | Duration | Teaching job |
|---|---|---:|---|
| 01 opener bridge | source frame | 3.2s | AI improves by reducing mistakes |
| 02 measure loss | source frame | 3.4s | error becomes a score |
| 03 loss curve | source frame | 3.2s | loss depends on weight setting |
| 04 gradient direction | accepted Runway clip | 5.0s | gradient points uphill; update moves opposite |
| 05 small update | accepted locked-arrow Runway clip | 5.0s | one small weight update |
| 06 lower loss | source frame | 3.4s | lower loss without perfect prediction |
| 07 repeat loop | source frame | 3.4s | repeated updates train the model |
| 08 step-size check | accepted Runway clip | 5.0s | too-large steps can overshoot |

## Voiceover Draft

Gradient descent is how AI learns from mistakes. First, the model makes a wrong prediction. That mistake becomes a loss score. The loss curve shows how different weight settings create different errors. The gradient points toward higher loss, so the update moves the opposite way. One small step changes the weight a little. The loss becomes lower, but not perfect. Training repeats many small steps. If the step is too large, it can overshoot. That is gradient descent: repeated careful steps toward lower error.

## Review Notes

- This is the correct comparison direction after rejecting the flat programmatic v3/v4 renders.
- The style is inherited from the accepted Warm Minimal Tablet Closeup source frames.
- The only animated segments are accepted in-tablet Runway clips for the mechanism-heavy scenes.
- Local TTS is only a review aid; final narration should use the normal production voice path.
