from uuid import UUID

from app.crud.base import CrudBase
from app.models.dessert import Dessert
from app.schemas.dessert import DessertCreate, DessertUpdate
from fastapi.encoders import jsonable_encoder
from sqlalchemy.orm import Session


class CrudDessert(CrudBase[Dessert, DessertCreate, DessertUpdate]):
    def create_with_owner(
        self, db: Session, *, obj_in: DessertCreate, user_id: UUID
    ) -> Dessert:
        obj_in_data = jsonable_encoder(obj_in)
        db_obj = self.model(**obj_in_data, user_id=user_id)
        db.add(db_obj)
        db.commit()
        db.refresh(db_obj)
        return db_obj


dessert = CrudDessert(Dessert)
