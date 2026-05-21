class PlanOptimizer:

    def optimize(self, plan):

        if len(plan.get("steps", [])) > 10:
            plan["steps"] = plan["steps"][:10]

        return plan