class CognitiveOSClient:

    def __init__(self, base_url, api_key):

        self.base_url = base_url
        self.api_key = api_key

    def chat(self, message: str):

        return self._request("/chat/completions", {
            "messages": [
                {"role": "user", "content": message}
            ]
        })

    def create_goal(self, description: str):

        return self._request("/goals/create", {
            "description": description
        })

    def get_trace(self, trace_id: str):

        return self._request(f"/traces/{trace_id}")