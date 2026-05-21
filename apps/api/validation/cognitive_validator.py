class CognitiveValidator:

    def __init__(self, executor, planner, trace_store):

        self.executor = executor
        self.planner = planner
        self.trace_store = trace_store

    def run_e2e(self, query: str, tenant_context=None):

        trace_id = "test-trace"

        plan = self.planner.plan(query)

        result = self.executor.execute(
            request_id=trace_id,
            selected_model=plan["plan"].get("model", "default"),
            fallbacks=[],
            messages=[{"role": "user", "content": query}],
            stream=False,
            tools=None,
        )

        trace = self.trace_store.get(trace_id)

        return {
            "plan": plan,
            "result": result,
            "trace": trace,
        }