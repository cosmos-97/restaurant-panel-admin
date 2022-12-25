from typing import List, Optional
from uuid import UUID
from datetime import datetime
from pydantic import BaseModel


class VendorBase(BaseModel):
    name: Optional[str] = None
    phone: Optional[str] = None
    categories: Optional[List[UUID]] = None

    class Config:
        orm_mode = True


class VendorCreate(VendorBase):
    name: str
    phone: str
    categories: List[UUID]


class VendorUpdate(VendorBase):
    pass


class Vendor(VendorBase):
    from app.schemas.category import Category
    from app.schemas.request import Request

    id: Optional[UUID]
    user_id: Optional[UUID]
    created_at: Optional[datetime]
    categories: Optional[List[Category]]
    requests: Optional[List[Request]]

    class Config:
        orm_mode = True
