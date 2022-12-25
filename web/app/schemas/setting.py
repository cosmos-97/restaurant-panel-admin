from typing import Optional

from pydantic import BaseModel, HttpUrl


class Appearance(BaseModel):
    welcome_screen_url: Optional[HttpUrl] = None
    logo_url: Optional[HttpUrl] = None
    title_1: Optional[str] = None
    title_2: Optional[str] = None

    class Config:
        orm_mode = True


class AppearanceCreate(Appearance):
    pass


class AppearanceUpdate(Appearance):
    pass


class StoreInfo(BaseModel):
    name: Optional[str] = None
    telephone: Optional[str] = None
    city: Optional[str] = None
    address_1: Optional[str] = None
    address_2: Optional[str] = None
    state: Optional[str] = None
    zip_code: Optional[str] = None
    tax_id: Optional[str] = None
    store_id: Optional[str] = None

    class Config:
        orm_mode = True


class StoreInfoCreate(StoreInfo):
    pass


class StoreInfoUpdate(StoreInfo):
    pass


class Receipt(BaseModel):
    address_1: Optional[str] = None
    address_2: Optional[str] = None
    tax_amount: Optional[float] = None
    other_charges: Optional[float] = None
    message: Optional[str] = None

    class Config:
        orm_mode = True


class ReceiptCreate(Receipt):
    pass


class ReceiptUpdate(Receipt):
    pass


class Sound(BaseModel):
    incoming_order: Optional[HttpUrl] = None
    ready_order: Optional[HttpUrl] = None

    class Config:
        orm_mode = True


class SoundCreate(Sound):
    pass


class SoundUpdate(Sound):
    pass
