from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

from app.database import get_db
from app.models import User
from app.routers.auth import get_current_user
from app.schemas.scenario import (
    ScenarioContent,
    ScenarioGenerateRequest,
    ScenarioListItem,
    ScenarioResponse,
)
from app.services import scenario_service

router = APIRouter(prefix="/scenarios", tags=["Scenarios"])


@router.post("/generate", response_model=ScenarioResponse, status_code=status.HTTP_201_CREATED)
def generate_scenario(
    request: ScenarioGenerateRequest,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user),
):
    try:
        return scenario_service.create_scenario(db, current_user.id, request)
    except ValueError as exc:
        raise HTTPException(status_code=503, detail=str(exc)) from exc
    except Exception as exc:
        raise HTTPException(status_code=502, detail=f"AI generation failed: {exc}") from exc


@router.get("/", response_model=list[ScenarioListItem])
def list_scenarios(
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user),
):
    return scenario_service.list_user_scenarios(db, current_user.id)


@router.get("/{scenario_id}", response_model=ScenarioResponse)
def get_scenario(
    scenario_id: int,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user),
):
    scenario = scenario_service.get_scenario(db, current_user.id, scenario_id)
    if not scenario:
        raise HTTPException(status_code=404, detail="Scenario not found")

    return ScenarioResponse(
        id=scenario.id,
        skill_target=scenario.skill_target,
        language=scenario.language,
        difficulty=scenario.difficulty,
        content=ScenarioContent.model_validate(scenario.content),
        created_at=scenario.created_at,
    )
