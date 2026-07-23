# OpenAI Media Pipeline Contract

Sources of truth:

- `tools/media_pipeline/openai_image_story_generate.py`
- `tools/media_pipeline/openai_image_story_pipeline.py`
- `tools/media_pipeline/openai_visual_qa.py`
- `tools/media_pipeline/openai_scene_adequacy.py`
- `tools/media_pipeline/openai_visual_models.py`
- `tools/media_pipeline/README.md`

## Environment

- Required key: `OPENAI_API_KEY`
- Image model: `OPENAI_IMAGE_MODEL`
- Responses agent model for image tool calls: `OPENAI_IMAGE_AGENT_MODEL`
- Vision QA model: `OPENAI_VISION_QA_MODEL`
- Timeout: `OPENAI_REQUEST_TIMEOUT_SECONDS`
- Image parallelism: `OPENAI_MAX_PARALLEL_IMAGES`
- QA parallelism: `OPENAI_MAX_PARALLEL_QA`

## Image Generation

The repo uses the OpenAI Responses API with the `image_generation` tool. Do not use an imagined direct image endpoint when the project wrapper already handles:

- prompt-pack parsing
- reference strategy
- character anchor generation
- per-card output files
- metadata
- LangSmith tracing

`OPENAI_IMAGE_MODEL` controls the image tool model. `OPENAI_IMAGE_AGENT_MODEL` controls the Responses model that invokes the tool.

## Vision QA

`openai_visual_qa.py` uses:

```python
client.responses.parse(..., text_format=VisualQAVerdict)
```

`VisualQAVerdict` is the Pydantic source of truth for structured QA output. Do not hand-roll a second schema unless the script is deliberately being updated.

`pass-with-caveats` is treated as blocking by the wrapper. The script rewrites caveated visual QA to `needs-revision` unless the caveats are fixed and the review is rerun as a clean `pass`.

## Scene Adequacy

Run `openai_scene_adequacy.py` before expensive image generation when a scene flow may not teach the mechanism clearly enough.

`openai_scene_adequacy.py` also treats `pass-with-caveats` as a false pass. It rewrites caveated scene adequacy to `needs-revision` and prevents `proceed-to-prompts` until the scene flow is repaired.

## Dry Runs

Use `--dry-run` where supported before calling OpenAI.
