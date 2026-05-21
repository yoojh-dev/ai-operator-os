class LatencyOptimizer:

    def optimize(self, config):

        if config["load"] > 0.8:
            return {
                "concurrency": 2,
                "cache_enabled": True
            }

        return {
            "concurrency": 5,
            "cache_enabled": False
        }