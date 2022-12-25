from typing import List, Optional
from uuid import UUID

from pydantic import BaseModel, HttpUrl


class ItemBase(BaseModel):
    name: Optional[str] = None
    description: Optional[str] = None
    logo_url: Optional[HttpUrl] = None
    category_id: Optional[UUID] = None
    hot_sides: Optional[List[UUID]] = None
    cold_sides: Optional[List[UUID]] = None
    sauces: Optional[List[UUID]] = None
    ingredients: Optional[List[UUID]] = None
    options: Optional[List[UUID]] = None
    special_instructions: Optional[bool] = None
    price: Optional[float] = None
    size: Optional[str] = None
    station_id: Optional[UUID] = None
    status: Optional[bool] = None
    is_archived: Optional[bool] = None
    notify_after_orders: Optional[int] = None

    class Config:
        orm_mode = True


class ItemCreate(ItemBase):
    name: str
    description: str
    logo_url: HttpUrl
    category_id: UUID
    special_instructions: bool
    price: float
    notify_after_orders: int
    station_id: UUID


class ItemUpdate(ItemBase):
    pass


class Category(BaseModel):
    id: Optional[UUID]
    user_id: Optional[UUID]
    category_name: Optional[str]
    logo_url: Optional[str]
    status: Optional[bool]

    class Config:
        orm_mode = True


class Item(ItemBase):
    from app.schemas.cold_side import ColdSide
    from app.schemas.hot_side import HotSide
    from app.schemas.ingredient import Ingredient
    from app.schemas.option import Option
    from app.schemas.sauce import Sauce
    from app.schemas.station import Station

    id: Optional[UUID]
    user_id: Optional[UUID]
    category: Optional[Category]
    sauces: Optional[List[Sauce]]
    hot_sides: Optional[List[HotSide]]
    cold_sides: Optional[List[ColdSide]]
    ingredients: Optional[List[Ingredient]]
    options: Optional[List[Option]]
    station: Optional[Station]

    class Config:
        orm_mode = True
