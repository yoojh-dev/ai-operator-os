class OpenAPIBuilder:

    def build(self):

        return {
            "openapi": "3.0.0",
            "paths": {
                "/chat/completions": {
                    "post": {
                        "summary": "Chat with Cognitive OS"
                    }
                },
                "/goals/create": {
                    "post": {
                        "summary": "Create autonomous goal"
                    }
                }
            }
        }