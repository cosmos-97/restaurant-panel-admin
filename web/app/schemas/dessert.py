from typing import Optional
from uuid import UUID

from pydantic import BaseModel


class DessertBase(BaseModel):
    dessert_name: Optional[str] = None
    station_id: Optional[UUID] = None
    status: Optional[bool] = None

    class Config:
        orm_mode = True


class DessertCreate(DessertBase):
    dessert_name: str


class DessertUpdate(DessertBase):
    pass


class Dessert(DessertBase):
    from app.schemas.station import Station

    id: Optional[UUID]
    user_id: Optional[UUID]
    station: Optional[Station]

    class Config:
        orm_mode = True
