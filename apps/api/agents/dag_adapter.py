from apps.api.execution.dag.dag import DAG
from apps.api.execution.dag.parallel_engine import ParallelDAGEngine
from apps.api.agents.agent_node_builder import AgentNodeBuilder


class AgentDagAdapter:

    def __init__(self, provider):

        self.provider = provider
        self.builder = AgentNodeBuilder()

    def execute(self, agent_results, context):

        nodes = self.builder.build(agent_results)

        dag = DAG(nodes=nodes)

        engine = ParallelDAGEngine(
            dag=dag,
            provider=self.provider,
            context=context,
        )

        return engine.run(
            model=context["model"],
            tools=context.get("tools"),
        )