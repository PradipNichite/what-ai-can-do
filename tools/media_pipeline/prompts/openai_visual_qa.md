# OpenAI Visual QA Prompt

Review the attached rendered visual assets for this repository.

The verdict must be based on the actual attached image pixels/contact sheet. Use prompt text and source context only to understand intent. Do not approve visual quality from prompt text alone.

Return a strict QA verdict with concrete visible evidence for:

- opener quality
- native generated composition
- pasted-overlay risk
- mechanism visibility
- technical understanding, not just recognition of labels
- false-completion risk: polished visuals that make the viewer feel done while hiding the actual mechanism
- mobile readability
- frame-by-frame repair notes

If a contact sheet is attached, treat its frame order as the sequence order.

For math-in-AI lessons, be especially skeptical. A frame can look beautiful and still fail if it only shows labels, arrows, curves, or icons without making the computation, comparison, representation, or update understandable.

Ask this before accepting:

- Could a student explain what changed, what was computed or compared, and why the next step follows?
- Does the visual show the causal chain, or does it jump from a problem to a result?
- Are diagrams doing teaching work, or are they decorative proof that a concept exists?
- Would the viewer leave with a usable mental model, or just a false sense that they understood?

If the sequence creates a false sense of technical completion, mark `false_completion_risk` as `high` and use `needs-revision` or `reject`, even when style, text readability, and opener quality are strong.
