from typing import List
from uuid import UUID

from app.crud.base import CrudBase
from app.models.category import Category
from app.schemas.category import CategoryCreate, CategoryUpdate
from fastapi.encoders import jsonable_encoder
from sqlalchemy.orm import Session


class CrudCategory(CrudBase[Category, CategoryCreate, CategoryUpdate]):
    def get_multi(
        self, db: Session, *, skip: int = 0, limit: int = 100
    ) -> List[Category]:
        return (
            db.query(Category).offset(skip).limit(limit).all(),
            db.query(Category).count(),
        )

    def create_with_owner(
        self, db: Session, *, obj_in: CategoryCreate, user_id: UUID
    ) -> Category:
        obj_in_data = jsonable_encoder(obj_in)
        db_obj = self.model(**obj_in_data, user_id=user_id)
        db.add(db_obj)
        db.commit()
        db.refresh(db_obj)
        return db_obj


category = CrudCategory(Category)
