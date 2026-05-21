from collections import defaultdict


class ToolGraph:

    def __init__(self):

        self.edges = defaultdict(list)

    def add_edge(self, from_tool: str, to_tool: str):

        self.edges[from_tool].append(to_tool)

    def get_next(self, tool_name: str):

        return self.edges.get(tool_name, [])