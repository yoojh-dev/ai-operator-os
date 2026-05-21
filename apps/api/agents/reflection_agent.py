class ReflectionAgent:

    def __init__(self, provider):

        self.provider = provider

    def run(self, context):

        response = self.provider.call(
            model="verifier-model",
            messages=[
                {
                    "role": "system",
                    "content": (
                        "You are a strict critic. "
                        "Evaluate the execution result."
                    ),
                },
                {
                    "role": "user",
                    "content": str(context["execution"]),
                },
            ],
        )

        return response