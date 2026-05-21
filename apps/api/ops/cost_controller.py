class CostController:

    def __init__(self):

        self.daily_budget = 10.0
        self.spent = 0.0

    def charge(self, cost: float):

        self.spent += cost

        if self.spent > self.daily_budget:
            raise Exception("Budget exceeded")