import json


class StreamToolState:
    """
    Streaming tool call assembly state
    """

    def __init__(self):

        self.tool_call_id = None
        self.tool_name = None

        self.arguments_buffer = ""

        self.finished = False

    def process_delta(self, delta: dict):

        tool_calls = delta.get("tool_calls")

        if not tool_calls:
            return

        tool_call = tool_calls[0]

        # id
        if tool_call.get("id"):
            self.tool_call_id = tool_call["id"]

        function = tool_call.get("function", {})

        # function name
        if function.get("name"):
            self.tool_name = function["name"]

        # arguments chunk accumulate
        if function.get("arguments"):

            self.arguments_buffer += (
                function["arguments"]
            )

    def is_complete(self):

        if (
            self.tool_call_id
            and self.tool_name
            and self.arguments_buffer
        ):
            return True

        return False

    def build_tool_call(self):

        return {
            "id": self.tool_call_id,
            "type": "function",
            "function": {
                "name": self.tool_name,
                "arguments": self.arguments_buffer,
            },
        }

    def parse_arguments(self):

        try:
            return json.loads(
                self.arguments_buffer
            )

        except Exception:
            return {}