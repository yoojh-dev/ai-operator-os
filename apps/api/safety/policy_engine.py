class PolicyEngine:

    def check(self, action):

        if "system_prompt" in str(action):
            return False

        if action.get("tool") in ["dangerous_tool"]:
            return False

        return True