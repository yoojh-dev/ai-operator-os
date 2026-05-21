from fastapi import APIRouter

router = APIRouter()


@router.get("/memory/query")
def query_memory(q: str, retriever):

    return {
        "query": q,
        "memories": retriever.retrieve_context(q),
    }