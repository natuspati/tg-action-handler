from credentials import TGCredSchema
from services import TGService
from settings import settings
from tg_client import BaseTGClient, TGClient


async def get_tg_service(tg_client: BaseTGClient | None = None) -> TGService:
    if not tg_client:
        tg_client = await get_tg_client()
    return TGService(tg_client)


async def get_tg_client(tg_credentials: TGCredSchema | None = None) -> TGClient:
    if not tg_credentials:
        tg_credentials = await get_tg_credentials()
    return TGClient(tg_credentials)


async def get_tg_credentials(
    api_id: int | None = None,
    api_hash: str | None = None,
    bot_token: str | None = None,
    phone_number: str | None = None,
) -> TGCredSchema:
    return TGCredSchema(
        api_id=api_id or settings.app_api_id,
        api_hash=api_hash or settings.app_api_hash,
        bot_token=bot_token or settings.bot_token,
        phone_number=phone_number or settings.phone_number,
    )
