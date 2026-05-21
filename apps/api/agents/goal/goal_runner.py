class GoalRunner:

    def __init__(self, executor, reflection_loop):

        self.executor = executor
        self.reflection_loop = reflection_loop

    def run(self, goal):

        goal.status = "running"

        context = {
            "messages": [
                {
                    "role": "user",
                    "content": goal.description,
                }
            ]
        }

        result, model = self.executor.execute(
            request_id=goal.id,
            selected_model="default",
            fallbacks=[],
            messages=context["messages"],
        )

        context["execution"] = result

        refined = self.reflection_loop.run(context)

        if "fail" in str(refined):
            goal.status = "failed"
        else:
            goal.status = "completed"

        goal.result = refined

        return goal