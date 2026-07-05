# Next Session Note: Documentation Consolidation

## Task

Consolidate the project Markdown docs so future Codex sessions load fewer, clearer, more enforceable instructions.

This is not a content-generation session. Do not create new lesson images, videos, prompt packs, or story assets.

## Why

The project has accumulated many Markdown files: guides, session notes, templates, pipeline docs, style notes, audits, and one-off handoffs. Some rules are repeated across files, and important process constraints can get buried.

The goal is to reduce clutter while preserving the actual decisions and learnings.

## Read First

```text
AGENTS.md
IMAGE_STORY_GATE.md
CONTENT_PIPELINE.md
NEW_SESSION_START_NOTE.md
HOW_AI_USES_MATH_SERIES_GUIDE.md
HOW_AI_USES_MATH_IMAGE_ONLY_GAP_AUDIT.md
VIDEO_PROMPT_TEMPLATES.md
```

Also review the official Codex mechanism summary already captured in this session:

```text
AGENTS.md = short mandatory repo instructions
hooks = enforcement/checker layer
skills = reusable workflow routing
rules = command permission policy, not creative-quality enforcement
```

## Scope

Inventory top-level Markdown files and classify them:

- Canonical rule/process docs to keep
- Templates to keep
- Current session handoff notes to keep temporarily
- Historical notes that can be archived
- Duplicate or stale docs that can be merged
- Oversized docs that should be summarized into canonical docs

## Hard Rule

Before creating any new Markdown file, search existing docs and decide whether an existing file should be updated instead.

New Markdown files are allowed only when they have a distinct lifecycle, owner, or output artifact.

## Desired Canonical Set

Aim for a small set like:

```text
AGENTS.md
IMAGE_STORY_GATE.md
CONTENT_PIPELINE.md
NEW_SESSION_START_NOTE.md
HOW_AI_USES_MATH_SERIES_GUIDE.md
HOW_AI_USES_MATH_SERIES_PLAN.md
HOW_AI_USES_MATH_LESSON_CORE_TEMPLATE.md
VIDEO_PROMPT_TEMPLATES.md
LOCALIZATION_GUIDE_MARATHI.md
PIPELINE_BOARD.md
PROJECT_STATUS.md
```

This list is a starting hypothesis, not a mandate. Adjust based on actual content.

## Process

1. Create an inventory table of Markdown files with purpose, current value, overlap, and proposed action.
2. Identify duplicate rules and move them into the correct canonical file.
3. Keep `AGENTS.md` short and mandatory. Do not turn it into a long guide.
4. Keep `IMAGE_STORY_GATE.md` as the hard gate for image-only educational stories.
5. Move old session notes into an archive folder only after their useful rules are merged.
6. Do not delete files outright unless the user explicitly approves. Prefer proposing an archive/delete list first.
7. Run `python tools/verify_image_story_gate.py --changed` if image-story docs are edited.

## Done When

- There is a compact inventory with recommended keep/merge/archive actions.
- Repeated critical rules are consolidated into canonical files.
- Any proposed archive/delete actions are listed clearly for approval.
- No new scattered process note is created except this handoff note.

## Consolidation Pass Result

Status: partial pass completed.

Edits made:

- `CONTENT_PIPELINE.md`: kept the pipeline rule, but pointed detailed image-story opener/native-text/overlay acceptance rules to `IMAGE_STORY_GATE.md`.
- `NEW_SESSION_START_NOTE.md`: shortened the image workflow reminder and routed review/generation details to `IMAGE_STORY_GATE.md` and `VISUAL_QA_CHECKLIST.md`.

No files were deleted or moved. Archive/delete candidates below still need user approval.

## Canonical Set Recommendation

Keep these as the small current canonical set:

