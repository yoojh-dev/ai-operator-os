class NormalizedMessage:

    def __init__(
        self,
        content=None,
        tool_calls=None,
        role="assistant",
    ):

        self.role = role
        self.content = content
        self.tool_calls = tool_calls or []


class NormalizedResponse:

    def __init__(
        self,
        message,
        raw_response,
    ):

        self.message = message
        self.raw_response = raw_response


def normalize_response(response):

    if response is None:
        return None

    if isinstance(response, dict):

        return {
            "content": (
                response.get("choices", [{}])[0]
                .get("message", "empty")
            ),
            "model": response.get("model"),
            "usage": response.get("usage", {}),
        }

    return {
        "content": str(response),
        "model": None,
        "usage": {},
    }