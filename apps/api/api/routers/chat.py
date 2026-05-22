from fastapi import APIRouter

from apps.api.bootstrap.container import get_container


router = APIRouter()


@router.post("/chat")
async def chat(payload: dict):
    container = get_container()

    result = await container.execution_coordinator.run(
        goal=payload["message"],
    )

    return {
        "result": result,
    }