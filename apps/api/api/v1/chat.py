from fastapi import APIRouter
from typing import Dict, Any
import uuid

router = APIRouter()


class ChatService:

    def __init__(self, planner, kernel, memory_system=None):
        self.planner = planner
        self.kernel = kernel
        self.memory_system = memory_system

    def run(self, message: str, context: Dict[str, Any]):

        trace_id = str(uuid.uuid4())

        # 1. plan 생성
        plan = self.planner.plan(
            goal=message,
            context={
                **context,
                "trace_id": trace_id
            }
        )

        # 2. execution 실행
        results = self.kernel.run(
            plan=plan,
            trace_id=trace_id
        )

        # 3. memory 저장 (optional)
        if self.memory_system:
            self.memory_system.save(
                trace_id=trace_id,
                data={
                    "message": message,
                    "results": [r.__dict__ for r in results]
                }
            )

        # 4. response 생성
        return {
            "trace_id": trace_id,
            "result": results[-1].output if results else None,
            "steps": len(results)
        }


# FastAPI endpoint
@router.post("/chat")
def chat(payload: Dict[str, Any]):

    return app_state.chat_service.run(
        message=payload["message"],
        context=payload.get("context", {})
    )