| File | Purpose | Action |
|---|---|---|
| `AGENTS.md` | Mandatory repo rules for agents | Keep short |
| `IMAGE_STORY_GATE.md` | Hard gate for image-only educational cards | Keep canonical |
| `CONTENT_PIPELINE.md` | Pipeline stages, status labels, movement rules | Keep canonical |
| `PIPELINE_BOARD.md` | Current item/status board | Keep canonical and update frequently |
| `PROJECT_STATUS.md` | Project snapshot and major decisions | Keep, but refresh when direction changes |
| `NEW_SESSION_START_NOTE.md` | Minimal fresh-session routing note | Keep, avoid detailed rule duplication |
| `BACKLOG_STRUCTURE.md` | Umbrella vs granular backlog structure | Keep |
| `EPISODE_IDEAS.md` | Topic and episode index | Keep |
| `RENDERER_GUIDE.md` | Multi-renderer strategy | Keep |
| `VISUAL_QA_CHECKLIST.md` | General visual QA checklist | Keep |
| `LOCALIZATION_GUIDE_MARATHI.md` | Marathi localization rules | Keep |
| `HOW_AI_USES_MATH_SERIES_GUIDE.md` | Math-in-AI series rules and quality bar | Keep canonical for series |
| `HOW_AI_USES_MATH_SERIES_PLAN.md` | Math-in-AI sequence and batch plan | Keep canonical for ordering/status |
| `HOW_AI_USES_MATH_LESSON_CORE_TEMPLATE.md` | New episode core template | Keep |
| `HOW_AI_USES_MATH_IMAGE_PREREQUISITES.md` | Pre-image technical checklist | Keep |
| `VIDEO_FIRST_VISUAL_GUIDE.md` | Video-frame vs image-card visual guidance | Keep |
| `VIDEO_PROMPT_TEMPLATES.md` | Reusable prompt templates | Keep |

## Inventory And Proposed Actions

| File group | Current value | Overlap / issue | Proposed action |
|---|---|---|---|
| `AGENTS.md` | Enforceable project rules | Should not become a guide | Keep as-is unless hard rules change |
| `IMAGE_STORY_GATE.md` | Smallest hard gate for image-only stories | Duplicated in pipeline/session/video docs | Keep canonical; route other docs to it |
| `CONTENT_PIPELINE.md` | Pipeline definitions and movement rules | Previously repeated full image-story gate | Keep edited version |
| `NEW_SESSION_START_NOTE.md` | Fast project orientation | Previously repeated image workflow details | Keep edited version |
| `PIPELINE_BOARD.md`, `PROJECT_STATUS.md` | Current state | Dates/status look older than newer assets | Refresh in a separate status session |
| `HOW_AI_USES_MATH_SERIES_GUIDE.md`, `HOW_AI_USES_MATH_SERIES_PLAN.md`, `HOW_AI_USES_MATH_LESSON_CORE_TEMPLATE.md`, `HOW_AI_USES_MATH_IMAGE_PREREQUISITES.md` | Core math-series system | Some image-only rules repeat across files | Keep; future edits should link to `IMAGE_STORY_GATE.md` instead of expanding rules |
| `HOW_AI_USES_MATH_IMAGE_ONLY_GAP_AUDIT.md` | Useful dated audit of missing image-only concept proofs | Some acceptance criteria duplicate the gate | Keep as audit until gaps are resolved, then archive |
| `HOW_AI_USES_MATH_LESSON_REVIEW_PACKET.md` | Large review packet / source for approval | Oversized for routine session loading | Keep as reference, do not put in default read-first list |
| `HOW_AI_USES_MATH_STYLE_DECISION_NOTE.md`, `HOW_AI_USES_MATH_EARLIER_LESSONS_STYLE_B_REFRESH_REVIEW.md` | Style decisions and reviews | Time-bound decisions | Keep until style is stable, then archive |
| `VIDEO_FIRST_VISUAL_GUIDE.md`, `LEARNING_VIDEO_FORMATS.md`, `VIDEO_PROMPT_TEMPLATES.md` | Video production guidance | Some overlap on micro-lesson openings | Keep; `VIDEO_PROMPT_TEMPLATES.md` should stay operational |
| `PHASE 1 - Video Pipeline Resume Note.md`, `PHASE_1_VIDEO_PIPELINE_QUICKSTART.md`, `SHORTS_CREATION_LEARNING_TIMELINE.md`, `NEW_VIDEO_TOPIC_SESSION_BRIEF.md` | Video pipeline history and handoffs | Not needed for every new session | Archive after the stable pipeline rules are reflected in `VIDEO_FIRST_VISUAL_GUIDE.md` and `CONTENT_PIPELINE.md` |
| `NEXT_SESSION_*_NOTE.md` files | Specific handoffs for one next session or parallel batch | Many are stale once assets exist | Archive completed/stale notes after checking their useful rules are in canonical docs |
| `CHARACTER_CONSISTENCY_GUIDE.md` | Prompting support for consistent characters | Mostly reusable production guidance | Keep as reference |
| `STYLE_GUIDE.md`, `VISUAL_JOURNEY_TEMPLATE.md`, `CONTENT_TEMPLATE.md`, `PROJECT_REQUIREMENTS.md`, `ROADMAP.md`, `RESEARCH_GUIDE.md` | Early project scaffolding | Some replaced by newer pipeline/renderer docs | Review one by one; likely archive older scaffolding after preserving any unique rules |
| `CODED_SKILLS_PROPOSAL.md` | Skill implementation planning | Distinct implementation proposal | Keep or move under `.agents/` docs if actively maintained |
| `YOUTUBE_CHANNEL_INITIATIVE.md` | Channel strategy | Distinct strategy doc | Keep, not part of default session load |
| `README.md` | Public repo overview | Can point to canonical docs | Keep; optional later refresh |

