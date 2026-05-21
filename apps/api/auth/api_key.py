class APIKeyAuth:

    def __init__(self, key_store):

        self.key_store = key_store

    def verify(self, api_key: str):

        tenant = self.key_store.get(api_key)

        if not tenant:
            raise Exception("Invalid API Key")

        return tenant