from typing import List, Optional
from uuid import UUID

from pydantic import BaseModel


class AlertBase(BaseModel):
    item_name: Optional[str] = None
    unit: Optional[str] = None
    time: Optional[float] = None
    action_needed: Optional[str] = None
    automatic_ordering: Optional[bool] = None
    users: Optional[List[UUID]] = None

    class Config:
        orm_mode = True


class AlertCreate(AlertBase):
    item_name: str
    unit: str
    time: float
    action_needed: str
    automatic_ordering: bool
    users: List[UUID]


class AlertUpdate(AlertBase):
    pass


class Alert(AlertBase):
    from app.schemas.user import User

    id: Optional[UUID]
    user_id: Optional[UUID]
    users: Optional[List[User]]

    class Config:
        orm_mode = True
