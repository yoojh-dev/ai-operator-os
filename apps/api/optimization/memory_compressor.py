class MemoryCompressor:

    def compress(self, memories: list):

        compressed = []

        for m in memories:

            compressed.append({
                "summary": m.get("summary"),
                "importance": m.get("importance", 0) * 0.7
            })

        return compressed