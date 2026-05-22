from .worker_node import WorkerNode


class WorkerPool:
    def __init__(self, size: int):
        self.nodes = [
            WorkerNode(f\"worker-{i}\")
            for i in range(size)
        ]

    async def dispatch(self, task):
        node = self.nodes[hash(task.id) % len(self.nodes)]
        return await node.execute(task)