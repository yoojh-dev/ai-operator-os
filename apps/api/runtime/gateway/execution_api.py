from apps.api.execution.dag.engine import DAGEngine


class ExecutionAPI:

    def __init__(self, dag_builder, kernel, auth, quota, tenant_ctx):

        self.dag_builder = dag_builder
        self.kernel = kernel
        self.auth = auth
        self.quota = quota
        self.tenant_ctx = tenant_ctx

    async def execute(self, request):

        # 1. AUTH
        tenant = self.auth.verify(request["api_key"])

        # 2. TENANT BIND
        self.tenant_ctx.set(tenant)

        # 3. QUOTA CHECK
        self.quota.check(tenant)

        # 4. SESSION
        session = request["session"]
        query = request["query"]

        dag = self.dag_builder.build(query)

        engine = DAGEngine(
            dag=dag,
            kernel=self.kernel,
            context=request["context"],
        )

        result = await engine.run(
            model=request.get("model", "default"),
            tools=request.get("tools"),
        )

        return {
            "session_id": session.session_id,
            "trace_id": session.trace_id,
            "result": result,
            "tenant_id": tenant,
        }