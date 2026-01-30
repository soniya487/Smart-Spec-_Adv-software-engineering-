from pydantic import BaseModel
from typing import List


# ---------- INPUT MODELS ----------

class RequirementInput(BaseModel):
    id: str
    text: str


class SRSInput(BaseModel):
    requirements: List[RequirementInput]


# ---------- OUTPUT MODELS ----------

class RewrittenRequirement(BaseModel):
    original_id: str
    original_text: str
    rewritten_text: str


class TraceabilityInfo(BaseModel):
    requirement_id: str
    rules_triggered: List[str]
    phase: str


class RTMEntry(BaseModel):
    requirement_id: str
    requirement_text: str
    detected_issues: List[str]
    related_rules: List[str]
    phase: str


class RequirementAnalysis(BaseModel):
    requirement_id: str
    quality_score: int
    ambiguities: List[str]


class AnalysisResult(BaseModel):
    overall_quality_score: int
    per_requirement_analysis: List[RequirementAnalysis]
    rewritten_requirements: List[RewrittenRequirement]
    traceability: List[TraceabilityInfo]
    rtm: List[RTMEntry]
