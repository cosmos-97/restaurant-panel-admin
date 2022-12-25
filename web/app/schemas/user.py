from typing import List, Optional
from uuid import UUID

from pydantic import BaseModel, EmailStr, constr


# Shared properties
class UserBase(BaseModel):
    username: Optional[str] = None
    phone: Optional[str] = None
    email: Optional[EmailStr] = None
    stations: Optional[List[UUID]] = None

    class Config:
        orm_mode = True


# Properties to receive via API on creation
class UserCreate(UserBase):
    username: str
    phone: str
    email: EmailStr
    password: constr(min_length=12)


# Properties to receive via API on update
class UserUpdate(UserBase):
    password: Optional[constr(min_length=12)] = None


class UserInDBBase(UserBase):
    from app.schemas.station import Station

    id: Optional[UUID] = None
    stations: Optional[List[Station]] = None

    class Config:
        orm_mode = True


# Additional properties to return via API
class User(UserInDBBase):
    pass


# Additional properties stored in DB
class UserInDB(UserInDBBase):
    hashed_password: str
