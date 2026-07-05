# Learning Video Formats

This project should not treat every video as a hook-first Short. We are building educational content, so the format should be chosen from the learning goal.

## Format 1: Hook-First Short

Use this when the goal is fast awareness or one memorable idea.

Typical length:

- 20-35 seconds

Best for:

- one surprising fact
- one misconception
- one tiny habit
- one quick before/after example

Structure:

1. Hook or tension
2. Visual example
3. One explanation
4. Memory anchor

Good qualities:

- fast pacing
- strong visual motion
- very few words
- one takeaway only

Risks:

- can feel like a list of sentences
- can create false understanding
- may skip the "why"
- may overuse captions and sound effects

Use carefully for education. It should invite learning, not pretend the whole lesson happened.

## Format 2: Micro-Lesson / Bite-Sized Learning

Use this when the goal is understanding and retention.

Typical length:

- 45-90 seconds

Best for:

- explaining a concept
- connecting intuition to mechanism
- teaching a mental model
- showing why a topic matters

Structure:

1. What you will learn
2. Familiar concept or situation
3. Concrete example
4. Core concept
5. Mechanism or step-by-step process
6. Where it appears in AI
7. Memory anchor
8. Quick check or recap

Good qualities:

- calm but not slow
- clear learning promise
- one concept path
- visual motion guides attention
- enough time for technical frames

Risks:

- can become a lecture if the script is too dense
- can feel static if source frames are poster-like
- needs stronger pacing discipline than a Short

This is the preferred default for this product.

### Math-In-AI Micro-Lessons

Full series rules live in `HOW_AI_USES_MATH_SERIES_GUIDE.md`.

For the series on how math topics are used in AI, use micro-lessons by default.

The learner is usually an 11th/12th standard or high-school student who has already studied the math concept, but has not seen its applied role in AI.

The opening should not behave like a social-media hook. It should make the learning objective clear:

```text
In this lesson, you will see how <school math concept> is used in AI to <AI use>.
```

Every math-in-AI micro-lesson should connect five things:

- familiar school concept
- AI version of the concept
- visible mechanism
- one simple technical example
- real AI application

Good example:

```text
Vectors in school have size and direction. In AI, text can be converted into vectors. Similar meanings become nearby vectors, so search can find related ideas even when the exact words differ.
```

Weak example:

```text
AI understands meaning like magic.
```

## Decision Rule

Choose the format by learning depth:

```text
If the viewer should remember one sentence:
  -> Hook-first Short

If the viewer should understand how something works:
  -> Micro-lesson
```

For topics like derivatives, AI learning, prompts, model training, and agents, micro-lessons are usually better.

## Script Differences

Shorts script:

```text
Most students use AI like a shortcut.
But the better way is this:
show the page, try first, then ask for a hint.
AI should be your coach, not your replacement.
```

Micro-lesson script:

```text
In this lesson, you will learn how AI can help you study without replacing your thinking.
This matters because the best learning happens when you stay active.
First, show AI the exact page or problem.
Then ask it to explain the doubt in steps.
Try the answer yourself.
Use a hint only when you are stuck.
The memory anchor is simple: AI should coach your effort, not do your work.
```

## Visual Differences

Hook-first Short:

- bigger motion
- fewer scenes
- fewer details
- captions can carry the punch
- 1-2 seconds per beat is acceptable

Micro-lesson:

- clearer scene progression
- slower technical frames
- visual cues instead of decorative motion
- captions only for terms or memory anchors
- 4-8 seconds per beat is acceptable

## Retention Rules

Every micro-lesson should define:

- `learning_goal`: what the viewer should understand
- `why_it_matters`: why the viewer should care
- `memory_anchor`: the one sentence to remember
- `quick_check`: one question or prompt at the end
- `cognitive_load`: low, medium, or high

Example:

```json
{
  "learning_goal": "Understand derivative as direction for reducing AI error.",
  "why_it_matters": "This is the intuition behind model training.",
  "memory_anchor": "Derivative tells AI which way to adjust.",
  "quick_check": "If error increases, should AI keep adjusting the same way?",
  "cognitive_load": "medium"
}
```

## Derivatives Recommendation

The derivative topic should become a micro-lesson, not a pure Short.

Recommended lesson flow:

1. "You will learn how derivatives help AI learn from mistakes."
2. "This matters because training AI means reducing error."
3. Missed basketball shot analogy.
4. Derivative as direction clue.
5. Prediction, correct answer, error.
6. Error curve and slope.
7. Small repeated updates.
8. Memory anchor: "Derivative tells AI which way to adjust."
9. Quick check.
