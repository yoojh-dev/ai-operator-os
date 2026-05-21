class UsageTracker:

    def __init__(self):

        self.usage = {}

    def record(self, tenant_id, tokens):

        self.usage.setdefault(tenant_id, 0)
        self.usage[tenant_id] += tokens