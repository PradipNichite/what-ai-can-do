# Gradient Descent Programmatic Animation v1

Purpose: test a deterministic programmatic-animation lane for technical lesson motion.

Manifest JSON: `outputs/video-manifests/gradient-descent-programmatic-animation-v1.json`

Renderer: `tools/render_programmatic_animation.py`

Animation backend: `pillow`

Renderer strategy: `programmatic-technical-animation`

Expected render:

```powershell
python tools/render_programmatic_animation.py `
  --spec outputs/video-manifests/gradient-descent-programmatic-animation-v1.json `
  --backend auto `
  --out outputs/video-renders/gradient-descent-programmatic-animation-v1.mp4 `
  --poster outputs/video-renders/gradient-descent-programmatic-animation-v1-poster.png `
  --report outputs/video-renders/gradient-descent-programmatic-animation-v1.render-report.json
```

## Learning Design

- School concept: slope and direction on a curve.
- AI use: reducing model error during training.
- Mechanism focus: optimization.
- Motion job: show a point stepping down a loss curve while the loss score decreases.

## Scene Timing

| Time | Visual action | Teaching job |
|---|---|---|
| 0.0-1.0s | Title and programmatic-motion tag appear | Signal this is a code-controlled technical animation |
| 1.0-2.2s | Loss curve draws in | Establish the loss landscape |
| 2.2-6.4s | Dot steps down the curve; loss meter decreases | Show repeated updates reducing error |
| 2.6-6.4s | Red tangent and green opposite arrow remain visible | Show that the gradient points uphill and the update moves opposite |
| 6.1-7.3s | Purple overshoot arrow appears | Warn that step size matters |
| 7.3-8.0s | Final low-loss state holds | Give the learner time to retain the mechanism |

## Review Notes

This is not a replacement for image-only story cards or cinematic image-to-video clips. It is a deterministic technical insert that can be combined with generated source frames, voiceover, captions, and final assembly.
