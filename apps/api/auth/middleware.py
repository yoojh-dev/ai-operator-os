class TenantMiddleware:

    def __init__(self, api_key_manager):

        self.api_key_manager = api_key_manager

    def resolve(self, request):

        api_key = request.headers.get("x-api-key")

        tenant = self.api_key_manager.validate(api_key)

        return tenant