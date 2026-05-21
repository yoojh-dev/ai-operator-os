class ReflectionLoop:

    def __init__(self, agent, max_iter=2):

        self.agent = agent
        self.max_iter = max_iter

    def run(self, context):

        current = context

        for _ in range(self.max_iter):

            critique = self.agent.run(current)

            if "good" in critique or "pass" in critique:
                break

            # rewrite plan
            current["messages"].append({
                "role": "system",
                "content": (
                    "Revise plan based on critique:\n"
                    + str(critique)
                ),
            })

            current["refined"] = True

        return current