from typing import Optional
from uuid import UUID

from pydantic import BaseModel


class OrderStationSauceBase(BaseModel):
    sauce_id: Optional[UUID] = None
    count: Optional[int] = None
    status: Optional[bool] = None

    class Config:
        orm_mode = True


class OrderStationSauceCreate(OrderStationSauceBase):
    sauce_id: UUID
    count: int


class OrderStationSauceUpdate(OrderStationSauceBase):
    pass


class OrderStationSauce(OrderStationSauceBase):
    from app.schemas.sauce import Sauce

    sauce: Optional[Sauce]
