import time
import threading


class Scheduler:

    def __init__(self, queue, worker):

        self.queue = queue
        self.worker = worker

    def start(self):

        def loop():

            while True:

                goal = self.queue.pop()

                if goal:
                    self.worker.execute(goal)

                time.sleep(1)

        thread = threading.Thread(target=loop)
        thread.daemon = True
        thread.start()