class CostRouter:

    def route(self, context):

        token_estimate = context.get("estimated_tokens", 0)

        if token_estimate > 2000:
            return "cheap_model"

        if token_estimate > 800:
            return "balanced_model"

        return "premium_model"