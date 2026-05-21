class FailureInjector:

    def inject_tool_failure(self, tool_name):

        def wrapper(*args, **kwargs):

            raise Exception(f"Injected failure in {tool_name}")

        return wrapper