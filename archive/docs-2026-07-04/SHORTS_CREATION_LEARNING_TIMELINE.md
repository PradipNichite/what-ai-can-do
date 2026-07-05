# Shorts Creation Learning Timeline

Date started: 2026-06-29

This log records what we learned while turning static visual stories into better short-form videos. It is meant to show progress over time: what looked bad, what improved, and what should become product logic later.

## Current Baseline

Best style so far:

- One continuous voiceover.
- Video-first or video-compatible source frames.
- Variable scene durations based on narration beats.
- Minimal extra captions.
- Image-to-video clips verified before final assembly.
- Creatomate used as the final assembly layer.

Current best reference videos:

- Student AI study: `outputs/video-renders/student-ai-study-video-first-story-edit-stable-en.mp4`
- Derivatives AI learning: `outputs/video-renders/derivatives-ai-learning-continuous-edit-en.mp4`
- Matrices images to numbers: `outputs/video-renders/matrices-images-become-numbers-micro-lesson-v1-en.mp4`
- Vectors style-corrected preview: `outputs/video-renders/vectors-how-ai-compares-meaning-micro-lesson-v2-en.mp4`

## Timeline

### 1. Static Slideshow Attempt

Early videos used static image cards one after another.

What failed:

- Felt boring and flat.
- No meaningful motion or action.
- Text overlays were small and not useful.
- Some images were cropped badly.
- The output looked like a simple slideshow, not a short.

Learning:

- A short needs visible action, not only nice images.
- Text appearing on top of static cards does not create energy.
- Static social story cards are not automatically good video frames.

### 2. Creatomate Motion/Overlay Attempt

We tried adding zooms, overlays, transitions, and captions in Creatomate.

What improved:

- The video had more visual activity than the static version.
- Captions and motion made some scenes feel less dead.

What failed:

- It still looked close to version 1.
- Text overlays felt random and not significant.
- Motion was artificial because the underlying images were static.
- Some transitions/crops hurt the image composition.

Learning:

- Post-production motion cannot fully compensate for weak video source frames.
- Captions should support the story, not become the story.
- We need image-to-video for real motion, not only pan/zoom.

### 3. First Runway Image-To-Video Attempt

We moved to Runway image-to-video using existing story images.

What improved:

- Some scenes finally had real motion.
- Characters, phones, arrows, and UI elements could move.
- The result felt more alive than Creatomate-only motion.

What failed:

- Motion intensity varied by scene.
- Some scenes stayed almost static.
- Voiceover and visual action were not always synchronized.
- Scene switching sometimes felt paused or stitched together.

Learning:

- Image-to-video must be planned per scene, not applied blindly.
- Motion prompts need one clear action target.
- Clip verification must happen before final assembly.

### 4. Scene-By-Scene Voiceover Test

We tried generating separate voiceovers for each scene.

What improved:

- Scene audio could be controlled independently.
- It seemed useful for exact per-scene timing.

What failed:

- The final video felt joined together.
- Pauses between clips made the rhythm feel broken.
- It sounded less like one continuous short.

Learning:

- Per-scene voiceover is not wrong, but it needs careful audio stitching.
- For now, one continuous voiceover gives better flow.
- Scene timing should follow narration beats, not equal blocks.

### 5. Indian-English Female Voice

We switched from a stronger/default voice to a softer Indian-English female voice.

What improved:

- The tone felt more natural for Indian education content.
- The video felt less harsh and more student-friendly.

Learning:

- Voice choice is part of story design, not an afterthought.
- For student explainers, calm clarity beats dramatic delivery.

Current preferred voice:

- ElevenLabs `ADd2WEtjmwokqUr0Y5Ad`
- Name used in manifest: `Zara - Soft and Serene Indian Voice`

### 6. Marathi Voice Test

We tried a Marathi version.

What failed:

- Pronunciation was not good enough.
- It reduced trust in the educational content.

Learning:

- Marathi can be ignored for now unless we find a much better voice/workflow.
- Localization needs native-quality pronunciation, not just translated text.

### 7. Video-First Student AI Study Version

We generated source frames specifically for video instead of reusing only image-only story cards.

What improved:

- Character/environment consistency improved.
- Motion prompts had clearer targets.
- Cropping and composition were better.
- The video felt more like a connected story.

