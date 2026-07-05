# Probability Source Frames - Review Notes

Status: visual-draft
Pipeline stage: 05 Visual Draft

## Technical Sequence

1. AI estimates possible answers, not certainty.
2. Probability is a scale from 0 to 1 / 0% to 100%.
3. AI assigns probability scores to options.
4. Highest probability is chosen.
5. Close scores mean uncertainty / low confidence.
6. Probability bars power image AI, recommendations, and chatbots.
7. Recap: input -> probability scores -> chosen answer.
8. Quick check: close top scores are more uncertain.

## Review Focus

- Check if all numbers and labels are readable on mobile.
- Check if frame 1 input/options are semantically aligned enough for the lesson.
- Check consistency with matrices/vectors-v3 warm student/tablet style.
- Do not send to Runway until the contact sheet passes technical teaching review.

## Visual QA Decision

Date: 2026-07-03

Decision:

```text
Use the existing Probability frames for the launch-batch motion pass.
Do not regenerate the full lesson before motion.
```

Reason:

- The eight-frame sequence clearly teaches the mechanism: possible answers -> probability scale -> scores -> highest score -> close-score uncertainty -> AI uses -> recap -> quick check.
- Frames 2, 3, 4, 5, and 8 are strong enough for mobile-first motion testing.
- The warm desk, teal/green learner clothing, tablet surface, and technical overlays are close enough to the current study-desk math-series style for the launch batch.
- A full Direction B refresh would improve consistency, but it is not required before a first publish-ready Probability Short.

Approved with cautions:

- Frame 1: acceptable, but the cat/dog/car input should be treated as "possible answers," not a guaranteed object-recognition truth.
- Frame 6: slightly text-dense. Use very gentle motion and avoid adding captions over the tablet.
- Frame 7: memory sentence is small. Keep camera movement locked or use only a mild push-in.

Motion gate:

```text
Proceed to Runway/image-to-video only after local source frames are uploaded and a manifest uses real public image_url values.
```
