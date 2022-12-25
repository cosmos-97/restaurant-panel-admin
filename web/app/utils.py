import enum
from typing import Generic, Optional, TypeVar

import sqlalchemy as sa
from jose import jwt
from pydantic.generics import GenericModel
from sqlalchemy.dialects.postgresql import TSVECTOR
from twilio.rest import Client

from app.core.config import settings

DataType = TypeVar("DataType")


class IResponseBase(GenericModel, Generic[DataType]):
    total_records_count: int = None
    page_size: int = None
    page_number: int = None
    records: Optional[DataType] = None


def verify_password_reset_token(token: str) -> Optional[str]:
    from app import schemas

    try:
        decoded_token = jwt.decode(token, settings.SECRET_KEY, algorithms=["HS256"])
        token_data = schemas.TokenPayload(**decoded_token)

        return token_data.sub
    except jwt.JWTError:
        return None


class OrderType(enum.Enum):
    DineIn = "DineIn"
    TakeOut = "TakeOut"

    def __str__(self) -> str:
        return self.name


# noinspection PyAbstractClass
class TSVector(sa.types.TypeDecorator):  # pylint:disable=abstract-method
    impl = TSVECTOR
    cache_ok = True


def send_message(phone_number: str, body: str):
    client = Client(settings.TWILIO_ACCOUNT_SID, settings.TWILIO_AUTH_TOKEN)
    message = client.messages.create(
        body=body,
        from_=settings.TWILIO_PHONE_NUMBER,
        to=phone_number,
    )
