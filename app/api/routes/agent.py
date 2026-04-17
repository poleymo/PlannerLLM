from fastapi import APIRouter, Depends
from app.api.dependent_manager import get_intent_service
from app.service.agentService import AgentService
from pydantic import BaseModel

router = APIRouter()


class PlanRequest(BaseModel):
    instruction: str

class PlanPromptRequest(BaseModel):
    instruction: str
    prompt: dict


@router.post("/plan")
def plan(req: PlanRequest, service: AgentService = Depends(get_intent_service)):
    return service.generate_plan(req.instruction)

@router.post("/plan-prompt")
def plan_prompt(req: PlanPromptRequest, service: AgentService = Depends(get_intent_service)):
    return service.generate_plan_prompt(req.instruction, req.prompt)