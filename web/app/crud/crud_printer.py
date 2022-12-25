from uuid import UUID

from app.crud.base import CrudBase
from app.models.printer import Printer
from app.schemas.printer import PrinterCreate, PrinterUpdate
from fastapi.encoders import jsonable_encoder
from sqlalchemy.orm import Session


class CrudPrinter(CrudBase[Printer, PrinterCreate, PrinterUpdate]):
    def create_with_owner(
        self, db: Session, *, obj_in: PrinterCreate, user_id: UUID
    ) -> Printer:
        obj_in_data = jsonable_encoder(obj_in)
        db_obj = self.model(**obj_in_data, user_id=user_id)
        db.add(db_obj)
        db.commit()
        db.refresh(db_obj)
        return db_obj


printer = CrudPrinter(Printer)
