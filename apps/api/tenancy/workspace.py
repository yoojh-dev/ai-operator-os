class Workspace:

    def __init__(self, workspace_id: str, owner_id: str):

        self.workspace_id = workspace_id
        self.owner_id = owner_id

        self.memory_store = {}
        self.goal_store = {}
        self.quota = {
            "requests_per_min": 60,
            "tokens_per_day": 100000,
        }