from typing import Optional
from uuid import UUID

from pydantic import BaseModel


class OrderStationBeverageBase(BaseModel):
    beverage_id: Optional[UUID] = None
    count: Optional[int] = None
    status: Optional[bool] = None

    class Config:
        orm_mode = True


class OrderStationBeverageCreate(OrderStationBeverageBase):
    beverage_id: UUID
    count: int


class OrderStationBeverageUpdate(OrderStationBeverageBase):
    pass


class OrderStationBeverage(OrderStationBeverageBase):
    from app.schemas.beverage import Beverage

    beverage: Optional[Beverage]
