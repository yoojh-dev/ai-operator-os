class ExecutionLimiter:

    def __init__(self):

        self.max_latency = 5.0
        self.max_iterations = 3

    def check_latency(self, latency: float):

        if latency > self.max_latency:
            raise Exception("Latency limit exceeded")

    def check_iterations(self, count: int):

        if count > self.max_iterations:
            raise Exception("Iteration limit exceeded")