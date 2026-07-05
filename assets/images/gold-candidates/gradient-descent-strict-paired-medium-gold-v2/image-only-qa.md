# OpenAI Visual QA - image-story

Generated: 2026-07-05T12:29:45+00:00
Model: `gpt-5.5`
Response ID: `resp_0c4d562a7181a60b006a4a4e2320e88192bb2117ba12752a34`
OpenAI request ID: `3f74cc76-29c5-46cb-b070-7ddea7f564ea`

## Inputs

- Image folder: `assets/images/gold-candidates/gradient-descent-strict-paired-medium-gold-v2/image-only`
- Contact sheet: `assets/images/gold-candidates/gradient-descent-strict-paired-medium-gold-v2/image-only-contact-sheet.jpg`
- Prompt pack: `assets/image-prompts/gradient-descent-how-ai-learns-from-mistakes-image-story.md`
- Source module: `modules/visual-ai-concepts/gradient-descent-how-ai-learns-from-mistakes.source.md`

Reviewed images:
- `assets\images\gold-candidates\gradient-descent-strict-paired-medium-gold-v2\image-only-contact-sheet.jpg`

## Verdict

- Status: `needs-revision`
- Intended use: `image-story`
- Next action: `regenerate-frame`

Strong native educational image-story with clear mechanism and good opener, but not ready as final because frame 6 omits required teaching text and frame 5’s update rule is visually awkward. Regenerate or revise those frames rather than the whole set.

## Gate Evidence

- Opener: `pass` - Frame 1 is self-contained: it names the lesson as “Gradient Descent: How AI Learns From Mistakes,” shows the wrong-prediction example with a cat image, “prediction: dog,” and “correct: cat,” and includes the school-math/AI bridge through “Slope tells which way to move” plus the sticky note about lowering error with small downhill steps.
- Opener required fix: None
- Native composition: `pass` - Across the contact sheet, text and diagrams are integrated into tablet screens, notebook pages, sticky notes, and poster-like brush headers. The warm desk, learner, tablet, notes, books, and diagrams feel like one coherent educational-card design rather than separate plain captions on stock backgrounds.
- Native composition required fix: None
- Overlay risk: `low` - Most labels are attached to believable surfaces: tablet UI chips, notebook pages, sticky notes, and diagram annotations. The large white brush-stroke headers are stylistically consistent across cards and read as native poster typography, not obvious post-production text boxes. The only non-card text is the contact-sheet filename strip below each frame, which is not part of the rendered card.
- Mechanism visibility: `partial` - The main mechanism is visible through the sequence: wrong prediction becomes a loss meter in frame 2; a high point appears on a U-shaped loss curve in frame 3; slope and downhill direction are shown in frame 4; a small update is shown in frame 5; lower loss and closer-but-still-wrong prediction are shown in frame 6; repeated steps appear in frame 7; small steps vs overshoot are compared in frame 8. However, frame 6 omits the required explanatory line “The prediction is closer, not perfect,” which weakens the intended teaching safeguard against implying perfection after one step.
- Mechanism required fix: Regenerate or revise frame 6 to include the missing required text “The prediction is closer, not perfect.” Keep the prediction still visibly imperfect, e.g. prediction remains dog while correct is cat, or use a closer-but-not-matching confidence display.
- Mobile readability: `partial` - Large headers and main tablet labels are generally readable on a phone-sized contact sheet: prediction/correct chips, loss meter, curve labels, slope, lower error, repeat, small step, and too far are visible. Some smaller notebook/sticky-note text is borderline but still mostly legible. Frame 5’s update rule is readable but split awkwardly as “new weight =” on one line and “old weight - small step” on the next, making the equation less clean than requested.
- Mobile readability required fix: Improve frame 5 equation layout if regenerating: show “new weight = old weight - small step” as one clear line or a cleaner two-line note where the equality relationship is unambiguous. Frame 6 must also add the missing sentence in readable size.

## Frame Notes

### Frame 1

- Status: `pass`
- Evidence: Strong opener. Lesson title, learning promise, slope connection, and wrong prediction example are all visible. Cat image with “prediction: dog” and “correct: cat” makes the mismatch obvious.
- Fix: None

### Frame 2

- Status: `pass`
- Evidence: Shows prediction dog vs correct cat, highlighted error gap, and a vertical loss meter labeled “loss.” Sticky note reads “loss = how wrong the model is.” Mechanism of mistake becoming score is visible.
- Fix: None

### Frame 3

- Status: `pass`
- Evidence: Large U-shaped loss curve dominates the tablet with a glowing point high on the right side. Text says “A model setting sits on a loss curve,” “High point = high error,” and “loss.” Minimal axis clutter.
- Fix: None

### Frame 4

- Status: `pass`
- Evidence: U-shaped curve has a marked point, local tangent/line, “slope” label, and a downhill arrow labeled toward “lower error.” Notebook note reinforces “Move downhill to lower error.”
- Fix: None

### Frame 5

- Status: `needs-revision`
- Evidence: The small-step mechanism is visible: old and new points are close together and connected by a short arrow labeled “small step.” The formula note is present but awkwardly split as “new weight =” then “old weight - small step,” rather than the requested clean expression.
- Fix: Revise equation layout to clearly read “new weight = old weight - small step,” ideally as one large notebook/tablet note with one equals sign and one minus sign.

### Frame 6

- Status: `needs-revision`
- Evidence: Shows lower loss meter, prediction dog and correct cat still separated, and a curve inset with a lower point. However, the required sentence “The prediction is closer, not perfect.” is missing from the rendered card.
- Fix: Add the missing text “The prediction is closer, not perfect.” in a readable tablet or notebook callout while keeping the prediction visibly not perfect.

### Frame 7

- Status: `pass`
- Evidence: Tablet shows a U-shaped loss curve with ordered dotted points and arrows descending toward the valley. Text reads “Training repeats the loop,” “small steps lower loss,” and “repeat.” Mechanism is clear and not just decorative.
- Fix: None

### Frame 8

- Status: `pass`
- Evidence: Quick check card clearly compares a green small-step dotted path descending into the valley with a red oversized path jumping past the valley and landing higher. Labels “small step” and “too far” are visible, and notebook text says the large step can overshoot.
- Fix: None
