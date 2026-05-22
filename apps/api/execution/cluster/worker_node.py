from typing import Any


class WorkerNode:
    def __init__(self, node_id: str):
        self.node_id = node_id

    def execute(self, task: Any):
        return task.run()