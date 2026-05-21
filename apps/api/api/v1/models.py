from fastapi import APIRouter

router = APIRouter()


SUPPORTED_MODELS = [
    {
        "id": "gemini/gemini-2.5-flash",
        "object": "model",
        "owned_by": "google",
    },
    {
        "id": "openrouter/meta-llama/llama-3.3-70b-instruct",
        "object": "model",
        "owned_by": "meta",
    },
]


@router.get("/models")
async def list_models():

    return {
        "object": "list",
        "data": SUPPORTED_MODELS,
    }