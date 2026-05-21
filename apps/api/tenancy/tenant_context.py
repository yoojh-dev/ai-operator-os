class TenantContext:

    def __init__(self):

        self._local = {}

    def set(self, tenant_id: str):

        self._local["tenant_id"] = tenant_id

    def get(self):

        return self._local.get("tenant_id")