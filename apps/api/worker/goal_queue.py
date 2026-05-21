from collections import deque


class GoalQueue:

    def __init__(self):

        self.queue = deque()

    def push(self, goal):

        self.queue.append(goal)

    def pop(self):

        if self.queue:
            return self.queue.popleft()

        return None