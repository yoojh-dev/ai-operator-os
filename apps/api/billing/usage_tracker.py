class UsageTracker:

    def __init__(self):

        self.usage = {}

    def log(self, tenant_id, tokens):

        self.usage.setdefault(tenant_id, 0)

        self.usage[tenant_id] += tokens

    def get_usage(self, tenant_id):

        return self.usage.get(tenant_id, 0)