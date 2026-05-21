class ExperimentRunner:

    def run(self, user_id: str, variants: dict):

        if hash(user_id) % 2 == 0:
            return variants["A"]

        return variants["B"]