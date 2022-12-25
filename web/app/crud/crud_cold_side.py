from uuid import UUID

from app.crud.base import CrudBase
from app.models.cold_side import ColdSide
from app.models.station import Station
from app.schemas.cold_side import ColdSideCreate, ColdSideUpdate
from fastapi import HTTPException
from fastapi.encoders import jsonable_encoder
from sqlalchemy.orm import Session


class CrudColdSide(CrudBase[ColdSide, ColdSideCreate, ColdSideUpdate]):
    def create_with_owner(
        self, db: Session, *, obj_in: ColdSideCreate, user_id: UUID
    ) -> ColdSide:
        obj_in_data = jsonable_encoder(obj_in)
        db_obj = self.model(**obj_in_data, user_id=user_id)

        if not db.query(Station).filter(Station.id == obj_in.station_id).count():
            raise HTTPException(status_code=404, detail="station not found")

        db.add(db_obj)
        db.commit()
        db.refresh(db_obj)
        return db_obj


cold_side = CrudColdSide(ColdSide)
