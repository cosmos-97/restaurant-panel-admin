from typing import Any, Dict, Union

from app.crud.base import CrudBase
from app.models.vendor import Vendor
from app.models.category import Category
from app.schemas.vendor import VendorCreate, VendorUpdate
from fastapi import HTTPException
from fastapi.encoders import jsonable_encoder
from sqlalchemy.orm import Session


class CrudVendor(CrudBase[Vendor, VendorCreate, VendorUpdate]):
    def create_with_owner(
        self, db: Session, *, obj_in: VendorCreate, user_id: int
    ) -> Vendor:
        obj_in_data = jsonable_encoder(obj_in)
        db_obj = self.model(**obj_in_data, user_id=user_id)

        if obj_in.categories and (
            categories := db.query(Category).filter(Category.id.in_(obj_in.categories))
        ).count() == len(obj_in.categories):
            db_obj.categories.extend(categories)
        elif obj_in.categories:
            raise HTTPException(status_code=404, detail="categories not found")

        db.add(db_obj)
        db.commit()
        db.refresh(db_obj)
        return db_obj

    def update(
        self,
        db: Session,
        *,
        db_obj: VendorCreate,
        obj_in: Union[VendorUpdate, Dict[str, Any]],
    ) -> Vendor:
        obj_data = jsonable_encoder(db_obj)

        if obj_in.categories and (
            categories := db.query(Category).filter(Category.id.in_(obj_in.categories))
        ).count() == len(obj_in.categories):
            db_obj.categories.clear()
            db_obj.categories.extend(categories)
        elif obj_in.categories:
            raise HTTPException(status_code=404, detail="categories not found")
        elif obj_in.categories == []:
            db_obj.categories.clear()

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
        return db_obj


vendor = CrudVendor(Vendor)
