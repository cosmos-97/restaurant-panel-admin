from uuid import UUID

from app.crud.base import CrudBase
from app.models.sauce import Sauce
from app.schemas.sauce import SauceCreate, SauceUpdate
from fastapi.encoders import jsonable_encoder
from sqlalchemy.orm import Session


class CrudSauce(CrudBase[Sauce, SauceCreate, SauceUpdate]):
    def create_with_owner(
        self, db: Session, *, obj_in: SauceCreate, user_id: UUID
    ) -> Sauce:
        obj_in_data = jsonable_encoder(obj_in)
        db_obj = self.model(**obj_in_data, user_id=user_id)
        db.add(db_obj)
        db.commit()
        db.refresh(db_obj)
        return db_obj


sauce = CrudSauce(Sauce)
