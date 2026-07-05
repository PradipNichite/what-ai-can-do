# Phase 1 Video Pipeline Quickstart

This prototype is Python-first and API-only. It does not use local FFmpeg or local video rendering.

For the running timeline of what we learned while improving the shorts, see:

```text
SHORTS_CREATION_LEARNING_TIMELINE.md
```

For the product distinction between hook-first Shorts and micro-lesson videos, see:

```text
LEARNING_VIDEO_FORMATS.md
```

## 1. Set API keys

In PowerShell:

```powershell
$env:ELEVENLABS_API_KEY="your_elevenlabs_api_key"
$env:ELEVENLABS_VOICE_ID="your_elevenlabs_voice_id"
$env:CREATOMATE_API_KEY="your_creatomate_api_key"
```

## 2. Generate voiceover

```powershell
python tools\generate_elevenlabs_voiceover.py
```

This creates:

```text
outputs/video-assets/ai-customer-support-agent.mr.voiceover.mp3
```

## 3. Make assets public

Creatomate must be able to fetch the scene images and voiceover from public URLs.

Required:

- public URL for this repo or asset folder
- public URL for the generated MP3

Then set:

```powershell
$env:VIDEO_ASSET_BASE_URL="https://your-public-host.example"
$env:VOICEOVER_URL="https://your-public-host.example/outputs/video-assets/ai-customer-support-agent.mr.voiceover.mp3"
```

The image URLs are built like:

```text
$VIDEO_ASSET_BASE_URL/assets/images/customer-support-mobile-story-mr/01-late-order.png
```

## 4. Dry run Creatomate JSON

```powershell
python tools\render_creatomate_phase1.py
```

This writes:

```text
outputs/video-renders/ai-customer-support-agent-mr-phase1.creatomate-source.json
```

## 5. Submit render

```powershell
python tools\render_creatomate_phase1.py --submit
```

The response is saved to:

```text
outputs/video-renders/ai-customer-support-agent-mr-phase1.creatomate-render-response.json
```

## Current lesson

Manifest:

```text
outputs/video-manifests/ai-customer-support-agent.mr.phase1.json
```

This uses the existing Marathi customer-support story cards and generates a 42-second 9:16 video.
