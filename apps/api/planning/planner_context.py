from dataclasses import dataclass, field


@dataclass
class PlannerContext:
    goal: str

    strategy: str | None = None

    memories: list = field(
        default_factory=list,
    )

    metadata: dict = field(
        default_factory=dict,
    )