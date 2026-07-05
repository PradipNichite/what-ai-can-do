# How I Created Bite-Sized Micro-Lessons Using AI

I started with a simple question:

Can AI help me create educational videos that actually improve understanding, not just flashy Shorts?

At first, I was thinking like most people think about short-form video: make it quick, add motion, add captions, make it visually attractive. But after a few experiments, I realized something important.

For learning content, a good video is not just a hook. It is a small lesson.

That shifted the whole process.

Instead of creating "Shorts", I started creating **micro-lessons**: short, visual, structured explanations that help a learner understand one concept and remember one useful idea.

Two examples I created were:

- **Derivatives: How AI Learns From Mistakes**
- **Matrices: How Images Become Numbers**

This article explains the process, the tools I used, and what each tool was useful for.

## What I Mean By A Micro-Lesson

A micro-lesson is not a full lecture. But it is also not just a catchy social media clip.

The structure I found useful was:

1. What you will learn
2. Why it matters
3. A concrete example or analogy
4. The core concept
5. A small technical glimpse
6. How AI or computers use it
7. One memory anchor
8. A quick check or recap

For example, the memory anchor for the derivatives lesson was:

> Derivative tells AI which way to adjust.

For the matrices lesson, it was:

> An image is a grid of numbers.

That one sentence matters. It keeps the lesson from becoming a pile of facts.

## Why I Moved Away From Hook-First Shorts

The first versions looked more like regular Shorts. They had quick captions, motion, and short sentence overlays.

But something felt wrong.

They looked active, but they did not always feel educational. Some versions felt like a list of sentences. Some felt like static images stitched together. Some had motion, but the voiceover and visuals were not always helping each other.

That taught me a useful lesson:

**A video can look engaging and still create false understanding.**

So I changed the target. Instead of asking, "Is this exciting enough?", I started asking:

- Will the learner understand the idea?
- Is the visual supporting the sentence being spoken?
- Is there one idea they will remember?
- Is the motion guiding attention, or just decorating the scene?

That is when the micro-lesson format started working better.

## The Pipeline I Used

The final workflow looked like this:

```text
Topic idea
  -> source explanation
  -> micro-lesson structure
  -> video-first image prompts
  -> source frames
  -> image-to-video clips
  -> voiceover
  -> final video assembly
  -> verification
  -> Markdown script archive
```

Each step had a different job.

## Step 1: Start With The Learning Goal

Before generating images or video, I wrote the learning goal.

For the matrices lesson:

```text
Understand that digital images can be represented as matrices of pixel values.
```

Then I wrote:

- why it matters
- the core explanation
- the memory anchor
- the micro-lesson flow
- one quick check

This became the source module:

```text
modules/visual-ai-concepts/matrices-how-images-become-numbers.source.md
```

This source file is important because it prevents the video from becoming random visuals. It tells the pipeline what the lesson is actually trying to teach.

## Step 2: Choose Micro-Lesson Instead Of Short

I documented the format decision separately:

```text
LEARNING_VIDEO_FORMATS.md
```

The rule is simple:

```text
If the viewer should remember one sentence:
  -> Hook-first Short

If the viewer should understand how something works:
  -> Micro-lesson
```

For topics like derivatives, matrices, vectors, probability, and AI training, micro-lessons are usually better.

## Step 3: Create Video-First Image Prompts

This was one of the biggest learnings.

Images for posts and images for videos are not the same.

A static educational image can contain lots of text, arrows, labels, and explanations. But when that image becomes a video, too much text becomes a problem. The video model may warp the text, crop the frame, or produce only tiny motion because it is trying to preserve a dense poster.

So I started creating **video-first source frames**.

Good video-first frames have:

- one clear action
- minimal embedded text
- large visual elements
- clear motion target
- space for captions
- less clutter

For the matrices lesson, the visual sequence was:

1. Student looks at a phone photo and notebook
2. Photo zooms into pixels
3. Grayscale pixels become brightness numbers
4. Numbers become a matrix
5. Color image splits into red, green, blue channels
6. AI scans grids for patterns
7. Recap: photo -> pixels -> matrix -> AI seeing

The prompt pack is saved here:

```text
assets/image-prompts/matrices-images-become-numbers-video-first.md
```

## Step 4: Generate Source Images

I used AI image generation to create the source frames.

Purpose:

- create clean 9:16 educational visuals
- keep a consistent visual style
- create scenes that are easy to animate later

The source frames were saved here:

```text
assets/images/matrices-images-become-numbers-video-first/
```

For each set, I also created a contact sheet. This made it easier to check the full visual sequence at once before spending video credits.

This step matters because if the source images are weak, no video tool can fully rescue the lesson.

## Step 5: Turn Images Into Motion With Runway

I used **Runway** for image-to-video.

Purpose:

- turn each source frame into a 5-second video clip
- add motion to phone screens, pixel zooms, graphs, UI scans, and character reactions
- make the lesson feel alive without losing the visual structure

Important settings that worked:

```text
model: gen4_turbo
ratio: 720:1280
duration: 5 seconds per clip
```

For each image, I wrote a motion prompt. The prompt did not re-explain the whole image. It described what should move.

Example:

```text
A circular zoom bubble expands over the phone photo, revealing clear square pixels.
The pixel grid sharpens gently while the phone remains steady.
Keep the full vertical frame visible. No new text. No crop.
```

