class PlannerAgent(BaseAgent):

    def run(self, context):

        return self.provider.call(
            model="planner-model",
            messages=context["messages"],
        )