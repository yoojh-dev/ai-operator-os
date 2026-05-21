import uuid


class ApiKeyManager:

    def __init__(self):

        self.keys = {}

    def create_key(self, workspace_id: str):

        key = str(uuid.uuid4())

        self.keys[key] = workspace_id

        return key

    def validate(self, key: str):

        return self.keys.get(key)