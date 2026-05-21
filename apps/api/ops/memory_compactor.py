class MemoryCompactor:

    def compact(self, memories):

        return [
            {
                "summary": m["summary"],
                "weight": m["weight"] * 0.8
            }
            for m in memories
            if m["importance"] > 0.3
        ]