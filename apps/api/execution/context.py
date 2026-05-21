from apps.api.memory.runtime.state import ExecutionState


class ExecutionContext:

    def __init__(self, request_id, model, messages):

        self.state = ExecutionState(
            request_id=request_id,
            messages=list(messages),
        )

    def set_plan(self, plan):

        self.state.plan = plan

    def add_message(self, message):

        self.state.append_message(message)

    def add_tool_result(self, tool_id, result):

        self.state.add_tool_result(tool_id, result)