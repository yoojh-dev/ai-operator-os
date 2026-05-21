class MemoryAwarePlanner:

    def __init__(self, retriever, provider):

        self.retriever = retriever
        self.provider = provider

    def build_context(self, query):

        memories = self.retriever.retrieve_context(query)

        return {
            "query": query,
            "memories": memories,
        }

    def plan(self, query):

        context = self.build_context(query)

        response = self.provider.call(
            model="planner-model",
            messages=[
                {
                    "role": "system",
                    "content": (
                        "You are a cognitive planner. "
                        "Use memories to improve planning."
                    ),
                },
                {
                    "role": "user",
                    "content": str(context),
                },
            ],
        )

        return response