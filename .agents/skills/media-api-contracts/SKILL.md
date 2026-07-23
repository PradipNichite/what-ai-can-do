---
name: media-api-contracts
description: Use before calling, debugging, or modifying media pipeline APIs in this repository, including Runway image-to-video, Creatomate renders, ElevenLabs voice/SFX, tmpfiles uploads, OpenAI image generation, OpenAI vision QA, API keys, request payloads, headers, response files, dry runs, polling, or manifest formats. Prevents guessing provider parameter names by routing Codex to the repo's proven wrapper scripts and provider-specific contract notes.
---

# Media API Contracts

Use this skill before making or changing external API calls in the media pipeline.

Do not guess env var names, endpoint paths, request field names, headers, manifest shapes, polling status values, or output file names. Treat the local wrapper scripts as the source of truth for the contract this repo currently uses.

## Required Workflow

1. Read `.env.example`.
2. Search the consuming script with `rg` before naming a key or parameter.
3. Read the provider reference needed for the task:
   - Runway image-to-video: `references/runway.md`
   - Creatomate assembly: `references/creatomate.md`
   - ElevenLabs voice/SFX: `references/elevenlabs.md`
   - tmpfiles uploads: `references/tmpfiles.md`
   - OpenAI image/vision pipeline: `references/openai-media.md`
4. Prefer existing wrapper scripts over hand-written HTTP calls.
5. Use dry-run or request-JSON output first when the script supports it.
6. Submit paid/remote API calls only after the request file or generated source JSON matches the reference contract.
7. Preserve provider response JSON, task JSON, final status JSON, render source JSON, and generated URLs in the expected output folders.
8. If a call fails because of a parameter, status, response shape, or auth lesson, update the relevant reference before ending the task.

## Local Wrappers

Use these entrypoints unless there is a clear reason to extend them:

- `tools/generate_runway_clips.py`
- `tools/render_creatomate_phase1.py`
- `tools/generate_scene_voiceovers.py`
- `tools/generate_elevenlabs_voiceover.py`
- `tools/generate_elevenlabs_sfx.py`
- `tools/upload_tmpfiles.py`
- `tools/openai_image_story_generate.py`
- `tools/openai_visual_qa.py`
- `tools/openai_scene_adequacy.py`

The root `tools/*.py` files are compatibility wrappers. The implementation lives under `tools/media_pipeline/`.

## Production Video Path

Production shorts must use:

```text
approved source frames -> image-to-video clips -> ElevenLabs voiceover -> Creatomate API assembly
```

Local still-image assembly is allowed only for timing/debug previews, not as a deliverable, comparison candidate, or final video.

## Failure Rule

If an API mistake happens twice, productize it:

- update the provider reference in this skill
- update the wrapper script or manifest checker if code can prevent it
- add or extend a static verifier if a future session can detect the mistake without calling the API
- update `AGENT_SYSTEM_OVERVIEW.md` if the workflow or hook set changed

Run:

```powershell
python tools/verify_media_api_contracts.py
```

This verifier is not a live API test. It checks that the repo's scripts, env names, hooks, and skill references still preserve the known-good local contracts.
