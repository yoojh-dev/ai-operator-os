class TraceRetentionPolicy:

    def apply(self, traces):

        return [
            t for t in traces
            if t["age_days"] < 7
        ]