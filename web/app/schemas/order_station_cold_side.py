from typing import Optional
from uuid import UUID

from pydantic import BaseModel


class OrderStationColdSideBase(BaseModel):
    cold_side_id: Optional[UUID] = None
    count: Optional[int] = None
    cold_side_size: Optional[str] = None
    status: Optional[bool] = None

    class Config:
        orm_mode = True


class OrderStationColdSideCreate(OrderStationColdSideBase):
    cold_side_id: UUID
    cold_side_size: str
    count: int


class OrderStationColdSideUpdate(OrderStationColdSideBase):
    pass


class OrderStationColdSide(OrderStationColdSideBase):
    from app.schemas.cold_side import ColdSide

    cold_side: Optional[ColdSide]
