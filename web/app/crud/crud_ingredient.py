from uuid import UUID

from app.crud.base import CrudBase
from app.models.ingredient import Ingredient
from app.schemas.ingredient import IngredientCreate, IngredientUpdate
from fastapi.encoders import jsonable_encoder
from sqlalchemy.orm import Session


class CrudIngredient(CrudBase[Ingredient, IngredientCreate, IngredientUpdate]):
    def create_with_owner(
        self, db: Session, *, obj_in: IngredientCreate, user_id: UUID
    ) -> Ingredient:
        obj_in_data = jsonable_encoder(obj_in)
        db_obj = self.model(**obj_in_data, user_id=user_id)
        db.add(db_obj)
        db.commit()
        db.refresh(db_obj)
        return db_obj


ingredient = CrudIngredient(Ingredient)
