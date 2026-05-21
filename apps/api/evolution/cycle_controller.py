class CycleController:

    def run_cycle(self, feedbacks, planner_config):

        analysis = BehaviorAnalyzer().analyze(feedbacks)

        policy_update = PolicyOptimizer().optimize(analysis)

        new_planner = PlannerMutator().mutate(
            planner_config,
            analysis
        )

        return {
            "policy_update": policy_update,
            "planner": new_planner
        }