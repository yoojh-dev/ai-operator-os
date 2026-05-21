from uuid import uuid4


class GoalManager:

    def __init__(self, runner, store):

        self.runner = runner
        self.store = store

    def create_goal(self, description: str):

        goal = Goal(
            id=str(uuid4()),
            description=description,
            status="pending",
            context={},
        )

        self.store.save(goal)

        return goal

    def execute_goal(self, goal_id: str):

        goal = self.store.get(goal_id)

        return self.runner.run(goal)