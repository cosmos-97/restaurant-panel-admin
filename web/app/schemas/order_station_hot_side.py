from typing import Optional
from uuid import UUID

from pydantic import BaseModel


class OrderStationHotSideBase(BaseModel):
    hot_side_id: Optional[UUID] = None
    count: Optional[int] = None
    hot_side_size: Optional[str] = None
    status: Optional[bool] = None

    class Config:
        orm_mode = True


class OrderStationHotSideCreate(OrderStationHotSideBase):
    hot_side_id: UUID
    hot_side_size: str
    count: int


class OrderStationHotSideUpdate(OrderStationHotSideBase):
    pass


class OrderStationHotSide(OrderStationHotSideBase):
    from app.schemas.hot_side import HotSide

    hot_side: Optional[HotSide]
