from typing import Optional
from uuid import UUID

from app import crud, models
from app.schemas.category import CategoryCreate
from sqlalchemy.orm import Session
from web.tests.utils.user import create_random_superuser
from web.tests.utils.utils import random_lower_string


def create_random_category(
    db: Session, *, user_id: Optional[UUID] = None
) -> models.Category:
    if user_id is None:
        user = create_random_superuser(db)
        user_id = user.id

    category_name = random_lower_string()
    category_in = CategoryCreate(category_name=category_name)
    return crud.category.create_with_owner(db=db, obj_in=category_in, user_id=user_id)
