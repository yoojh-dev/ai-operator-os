class DashboardBuilder:

    def build(self, metrics):

        return {
            "system_health": {
                "latency": metrics["latency"],
                "cost": metrics["cost"],
                "quality": metrics["quality"],
            },
            "status": "healthy"
        }