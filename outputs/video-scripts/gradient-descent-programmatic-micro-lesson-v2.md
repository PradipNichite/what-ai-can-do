# Gradient Descent Programmatic Micro-Lesson v2

Purpose: wrap the technical curve animation inside a self-contained teaching flow so the motion is not isolated.

Manifest JSON: `outputs/video-manifests/gradient-descent-programmatic-micro-lesson-v2.json`

Renderer: `tools/render_programmatic_animation.py`

Animation backend: `pillow`

Renderer strategy: `programmatic-technical-animation`

## Render Command

```powershell
python tools/render_programmatic_animation.py `
  --spec outputs/video-manifests/gradient-descent-programmatic-micro-lesson-v2.json `
  --backend auto `
  --out outputs/video-renders/gradient-descent-programmatic-micro-lesson-v2.mp4 `
  --poster outputs/video-renders/gradient-descent-programmatic-micro-lesson-v2-poster.png `
  --report outputs/video-renders/gradient-descent-programmatic-micro-lesson-v2.render-report.json
```

## Learning Design

- School concept: slope and direction on a curve.
- AI use: reducing model error during training.
- Mechanism focus: optimization.
- Visual promise: show why "move opposite the gradient" lowers loss.

## Scene Timing

| Time | Visual action | Teaching job |
|---|---|---|
| 0.0-3.4s | Wrong prediction becomes a loss score | Give the animation a reason to exist |
| 3.4-6.0s | Loss curve appears as a map of possible settings | Bridge from mistake to curve |
| 6.0-15.2s | Dot steps down the curve and loss meter falls | Teach the core mechanism |
| 15.2-17.4s | Overshoot warning | Show why step size matters |
| 17.4-20.0s | Three-step recap | Make the takeaway self-contained |

## Text Readability Notes

This version intentionally uses short captions, larger fonts, and fewer simultaneous labels than v1. The contact sheet should be checked before using the clip in a final video.
