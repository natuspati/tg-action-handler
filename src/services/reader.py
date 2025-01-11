from tg_client import BaseTGClient


class TGService:
    def __init__(self, client: BaseTGClient):
        self._client = client

    async def send_message(self, recipient: str, message: str) -> None:
        await self._client.send_message(recipient, message)
