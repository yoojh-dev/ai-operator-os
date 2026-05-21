import redis
import json


class RedisGoalQueue:

    def __init__(self, redis_url="redis://localhost:6379"):

        self.client = redis.Redis.from_url(redis_url)

    def push(self, goal):

        self.client.lpush(
            "goal_queue",
            json.dumps(goal.__dict__)
        )

    def pop(self):

        data = self.client.brpop("goal_queue", timeout=5)

        if not data:
            return None

        return json.loads(data[1])