Learning:

- Image-only story cards and video source frames must be treated differently.
- For productization, the pipeline should branch:
  - static story/card generation
  - video-source-frame generation
  - voiceover script
  - image-to-video clips
  - final edit

Related docs:

- `VIDEO_FIRST_VISUAL_GUIDE.md`
- `CHARACTER_CONSISTENCY_GUIDE.md`
- `VIDEO_PROMPT_TEMPLATES.md`

### 8. Shorts-Style Caption/SFX Version

We tried a punchier Shorts-style version with large captions and SFX.

What improved:

- More energy.
- Better hook and pace.
- SFX added some production feel.

What failed:

- It felt like a list of sentences.
- Captions started driving the video instead of the visual story.
- It felt less continuous than the calmer synced version.

Learning:

- Shorts energy is not the same as many captions.
- A good educational short needs flow first, then punch.
- Captions should be sparse and intentional.

### 9. Continuous Student AI Study Edit

We created a continuous-story edit with one voiceover, fewer captions, and variable scene timing.

What worked:

- Best sync between voiceover and visual actions.
- Felt like one story instead of separate slides.
- Minimal captions made the visuals easier to watch.
- Motion was enough without feeling chaotic.

Current reference:

- `outputs/video-renders/student-ai-study-video-first-story-edit-stable-en.mp4`

Learning:

- This became the best baseline.
- Future videos should start from this pattern.

### 10. Derivatives Learning Video

We reused an existing derivative visual story and converted it into video with the same continuous-story approach.

What worked:

- Existing educational story cards could be converted into a useful video.
- One continuous voiceover kept the technical explanation coherent.
- No extra captions avoided clutter because the source cards already had text.
- Verification showed strong final motion and low black border.

What was limited:

- Some graph-heavy cards had subtle motion only, because preserving text/math was more important than dramatic movement.
- These older cards are still more like posters than video-first frames.

Current reference:

- `outputs/video-renders/derivatives-ai-learning-continuous-edit-en.mp4`

Learning:

- Text-heavy math cards need locked/subtle motion.
- Action/analogy cards can carry stronger movement.
- For future derivative/math videos, we should create separate video-source frames with fewer labels and let voiceover explain more.

### 11. Derivatives Retention Edit v2

After reviewing the first derivative video, we decided the target should be information retention and understanding, not flashy motion that creates false confidence.

What changed:

- Shortened the voiceover from about 32 seconds to about 26 seconds.
- Rewrote the narration around one memory anchor: `Derivative tells AI which way to adjust.`
- Kept all scene durations under the original Runway clip length to avoid frozen/blank-feeling holds.
- Removed extra captions because the source cards already contain the teaching text.
- Ran a denser scan at 0.5-second intervals, not only a 10-frame contact sheet.

What improved:

- The edit is tighter.
- No true black/blank frames were detected.
- The video keeps the useful action/motion from the Runway clips.
- The explanation now has a clearer retention goal.

What remains limited:

- Some graph-heavy and text-heavy cards still feel static because the source assets are poster-style cards.
- Preserving formulas/text reduces how much motion we can safely ask Runway to create.
- The next quality jump requires new video-first math frames, not only a better edit.

Current reference:

- `outputs/video-renders/derivatives-ai-learning-retention-edit-v2-en.mp4`

Learning:

- Retention-focused videos need one memorable sentence, repeated visually and verbally.
- Technical cards should use motion to guide attention, not to decorate.
- A dense frame scan catches "pause feeling" better than a simple contact sheet.
- If a scene needs real motion, the source frame must contain a clear physical or UI action.

### 12. Format Shift: Shorts To Micro-Lessons

We realized that the product should not default to hook-first Shorts for every topic.

What changed:

- Shorts are useful for one quick idea, but they can create false understanding.
- Concept-heavy topics need a micro-lesson format.
- A micro-lesson can be 45-90 seconds if the structure supports learning.
- The video should start with what the viewer will learn and why it matters.

New product distinction:

- Hook-first Short: attention and one memory sentence.
- Micro-lesson / bite-sized learning: understanding, retention, and concept flow.

Learning:

