from typing import Optional
from uuid import UUID

from pydantic import BaseModel


class OrderStationItemBase(BaseModel):
    item_id: Optional[UUID] = None
    count: Optional[int] = None
    status: Optional[bool] = None

    class Config:
        orm_mode = True


class OrderStationItemCreate(OrderStationItemBase):
    item_id: UUID
    count: int


class OrderStationItemUpdate(OrderStationItemBase):
    pass


class OrderStationItem(OrderStationItemBase):
    from app.schemas.item import Item

    item: Optional[Item]
