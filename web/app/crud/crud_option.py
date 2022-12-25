from uuid import UUID

from app.crud.base import CrudBase
from app.models.option import Option
from app.schemas.option import OptionCreate, OptionUpdate
from fastapi.encoders import jsonable_encoder
from sqlalchemy.orm import Session


class CrudOption(CrudBase[Option, OptionCreate, OptionUpdate]):
    def create_with_owner(
        self, db: Session, *, obj_in: OptionCreate, user_id: UUID
    ) -> Option:
        obj_in_data = jsonable_encoder(obj_in)
        db_obj = self.model(**obj_in_data, user_id=user_id)
        db.add(db_obj)
        db.commit()
        db.refresh(db_obj)
        return db_obj


option = CrudOption(Option)
