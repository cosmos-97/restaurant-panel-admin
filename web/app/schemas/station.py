from typing import Optional, List
from uuid import UUID

from pydantic import BaseModel


class StationBase(BaseModel):
    station_name: Optional[str] = None
    max_time: Optional[int] = None
    statuses: Optional[List[str]] = None

    class Config:
        orm_mode = True


class StationCreate(StationBase):
    station_name: str
    max_time: int


class StationUpdate(StationBase):
    pass


class Station(StationBase):
    id: Optional[UUID]
    user_id: Optional[UUID]
    channel_name: Optional[str]

    class Config:
        orm_mode = True
