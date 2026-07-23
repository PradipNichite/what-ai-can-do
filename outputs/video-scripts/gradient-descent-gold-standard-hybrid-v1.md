# Gradient Descent Gold Standard Hybrid v1

Purpose: create the flagship hybrid micro-lesson for "How AI Uses Math" by combining native story image-to-video, a precise embedded programmatic mechanism insert, ElevenLabs voiceover, and Creatomate assembly. This is a lesson-design blueprint, not a rendered candidate yet.

Status: `source-draft`

Source module: `modules/visual-ai-concepts/gradient-descent-how-ai-learns-from-mistakes.source.md`

Supersedes: `outputs/video-scripts/gradient-descent-complete-lesson-hybrid-creatomate-v2.md`

Style reference contact sheet: `assets/images/gold-candidates/gradient-descent-scene-gated-full-v3/gradient-descent-scene-gated-full-v3-contact-sheet.jpg`

Style reference note: the old folder name says gold candidate, but its caveated QA is not a clean acceptance. Use it only as reference for native educational story language until the new version earns clean visual QA.

Required before media generation:

- clean scene adequacy pass
- regenerated source frames or repaired prompt pack
- contact sheet inspected with ChatGPT vision
- no `pass-with-caveats` promotion

## Gold Standard Thesis

This video should make a cold student feel a real learning progression, not just engagement. The learner should be able to explain:

```text
The model has a current setting. That setting makes a prediction. The mistake becomes loss. The current setting becomes a point on a loss curve. The slope tells which way loss rises. Gradient descent steps the opposite way, checks the new loss, and repeats.
```

## Format

- Type: micro-lesson, not hook-first short
- Target length: 70-85 seconds
- Aspect ratio: 9:16
- Voice: calm Indian-English educator
- Visual world: native warm student/tablet story
- Technical insert: one embedded programmatic tablet sequence, styled as part of the same lesson world

## Motion Policy

Use image-to-video for human context, example continuity, loss-meter reveal, learner attention, and recap flow.

Use programmatic animation only for the exact mechanism island:

```text
loss curve -> W1 point -> tangent -> gradient/uphill cue -> opposite update arrow -> W2 point -> lower loss
```

The programmatic insert must appear on the tablet/notebook surface as a style-preserving enhancement. It must not become a standalone flat white graph scene.

## Scene Plan

| # | Time | Beat | Lane | Cold-student question answered |
|---|---:|---|---|---|
| 1 | 0-5s | Learning promise: school slope helps AI reduce error | image-to-video | What lesson is this? |
| 2 | 5-10s | Familiar slope: a curve has a local direction | image-to-video | What school idea are we using? |
| 3 | 10-16s | Tiny AI task: animal example enters a model | image-to-video | What concrete AI task are we following? |
| 4 | 16-22s | Current setting W1 predicts dog, target is cat | image-to-video | What object is wrong? |
| 5 | 22-28s | The mistake becomes `loss 8/10` | image-to-video / hybrid overlay | What changed from prediction to score? |
| 6 | 28-34s | W1 is placed on the loss curve | image-to-video | Why are we looking at a graph? |
| 7 | 34-42s | Tangent and gradient show higher-loss direction | programmatic insert | What does slope tell us here? |
| 8 | 42-49s | Opposite small step moves W1 to W2 | programmatic insert | Why does the point move that way? |
| 9 | 49-56s | W2 gives lower loss, but not perfect | programmatic insert + story return | Did the step help, and is learning finished? |
| 10 | 56-64s | Repeat loop: measure, slope, opposite step, check | image-to-video | Why is this called training? |
| 11 | 64-74s | Quick check: small steps vs huge overshoot | image-to-video with controlled graph overlay | Why not one huge jump? |
| 12 | 74-82s | Memory anchor recap | image-to-video | What should I remember? |

## Voiceover Draft

In this lesson, slope from school graphs becomes a tool for AI training.

First, remember what slope gives you: at one point on a curve, it tells which way the curve is rising.

Now follow one tiny AI example. The model sees an animal image. Its current setting, W1, predicts dog, but the correct answer is cat.

