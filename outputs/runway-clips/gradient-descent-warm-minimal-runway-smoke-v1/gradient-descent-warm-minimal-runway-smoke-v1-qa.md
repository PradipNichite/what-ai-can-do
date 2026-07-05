# Gradient Descent Warm Minimal Runway Smoke v1 QA

Status: pass-with-caveats
Intended use: video-first Runway smoke test

## Inputs

- Source module: `modules/visual-ai-concepts/gradient-descent-how-ai-learns-from-mistakes.source.md`
- Prompt pack: `assets/image-prompts/gradient-descent-how-ai-learns-from-mistakes-video-first.md`
- Source image folder: `assets/images/gradient-descent-how-ai-learns-from-mistakes-video-first-warm-minimal-v1/`
- Source contact sheet: `assets/images/gradient-descent-how-ai-learns-from-mistakes-video-first-warm-minimal-v1/gradient-descent-warm-minimal-source-contact-sheet.jpg`
- Runway manifest: `outputs/video-manifests/gradient-descent-warm-minimal-runway-smoke-v1.json`
- Clip folder: `outputs/runway-clips/gradient-descent-warm-minimal-runway-smoke-v1/`

## Pixel Health

- Files/images opened with ChatGPT vision:
  - `verification/warm-04-gradient-direction.contact-sheet.jpg`
  - `verification/warm-05-small-update.contact-sheet.jpg`
  - `verification/warm-05-small-update-locked-arrow.contact-sheet.jpg`
  - `verification/warm-08-step-size-check.contact-sheet.jpg`
- Any obvious blank/corrupt/missing frame seen by vision: no
- Verification summaries:
  - `warm-04-gradient-direction.mp4`: mean frame diff 2.76, max 5.67, black border mean 0.071
  - `warm-05-small-update.mp4`: mean frame diff 1.38, max 2.46, black border mean 0.099
  - `warm-05-small-update-locked-arrow.mp4`: mean frame diff 0.65, max 1.08, black border mean 0.099
  - `warm-08-step-size-check.mp4`: mean frame diff 1.19, max 1.50, black border mean 0.108
- Caveats: frames 5 and 8 keep about 10 percent black border because the tablet itself is dark and framed; this did not appear as corruption in visual inspection.

## Visual Review

- Opener: not tested in this smoke set; source frame opener passed still-image QA separately.
- Native composition: pass. The tested clips keep the tablet/desk source-frame style and do not introduce unrelated objects or pasted text.
- Mechanism visibility: pass-with-caveats. Frame 4 preserves the gradient-uphill cue and opposite downhill update. Frame 8 preserves the small-step versus too-far comparison. The first frame-5 clip over-animated the point around the curve, but the locked-arrow variant preserves the intended small update mechanism.
- Text readability: pass-with-caveats. Labels remain readable in sampled frames. Frame 4's small labels should still use locked/gentle motion in future clips.
- Sequence: pass for smoke-test purpose. The tested clips cover the riskiest mechanism moments: gradient direction, small update, and step-size overshoot.
- Style consistency: pass. Warm Minimal Tablet Closeup survives Runway for these technical frames.

## Clip Decisions

- `warm-04-gradient-direction.mp4`: pass. Use as the preferred motion pattern for gradient direction.
- `warm-05-small-update.mp4`: reject for production. The point travels around the curve and can confuse the small-update mechanism.
- `warm-05-small-update-locked-arrow.mp4`: pass. Prefer this prompt pattern for frame 5: keep points fixed, pulse only the short arrow.
- `warm-08-step-size-check.mp4`: pass-with-caveats. The comparison survives; keep motion gentle and avoid extra zoom in final assembly.

## Verdict

Warm Minimal Tablet Closeup is now proven enough for Gradient Descent video-first production. Use the accepted source frames and the locked-arrow Runway motion pattern for frame 5. The next useful project step is to repeat the Warm Minimal source-frame pass for Statistics, then compare whether it survives Runway as well as Gradient.
