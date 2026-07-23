# ElevenLabs Voice And SFX Contract

Sources of truth:

- `tools/media_pipeline/generate_scene_voiceovers.py`
- `tools/media_pipeline/generate_elevenlabs_voiceover.py`
- `tools/media_pipeline/generate_elevenlabs_sfx.py`
- `tools/media_pipeline/render_creatomate_phase1.py` for default voice lookup.

## Environment

- Key: `ELEVENLABS_API_KEY`
- Optional voice: `ELEVENLABS_VOICE_ID`
- Optional model: `ELEVENLABS_MODEL_ID`
- Default model: `eleven_multilingual_v2`
- Preferred prototype voice when no user override is present: `Zara - Soft and Serene Indian Voice`
- Preferred prototype voice ID: `ADd2WEtjmwokqUr0Y5Ad`

## Headers

- `xi-api-key: <ELEVENLABS_API_KEY>`
- `accept: audio/mpeg` for TTS
- `content-type: application/json`

## Voice Endpoints

- Voices list: `GET https://api.elevenlabs.io/v1/voices`
- Text to speech: `POST https://api.elevenlabs.io/v1/text-to-speech/{voice_id}`
- Sound effects: `POST https://api.elevenlabs.io/v1/sound-generation`

## TTS Payload

The repo uses:

```json
{
  "text": "voiceover text",
  "model_id": "eleven_multilingual_v2",
  "voice_settings": {
    "stability": 0.54,
    "similarity_boost": 0.78,
    "style": 0.08,
    "use_speaker_boost": true
  }
}
```

Use a single continuous voiceover for lesson prototypes unless a manifest explicitly chooses scene-level voiceovers. A continuous voiceover generally feels less stitched together and more like one complete lesson.

`generate_scene_voiceovers.py` writes one MP3 per scene with `scenes[].voiceover_text`, then can patch `scenes[].voiceover_url` into the manifest with `--write-manifest`.

## Output Files

Scene voiceovers go under:

```text
outputs/video-assets/<manifest-id>/
```

If uploading is enabled, tmpfiles direct-download URLs are written back into scene `voiceover_url` fields.
