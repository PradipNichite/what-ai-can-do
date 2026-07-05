# Phase 1 Video Pipeline Resume Note

Date: 2026-06-29

## Goal

Start Phase 1 of the API-first video generation pipeline.

This phase is implementation planning / prototype setup for converting one existing lesson into a polished 9:16 video using cloud APIs only. No local FFmpeg or local rendering.

## Chosen Starting Direction

Use **Creatomate first** for final video assembly.

Reason:

- Existing lesson assets are already structured.
- Creatomate is strong for template-driven automation.
- It supports API-based rendering, image placement, motion/zoom/pan, captions, transitions, music, and 9:16 exports.
- It is a simpler first step than introducing image-to-video generation immediately.

## Phase 1 Scope

Create one proof-of-concept lesson video using:

- Existing story structure
- Existing voiceover script/audio
- Scene-by-scene captions
- Existing 9:16 scene images
- Scene order
- Timing information
- Animated still-image motion such as zoom/pan/Ken Burns style
- Caption animation
- Light scene transitions
- Background music if available
- 9:16 final export

## Explicitly Out of Scope for Phase 1

- No Runway image-to-video yet
- No Kling / Luma / Pika / Hailuo testing yet
- No full image-to-video workflow
- No local FFmpeg
- No manual Premiere / CapCut / dashboard-only workflow
- No broad product build before validating one lesson

## Recommended Next Steps

1. Pick one representative lesson with complete assets.
2. Inspect the local asset structure and identify:
   - Scene images
   - Voiceover audio
   - Captions
   - Scene timing
   - Any existing metadata JSON/Markdown
3. Read Creatomate API/template docs as needed.
4. Design a minimal Creatomate template:
   - 9:16 canvas
   - One image layer per scene or reusable scene composition
   - Animated scale/position for Ken Burns-style movement
   - Caption text layer
   - Audio layer for voiceover
   - Optional music layer
5. Create a small lesson manifest format if one does not already exist.
6. Render one cloud-generated video through Creatomate.
7. Review output quality:
   - Caption timing
   - Image framing
   - Motion pacing
   - Audio sync
   - Export quality
8. Only after Phase 1 looks good, begin Phase 2 with 2-3 Runway-generated hero clips.

## Success Criteria

Phase 1 is successful when we can produce one complete 9:16 lesson video from existing assets using a cloud rendering API, with no local video processing.

## Research Document

Related research file:

`C:\Users\Pradip Nichite\Documents\What AI Can Do\API-First Video Generation Pipeline Research.md`

