from apps.api.planning.merge.schema import Plan, PlanStep


class PlanMerger:

    def merge(self, multi_output: dict) -> Plan:

        steps = []
        step_id = 1

        for source, items in multi_output.items():

            for item in items:

                steps.append(
                    PlanStep(
                        id=step_id,
                        action=item["action"],
                        input=item.get("input", {}),
                        source=source,
                    )
                )

                step_id += 1

        return Plan(steps=steps)