from fastapi import APIRouter

router = APIRouter()


@router.get("/trace/{trace_id}")
def get_trace(trace_id: str, trace_store):

    return {
        "trace_id": trace_id,
        "events": trace_store.get(trace_id),
    }


@router.get("/replay/{trace_id}")
def replay(trace_id: str, replay_api):

    return replay_api.replay(trace_id)