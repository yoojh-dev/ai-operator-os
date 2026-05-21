class BaseTool:

    name: str
    description: str

    def run(self, args: dict):

        raise NotImplementedError

    def openai_schema(self):

        raise NotImplementedError