from datetime import tzinfo

import pytz
from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    model_config = SettingsConfigDict(
        env_file=".env",
        env_prefix="TG_",
        case_sensitive=False,
        env_file_encoding="utf-8",
        extra="ignore",
    )

    app_api_id: int
    app_api_hash: str
    bot_token: str
    phone_number: str

    periodic_message_start_time: int = 8
    periodic_message_end_time: int = 22
    periodic_message: str
    periodic_message_recipient: str

    tz: str = "Asia/Almaty"

    @property
    def time_zone(self) -> tzinfo:
        return pytz.timezone(self.tz)


settings = Settings()
