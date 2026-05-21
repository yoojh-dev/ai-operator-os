from apps.api.providers.litellm_provider import call_llm


class AgentExecutor:

    def __init__(self, tool_executor):
        self.tool_executor = tool_executor

    def run(self, model: str, messages: list, plan: list):

        context = messages.copy()
        result = None

        for step in plan.steps:

            if step.tool:
                tool_result = self.tool_executor.execute([
                    {
                        "function": {
                            "name": step.tool,
                            "arguments": {
                                "input": step.input
                            },
                        },
                        "id": f"tool_{step.step}",
                    }
                ])

                context.append({
                    "role": "tool",
                    "content": str(tool_result),
                })

            else:
                response = call_llm(
                    model=model,
                    messages=context,
                )

                context.append({
                    "role": "assistant",
                    "content": response.choices[0].message.content,
                })

        return result