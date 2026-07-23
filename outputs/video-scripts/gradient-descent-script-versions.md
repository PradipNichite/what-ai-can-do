# Gradient Descent Script Versions

This index tracks Gradient Descent video versions so older experiments do not get mistaken for the current candidate path.

## Active Direction

| Version | Status | Use |
|---|---|---|
| `gradient-descent-gold-standard-hybrid-v1.md` | `source-draft` | Current gold-standard lesson blueprint. Use for scene adequacy and future source-frame regeneration. |

## Reference / Failure Calibration

| Version | Status | Reason |
|---|---|---|
| `gradient-descent-complete-lesson-hybrid-creatomate-v2.md` | `needs-revision` | Hybrid render had pipeline shape but failed cold-student comprehension and reused caveated assets. |
| `gradient-descent-native-story-lesson-edit-v1.md` | `reference-only` | Useful native-story direction, not a clean accepted video candidate. |
| `gradient-descent-warm-minimal-lesson-edit-v1.md` | `reference-only` | Warm Minimal direction is rejected for this lesson unless explicitly re-approved. |
| `gradient-descent-complete-lesson-short-v4.md` | `reject/reference-only` | Programmatic-heavy version did not preserve native lesson style. |
| `gradient-descent-programmatic-*.md` | `reference-only` | Useful for technical motion experiments, not a full lesson candidate. |

## Current Rule

No Gradient Descent version may be called candidate, accepted, visual-QA, or publish-ready unless it has:

- clean scene adequacy pass
- actual frame/contact-sheet visual QA
- no `pass-with-caveats` promotion
- style-preserving programmatic insert, not a replacement style
