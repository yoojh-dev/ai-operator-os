class FeatureFlags:

    def __init__(self):

        self.flags = {
            "planner_v3": True,
            "replay_engine": False,
            "analytics": True,
        }

    def is_enabled(self, feature: str):

        return self.flags.get(feature, False)