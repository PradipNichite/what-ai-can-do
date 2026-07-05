# Visual QA Checklist

Every generated visual renderer needs a review phase before it is treated as final.

Visual QA must use ChatGPT vision capability to inspect the actual rendered image, contact sheet, or video preview frames. Local scripts can help find missing files, blank frames, dimensions, motion scores, or text-shaping risks, but they cannot approve visual quality.

## Text Rendering QA

Use this especially for Marathi, Hindi, or any script with joined letters, matras, or conjuncts.

- Does every caption render in the correct script?
- Are joined letters, matras, and half-letters shaped correctly?
- Are there any missing glyph boxes, question marks, broken characters, or misplaced marks?
- Is the caption readable on a phone?
- Does the caption fit inside the panel without crowding?
- Does the text preserve natural spoken language?
- Are common English terms handled according to the localization guide?

## Visual Story QA

- Did ChatGPT vision inspect the actual rendered image/contact sheet, not only file names, prompts, or source Markdown?
- Can a viewer understand the story by swiping through the frames?
- Does each frame communicate one idea?
- Is the learner's emotional journey clear?
- Does the visual show the hidden workflow, not only the final concept?
- Is the Indian/local context visible but not forced?
- Is the output native to the medium, not a Markdown page pasted into an image?

## Technical Understanding QA

Use this especially for "How AI Uses Math" lessons.

- Does the visual explain what is being represented, computed, compared, scored, or updated?
- Does each technical step visibly cause the next step, instead of jumping from a label to a conclusion?
- Could a student explain what changed and why after seeing the frame or sequence?
- Are graphs, arrows, scores, paths, meters, or icons doing teaching work, not just decorating the topic?
- Does the sequence avoid a false sense of understanding where the viewer feels complete but cannot explain the mechanism?
- If a polished visual hides the actual mechanism, mark it `needs-revision` or `reject` even if style and readability are good.

## Marathi-Specific QA

- Does the copy sound like spoken Marathi?
- Are familiar English terms written naturally in Marathi letters where appropriate?
- Did we avoid pure, formal, textbook Marathi?
- Did we avoid awkward English phrases where simple Marathi sounds better?
- Did a human reviewer inspect the final rendered image, not only the source text?

## Status Labels

Use these labels in review logs:

- `pass`: ready to use.
- `revise-copy`: language needs improvement.
- `rerender-text`: text rendering failed.
- `rerender-visual`: image composition or story clarity failed.
- `needs-human-review`: not final until a person checks it.
