# Gradient Descent Programmatic Classifier Short v3

Purpose: comparison-ready shorts video that follows the motion strategy classifier output instead of using image-to-video for every technical beat.

Manifest JSON: `outputs/video-manifests/gradient-descent-programmatic-classifier-short-v3.json`

Motion strategy source: `outputs/video-manifests/gradient-descent-motion-strategy-v1.json`

Renderer: `tools/render_programmatic_animation.py`

Animation backend: `pillow`

Renderer strategy: `programmatic-technical-animation`

Rendered video: `outputs/video-renders/gradient-descent-programmatic-classifier-short-v3.mp4`

Rendered video with local TTS voiceover: `outputs/video-renders/gradient-descent-programmatic-classifier-short-v3-with-voiceover.mp4`

Local voiceover WAV: `outputs/video-assets/gradient-descent-programmatic-classifier-short-v3.voiceover.wav`

## Render Command

```powershell
python tools/render_programmatic_animation.py `
  --spec outputs/video-manifests/gradient-descent-programmatic-classifier-short-v3.json `
  --backend auto `
  --out outputs/video-renders/gradient-descent-programmatic-classifier-short-v3.mp4 `
  --poster outputs/video-renders/gradient-descent-programmatic-classifier-short-v3-poster.png `
  --report outputs/video-renders/gradient-descent-programmatic-classifier-short-v3.render-report.json
```

## Verification Command

```powershell
python tools/verify_video_motion.py outputs/video-renders/gradient-descent-programmatic-classifier-short-v3.mp4 --samples 12
```

Voiceover comparison version was muxed with local Windows TTS and the bundled
`imageio-ffmpeg` binary. Treat this audio as a timing aid only, not final
ElevenLabs narration.

## Classifier-Based Scene Timing

| Time | Source step | Scene | Strategy | Teaching job |
|---|---:|---|---|---|
| 0.0-3.0s | 1 | Wrong prediction | `image-to-video` | Establish why the model needs learning |
| 3.0-5.7s | 2 | Measure loss | `hybrid-overlay` | Turn the mistake into a visible loss score |
| 5.7-8.3s | 3 | Loss curve | `programmatic-technical-animation` | Show settings mapped to loss |
| 8.3-11.1s | 4 | Gradient direction | `programmatic-technical-animation` | Show uphill gradient direction |
| 11.1-14.0s | 5 | Small update | `programmatic-technical-animation` | Move opposite the gradient |
| 14.0-16.4s | 6 | Lower loss | `hybrid-overlay` | Show the loss score getting lower |
| 16.4-20.2s | 7 | Repeat | `programmatic-technical-animation` | Show repeated small steps |
| 20.2-24.0s | 8 | Quick check | `programmatic-technical-animation` | Show step size overshoot risk |

## Voiceover Draft

Gradient descent starts when a model gets an answer wrong. The mistake becomes a loss score. The loss curve shows which settings are better or worse. The gradient points uphill, so the update moves the other way. Repeating small careful steps lowers the loss. But if the step is too large, it can overshoot the low point.

## Review Notes

- This version uses large on-screen captions so it still works without audio.
- Primary text must remain readable in the contact sheet.
- The technical graph, dot, arrows, and loss meter are code-controlled, so they should not drift or morph between frames.