- For derivatives, micro-lesson is the better format.
- We should optimize for `understanding + retention`, not only visual energy.
- Motion should guide attention to the concept, not distract from it.
- The key output is not just a video; it is a learning experience.

Related doc:

- `LEARNING_VIDEO_FORMATS.md`

### 13. Derivatives Micro-Lesson v1

We created the first lesson-mode derivative video.

What changed:

- Added an explicit lesson structure instead of a hook-first short structure.
- Started with what the viewer will learn.
- Added why the concept matters.
- Added a `Derivative at a point` bridge clip before the direction/error sequence.
- Kept the voiceover continuous and calmer.
- Used sparse captions only for lesson signposts and the memory anchor.

Current reference:

- `outputs/video-renders/derivatives-ai-learning-micro-lesson-v1-en.mp4`

What worked:

- The concept path is clearer than the 26-second retention edit.
- The video now feels more like a bite-sized lesson than a social short.
- The visual sequence has a better learning order:
  - mistake
  - slope at a point
  - direction clue
  - prediction/error
  - error curve
  - update rule
  - repeated corrections
  - why it matters

What remains limited:

- Some graph/math scenes are still low-motion because the source cards are poster-style.
- A better v2 should generate video-first math frames with fewer labels and larger animated graph elements.
- Lesson mode benefits from more time, but only if each extra second has visual or cognitive purpose.

Learning:

- Micro-lessons need explicit lesson signposts, but not heavy captions.
- The first 5 seconds can state the learning goal without needing a dramatic hook.
- Longer videos are acceptable when they improve comprehension.
- The next improvement should be better video-first source frames, not more editing tricks.

### 14. Matrices Micro-Lesson v1

We created the first matrices micro-lesson: `How Images Become Numbers`.

What changed:

- Started video-first instead of converting dense poster cards.
- Generated source frames with minimal embedded text.
- Used the micro-lesson format from the beginning:
  - what you will learn
  - photo becomes pixels
  - grayscale values become numbers
  - rows and columns become a matrix
  - color images use RGB grids
  - AI scans grids for patterns
  - recap memory anchor

Current reference:

- `outputs/video-renders/matrices-images-become-numbers-micro-lesson-v1-en.mp4`

What worked:

- The visual frames are cleaner and more video-ready than the derivative poster cards.
- The lesson has stronger motion in the early and middle scenes.
- The core memory anchor is simple: `An image is a grid of numbers.`
- The topic naturally supports visual explanation, especially pixels, grids, and RGB channels.

What remains limited:

- The pixel zoom bubble becomes too white at one sampled moment.
- The final recap clip has low motion, though it is visually clear.
- Character consistency is good enough for a draft, but not locked enough for product scale.

Learning:

- Video-first generation before Runway improves the experience significantly.
- Matrices are a strong micro-lesson topic because the abstract math has a concrete visual object: the image grid.
- For v2, generate even cleaner technical frames with larger pixel/matrix elements and fewer decorative objects.
- A future product should offer a "technical visual clarity" mode for math-heavy frames.

### 15. Vectors Visual Style Correction

We created the vectors micro-lesson: `How AI Compares Meaning`.

What happened:

- v1 explained the concept but used flat diagram-style source frames.
- The images did not match the established look of the earlier matrices lesson.
- The concept was also harder to understand because the visuals depended too much on labels and abstract charts.

What changed in v2:

- Rebuilt the source frames in the warm Indian student/tablet style.
- Used the same visual world as matrices: student at desk, teal shirt, lamp, notebook, tablet overlays.
- Replaced flat poster diagrams with icon-based tablet visuals:
  - related meaning icons
  - vector number chips
  - meaning-space clusters
  - direction arrows
  - semantic-search dots
  - recommendation cards
  - recap chain
- Reduced embedded text so the voiceover carries the explanation.

What still needs improvement:

- v2 fixed visual style, but some frames still feel generic compared with matrices.
- The matrices lesson works better because the viewer can see a real technical transformation: image -> pixels -> numbers -> matrix -> AI scan.
- The vectors lesson needs stronger visible mechanism, not only related icons and glowing UI.
- Future vector frames should make the technical sequence unmistakable:
  - sentence or query becomes number chips
  - number chips become a point/vector
  - similar points cluster nearby
  - distance or angle is visually compared
  - nearest point becomes the search/recommendation result

