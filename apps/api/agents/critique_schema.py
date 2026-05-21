from pydantic import BaseModel


class CritiqueResult(BaseModel):

    score: float
    issues: list[str]
    improvements: list[str]
    should_rewrite: bool