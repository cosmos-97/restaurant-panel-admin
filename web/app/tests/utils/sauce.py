from typing import Optional
from uuid import UUID

from app import crud, models
from app.schemas.sauce import SauceCreate
from sqlalchemy.orm import Session
from app.tests.utils.user import create_random_superuser
from app.tests.utils.utils import random_lower_string


def create_random_sauce(db: Session, *, user_id: Optional[UUID] = None) -> models.Sauce:
    if user_id is None:
        user = create_random_superuser(db)
        user_id = user.id

    sauce_name = random_lower_string()
    sauce_in = SauceCreate(sauce_name=sauce_name)
    return crud.sauce.create_with_owner(db=db, obj_in=sauce_in, user_id=user_id)
