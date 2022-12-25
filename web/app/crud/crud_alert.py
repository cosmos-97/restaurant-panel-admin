from typing import Any, Dict, Union

from app.crud.base import CrudBase
from app.models.alert import Alert
from app.models.user import User
from app.schemas.alert import AlertCreate, AlertUpdate
from app.utils import send_message
from fastapi import HTTPException
from fastapi.encoders import jsonable_encoder
from sqlalchemy.orm import Session


class CrudAlert(CrudBase[Alert, AlertCreate, AlertUpdate]):
    def create_with_owner(
        self, db: Session, *, obj_in: AlertCreate, user_id: int
    ) -> Alert:
        obj_in_data = jsonable_encoder(obj_in)
        db_obj = self.model(**obj_in_data, user_id=user_id)

        if obj_in.users and (
            users := db.query(User).filter(User.id.in_(obj_in.users))
        ).count() == len(obj_in.users):
            for user in users:
                send_message(user.phone, obj_in.action_needed)
            db_obj.users.extend(users)
        elif obj_in.users:
            raise HTTPException(status_code=404, detail="users not found")

        db.add(db_obj)
        db.commit()
        db.refresh(db_obj)
        return db_obj

    def update(
        self,
        db: Session,
        *,
        db_obj: AlertCreate,
        obj_in: Union[AlertUpdate, Dict[str, Any]],
    ) -> Alert:
        obj_data = jsonable_encoder(db_obj)

        if obj_in.users and (
            users := db.query(User).filter(User.id.in_(obj_in.users))
        ).count() == len(obj_in.users):
            db_obj.users.clear()
            db_obj.users.extend(users)
        elif obj_in.users:
            raise HTTPException(status_code=404, detail="users not found")
        elif obj_in.users == []:
            db_obj.users.clear()

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


alert = CrudAlert(Alert)
