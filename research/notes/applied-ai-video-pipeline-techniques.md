# Applied AI Video Pipeline Techniques

Date: 2026-06-29

## Why the Current Prototype Feels Uneven

The current Runway + Creatomate prototype is much better than the still-card slideshow, but it still shows common early AI-video pipeline problems:

- Visual clips are generated independently, so motion intensity varies by scene.
- Voiceover pacing is not yet planned before clip generation.
- Scene durations were chosen mechanically instead of from spoken beat length.
- Some prompts asked for more motion, but stronger motion sometimes damaged text.
- Verification happened after rendering instead of being a formal gate before assembly.

## Techniques To Adopt

### 1. Build From Audio Beats, Not Equal Scene Blocks

Production-style automated video systems usually split the script into beats first, then create or select visuals per beat.

For this project:

- Generate or write narration as short beat lines.
- Estimate spoken duration for each beat before generating video.
- Use variable scene durations.
- Keep each visual clip duration tied to the actual spoken beat, not a fixed 5 seconds.

Target manifest shape:

```json
{
  "beat": "Give context",
  "voiceover_text": "Give it your class, topic, and exact doubt.",
  "target_duration": 4.2,
  "visual_role": "demonstration",
  "motion_role": "phone scan and UI response"
}
```

### 2. Use Motion Roles Per Scene

Runway's Gen-4 prompting guidance emphasizes describing camera motion and subject motion for the input image. For educational cards, prompts should not restate the whole image. They should assign one clear motion role:

- `reaction`: student facial expression or eye movement
- `demonstration`: phone moves, notebook writing, page scan
- `UI activity`: arrows, phone assistant, checklist, step cards
- `summary pulse`: nodes light up in sequence

Avoid asking every scene for the same level of motion.

### 3. Preserve Text By Separating Text-Heavy And Motion-Heavy Shots

Our tests showed the tradeoff clearly:

- More aggressive motion improved flow.
- But text-heavy cards could warp, blank, or morph.

Technique:

- For text-heavy scenes, use locked camera and small UI/character motion.
- For motion-heavy scenes, reduce on-image text or generate a cleaner visual without dense labels.
- If we want stronger action, generate a separate image specifically for video, not reuse the carousel card.

### 4. Create Video-Specific Source Frames

The existing cards were designed as standalone social images. They already contain text, labels, and composition. That makes them fragile when animated.

Better next pipeline:

- Keep carousel cards for sharing.
- Generate separate video source frames with less embedded text.
- Move narration/captions into audio/subtitle layers.
- Let Runway animate characters, phone, hands, and UI without having to preserve lots of text.

Video source frame rules:

- one main action per frame
- fewer small text regions
- clear subject separation
- room for motion
- phone/notebook/UI elements large enough to animate

### 5. Use First/Last Frame Control Where Useful

For scenes that need a visible action arc, use first/last frame or start/end frame workflows when available:

- phone moves from desk to page
- confused face becomes aha face
- checklist changes from empty to checked
- summary nodes light in sequence

This is better than asking the model to invent the whole transition from one still.

### 6. Add Verification Gates Before Assembly

Every generated clip should be scored and contact-sheet checked before stitching:

- full-frame preserved
- no black tail
- readable text
- motion score above threshold for scenes that need motion
- no major identity drift
- no UI/text corruption

Current verifier already creates:

- contact sheets
- frame-difference motion score
- black-border ratio

Add next:

- per-scene pass/fail notes
- compare against previous generation
- reject if text-heavy scene shows text morphing

### 7. Assemble With Edit Logic, Not Just Concatenation

Creatomate should be used as the edit assembly layer:

- variable scene timing
- continuous voiceover or planned scene voiceovers
- optional subtle music bed
- lower-third captions only when useful
- no overlay text when the image already contains text
- avoid crossfades that create dark frames unless verified

For our current educational style, hard cuts or very short clean cuts may be better than fades.

## Applied Next Pipeline

Recommended next iteration:

1. Create a beat-timed narration manifest.
2. Generate video-specific source images from the existing story, with less embedded text.
3. Generate Runway clips from those video frames.
4. Verify each clip.
5. Assemble in Creatomate with beat-aware timing.
6. Add optional captions only after audio sync is good.

## Sources

- Runway Gen-4 Video Prompting Guide: https://help.runwayml.com/hc/en-us/articles/39789879462419-Gen-4-Video-Prompting-Guide
- Runway API docs: https://docs.dev.runwayml.com/api
- Creatomate API / automation overview: https://creatomate.com/
- Creatomate templates and automation use cases: https://creatomate.com/templates
- n8n automated AI video workflow example using ElevenLabs and Creatomate: https://n8n.io/workflows/3442-fully-automated-ai-video-generation-and-multi-platform-publishing/
- Runway Academy custom workflow description: https://academy.runwayml.com/courses
