from dataclasses import (
    dataclass,
    field,
)

from typing import (
    Any,
    Dict,
    Optional,
)


@dataclass
class ToolResult:

    name: str

    success: bool

    output: Any

    error: Optional[str] = None

    meta: Dict[str, Any] = field(
        default_factory=dict
    )