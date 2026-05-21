class Sandbox:

    def __init__(self):

        self.max_steps = 10
        self.max_tools = 5

    def validate(self, execution_context):

        if execution_context.get("step_count", 0) > self.max_steps:
            raise Exception("Step limit exceeded")

        if execution_context.get("tool_calls", 0) > self.max_tools:
            raise Exception("Tool limit exceeded")

        return True