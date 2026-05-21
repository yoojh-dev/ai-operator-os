class AgentWorker:

    def __init__(self, goal_manager, event_bus):

        self.goal_manager = goal_manager
        self.event_bus = event_bus

    def execute(self, goal):

        self.event_bus.emit("goal_started", goal.id)

        try:

            result = self.goal_manager.execute_goal(goal.id)

            self.event_bus.emit(
                "goal_completed",
                {
                    "id": goal.id,
                    "result": result,
                },
            )

        except Exception as e:

            self.event_bus.emit(
                "goal_failed",
                {
                    "id": goal.id,
                    "error": str(e),
                },
            )