import time


class QuotaManager:

    def __init__(self):

        self.calls = {}

    def check(self, tenant_id: str, limit=100):

        now = int(time.time())

        window = self.calls.setdefault(tenant_id, {})

        window[now] = window.get(now, 0) + 1

        total = sum(window.values())

        if total > limit:
            raise Exception("Quota exceeded")