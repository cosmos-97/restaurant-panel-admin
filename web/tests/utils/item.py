from typing import Optional
from uuid import UUID

from app import crud, models
from app.schemas.item import ItemCreate
from sqlalchemy.orm import Session
from web.tests.utils.category import create_random_category
from web.tests.utils.user import create_random_superuser
from web.tests.utils.utils import random_lower_string


def create_random_item(
    db: Session, *, user_id: Optional[int] = None, category_id: Optional[UUID] = None
) -> models.Item:
    if user_id is None:
        user = create_random_superuser(db)
        user_id = user.id

    if category_id is None:
        category = create_random_category(db, user_id=user_id)
        category_id = category.id

    title = random_lower_string()
    description = random_lower_string()
    item_in = ItemCreate(title=title, description=description, category_id=category_id)
    return crud.item.create_with_owner(db=db, obj_in=item_in, user_id=user_id)
