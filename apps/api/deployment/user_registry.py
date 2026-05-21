class UserRegistry:

    def __init__(self):

        self.users = {}

    def register(self, user_id: str):

        self.users[user_id] = {
            "usage_count": 0,
            "tier": "free",
        }

    def increment(self, user_id: str):

        self.users[user_id]["usage_count"] += 1