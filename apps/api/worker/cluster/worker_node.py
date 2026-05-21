class WorkerNode:

    def __init__(self, worker_id, executor):

        self.worker_id = worker_id
        self.executor = executor

    def start(self, queue):

        while True:

            goal_data = queue.pop()

            if not goal_data:
                continue

            print(f"[{self.worker_id}] executing {goal_data['id']}")

            self.executor.execute_goal(goal_data["id"])