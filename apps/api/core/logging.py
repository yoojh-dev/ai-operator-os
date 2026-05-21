import json
import time


def log_event(
    event: str,
    **kwargs,
):

    payload = {
        "event": event,
        "timestamp": time.time(),
        **kwargs,
    }

    print(
        json.dumps(
            payload,
            ensure_ascii=False,
        )
    )