That mismatch becomes a number called loss. Here the loss is high: 8 out of 10.

To improve, the model asks a graph question: if I changed this setting, would the loss go up or down?

On the loss curve, W1 is a high-loss point. The local slope points toward higher loss. So gradient descent does the important move: it takes a small step in the opposite direction.

Now the model is at W2. It checks again. The prediction is closer, and loss drops to 5 out of 10. Not perfect, but better.

Training is this loop repeated: measure the loss, read the slope, step opposite, check again.

Quick check: why not one huge jump? Because the slope is only a local clue. A huge step can overshoot the low-loss valley and land at higher loss.

Memory anchor: gradient descent means measure loss, read slope, step opposite, repeat.

## Visual Requirements By Scene

| # | Source frame requirement | Motion target | Must avoid |
|---|---|---|---|
| 1 | Title, school notebook slope, AI training tablet, same learner | subtle push-in, bridge line lights | vague motivational opener |
| 2 | Simple curve and tangent in notebook | pencil draws tangent | dense derivative notation |
| 3 | Animal image/input card, tiny model panel, target cat card waiting | input slides into model | generic glowing AI |
| 4 | W1 badge connected to prediction chips | dog prediction appears, target cat stays fixed | losing W1 continuity |
| 5 | Gap between dog prediction and cat target feeds loss meter | gap lights and fills meter to 8/10 | loss as emotional warning |
| 6 | Same W1 badge becomes a point on loss curve | W1 dot lands high on curve | graph appearing without relation to W1 |
| 7 | Tablet graph designed to host programmatic insert | tangent and uphill gradient draw precisely | gradient shown downhill |
| 8 | Old W1, new W2, short opposite arrow | arrow pulses; W2 appears nearby | point sliding wildly along curve |
| 9 | W2 lower on curve, prediction closer, loss 5/10 | meter shrinks; "not perfect yet" cue | implying one step solves training |
| 10 | Loop strip with four icons: loss, slope, opposite step, check | icons light in order | decorative loop without steps |
| 11 | Split graph: careful small steps vs huge overshoot | huge arrow lands higher; small path descends | huge jump looking faster/better |
| 12 | Recap chain on tablet with learner satisfied but still studying | chain lights once | slogan-only ending |

## Programmatic Insert Spec

The insert should be rendered as a transparent or tablet-background-compatible animation layer:

- background: warm off-white tablet surface, matching native story palette
- axes: `model setting` on x-axis, `loss` on y-axis
- curve: smooth U-shaped loss curve
- points: W1 high on right slope, W2 slightly lower and closer to valley
- labels: `loss`, `W1`, `W2`, `gradient: higher loss`, `opposite step`
- sequence:
  1. draw curve and W1
  2. draw tangent at W1
  3. show uphill gradient cue
  4. pulse short opposite update arrow
  5. reveal W2 lower on curve
  6. shrink loss meter from 8/10 to 5/10
- forbidden: standalone PPT styling, whiteboard-only scene, dense formula panel, full-screen graph that drops the learner/story world

## QA Rubric For This Version

A clean pass requires all of these:

- A cold student can identify the tracked object: current setting W1, then W2.
- Every scene answers what changed and why the next scene follows.
- The graph is introduced as "loss changes when the setting changes," not as a random math visual.
- The gradient/uphill direction and opposite update direction are visually distinct.
- The programmatic insert preserves the native story style instead of replacing it.
- The viewer understands that one update lowers loss but does not finish learning.
- The quick check proves why step size matters.
- No caveated verdict is promoted.

## Next Production Steps

1. Run scene adequacy against the repaired source module and this blueprint.
2. If clean pass, update or recreate the video-first prompt pack from this 12-beat plan.
3. Generate source frames and contact sheet.
4. Run visual QA from actual pixels.
5. Render the programmatic insert as a style-preserving tablet sequence.
6. Generate only the highest-risk Runway clips first: scenes 5, 7/8 integration, and 11.
7. Assemble with one ElevenLabs voiceover in Creatomate.
8. Inspect sampled frames/contact sheet before any candidate claim.
