class MetricsCollector:

    def __init__(self):

        self.metrics = {}

    def record_latency(self, tenant_id, latency):

        self.metrics.setdefault(tenant_id, [])

        self.metrics[tenant_id].append({
            "latency": latency
        })

    def record_cost(self, tenant_id, cost):

        self.metrics.setdefault(tenant_id, [])

        self.metrics[tenant_id].append({
            "cost": cost
        })