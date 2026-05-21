class StateBuilder:

    def build(self, trace):

        state = {
            "memory": {},
            "execution_state": {},
            "planner_state": {},
        }

        for event in trace:

            if event.type == "memory":
                state["memory"] = event.payload

            elif event.type == "execution":
                state["execution_state"].update(event.payload)

            elif event.type == "planner":
                state["planner_state"].update(event.payload)

        return state