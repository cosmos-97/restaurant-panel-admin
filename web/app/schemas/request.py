from datetime import datetime
from typing import Optional
from uuid import UUID

from pydantic import BaseModel


class RequestBase(BaseModel):
    vendor_id: Optional[UUID] = None
    product: Optional[str] = None
    price: Optional[float] = None
    quantity: Optional[float] = None
    unit: Optional[str] = None
    status: Optional[bool] = None

    class Config:
        orm_mode = True


class RequestCreate(RequestBase):
    vendor_id: UUID
    product: str
    price: float
    quantity: float
    unit: str
    status: bool


class RequestUpdate(RequestBase):
    pass


class Vendor(BaseModel):
    id: Optional[UUID]
    user_id: Optional[UUID]
    name: Optional[str]
    phone: Optional[str]
    created_at: Optional[datetime]

    class Config:
        orm_mode = True


class Request(RequestBase):
    id: Optional[int]
    user_id: Optional[UUID]
    created_at: Optional[datetime]
    vendor: Optional[Vendor]

    class Config:
        orm_mode = True
