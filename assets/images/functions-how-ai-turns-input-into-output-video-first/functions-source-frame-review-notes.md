# Functions Source Frame Review Notes

Topic: Functions: How AI Turns Input Into Output

Status: visual-draft
Pipeline stage: 05 Visual Draft

Source module: `modules/visual-ai-concepts/functions-how-ai-turns-input-into-output.source.md`
Prompt pack: `assets/image-prompts/functions-how-ai-turns-input-into-output-video-first.md`
Contact sheet: `assets/images/functions-how-ai-turns-input-into-output-video-first/functions-video-first-source-contact-sheet.jpg`

## Overall Review

This frame set is technically useful for review. It clearly teaches:

```text
school function -> AI model -> input numbers -> learned transformation -> output scores -> prediction
```

The main issue is visual style. The frames are warmer and study-desk based, but several images lean more realistic/photographic than the established illustrated matrices/vectors style. Before final video production, decide whether to accept this more realistic look or regenerate with a stricter illustration/style-reference pass.

## Frame Notes

| # | File | Technical job | Review |
|---|---|---|---|
| 1 | `01-learning-objective.png` | Connects school function to AI model | Good concept bridge: notebook `input -> f -> output` and tablet `input -> model -> scores`. |
| 2 | `02-familiar-school-function.png` | Reminds learner of `y = f(x)` | Clear school math frame. Slightly more realistic than desired. |
| 3 | `03-ai-input-example.png` | Shows input entering model | Good AI task setup. Model box has technical glow, but learner/style may drift. |
| 4 | `04-input-becomes-numbers.png` | Shows input becoming features/numbers | Strong technical frame. `[fur 1]`, `[ears 1]`, `[wheels 0]` makes the representation step visible. |
| 5 | `05-learned-transformation.png` | Shows learned function transforming numbers | Strongest mechanism frame. It avoids a plain black box by showing number chips moving through model function panels. |
| 6 | `06-output-scores.png` | Shows numeric output scores | Clear score bars. Good separation from probability lesson because these are called scores, not probabilities. |
| 7 | `07-highest-score-prediction.png` | Shows highest score becoming prediction | Clear comparison. Need to avoid implying guaranteed truth in voiceover. |
| 8 | `08-quick-check-output.png` | Learner compares scores | Good quick-check frame with dog as highest score. |

## Technical Teaching Value

Passes:

- Every frame has a visible teaching job.
- The sequence shows the mechanism, not only a student reaction.
- The central idea is technically accurate for high-school level: an AI model can be understood as a learned function from numeric input to output scores.
- The score/probability boundary is mostly preserved.

Risks:

- Style consistency is weaker than matrices/vectors because these frames lean realistic.
- Some frames may need text QA at full size before video generation.
- Character identity is not perfectly stable across frames.
- Features like `[fur 1]` are a simplified teaching representation and should be described as a simple example, not how all models literally represent images.

## Recommendation

Use this as a first visual draft for technical review.

Before Runway/video generation, decide:

1. Keep this more realistic draft and proceed to animatic.
2. Regenerate with a stricter illustrated style reference.
3. Keep the technically strongest frames, especially frames 4-7, and regenerate only frames 1-3/8 for style consistency.
