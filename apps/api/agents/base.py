class BaseAgent:

    def __init__(self, name, provider):

        self.name = name
        self.provider = provider

    def run(self, context):

        raise NotImplementedError