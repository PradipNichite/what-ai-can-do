# Gradient Descent Complete Lesson Short v4

Purpose: a complete micro-lesson first, with programmatic animation used only where it helps the mechanism.

Manifest JSON: `outputs/video-manifests/gradient-descent-complete-lesson-short-v4.json`

Source module: `modules/visual-ai-concepts/gradient-descent-how-ai-learns-from-mistakes.source.md`

Motion strategy source: `outputs/video-manifests/gradient-descent-motion-strategy-v1.json`

Renderer: `tools/render_programmatic_animation.py`

Animation backend: `pillow`

Renderer strategy: `hybrid-complete-lesson-with-programmatic-mechanism`

Rendered video: `outputs/video-renders/gradient-descent-complete-lesson-short-v4.mp4`

Rendered video with local TTS voiceover: `outputs/video-renders/gradient-descent-complete-lesson-short-v4-with-voiceover.mp4`

Local voiceover WAV: `outputs/video-assets/gradient-descent-complete-lesson-short-v4.voiceover.wav`

## Lesson Intent

This version follows the project guide: applied math understanding, technically correct explanation, one concrete example, visible mechanism, and a retained concept-to-AI connection.

The animation is not the product. The product is the lesson:

```text
slope on a graph -> loss score -> small opposite-gradient update -> repeated lower loss
```

## Render Command

```powershell
python tools/render_programmatic_animation.py `
  --spec outputs/video-manifests/gradient-descent-complete-lesson-short-v4.json `
  --backend auto `
  --out outputs/video-renders/gradient-descent-complete-lesson-short-v4.mp4 `
  --poster outputs/video-renders/gradient-descent-complete-lesson-short-v4-poster.png `
  --report outputs/video-renders/gradient-descent-complete-lesson-short-v4.render-report.json
```

## Verification Command

```powershell
python tools/verify_video_motion.py outputs/video-renders/gradient-descent-complete-lesson-short-v4.mp4 --samples 12
```

## Scene Timing

| Time | Scene | Teaching job | Strategy |
|---|---|---|---|
| 0.0-5.0s | Opener | Connect school slope to AI training | designed lesson card |
| 5.0-10.0s | Mistake/loss | Make the cat/dog mistake concrete | hybrid overlay |
| 10.0-14.5s | Setting | Show that training changes a model setting | designed lesson card |
| 14.5-23.0s | Mechanism | Animate the gradient/update mechanism | programmatic technical animation |
| 23.0-28.5s | Repeat | Show loss reducing through repeated updates | designed lesson card |
| 28.5-32.5s | Step size | Show why a huge jump can overshoot | programmatic technical animation |
| 32.5-36.0s | Takeaway | State the memory anchor | designed lesson card |

## Voiceover Draft

Gradient descent is how AI uses slope to reduce mistakes. In this example, the model should say cat, but says dog. That mistake becomes loss: eight out of ten. Training does not directly force the answer. It changes a weight. On the loss curve, the gradient points uphill, toward higher error. So the model moves a small step the opposite way. The loss becomes lower. Repeat this on many examples. If the step is too big, it can overshoot. Remember: repeated small downhill steps on an error curve.

## Review Notes

- The first scene identifies the lesson, school concept, AI use, and concrete example.
- The mechanism scene is animated, but the surrounding scenes carry context, result, repeat loop, and memory anchor.
- This should be compared against the earlier image-to-video short for lesson completeness, not animation amount.
- The local TTS voiceover is only a review aid. Use ElevenLabs or a human voice pass for any final version.
