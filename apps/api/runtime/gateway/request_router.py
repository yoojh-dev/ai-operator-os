class RequestRouter:

    def __init__(self, execution_api):

        self.execution_api = execution_api

    async def route(self, request):

        # future: tenant routing, A/B, model routing

        return await self.execution_api.execute(request)