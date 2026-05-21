from pydantic import BaseModel


class PlanStep(BaseModel):

    step: int

    action: str

    tool: str | None = None

    input: dict | None = None


class ExecutionPlan(BaseModel):

    objective: str

    steps: list[PlanStep]