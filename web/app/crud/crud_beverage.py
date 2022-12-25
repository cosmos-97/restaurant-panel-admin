from uuid import UUID

from app.crud.base import CrudBase
from app.models.beverage import Beverage
from app.schemas.beverage import BeverageCreate, BeverageUpdate
from fastapi.encoders import jsonable_encoder
from sqlalchemy.orm import Session


class CrudBeverage(CrudBase[Beverage, BeverageCreate, BeverageUpdate]):
    def create_with_owner(
        self, db: Session, *, obj_in: BeverageCreate, user_id: UUID
    ) -> Beverage:
        obj_in_data = jsonable_encoder(obj_in)
        db_obj = self.model(**obj_in_data, user_id=user_id)
        db.add(db_obj)
        db.commit()
        db.refresh(db_obj)
        return db_obj


beverage = CrudBeverage(Beverage)
