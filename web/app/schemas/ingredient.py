from typing import Optional
from uuid import UUID

from pydantic import BaseModel


class IngredientBase(BaseModel):
    ingredient_name: Optional[str] = None
    measuring_unit: Optional[str] = None
    quantity: Optional[float] = None
    status: Optional[bool] = None

    class Config:
        orm_mode = True


class IngredientCreate(IngredientBase):
    ingredient_name: str
    measuring_unit: str
    quantity: float


class IngredientUpdate(IngredientBase):
    pass


class Ingredient(IngredientBase):
    id: Optional[UUID]
    user_id: Optional[UUID]

    class Config:
        orm_mode = True
