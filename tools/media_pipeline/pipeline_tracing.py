"""LangSmith tracing helpers for media pipeline runs."""

from __future__ import annotations

from contextlib import contextmanager, nullcontext
from typing import Any, Iterator


def truthy(value: str | None) -> bool:
    return (value or "").strip().lower() in {"1", "true", "yes", "on"}


def langsmith_enabled() -> bool:
    import os

    tracing_on = (
        truthy(os.environ.get("LANGSMITH_TRACING"))
        or truthy(os.environ.get("LANGSMITH_TRACING_V2"))
        or truthy(os.environ.get("LANGCHAIN_TRACING_V2"))
    )
    return tracing_on and bool(os.environ.get("LANGSMITH_API_KEY"))


def langsmith_project() -> str | None:
    import os

    return os.environ.get("LANGSMITH_PROJECT") or None


@contextmanager
def trace_run(
    name: str,
    *,
    run_type: str = "chain",
    parent: Any = None,
    inputs: dict[str, Any] | None = None,
    metadata: dict[str, Any] | None = None,
    tags: list[str] | None = None,
) -> Iterator[Any]:
    if not langsmith_enabled():
        with nullcontext(None) as run:
            yield run
        return

    import langsmith as ls

    with ls.trace(
        name,
        run_type=run_type,
        parent=parent,
        inputs=inputs,
        metadata=metadata,
        tags=tags,
        project_name=langsmith_project(),
    ) as run:
        yield run


def end_trace(run: Any, outputs: dict[str, Any]) -> None:
    if run is not None:
        run.end(outputs=outputs)


def trace_id(run: Any) -> str | None:
    if run is None:
        return None
    run_id = getattr(run, "id", None)
    return str(run_id) if run_id else None


def flush_traces() -> None:
    if not langsmith_enabled():
        return
    try:
        from langsmith import Client

        Client().flush()
    except Exception:
        return
