from typing import List, Optional
from uuid import UUID

from pydantic import BaseModel


class CategoryBase(BaseModel):
    category_name: Optional[str] = None
    logo_url: Optional[str] = None
    status: Optional[bool] = None

    class Config:
        orm_mode = True


class CategoryCreate(CategoryBase):
    category_name: str
    logo_url: str


class CategoryUpdate(CategoryBase):
    pass


class Category(CategoryBase):
    from app.schemas.combo import Combo
    from app.schemas.item import Item
    from app.schemas.special import Special

    id: Optional[UUID]
    user_id: Optional[UUID]
    items: List[Item]
    combos: List[Combo]
    specials: List[Special]

    class Config:
        orm_mode = True
