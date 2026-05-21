class WorkerPool:

    def __init__(self, workers):

        self.workers = workers

    def start_all(self, queue):

        for w in self.workers:
            w.start(queue)