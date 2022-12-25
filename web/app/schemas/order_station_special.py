from typing import Optional
from uuid import UUID

from pydantic import BaseModel


class OrderStationSpecialBase(BaseModel):
    special_id: Optional[UUID] = None
    count: Optional[int] = None
    status: Optional[bool] = None

    class Config:
        orm_mode = True


class OrderStationSpecialCreate(OrderStationSpecialBase):
    special_id: UUID
    count: int


class OrderStationSpecialUpdate(OrderStationSpecialBase):
    pass


class OrderStationSpecial(OrderStationSpecialBase):
    from app.schemas.special import Special

    special: Optional[Special]
