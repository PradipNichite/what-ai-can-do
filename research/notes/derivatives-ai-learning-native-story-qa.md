# Derivatives AI Learning Native Story QA

## 2026-06-28 Review

Renderer:

- `assets/images/derivatives-ai-learning-native-story/`

Finding:

- The original five-card sequence successfully explained derivatives as a direction clue rather than a formula.
- The added technical cards improve the learning value by showing tangent slope, error curve direction, and a simple weight-update rule.
- The expanded eight-card sequence is closer to the desired goal: not only "derivative is useful", but a glimpse of how the number is used during AI training.

Risks:

- Frame 8 may be too dense for mobile viewing.
- Generated text includes some extra helpful labels beyond prompts.
- The math-glimpse card includes a decorative icon beside the formula. It does not harm the explanation, but the learner's attention should remain on `new weight = old weight - small step × slope`.
- Human review should confirm if the transition from basketball intuition to model weight/error feels smooth enough.

Technical Frame Review:

- `02-derivative-at-a-point.png`: pass. Clearly shows tangent line, point, tiny step, tiny change, and slope as direction plus speed.
- `04-derivative-reduces-error.png`: pass. Clearly shows error curve, current point, lower error movement, and positive/negative/zero slope cases.
- `05-the-math-glimpse.png`: pass with note. Formula text is readable and useful; the generated visual uses `Δerror / Δweight` and the update rule correctly for an introductory glimpse.

Status:

- `pass` as stronger prototype direction.
- `needs-human-review` before release.
