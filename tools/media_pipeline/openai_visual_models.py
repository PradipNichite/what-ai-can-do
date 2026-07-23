"""Pydantic schemas for OpenAI visual QA structured output."""

from __future__ import annotations

from typing import Literal

from pydantic import BaseModel, ConfigDict, Field


class GateCheck(BaseModel):
    model_config = ConfigDict(extra="forbid")

    status: Literal["pass", "fail", "partial"]
    evidence: str = Field(description="Visible evidence from the reviewed image files.")
    required_fix: str = Field(
        description="Concrete fix required, or 'None' when this gate passes."
    )


class OverlayRisk(BaseModel):
    model_config = ConfigDict(extra="forbid")

    status: Literal["low", "medium", "high"]
    evidence: str = Field(description="Visible evidence for pasted-overlay risk.")


class FalseCompletionRisk(BaseModel):
    model_config = ConfigDict(extra="forbid")

    status: Literal["low", "medium", "high"]
    evidence: str = Field(
        description=(
            "Visible evidence that the asset either teaches the technical idea "
            "or only creates a polished false sense of understanding."
        )
    )
    required_fix: str = Field(
        description="Concrete fix required, or 'None' when the risk is low."
    )


class FrameNote(BaseModel):
    model_config = ConfigDict(extra="forbid")

    frame: int
    status: Literal["pass", "needs-revision", "reject"]
    evidence: str = Field(description="Visible frame-specific evidence.")
    fix: str = Field(description="Targeted repair instruction, or 'None'.")


class SceneAdequacyCheck(BaseModel):
    model_config = ConfigDict(extra="forbid")

    status: Literal["pass", "partial", "fail"]
    evidence: str = Field(description="Evidence from the lesson source or scene flow.")
    required_fix: str = Field(
        description="Concrete fix required, or 'None' when this gate passes."
    )


class SceneAdequacyRisk(BaseModel):
    model_config = ConfigDict(extra="forbid")

    status: Literal["low", "medium", "high"]
    evidence: str = Field(description="Evidence for the risk level.")
    required_fix: str = Field(
        description="Concrete fix required, or 'None' when the risk is low."
    )


class SceneNote(BaseModel):
    model_config = ConfigDict(extra="forbid")

    scene: int
    title: str
    status: Literal["pass", "needs-revision", "missing", "merge-or-cut"]
    learning_job: str = Field(
        description="The one technical learning job this scene should perform."
    )
    visible_evidence: str = Field(
        description="What the learner should visibly inspect or compare."
    )
    transformation_or_comparison: str = Field(
        description="The represented, computed, compared, scored, or updated step."
    )
    misconception_risk: str = Field(
        description="False impression this scene could create if left unchanged."
    )
    required_fix: str = Field(
        description="Specific scene-level repair, or 'None' when this scene passes."
    )


class MissingScene(BaseModel):
    model_config = ConfigDict(extra="forbid")

    insert_after_scene: int = Field(
        description="Scene number after which the missing scene should be inserted; use 0 for before scene 1."
    )
    title: str
    learning_job: str
    why_needed: str
    must_show: str


class SceneAdequacyVerdict(BaseModel):
    model_config = ConfigDict(extra="forbid")

    status: Literal["pass", "pass-with-caveats", "needs-revision", "reject"] = Field(
        description=(
            "Use pass only when the scene flow has no unresolved caveats. "
            "pass-with-caveats is blocking, not permission to proceed; prefer "
            "needs-revision when caveats affect comprehension, causal flow, or "
            "renderer readiness."
        )
    )
    scene_count: SceneAdequacyCheck
    mechanism_chain: SceneAdequacyCheck
    technical_completeness: SceneAdequacyCheck
    opener_readiness: SceneAdequacyCheck
    renderer_readiness: SceneAdequacyCheck
    false_completion_risk: SceneAdequacyRisk
    scene_notes: list[SceneNote]
    missing_scenes: list[MissingScene]
    recommended_scene_flow: list[str] = Field(
        description="Concise ordered scene flow that should be used before prompt writing."
    )
    verdict: str = Field(description="Short human-readable overall verdict.")
    next_action: Literal[
        "proceed-to-prompts",
        "revise-scene-flow",
        "revise-source-module",
        "split-lesson",
    ]


class VisualQAVerdict(BaseModel):
    model_config = ConfigDict(extra="forbid")

    status: Literal[
        "pass",
        "pass-with-caveats",
        "needs-revision",
        "reject",
        "reference-only",
    ] = Field(
        description=(
            "Use pass only when there are no unresolved caveats for the intended "
            "use. pass-with-caveats is blocking and must not pair with accept or "
            "promotion to candidate/visual-qa/publish-ready."
        )
    )
    intended_use: Literal["image-story", "video-first", "style-reference", "skill-base"]
    opener: GateCheck
    native_composition: GateCheck
    overlay_risk: OverlayRisk
    mechanism_visibility: GateCheck
    technical_understanding: GateCheck
    false_completion_risk: FalseCompletionRisk
    mobile_readability: GateCheck
    frame_notes: list[FrameNote]
    verdict: str = Field(description="Short human-readable overall verdict.")
    next_action: Literal[
        "accept",
        "regenerate-frame",
        "regenerate-set",
        "revise-prompt-pack",
        "use-as-reference-only",
    ]
