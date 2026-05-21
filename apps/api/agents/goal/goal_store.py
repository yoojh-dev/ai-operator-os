class GoalStore:

    def __init__(self):

        self.store = {}

    def save(self, goal):

        self.store[goal.id] = goal

    def get(self, goal_id):

        return self.store.get(goal_id)