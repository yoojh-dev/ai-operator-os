import asyncio


class WorkerPool:

    def __init__(self, workers: list):

        self.workers = workers
        self.index = 0

    async def dispatch(self, job):

        worker = self.workers[self.index % len(self.workers)]
        self.index += 1

        return await worker.run(job)