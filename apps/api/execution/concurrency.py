import asyncio


class BackpressureController:

    def __init__(self, max_concurrency=5):

        self.semaphore = asyncio.Semaphore(max_concurrency)

    async def acquire(self):

        await self.semaphore.acquire()

    def release(self):

        self.semaphore.release()