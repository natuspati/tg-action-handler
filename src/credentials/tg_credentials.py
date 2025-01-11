from base_lib.schema import BaseSchema


class TGCredSchema(BaseSchema):
    api_id: int
    api_hash: str
    bot_token: str
    phone_number: str
