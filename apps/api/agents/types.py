from enum import Enum


class AgentType(Enum):

    PLANNER = "planner"
    RESEARCH = "research"
    TOOL = "tool"
    EXECUTOR = "executor"
    VERIFIER = "verifier"