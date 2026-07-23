# Runway Image-To-Video Contract

Source of truth: `tools/media_pipeline/generate_runway_clips.py`.

## Environment

- Key: `RUNWAYML_API_SECRET`
- Do not use guessed variants such as `RUNWAY_API_KEY`.
- `.env.example` contains the expected key name.

## Endpoint

- Base URL: `https://api.dev.runwayml.com/v1`
- Create task: `POST /image_to_video`
- Poll task: `GET /tasks/{task_id}`
- Version header: `x-runway-version: 2024-11-06`

## Headers

- `authorization: Bearer <RUNWAYML_API_SECRET>`
- `content-type: application/json`
- `x-runway-version: 2024-11-06`
- `user-agent: WhatAICanDo-Runway-Python/0.1`

## Request Payload

The repo writes one `*.request.json` per clip before submitting:

```json
{
  "model": "gen4_turbo",
  "promptImage": "https://...",
  "promptText": "motion prompt",
  "ratio": "720:1280",
  "duration": 5
}
```

Use `promptImage` and `promptText`; do not rename them to guessed snake_case fields.

## Manifest Shape

The input manifest has:

- `id`
- optional `model`, default `gen4_turbo`
- optional `ratio`, default `720:1280`
- optional `duration`, default `5`
- `clips[]`
- each clip has `id`, `image_url`, `prompt`

## Output Files

For manifest `<manifest id>`, files go under `outputs/runway-clips/<manifest id>/`:

- `<clip-id>.request.json`
- `<clip-id>.task.json`
- `<clip-id>.final.json`
- `<clip-id>.mp4`

## Process

1. Run without `--submit` first to write request JSON.
2. Inspect request JSON before submitting.
3. Submit with `--submit`.
4. Poll/download with `--wait` only when desired.
5. Keep failures as `*.final.json` evidence.
