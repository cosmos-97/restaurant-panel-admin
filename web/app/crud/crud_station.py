from uuid import UUID

from app.crud.base import CrudBase
from app.models.station import Station
from app.schemas.station import StationCreate, StationUpdate
from fastapi.encoders import jsonable_encoder
from sqlalchemy.orm import Session


class CrudStation(CrudBase[Station, StationCreate, StationUpdate]):
    def create_with_owner(
        self, db: Session, *, obj_in: StationCreate, user_id: UUID
    ) -> Station:
        obj_in_data = jsonable_encoder(obj_in)
        db_obj = self.model(**obj_in_data, user_id=user_id)
        db.add(db_obj)
        db.commit()
        db.refresh(db_obj)
        return db_obj


station = CrudStation(Station)
