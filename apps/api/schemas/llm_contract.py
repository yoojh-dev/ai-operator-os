from dataclasses import dataclass
from typing import Any, Optional


@dataclass
class LLMContract:

    content: str
    model: str

    usage: dict

    stream: bool = False

    delta: Optional[str] = None

    raw: Any = None