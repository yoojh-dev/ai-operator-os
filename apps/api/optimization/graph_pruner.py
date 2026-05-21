class GraphPruner:

    def prune(self, plan_graph: dict):

        return {
            k: v for k, v in plan_graph.items()
            if not v.get("optional", False)
        }