class ReasoningBudget:

    def __init__(self, max_steps=8, max_tools=5):

        self.max_steps = max_steps
        self.max_tools = max_tools

    def allow_step(self, step_count: int) -> bool:

        return step_count < self.max_steps

    def allow_tool(self, tool_count: int) -> bool:

        return tool_count < self.max_tools