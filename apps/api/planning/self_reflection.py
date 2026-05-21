class SelfReflection:

    def refine_plan(self, plan):

        if "step" not in str(plan):
            return plan

        if len(plan.get("steps", [])) > 8:
            plan["steps"] = plan["steps"][:8]

        plan["refined"] = True

        return plan