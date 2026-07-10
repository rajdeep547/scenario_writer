from datetime import datetime
from typing import Literal

from pydantic import BaseModel, Field


Language = Literal["en", "hi"]
Difficulty = Literal["M01", "M02", "M03", "M04", "M05", "M06", "M07"]


class StrategyChip(BaseModel):
    label: str
    approach: str
    explanation: str


class RubricItem(BaseModel):
    criterion: str
    score: int = Field(ge=1, le=5)
    description: str


class ScenarioContent(BaseModel):
    scene: str
    characters: list[str]
    antagonist_line: str
    strategy_chips: list[StrategyChip]
    rubric: list[RubricItem]
    success_criteria: list[str]
    transfer_targets: list[str]


class ScenarioGenerateRequest(BaseModel):
    skill_target: str = Field(min_length=2, max_length=255)
    language: Language = "en"
    difficulty: Difficulty = "M01"


class ScenarioResponse(BaseModel):
    id: int
    skill_target: str
    language: str
    difficulty: str
    content: ScenarioContent
    created_at: datetime

    model_config = {"from_attributes": True}


class ScenarioListItem(BaseModel):
    id: int
    skill_target: str
    language: str
    difficulty: str
    created_at: datetime

    model_config = {"from_attributes": True}
