class AdminDashboard:

    def __init__(self, usage_tracker):

        self.usage_tracker = usage_tracker

    def get_stats(self):

        return {
            "total_usage": self.usage_tracker.usage,
        }