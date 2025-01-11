from telethon import TelegramClient

from credentials import TGCredSchema
from tg_client.base_client import BaseTGClient


class MainTGClient(BaseTGClient):
    def __init__(
        self,
        credentials: TGCredSchema,
        session: str | None = None,
    ):
        super().__init__(credentials)
        self._session = session or "default"
        self._login_code: str | None = None
        self._client: TelegramClient | None = None

    @property
    async def client(self) -> TelegramClient:
        if not self._client:
            self._client = TelegramClient(
                session=self._session,
                api_id=self._api_id,
                api_hash=self._api_hash,
            )
            await self._client.start(
                phone=lambda: self._phone_number, code_callback=self._get_code
            )
        return self._client

    async def send_message(self, recipient: str, message: str) -> None:
        client = await self.client
        await client.send_message(
            entity=recipient,
            message=message,
        )

    def _get_code(self) -> str:
        if not self._login_code:
            self._login_code = input("Enter code: ")
        return self._login_code
