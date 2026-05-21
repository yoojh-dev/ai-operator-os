class LatencyController:

    def adjust(self, load: float):

        if load > 0.8:
            return {
                "concurrency": 2,
                "streaming": True,
                "tool_depth": "shallow"
            }

        return {
            "concurrency": 5,
            "streaming": False,
            "tool_depth": "deep"
        }