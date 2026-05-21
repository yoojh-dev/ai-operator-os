# apps/api/execution/runtime/execution_kernel.py

from typing import Any, Dict, List


class ExecutionKernel:

    def __init__(self, tool_executor, event_emitter):
        self.tool_executor = tool_executor
        self.event_emitter = event_emitter

    def run(self, plan: List[Dict[str, Any]], trace_id: str):

        results = []

        # execution start
        self.event_emitter.emit(
            trace_id=trace_id,
            node_id="kernel",
            event_type="execution.start",
            payload={"plan_size": len(plan)},
        )

        # flat execution (NO DAG)
        for step in plan:

            node_id = step["node_id"]
            tool_contract = step["tool_contract"]

            self.event_emitter.emit(
                trace_id=trace_id,
                node_id=node_id,
                event_type="execution.node.start",
                payload=step,
            )

            result = self.tool_executor.execute(tool_contract)

            self.event_emitter.emit(
                trace_id=trace_id,
                node_id=node_id,
                event_type="execution.node.end",
                payload={
                    "success": result.success,
                    "output": result.output,
                    "error": result.error,
                },
            )

            results.append(result)

        self.memory.save(
            trace_id=trace_id,
            data={
                "plan": plan,
                "results": results
            }
        )

        # execution end
        self.event_emitter.emit(
            trace_id=trace_id,
            node_id="kernel",
            event_type="execution.end",
            payload={"result_count": len(results)},
        )

        return results