class StrategyOptimizer:

    def optimize(self, patterns):

        score_map = {
            "fast": 0,
            "balanced": 0,
            "safe": 0,
        }

        for p in patterns:

            outcome = p["outcome"]

            if outcome["success"]:
                score_map["balanced"] += 1
            else:
                score_map["safe"] += 1

            if outcome["latency"] < 3:
                score_map["fast"] += 1

        return max(score_map, key=score_map.get)