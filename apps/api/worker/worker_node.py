class WorkerNode:

    def __init__(self, kernel):

        self.kernel = kernel

    async def run(self, job):

        return await self.kernel.execute_node(
            node=job.node,
            trace_id=job.trace_id,
            messages=job.messages,
            tools=job.tools,
        )