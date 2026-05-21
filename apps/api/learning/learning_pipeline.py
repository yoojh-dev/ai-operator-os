class LearningPipeline:

    def __init__(self, feedback_collector, pattern_memory):

        self.feedback_collector = feedback_collector
        self.pattern_memory = pattern_memory

    def run(self, trace_id: str, plan):

        feedback = self.feedback_collector.collect(trace_id)

        self.pattern_memory.store(
            plan=plan,
            outcome=feedback
        )

        return feedback