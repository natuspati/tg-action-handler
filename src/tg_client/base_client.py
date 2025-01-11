from abc import ABC, abstractmethod

from base_lib.utilities import SingletonABCMeta
from credentials import TGCredSchema


class BaseTGClient(ABC, metaclass=SingletonABCMeta):
    def __init__(self, credentials: TGCredSchema):
        self._api_id = credentials.api_id
        self._api_hash = credentials.api_hash
        self._bot_token = credentials.bot_token
        self._phone_number = credentials.phone_number

    @abstractmethod
    async def send_message(self, recipient: str, message: str) -> None:
        pass
