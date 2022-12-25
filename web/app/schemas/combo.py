from typing import List, Optional
from uuid import UUID

from pydantic import BaseModel, HttpUrl


class ComboBase(BaseModel):
    name: Optional[str] = None
    description: Optional[str] = None
    logo_url: Optional[HttpUrl] = None
    category_id: Optional[UUID] = None
    type: Optional[str] = None
    size: Optional[str] = None
    quantity_sides: Optional[int] = None
    quantity_sauces: Optional[int] = None
    price: Optional[float] = None
    discount_beverage: Optional[bool] = None
    price_beverage: Optional[float] = None
    discount_dessert: Optional[bool] = None
    price_dessert: Optional[float] = None
    hot_sides: Optional[List[UUID]] = None
    cold_sides: Optional[List[UUID]] = None
    items: Optional[List[UUID]] = None
    sauces: Optional[List[UUID]] = None
    ingredients: Optional[List[UUID]] = None
    beverages: Optional[List[UUID]] = None
    options: Optional[List[UUID]] = None
    station_id: Optional[UUID] = None
    desserts: Optional[List[UUID]] = None
    special_instructions: Optional[bool] = None
    status: Optional[bool] = None
    is_archived: Optional[bool] = None
    notify_after_orders: Optional[int] = None

    class Config:
        orm_mode = True


class ComboCreate(ComboBase):
    name: str
    description: str
    logo_url: HttpUrl
    category_id: UUID
    type: str
    price: float
    discount_beverage: bool
    discount_dessert: bool
    special_instructions: bool
    notify_after_orders: int
    station_id: UUID


class ComboUpdate(ComboBase):
    pass


class Category(BaseModel):
    id: Optional[UUID]
    user_id: Optional[UUID]
    category_name: Optional[str]
    logo_url: Optional[str]
    status: Optional[bool]

    class Config:
        orm_mode = True


class Combo(ComboBase):
    from app.schemas.beverage import Beverage
    from app.schemas.cold_side import ColdSide
    from app.schemas.dessert import Dessert
    from app.schemas.hot_side import HotSide
    from app.schemas.ingredient import Ingredient
    from app.schemas.item import Item
    from app.schemas.option import Option
    from app.schemas.sauce import Sauce
    from app.schemas.station import Station

    id: Optional[UUID]
    user_id: Optional[UUID]
    category: Optional[Category]
    items: Optional[List[Item]]
    sauces: Optional[List[Sauce]]
    hot_sides: Optional[List[HotSide]]
    cold_sides: Optional[List[ColdSide]]
    ingredients: Optional[List[Ingredient]]
    options: Optional[List[Option]]
    beverages: Optional[List[Beverage]]
    desserts: Optional[List[Dessert]]
    station: Optional[Station]

    class Config:
        orm_mode = True
