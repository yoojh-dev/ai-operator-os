import asyncio


class StreamGateway:

    def __init__(self):

        self.clients = set()

    async def connect(self, websocket):

        self.clients.add(websocket)

        try:

            while True:
                await asyncio.sleep(0.1)

        finally:
            self.clients.remove(websocket)

    async def broadcast(self, event):

        dead = []

        for client in self.clients:

            try:
                await client.send_json(event)

            except Exception:
                dead.append(client)

        for d in dead:
            self.clients.remove(d)