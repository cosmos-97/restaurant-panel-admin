from typing import Optional
from uuid import UUID

from pydantic import BaseModel


class BeverageBase(BaseModel):
    beverage_name: Optional[str] = None
    station_id: Optional[UUID] = None
    status: Optional[bool] = None

    class Config:
        orm_mode = True


class BeverageCreate(BeverageBase):
    beverage_name: str


class BeverageUpdate(BeverageBase):
    pass


class Beverage(BeverageBase):
    from app.schemas.station import Station

    id: Optional[UUID]
    user_id: Optional[UUID]
    station: Optional[Station]

    class Config:
        orm_mode = True
