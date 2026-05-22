from abc import ABC, abstractmethod


class BaseTool(ABC):
    name: str

    @abstractmethod
    async def execute(self, params: dict):
        pass