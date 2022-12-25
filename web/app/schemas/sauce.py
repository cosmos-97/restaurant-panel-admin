from typing import Optional
from uuid import UUID

from pydantic import BaseModel


class SauceBase(BaseModel):
    sauce_name: Optional[str] = None
    station_id: Optional[UUID] = None
    status: Optional[bool] = None

    class Config:
        orm_mode = True


class SauceCreate(SauceBase):
    sauce_name: str


class SauceUpdate(SauceBase):
    pass


class Sauce(SauceBase):
    from app.schemas.station import Station

    id: Optional[UUID]
    user_id: Optional[UUID]
    station: Optional[Station]

    class Config:
        orm_mode = True
