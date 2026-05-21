class PolicyMemory:

    def __init__(self):

        self.policies = {}

    def update(self, key, value):

        self.policies[key] = value

    def get(self, key):

        return self.policies.get(key)