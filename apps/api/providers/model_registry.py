MODEL_REGISTRY = {
    "gemini/gemini-2.5-flash": {
        "provider": "google",
        "supports_tools": True,
        "supports_stream": True,
        "supports_vision": True,
        "context_window": 1_000_000,
        "priority": 1,
        "fallbacks": [
            "openrouter/meta-llama/llama-3.3-70b-instruct",
        ],
    },
    "openrouter/meta-llama/llama-3.3-70b-instruct": {
        "provider": "openrouter",
        "supports_tools": True,
        "supports_stream": True,
        "supports_vision": False,
        "context_window": 128_000,
        "priority": 2,
        "fallbacks": [],
    },
}