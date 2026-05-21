class NormalizedStreamDelta:

    def __init__(
        self,
        content=None,
        tool_calls=None,
        role="assistant",
    ):

        self.role = role
        self.content = content
        self.tool_calls = tool_calls or []


class NormalizedStreamChunk:

    def __init__(
        self,
        delta,
        finish_reason=None,
        raw_chunk=None,
    ):

        self.delta = delta
        self.finish_reason = finish_reason
        self.raw_chunk = raw_chunk


def normalize_stream_chunk(chunk):

    if chunk is None:
        return None

    if isinstance(chunk, dict):

        return {
            "type": "stream",
            "content": chunk.get("delta") or chunk.get("content"),
        }

    return {
        "type": "stream",
        "content": str(chunk),
    }