This was a key learning:

**Image-to-video prompts should focus on motion, not the full story.**

## Step 6: Generate Voiceover With ElevenLabs

I used **ElevenLabs** for voiceover.

Purpose:

- generate a natural spoken explanation
- keep the voice consistent across videos
- create a calm educator tone

The voice that worked best for this style was an Indian-English female voice:

```text
Zara - Soft and Serene Indian Voice
Voice ID: ADd2WEtjmwokqUr0Y5Ad
```

I learned that one continuous voiceover usually works better than separate voiceover clips per scene.

Separate scene voiceovers made the video feel stitched together. A continuous voiceover made it feel like one lesson.

## Step 7: Measure Voiceover Duration Before Final Timing

One practical issue was sync.

If the voiceover is longer than the video clips, the final video starts to feel paused or broken. If clips are stretched too long, motion dies and the learner feels the video has frozen.

So the better order is:

1. Write the voiceover script.
2. Generate the MP3.
3. Measure the actual duration.
4. Adjust scene durations.
5. Only then render the final video.

This helped reduce awkward pauses.

## Step 8: Assemble The Final Video With Creatomate

I used **Creatomate** for final video assembly.

Purpose:

- combine the Runway video clips
- add the ElevenLabs voiceover
- place sparse captions
- export a final 9:16 MP4
- provide a cloud render URL

Creatomate was useful because it let me treat the final video as a structured render from JSON.

Each final video had a manifest like:

```text
outputs/video-manifests/matrices-images-become-numbers-micro-lesson-v1.en.json
```

The manifest included:

- title
- language
- output size
- learning design
- voiceover text
- scene order
- scene durations
- caption timings
- video URLs

This made the process repeatable.

## Step 9: Use Sparse Captions

Another lesson:

More captions do not always mean better learning.

For micro-lessons, I used captions only for signposts and memory anchors:

- What you will learn
- Why it matters
- Rows + columns = matrix
- Image = grid of numbers

The voiceover explains the lesson. The captions should guide attention, not compete with the visuals.

## Step 10: Verify The Video

I used local verification scripts after rendering.

Purpose:

- create contact sheets
- measure motion between frames
- check black-border ratio
- detect blank or low-motion sections

The main script:

```text
tools/verify_video_motion.py
```

Example output:

```text
outputs/video-renders/verification/matrices-images-become-numbers-micro-lesson-v1-en.contact-sheet.jpg
outputs/video-renders/verification/matrices-images-become-numbers-micro-lesson-v1-en.motion-report.json
```

I also used dense timestamp sheets when a video felt paused or blank.

This helped separate two different problems:

- true blank frame
- visible frame with very low motion

That distinction matters. A low-motion math frame may be acceptable if the learner needs time to understand it. A blank frame is a render problem.

## Step 11: Keep Both JSON And Markdown

JSON is good for rendering, but bad for human review.

So I started keeping Markdown script versions too.

For example:

```text
outputs/video-scripts/derivatives-ai-learning-micro-lesson-v1.md
outputs/video-scripts/derivatives-ai-learning-script-versions.md
```

The Markdown version includes:

- purpose of the version
- linked manifest JSON
- linked voiceover file
- rendered video link
- learning design
- full voiceover script
- scene timing table
- review notes

This makes it easier to compare versions and understand why one video worked better than another.

## Services I Used And Why

| Service / Tool | Purpose |
|---|---|
| Codex | Planning, writing source modules, prompts, manifests, scripts, docs, and running the pipeline |
| AI image generation | Creating 9:16 video-first source frames |
| Runway | Turning source images into short motion clips |
| ElevenLabs | Creating natural voiceover |
| Creatomate | Assembling final video from clips, captions, and audio |
| Local Python scripts | Uploading assets, generating manifests, rendering, and verification |
| Markdown docs | Human-readable review, versioning, and repeatability |
| JSON manifests | Machine-readable render instructions |

## What Worked Best

The best results came when I treated the process as learning design first, video production second.

The strongest rules were:

- Start with the learning goal.
- Create one memory anchor.
- Use one continuous voiceover.
- Generate video-first source frames.
- Keep captions sparse.
- Use motion to guide attention.
- Verify before accepting the output.
- Store both JSON and Markdown versions.

## What Did Not Work Well

Some things looked promising but did not work as well:

- using dense poster cards as video frames
- adding random text overlays
- forcing every video into 20-30 seconds
- treating motion as decoration
- generating voiceover scene by scene without smooth stitching
- stretching clips beyond their useful motion

Those mistakes were useful because they clarified the product direction.

## The Product Direction

The direction now is not "make AI Shorts".

The direction is:

> Create bite-sized visual lessons that help students understand where math, AI, and technology connect.

For concept-heavy topics, micro-lessons are better than hook-first Shorts.

The derivative lesson taught me that a video needs a memory anchor.

The matrices lesson taught me that starting video-first makes the output much better.

Together, they became the working template for future topics.

## The Repeatable Template

For the next topic, I can start a new session and give only:

```text
Topic: Vectors and how AI compares meaning.
```

Then the pipeline can follow the same structure:

```text
source module
  -> video-first prompt pack
  -> source frames
  -> Runway clips
  -> ElevenLabs voiceover
  -> Creatomate render
  -> verification
  -> Markdown script version
```

That is the real value of the experiment. Not just one good video, but a repeatable way to create many small lessons.

