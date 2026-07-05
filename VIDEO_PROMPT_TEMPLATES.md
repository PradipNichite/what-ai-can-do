# Video Prompt Templates

Reusable templates for generating video-first source frames and image-to-video clips.

For math-in-AI micro-lessons, use teaching-first language. Do not make the opening frame a dramatic hook. The first frame should connect the school concept to the AI use.

Self-contained lesson rule:

- The first frame/card must name the lesson topic or make it unmistakable.
- It must say what the learner is about to understand.
- It must connect the school concept to the AI use before showing detailed mechanism steps.
- It must introduce the concrete example if later frames depend on that example.
- Do not begin with an unexplained diagram, object, or random visual sequence.

Native generated text rule for image-story cards:

- Use ChatGPT/image generation to create the full educational card composition with text included in the generated image.
- Text should be integrated as poster typography, tablet UI, notebook writing, sticky notes, speech bubbles, diagram labels, arrows, or callouts.
- Do not generate a background image and then add a generic text overlay as the main lesson layer.
- Prompt explicitly: "the card should feel like one complete designed educational poster, where illustration, diagram, and text are integrated together."

## Source Image Prompt Template

```text
Use case: illustration-story
Asset type: 9:16 source frame for image-to-video animation
Primary request: Create frame <N> of a video-first educational short about <topic>.

Scene/backdrop: <same recurring environment>
Subject: Same recurring character: <character bible summary>
Style/medium: warm modern Indian educational illustration, clean and polished, designed as source frame for image-to-video.
Composition/framing: vertical 9:16, one clear action, large subject, clear foreground/background separation, enough margin for subtle camera movement.

Text (verbatim): "<minimal text>"

Motion target for later video: <what should move>

Constraints:
- minimal text only
- no extra text
- no logos
- no watermark
- avoid dense labels
- make it easy to animate <motion target>
- keep character and environment consistent
- for frame 1, make the lesson self-contained: topic, learning promise, school concept, AI use, and example/task must be visible or plainly stated
- for image-only cards, text must be natively integrated into the generated design, not pasted on as a separate caption overlay
```

## Runway Image-To-Video Prompt Template

```text
<Motion target sentence.>
<Character/action sentence.>
<UI/object motion sentence.>
Keep the full vertical frame visible.
Keep existing text unchanged and readable.
No new text.
No crop.
```

## Locked Text-Heavy Prompt

Use when the image contains important text.

```text
Locked camera. Preserve the full vertical frame exactly.
Keep every word readable and unchanged.
Do not alter labels or create new text.
Add small continuous motion only: <small motion list>.
No zoom. No crop. No text morphing.
```

## Action Scene Prompt

Use when the image has low text and a clear action.

```text
<Subject> performs <action> naturally.
<Object/UI> responds with <motion>.
Add gentle parallax and subtle camera push-in.
Keep the full vertical frame visible.
No new text. No crop.
```

## Educational Short Scene Plan Template

```json
{
  "id": "scene-id",
  "scene_type": "learning_objective | familiar_concept | concrete_example | mechanism | ai_application | practice | feedback | summary",
  "duration": 4.0,
  "voiceover_text": "Short spoken line.",
  "motion_role": "phone_scan | writing | step_highlight | check_answer",
  "school_concept": "The familiar math idea, for math-in-AI lessons.",
  "ai_use": "The AI behavior this scene connects to.",
  "mechanism": "What is transformed, compared, scored, updated, or represented.",
  "text_density": "low | medium | high",
  "source_image_prompt": "...",
  "runway_prompt": "...",
  "verification": {
    "min_motion_score": 3,
    "max_black_border_ratio": 0.08,
    "manual_text_review": true
  }
}
```

## Example: Student Study Scene

Source image:

```text
Text: "Show the page"
Motion target: phone lifts over textbook and scan light crosses page
```

Runway:

```text
Student lifts the phone slightly over the textbook as if taking a photo.
A soft scan light moves across the page.
Natural hand movement, clean parallax.
Keep the full vertical frame visible.
No new text. No crop.
```
