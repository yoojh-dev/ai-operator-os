class PlanValidator:

    def validate(self, plan):

        if not plan.steps:
            raise ValueError("Plan is empty")

        for step in plan.steps:

            if not step.action:
                raise ValueError(f"Invalid step action: {step}")

            if step.input is None:
                step.input = {}

        return plan