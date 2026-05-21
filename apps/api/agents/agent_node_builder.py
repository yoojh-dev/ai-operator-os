from apps.api.execution.dag.node import Node


class AgentNodeBuilder:

    def build(self, agent_outputs: dict):

        nodes = []

        for agent_name, output in agent_outputs.items():

            node = Node(
                id=f"agent_{agent_name}",
                action=agent_name,
                input=output,
                depends_on=[],
            )

            nodes.append(node)

        return nodes