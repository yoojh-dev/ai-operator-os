class VerifierAgent(BaseAgent):

    def run(self, context):

        return self.provider.call(
            model="verifier-model",
            messages=context["messages"],
        )