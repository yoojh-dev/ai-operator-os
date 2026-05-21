class ReplayEngine:

    def replay(self, trace):

        for step in trace.steps:

            print(f"[REPLAY] {step['step']}")

            print("INPUT:", step["input"])
            print("OUTPUT:", step["output"])