# OpenAI Visual QA - video-first

Generated: 2026-07-05T07:48:38+00:00
Model: `gpt-5.5`
Response ID: `resp_067a83db37ed4b81006a4a0c3c7df0819b92dceacf3c50b340`
OpenAI request ID: `155c50b5-0386-459d-a8ff-0534ceefd1fe`

## Inputs

- Image folder: `assets/images/gold-candidates/probability-strict-paired-medium/video-first`
- Contact sheet: `assets/images/gold-candidates/probability-strict-paired-medium/video-first-contact-sheet.jpg`
- Prompt pack: `assets/image-prompts/probability-how-ai-handles-uncertainty-video-first-v2.md`
- Source module: `modules/visual-ai-concepts/probability-how-ai-handles-uncertainty.source.md`

Reviewed images:
- `assets\images\gold-candidates\probability-strict-paired-medium\video-first-contact-sheet.jpg`

## Verdict

- Status: `needs-revision`
- Intended use: `video-first`
- Next action: `regenerate-frame`

Good video-first set with strong native style and mostly clear probability mechanism, but it needs localized revisions before Runway generation. The main blocker is frame 1: the input image looks like a dog while the sequence later selects cat, which can confuse the example. Frames 3 and 6 also need readability improvements for mobile/video use.

## Gate Evidence

- Opener: `partial` - Frame 1 is visually strong: warm Indian study room, recurring teenage learner, tablet large, and three option cards labelled cat/dog/car are clear. However the central input photo visibly looks like a dog, while the later sequence chooses cat as highest probability. That creates an avoidable story conflict in the opening example.
- Opener required fix: Regenerate frame 1 with an ambiguous animal image or a cat-like input image that matches the later cat-highest score, while keeping the cat/dog/car option cards large and unselected.
- Native composition: `pass` - All frames look like native generated educational illustrations in the same warm desk/tablet world. Text is mostly embedded on tablet UI, option cards, and notebook surfaces rather than appearing as a generic post-production caption. The character, desk lamp, books, notebook, plant, and tablet remain consistent.
- Native composition required fix: None.
- Overlay risk: `low` - The UI elements appear integrated into tablet screens and physical cards with consistent perspective, lighting, and glow. The notebook text in frame 7 is drawn into the page. No obvious pasted rectangular overlay or mismatched typography layer dominates the compositions. The contact-sheet filename labels are outside the rendered frames and do not affect asset quality.
- Mechanism visibility: `partial` - The sequence mostly shows the intended probability mechanism: options in frame 1, 0-to-1 scale in frame 2, probability bars in frame 3, highlighted top score in frame 4, close scores plus low-confidence meter in frame 5, AI-use panels in frame 6, recap chain in frame 7, and quick-check comparison in frame 8. Weak points: frame 1’s dog input conflicts with later cat choice; frame 3 uses icons plus numeric values but does not clearly render the requested combined labels 'cat 0.72', 'dog 0.20', 'car 0.08'; frame 6’s mini-panel details are quite small.
- Mechanism required fix: Fix frame 1 story consistency. Preferably also regenerate or edit frame 3 so each bar has clear text labels matching cat/dog/car scores, and enlarge frame 6 tablet panels/labels slightly if possible.
- Mobile readability: `partial` - Major tablet elements are generally readable in the contact sheet: frame 2 scale labels, frame 4 chosen: cat, frame 5 low confidence, frame 7 confidence-weighted guess, and frame 8 A/B numbers. Some smaller UI labels are borderline for mobile viewing, especially frame 6 'recommendation' and small panel details, and frame 3 category-score pairing depends heavily on icons instead of readable text labels.
- Mobile readability required fix: Increase label size/contrast in frames 3 and 6. Keep all technical numbers large enough to read after video compression.

## Frame Notes

### Frame 1

- Status: `needs-revision`
- Evidence: Strong opener composition with student, tablet, and cat/dog/car cards. The central tablet image visibly appears to show a dog, which conflicts with later frames where cat is the highest-probability and chosen answer.
- Fix: Regenerate with an ambiguous input photo or cat-like input image. Keep only 'cat', 'dog', 'car' text and leave all options unselected.

### Frame 2

- Status: `pass`
- Evidence: Clear tablet-centered probability scale with 0, 0.5, 1 and 0%, 50%, 100%. Pointer sits around 0.7 and learner finger provides a good motion cue.
- Fix: None.

### Frame 3

- Status: `needs-revision`
- Evidence: The bar chart correctly shows cat tallest, dog medium, car shortest with values 0.72, 0.20, 0.08. However the requested readable labels 'cat 0.72', 'dog 0.20', 'car 0.08' are not fully present; category identity is mostly via small icons under the bars.
- Fix: Add clear mobile-readable category-score labels beside or under each bar: cat 0.72, dog 0.20, car 0.08. Keep layout sparse.

### Frame 4

- Status: `pass`
- Evidence: Cat bar is highlighted/glowing, dog and car bars are dimmer, and 'chosen: cat' is readable. This communicates highest-score selection without a certainty claim.
- Fix: None.

### Frame 5

- Status: `pass`
- Evidence: Cat 0.42 and dog 0.39 bars are visibly close, car 0.19 is lower, and a yellow 'low confidence' meter is shown. Student expression looks thoughtful/uncertain.
- Fix: None.

### Frame 6

- Status: `needs-revision`
- Evidence: Three real-AI panels are visible and labelled image AI, recommendation, chatbot. The mechanism is present through small bars and highlights, but panel text and internal bars are small and may be marginal on phone after animation/compression.
- Fix: Enlarge the tablet UI panels and labels slightly; reduce decorative spacing so the three panels occupy more of the tablet.

### Frame 7

- Status: `pass`
- Evidence: Recap chain is clear: input -> scores -> choice, with glowing nodes. Notebook note 'confidence-weighted guess' is readable and integrated into the page.
- Fix: None.

### Frame 8

- Status: `pass`
- Evidence: Quick check comparison is clear: Card A has one tall 0.90 winner, Card B has close 0.42 and 0.39 bars with yellow glow, and the learner points toward B.
- Fix: None.
