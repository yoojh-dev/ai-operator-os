class FeedbackLoop:

    def __init__(self, analyzer, pattern_memory):

        self.analyzer = analyzer
        self.pattern_memory = pattern_memory

    def process(self, execution_trace, plan):

        outcome = self.analyzer.analyze(execution_trace)

        self.pattern_memory.store(plan, outcome)

        return outcome