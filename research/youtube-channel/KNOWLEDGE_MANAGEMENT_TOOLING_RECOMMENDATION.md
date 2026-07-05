# Knowledge Management Tooling Recommendation

This document answers how to manage ideas, concepts, playlists, renderers, and channel plans as the project grows.

## Recommendation

Use this stack:

```text
Markdown as source of truth
Generated HTML viewer for navigation
ClickUp only for execution tasks
```

Do not move the knowledge system fully into ClickUp yet.

## Why Markdown Should Stay Primary

Markdown is best for this project because:

- Codex can read and edit it easily.
- It works well with Git history.
- It supports long-form reasoning, not just task fields.
- It keeps prompts, decisions, notes, and concepts close to the assets.
- It does not force premature structure.
- It works offline and remains portable.

The current project already uses Markdown as a thinking and production layer:

```text
modules/
research/
backlog/
outputs/mobile-stories/
assets/image-prompts/
```

This is a strength.

## Why A HTML Viewer Helps

Markdown is good for writing, but weak for browsing.

A generated HTML viewer can make it easier to:

- see all concepts at once
- filter by status
- filter by theme or folder
- search across titles and summaries
- navigate to source files
- see what is active, parked, or ready
- browse ideas without opening many files manually

The viewer should not become the source of truth.

It should be regenerated from Markdown.

## Why Not ClickUp First

ClickUp is useful when work becomes execution-heavy:

- due dates
- assignments
- recurring reviews
- checklist accountability
- production sprints
- publishing calendar

But ClickUp is weaker for:

- free-form idea capture
- conceptual relationships
- prompt preservation
- lesson cores
- renderer-specific notes
- long reasoning documents
- versioned knowledge

So ClickUp should be used later for active production tasks, not as the main knowledge base.

## Best Current Setup

Use three layers:

```text
knowledge/ = capture and themes
concepts/ = committed concept production
channel/ = YouTube publishing plan
```

Then generate:

```text
outputs/knowledge-viewer/index.html
```

from the Markdown files.

## What The Viewer Should Show First

Minimum useful viewer:

- all Markdown docs from key folders
- title
- status
- type
- folder/category
- path
- search box
- category filter
- status filter
- quick links to source files

Later:

- concept graph
- playlist board
- renderer status matrix
- launch readiness view
- ClickUp sync for active tasks

## ClickUp Rule

Use ClickUp only when a concept becomes an active task.

Example:

```text
Markdown: "Images Become Matrices" concept, scene plan, prompts, QA notes
ClickUp: "Record voiceover for Images Become Matrices Short by Friday"
```

So ClickUp should track work commitments, not replace thinking.

## Bottom Line

Best thing to build now:

```text
a static HTML knowledge viewer generated from Markdown
```

It gives visual navigation without sacrificing the source-first workflow.
