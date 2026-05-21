class SLOMonitor:

    def check(self, metrics):

        if metrics["avg_latency"] > 2.0:
            raise Exception("SLO breach: latency")

        if metrics["error_rate"] > 0.05:
            raise Exception("SLO breach: error rate")

        return True