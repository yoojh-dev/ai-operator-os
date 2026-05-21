class PatternMemory:

    def __init__(self):

        self.db = []

    def add(self, sample):

        self.db.append(sample)

    def search(self, query):

        # MVP: naive similarity (upgrade later to embeddings)
        return sorted(
            self.db,
            key=lambda x: x["meta"]["step_count"],
        )[:3]