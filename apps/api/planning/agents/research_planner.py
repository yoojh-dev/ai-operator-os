from apps.api.planning.base import BasePlanner


class ResearchPlanner(BasePlanner):

    def __init__(self, provider):
        self.provider = provider

    def create_plan(self, model, messages):

        return self.provider.call(
            model=model,
            messages=[
                {
                    "role": "system",
                    "content": "Focus on analysis and context gathering.",
                }
            ]
            + messages,
        ).message.content