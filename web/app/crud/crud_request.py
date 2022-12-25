from uuid import UUID
from app.models.vendor import Vendor
from app.crud.base import CrudBase
from app.models.request import Request
from app.schemas.request import RequestCreate, RequestUpdate
from fastapi.encoders import jsonable_encoder
from sqlalchemy.orm import Session
from fastapi import HTTPException


class CrudRequest(CrudBase[Request, RequestCreate, RequestUpdate]):
    def create_with_owner(
        self, db: Session, *, obj_in: RequestCreate, user_id: UUID
    ) -> Request:
        obj_in_data = jsonable_encoder(obj_in)
        db_obj = self.model(**obj_in_data, user_id=user_id)

        if not db.query(Vendor).filter(Vendor.id == obj_in.vendor_id).count():
            raise HTTPException(status_code=404, detail="vendor not found")

        db.add(db_obj)
        db.commit()
        db.refresh(db_obj)
        return db_obj


request = CrudRequest(Request)
