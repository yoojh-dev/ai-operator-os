class StreamBridge:

    def __init__(self, event_bus, stream_gateway):

        self.gateway = stream_gateway

        event_bus.subscribe("node_start", self.forward)
        event_bus.subscribe("node_success", self.forward)
        event_bus.subscribe("node_failed", self.forward)

    def forward(self, event):

        import asyncio

        asyncio.create_task(
            self.gateway.broadcast(event)
        )