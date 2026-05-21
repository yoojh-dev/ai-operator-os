class PatternMemory:

    def __init__(self):

        self.patterns = []

    def store(self, plan, outcome):

        self.patterns.append({
            "plan": plan,
            "outcome": outcome,
        })

    def retrieve(self):

        return self.patterns