# Gradient Descent Source Frame Review Notes

Image set: `gradient-descent-how-ai-learns-from-mistakes-video-first`

Contact sheet: `gradient-descent-video-first-source-contact-sheet.jpg`

## Overall Read

The set fits the newer Direction B math-series style: realistic warm study desk, recurring Indian teenage learner, teal/green shirt, wooden desk, lamp, notebook/books/plant, and tablet-based technical overlays.

The sequence clearly shows gradient descent as repeated training improvement rather than only a derivative/slope explanation:

```text
wrong prediction -> loss -> loss curve -> downhill direction -> small update -> lower loss -> repeat -> step-size check
```

## Frame Notes

| # | Frame | Review |
|---|---|---|
| 1 | Wrong prediction | Strong setup after regeneration. The input image is visibly a cat while the model predicts dog and the correct answer is cat. Text is readable. |
| 2 | Measure loss | Loss meter and error gap are visually clear. Small labels inside the prediction/correct chips may not survive image-to-video; voiceover should carry those details. |
| 3 | Loss curve | Large U-shaped loss curve reads well on mobile. Point is high on the curve and clearly visible. |
| 4 | Gradient direction | Downhill arrow is clear and connects slope to lower error. Extra axis labels appeared despite prompt constraints; acceptable for draft, but text preservation should be checked before Runway use. |
| 5 | Small update | Best technical frame. The old point, new point, short step, and update visual are readable. Text-heavy enough to require locked-camera video prompting. |
| 6 | Lower loss | Shows lower meter and closer prediction/correct chips. Prediction is improved but not perfect, which is technically useful. Some chip text is small. |
| 7 | Repeat | Strong repeated-update frame. Dotted path descends toward the valley and clearly communicates many small steps. |
| 8 | Step size check | Small-step path vs too-far overshoot is readable and visually distinct. Good quick-check frame. |

## Text And Math Risks Before Video Generation

- Frame 4 includes extra labels such as `Loss` and model-parameter axis text. These are not harmful, but Runway may warp them.
- Frame 5 includes the update visual `weight -> weight - small step`. Use a locked-text prompt and reject if the formula mutates.
- Frame 2 and Frame 6 have small internal chip labels. The voiceover should not depend on those being perfectly readable.
- Frame 8 has two short labels that are important for the quick check; preserve with locked camera and no new text.

## Recommended Runway Handling

- Use locked-camera prompts for Frames 4, 5, 6, and 8 because text/graph integrity matters.
- Use subtle motion only: curve draw, point step, meter shrink, dotted path sequence.
- Avoid strong zooms or rotations; the tablet overlays are the lesson.
- Reject any clip where the point moves uphill, the small step becomes a large jump, or the overshoot path looks like the successful path.

## Acceptance Check

- Repeated improvement is visible: yes.
- Loss curve and downhill steps are readable on mobile: yes.
- Point moves from higher loss to lower loss: yes, especially Frames 5 and 7.
- Learner, desk, lighting, tablet, and palette match newer math lessons: yes.
- Contact sheet belongs beside Functions, Statistics, and Linear Equations: yes.
- Text/math risks noted before video generation: yes.
