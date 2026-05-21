from dataclasses import dataclass
from typing import Any, Dict


@dataclass
class ToolContract:

    name: str

    args: Dict[str, Any]

    trace_id: str

    node_id: str

    timeout: Optional[int] = None

    retry_policy: Optional[dict] = None

    stream: bool = False