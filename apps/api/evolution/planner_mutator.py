class PlannerMutator:

    def mutate(self, planner_config, analysis):

        if analysis.get("tool_failure_clusters"):
            planner_config["tool_selection_bias"] = "conservative"

        if analysis.get("high_latency_paths"):
            planner_config["reasoning_depth"] = "shallow"

        return planner_config