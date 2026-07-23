# Creatomate Render Contract

Source of truth: `tools/media_pipeline/render_creatomate_phase1.py`.

## Environment

- Key: `CREATOMATE_API_KEY`
- Optional asset settings:
  - `VIDEO_ASSET_BASE_URL`
  - `VOICEOVER_URL`
  - `MUSIC_URL`
  - `ELEVENLABS_VOICE_ID`
  - `ELEVENLABS_MODEL_ID`

## Endpoint

- Start render: `POST https://api.creatomate.com/v1/renders`
- Fetch render: `GET https://api.creatomate.com/v1/renders/{render_id}`

## Headers

- `authorization: Bearer <CREATOMATE_API_KEY>`
- `content-type: application/json` for `POST`
- `user-agent: Creatomate-Phase1-Python/0.1`

## Request Payload

Creatomate receives:

```json
{
  "source": {
    "output_format": "mp4",
    "width": 1080,
    "height": 1920,
    "frame_rate": 30,
    "duration": 30,
    "elements": []
  }
}
```

Do not submit the project manifest directly. The script first converts the manifest into a Creatomate `source`.

## Output Files

Files go under `outputs/video-renders/`:

- `<manifest-id>.creatomate-source.json`
- `<manifest-id>.creatomate-render-response.json`
- `<manifest-id>.creatomate-render-final.json`

## Voiceover Rules

The script supports:

- scene-level `voiceover_url`
- `--voiceover-url` or `VOICEOVER_URL`
- manifest `voiceover.public_url`
- Creatomate ElevenLabs provider string only when `voiceover.provider` is `creatomate-elevenlabs`

If no usable voiceover exists, the script exits.

## Process

1. Run without `--submit` first.
2. Inspect `<manifest-id>.creatomate-source.json`.
3. Confirm source uses expected image/video/audio URLs or data URIs.
4. Submit with `--submit`.
5. Poll with `--wait` when needed.
