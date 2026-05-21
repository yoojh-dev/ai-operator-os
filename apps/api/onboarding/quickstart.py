class Quickstart:

    def generate(self):

        return """
        # Cognitive OS Quickstart

        from cognitive_os import CognitiveOSClient

        client = CognitiveOSClient(
            base_url="http://localhost:8000",
            api_key="your-key"
        )

        response = client.chat("Hello system")

        print(response)
        """