from typing import Optional
from uuid import UUID

from pydantic import BaseModel


class OrderStationComboBase(BaseModel):
    combo_id: Optional[UUID] = None
    count: Optional[int] = None
    status: Optional[bool] = None

    class Config:
        orm_mode = True


class OrderStationComboCreate(OrderStationComboBase):
    combo_id: UUID
    count: int


class OrderStationComboUpdate(OrderStationComboBase):
    pass


class OrderStationCombo(OrderStationComboBase):
    from app.schemas.combo import Combo

    combo: Optional[Combo]
