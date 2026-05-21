class StateRebuilder:

    def rebuild(self, events):

        state = {}

        for event in events:

            node = event.get("node_id")
            etype = event.get("event_type")
            payload = event.get("payload")

            if etype == "node_start":
                state[node] = {"status": "running"}

            elif etype == "node_success":
                state[node] = {
                    "status": "success",
                    "output": payload.get("result")
                }

            elif etype == "node_failed":
                state[node] = {
                    "status": "failed",
                    "error": payload.get("error")
                }

        return state