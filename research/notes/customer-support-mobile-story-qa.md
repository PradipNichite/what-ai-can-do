# Customer Support Mobile Story QA

## 2026-06-28 Review

Renderer:

- `assets/images/customer-support-mobile-story-mr/`

Finding:

- Initial Marathi captioned images failed text rendering QA.
- Devanagari joined letters and matras did not render reliably because the Python/Pillow renderer did not have `raqm` shaping support.
- This is a renderer failure, not a copywriting failure.

Action:

- Treat the previous Pillow-rendered Marathi images as failed.
- Replace the caption renderer with a Chrome-based renderer because browser text layout shapes Devanagari correctly.
- Add visual QA checklist before future localized images are accepted.

Status:

- `rerender-text`
- `needs-human-review`

## 2026-06-28 Re-Render Review

Renderer:

- `tools/generate_marathi_captioned_story.py`
- Chrome headless screenshot renderer.

Finding:

- Browser rendering fixes the Devanagari shaping issue seen with Pillow.
- Reviewed frames 1 and 4 visually after re-render.
- Joined letters and matras appear correctly in the inspected frames.

Status:

- `pass` for technical text shaping in inspected frames.
- `needs-human-review` for final Marathi copy and public release.
