from pydantic import BaseModel

from typing import List
from typing import Optional
from typing import Literal
from typing import Dict
from typing import Any

from typing import Optional
from pydantic import BaseModel


# ==========================================
# Tool schemas
# ==========================================


class ToolFunction(BaseModel):
    name: str
    description: Optional[str] = None
    parameters: Dict[str, Any]


class Tool(BaseModel):
    type: str = "function"
    function: ToolFunction


# ==========================================
# Message schema
# ==========================================


class Message(BaseModel):
    """
    OpenAI compatible message schema
    """

    role: Literal[
        "system",
        "user",
        "assistant",
        "tool",
    ]

    content: Optional[str] = None

    # tool calling support
    tool_calls: Optional[List[Dict[str, Any]]] = None


# ==========================================
# Chat completion request
# ==========================================


class ChatCompletionRequest(BaseModel):
    model: str

    messages: List[Message]

    temperature: Optional[float] = 0.7
    stream: Optional[bool] = False

    top_p: Optional[float] = None
    max_tokens: Optional[int] = None
    stop: Optional[Any] = None

    # OpenAI tool calling
    tools: Optional[List[Tool]] = None
    tool_choice: Optional[Any] = None


class ChatMessage(BaseModel):
    role: str
    content: Optional[str]


class ChatChoice(BaseModel):
    index: int
    message: ChatMessage
    finish_reason: Optional[str] = "stop"


class ChatCompletionResponse(BaseModel):
    id: str
    object: str = "chat.completion"
    created: int
    model: str
    choices: list[ChatChoice]