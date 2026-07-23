# Tmpfiles Upload Contract

Sources of truth:

- `tools/media_pipeline/upload_tmpfiles.py`
- `tools/media_pipeline/generate_scene_voiceovers.py`

## Endpoint

- Upload: `POST https://tmpfiles.org/api/v1/upload`

## Request

- Multipart form field name: `file`
- Content type is guessed from the local file name.
- `upload_tmpfiles.py` adds:
  - `user-agent: WhatAICanDo-Media-Pipeline/0.1`
  - `accept: application/json`

## URL Conversion

The API response URL must be converted from:

```text
https://tmpfiles.org/<path>
```

to:

```text
https://tmpfiles.org/dl/<path>
```

Use the direct `/dl/` URL in manifests for Runway, Creatomate, or voiceover assets.

## Output

The helper prints:

```text
<file-name>: <direct-download-url>
```

With `--json-out`, it writes a JSON object mapping file names to direct URLs.
