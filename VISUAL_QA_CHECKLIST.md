# Visual QA Checklist

Every generated visual renderer needs a review phase before it is treated as final.

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

- Can a viewer understand the story by swiping through the frames?
- Does each frame communicate one idea?
- Is the learner's emotional journey clear?
- Does the visual show the hidden workflow, not only the final concept?
- Is the Indian/local context visible but not forced?
- Is the output native to the medium, not a Markdown page pasted into an image?

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
