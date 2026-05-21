import random


class TrafficSplitter:

    def __init__(self, rollout_rate=0.1):

        self.rollout_rate = rollout_rate

    def allow(self):

        return random.random() < self.rollout_rate