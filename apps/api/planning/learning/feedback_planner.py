class FeedbackPlanner:

    def __init__(self, provider, retriever):

        self.provider = provider
        self.retriever = retriever

    def create_plan(self, model, messages):

        query = messages[-1]["content"]

        similar = self.retriever.retrieve(query)

        context = "\n".join([
            str(item["plan"])
            for item in similar
        ])

        response = self.provider.call(
            model=model,
            messages=[
                {
                    "role": "system",
                    "content": (
                        "You are a planner. "
                        "Use past successful patterns."
                    ),
                },
                {
                    "role": "system",
                    "content": f"Relevant past plans:\n{context}",
                },
                *messages,
            ],
        )

        return response