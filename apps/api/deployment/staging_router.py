class StagingRouter:

    def route(self, user_id: str):

        if user_id.startswith("test"):
            return "staging"

        return "production"