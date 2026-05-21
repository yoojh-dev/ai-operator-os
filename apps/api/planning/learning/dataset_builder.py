import json

from apps.api.planning.learning.trace_analyzer import TraceAnalyzer


class DatasetBuilder:

    def __init__(self):

        self.analyzer = TraceAnalyzer()

    def build(self, request, trace):

        analysis = self.analyzer.analyze(trace)

        sample = {
            "input": {
                "messages": request["messages"],
                "model": request["model"],
            },

            "output": {
                "plan": {
                    "tool_sequence": analysis["tool_sequence"],
                    "step_count": analysis["step_count"],
                }
            },

            "meta": {
                "success": analysis["success"],
                "trace_length": len(trace.steps),
            }
        }

        return sample

    def to_jsonl(self, dataset: list):

        return "\n".join(
            json.dumps(d, ensure_ascii=False)
            for d in dataset
        )