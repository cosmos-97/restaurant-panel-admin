from typing import Optional
from uuid import UUID

from pydantic import BaseModel


class HotSideBase(BaseModel):
    name: Optional[str] = None
    station_id: Optional[UUID] = None
    status: Optional[bool] = None

    class Config:
        orm_mode = True


class HotSideCreate(HotSideBase):
    name: str
    station_id: UUID


class HotSideUpdate(HotSideBase):
    pass


class HotSide(HotSideBase):
    from app.schemas.station import Station

    id: Optional[UUID]
    user_id: Optional[UUID]
    station: Optional[Station]

    class Config:
        orm_mode = True
