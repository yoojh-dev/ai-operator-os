class MemoryWeighting:

    def weight(self, memories, query):

        weighted = []

        for m in memories:

            score = m.get("score", 0.5)

            relevance = self._relevance(m, query)

            final_weight = (score * 0.6) + (relevance * 0.4)

            weighted.append({
                "memory": m,
                "weight": final_weight,
            })

        return sorted(
            weighted,
            key=lambda x: x["weight"],
            reverse=True,
        )

    def _relevance(self, memory, query):

        # simple heuristic MVP
        return 1.0 if query in str(memory) else 0.3