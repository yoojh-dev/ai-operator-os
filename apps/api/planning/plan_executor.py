from apps.api.tools.registry import (
    ToolRegistry,
)

from apps.api.tools.runtime.executor import (
    ToolExecutor,
)

from apps.api.tools.runtime.tool_contract import (
    ToolContract,
)


class PlanExecutor:

    def __init__(self, provider):

        self.provider = provider

        self.registry = ToolRegistry()

        self.tool_executor = (
            ToolExecutor(
                self.registry
            )
        )

    def execute(
        self,
        model: str,
        plan,
    ):

        execution_context = []

        for step in plan.steps:

            result = self._execute_step(
                step=step,
                execution_context=(
                    execution_context
                ),
            )

            execution_context.append({
                "step": step.step,
                "action": step.action,
                "result": result,
            })

        return self._build_final_response(
            model=model,
            objective=plan.objective,
            execution_context=(
                execution_context
            ),
        )

    def _execute_step(
        self,
        step,
        execution_context,
    ):

        # tool execution
        if step.tool:

            contract = ToolContract(
                name=step.tool,
                args=step.input or {},
                trace_id="planning-trace",
                node_id=step.step,
            )

            result = (
                self.tool_executor
                .execute(contract)
            )

            return {
                "success": result.success,
                "output": result.output,
                "error": result.error,
            }

        # reasoning step
        return {
            "status": "completed",
        }

    def _build_final_response(
        self,
        model: str,
        objective: str,
        execution_context: list,
    ):

        response = self.provider.call(
            model=model,
            messages=[
                {
                    "role": "system",
                    "content": (
                        "You are a response synthesizer."
                    ),
                },
                {
                    "role": "user",
                    "content": (
                        f"""
Objective:
{objective}

Execution Results:
{execution_context}

Generate final response.
"""
                    ),
                },
            ],
        )

        return response