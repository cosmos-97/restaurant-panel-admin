from typing import Optional
from uuid import UUID

from pydantic import BaseModel


class OptionBase(BaseModel):
    option_name: Optional[str] = None
    status: Optional[bool] = None

    class Config:
        orm_mode = True


class OptionCreate(OptionBase):
    option_name: str


class OptionUpdate(OptionBase):
    pass


class Option(OptionBase):
    id: Optional[UUID]
    user_id: Optional[UUID]

    class Config:
        orm_mode = True
