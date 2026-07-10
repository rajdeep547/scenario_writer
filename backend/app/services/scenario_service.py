from sqlalchemy.orm import Session

from app.models import Scenario
from app.schemas.scenario import ScenarioGenerateRequest, ScenarioResponse
from app.services.groq_service import groq_service


def create_scenario(db: Session, user_id: int, request: ScenarioGenerateRequest) -> ScenarioResponse:
    content = groq_service.generate_scenario(request)

    scenario = Scenario(
        user_id=user_id,
        skill_target=request.skill_target,
        language=request.language,
        difficulty=request.difficulty,
        content=content.model_dump(),
    )
    db.add(scenario)
    db.commit()
    db.refresh(scenario)

    return ScenarioResponse(
        id=scenario.id,
        skill_target=scenario.skill_target,
        language=scenario.language,
        difficulty=scenario.difficulty,
        content=content,
        created_at=scenario.created_at,
    )


def list_user_scenarios(db: Session, user_id: int) -> list[Scenario]:
    return (
        db.query(Scenario)
        .filter(Scenario.user_id == user_id)
        .order_by(Scenario.created_at.desc())
        .all()
    )


def get_scenario(db: Session, user_id: int, scenario_id: int) -> Scenario | None:
    return (
        db.query(Scenario)
        .filter(Scenario.id == scenario_id, Scenario.user_id == user_id)
        .first()
    )
