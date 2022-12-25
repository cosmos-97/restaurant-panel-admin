from uuid import UUID

from app.crud.base import CrudBase
from app.models.setting import Appearance, Receipt, Sound, StoreInfo
from app.schemas.setting import (
    AppearanceCreate,
    AppearanceUpdate,
    ReceiptCreate,
    ReceiptUpdate,
    SoundCreate,
    SoundUpdate,
    StoreInfoCreate,
    StoreInfoUpdate,
)
from fastapi.encoders import jsonable_encoder
from sqlalchemy.orm import Session


class CrudAppearance(CrudBase[Appearance, AppearanceCreate, AppearanceUpdate]):
    def get(self, db: Session) -> Appearance:
        return db.query(self.model).first()

    def create_or_update(
        self, db: Session, *, obj_in: AppearanceCreate, user_id: UUID
    ) -> Appearance:
        db_obj = self.get(db)
        if db_obj:
            obj_data = jsonable_encoder(db_obj)
            if isinstance(obj_in, dict):
                update_data = obj_in
            else:
                update_data = obj_in.dict(exclude_unset=True)
            for field in obj_data:
                if field in update_data:
                    setattr(db_obj, field, update_data[field])
            db.add(db_obj)
            db.commit()
            db.refresh(db_obj)
        else:
            obj_in_data = jsonable_encoder(obj_in)
            db_obj = self.model(**obj_in_data, user_id=user_id)
            db.add(db_obj)
            db.commit()
            db.refresh(db_obj)

        return db_obj


class CrudStoreInfo(CrudBase[StoreInfo, StoreInfoCreate, StoreInfoUpdate]):
    def get(self, db: Session) -> StoreInfo:
        return db.query(self.model).first()

    def create_or_update(
        self, db: Session, *, obj_in: StoreInfoCreate, user_id: UUID
    ) -> StoreInfo:
        db_obj = self.get(db)
        if db_obj:
            obj_data = jsonable_encoder(db_obj)
            if isinstance(obj_in, dict):
                update_data = obj_in
            else:
                update_data = obj_in.dict(exclude_unset=True)
            for field in obj_data:
                if field in update_data:
                    setattr(db_obj, field, update_data[field])
            db.add(db_obj)
            db.commit()
            db.refresh(db_obj)
        else:
            obj_in_data = jsonable_encoder(obj_in)
            db_obj = self.model(**obj_in_data, user_id=user_id)
            db.add(db_obj)
            db.commit()
            db.refresh(db_obj)

        return db_obj


class CrudReceipt(CrudBase[Receipt, ReceiptCreate, ReceiptUpdate]):
    def get(self, db: Session) -> Receipt:
        return db.query(self.model).first()

    def create_or_update(
        self, db: Session, *, obj_in: ReceiptCreate, user_id: UUID
    ) -> Receipt:
        db_obj = self.get(db)
        if db_obj:
            obj_data = jsonable_encoder(db_obj)
            if isinstance(obj_in, dict):
                update_data = obj_in
            else:
                update_data = obj_in.dict(exclude_unset=True)
            for field in obj_data:
                if field in update_data:
                    setattr(db_obj, field, update_data[field])
            db.add(db_obj)
            db.commit()
            db.refresh(db_obj)
        else:
            obj_in_data = jsonable_encoder(obj_in)
            db_obj = self.model(**obj_in_data, user_id=user_id)
            db.add(db_obj)
            db.commit()
            db.refresh(db_obj)

        return db_obj


class CrudSound(CrudBase[Sound, SoundCreate, SoundUpdate]):
    def get(self, db: Session) -> Sound:
        return db.query(self.model).first()

    def create_or_update(
        self, db: Session, *, obj_in: SoundCreate, user_id: UUID
    ) -> Sound:
        db_obj = self.get(db)
        if db_obj:
            obj_data = jsonable_encoder(db_obj)
            if isinstance(obj_in, dict):
                update_data = obj_in
            else:
                update_data = obj_in.dict(exclude_unset=True)
            for field in obj_data:
                if field in update_data:
                    setattr(db_obj, field, update_data[field])
            db.add(db_obj)
            db.commit()
            db.refresh(db_obj)
        else:
            obj_in_data = jsonable_encoder(obj_in)
            db_obj = self.model(**obj_in_data, user_id=user_id)
            db.add(db_obj)
            db.commit()
            db.refresh(db_obj)

        return db_obj


appearance = CrudAppearance(Appearance)
store_info = CrudStoreInfo(StoreInfo)
receipt = CrudReceipt(Receipt)
sound = CrudSound(Sound)