## Proposed Archive List For Approval

Archive only after confirming no unique current instruction remains:

```text
NEXT_SESSION_COORDINATES_IMAGE_SET_NOTE.md
NEXT_SESSION_GRADIENT_DESCENT_IMAGE_SET_NOTE.md
NEXT_SESSION_GRAPHS_IMAGE_SET_NOTE.md
NEXT_SESSION_IMAGE_ONLY_FUNCTIONS_NOTE.md
NEXT_SESSION_IMAGE_ONLY_GRADIENT_DESCENT_NOTE.md
NEXT_SESSION_IMAGE_ONLY_GRAPHS_NOTE.md
NEXT_SESSION_IMAGE_ONLY_LINEAR_EQUATIONS_NOTE.md
NEXT_SESSION_IMAGE_ONLY_PARALLEL_BATCH_NOTE.md
NEXT_SESSION_IMAGE_ONLY_SERIES_INTRO_NOTE.md
NEXT_SESSION_IMAGE_ONLY_STATISTICS_NOTE.md
NEXT_SESSION_LOGIC_IMAGE_SET_NOTE.md
NEXT_SESSION_PROBABILITY_VIDEO_NOTE.md
NEXT_SESSION_REMAINING_MATH_IMAGE_SETS_NOTE.md
PHASE 1 - Video Pipeline Resume Note.md
PHASE_1_VIDEO_PIPELINE_QUICKSTART.md
NEW_VIDEO_TOPIC_SESSION_BRIEF.md
SHORTS_CREATION_LEARNING_TIMELINE.md
HOW_AI_USES_MATH_IMAGE_ONLY_GAP_AUDIT.md
HOW_AI_USES_MATH_STYLE_DECISION_NOTE.md
HOW_AI_USES_MATH_EARLIER_LESSONS_STYLE_B_REFRESH_REVIEW.md
```

Keep this note temporarily until the user approves archive actions. After archiving is done, archive this note too.

## Remaining Consolidation Tasks

1. Refresh `PIPELINE_BOARD.md` and `PROJECT_STATUS.md` against the newer math-series assets.
2. Decide whether `LEARNING_VIDEO_FORMATS.md` should stay separate or be summarized into `VIDEO_FIRST_VISUAL_GUIDE.md`.
3. Review early scaffolding docs (`PROJECT_REQUIREMENTS.md`, `ROADMAP.md`, `STYLE_GUIDE.md`, `CONTENT_TEMPLATE.md`, `VISUAL_JOURNEY_TEMPLATE.md`) for unique rules before archiving.
4. After user approval, move archive candidates into a dated archive folder instead of deleting.