Current reference:

- v2 frames: `assets/images/vectors-how-ai-compares-meaning-video-first-v2/`
- v2 prompt pack: `assets/image-prompts/vectors-how-ai-compares-meaning-video-first-v2.md`
- v2 preview: `outputs/video-renders/vectors-how-ai-compares-meaning-micro-lesson-v2-en.mp4`

Learning:

- Future topic sessions must inspect existing best source frames before generating new images.
- The default visual style is now the warm student/tablet educational illustration from matrices and vectors v2.
- For abstract AI/math concepts, place diagrams inside the consistent study environment as tablet overlays.
- A contact sheet is not only a QA artifact; it is a style gate.
- If a new frame set looks like isolated flat diagram cards, revise before Runway generation.
- Style consistency is not enough. A source frame must also show a concrete technical step.
- Still images alone can be misleading; create a quick animatic or preview render before judging whether the video teaches well.

## Product Rules Emerging

### Asset Version Records

- Every video JSON manifest should have a matching Markdown script file.
- JSON remains the render source.
- Markdown is the human-readable review source.
- Keep a script-version index for episodes with multiple cuts.
- This helps compare what changed across continuous edit, retention edit, and micro-lesson versions.

### Format Choice

- Use hook-first Shorts for fast awareness or one memorable idea.
- Use micro-lessons when the viewer needs to understand how something works.
- Do not force every lesson into 20-30 seconds.
- A 45-90 second video is acceptable when it has a clear learning path.
- For this product, micro-lesson should be the default for concept-heavy topics.

### Script And Timing

- Write the voiceover as one continuous short first.
- Split it into beats only after the script feels natural.
- Assign variable durations based on spoken beats.
- Avoid equal scene timing unless the narration actually supports it.

### Visual Planning

- Use fewer, stronger scenes when the topic is concept-heavy.
- Use more micro-scenes only when each one shows a distinct action.
- Treat image-only cards and video frames as separate deliverables.
- Keep video frames less text-heavy than static story cards.
- Match the established warm Indian student/tablet visual style unless explicitly asked otherwise.
- Inspect matrices and vectors-v2 source frames before generating a new topic's images.
- Use the source contact sheet as a style gate before Runway generation.
- For abstract concepts, show diagrams as tablet overlays rather than standalone flat cards.
- For every scene, write the technical learning job before generating the image.
- Require visible evidence of the concept: transformation, comparison, mechanism, or result.
- Do not approve frames whose only value is that they look nice or match the palette.
- Build a rough preview/animatic when possible, because still frames do not reveal video teaching quality.

### Motion Prompting

- Give each scene one motion role:
  - reaction
  - demonstration
  - UI activity
  - graph highlight
  - training loop
  - final summary glow
- Do not ask every scene for high motion.
- For text-heavy frames, preserve layout and use subtle animation.
- For action frames, allow stronger subject motion.

### Voiceover

- Prefer one continuous voiceover for flow.
- Use per-scene voiceover only if we also implement clean audio stitching and no audible pauses.
- Indian-English female voice currently works best for this audience.
- Ignore Marathi for now until pronunciation quality improves.

### Captions And Text

- If the image already has strong text, do not add more captions.
- Use only 2-3 key captions in a short if needed.
- Captions should emphasize a turning point, not repeat every sentence.
- Avoid random overlay text that competes with the visual.

### Verification

Every final candidate should have:

- local MP4
- cloud render URL
- source manifest
- Runway clip requests/final JSON
- contact sheet
- motion report
- black-border check
- dense scan when the video feels paused, blank, or broken

Use:

```powershell
python tools\verify_video_motion.py path\to\video.mp4 --samples 10
```

If the user reports a blank/pause feeling, sample every 0.5 seconds and inspect:

- black frame ratio
- low frame difference
- contact sheet with timestamps

This distinguishes a true blank render failure from a visible but low-information/static section.

## Open Product Gaps

- Replace temporary `tmpfiles.org` asset hosting with stable storage.
- Add automated beat-duration estimation from voiceover.
- Add a per-scene QA file where we mark clips as pass/fail.
- Add stable character reference workflow for future source images.
- Add optional background music only after voice/visual sync is solid.
- Build a UI later for prompt -> story -> images -> video -> QA.
