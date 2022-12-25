from typing import Any, Dict, Optional, Union

from app.core.security import get_password_hash, verify_password
from app.crud.base import CrudBase
from app.models.station import Station
from app.models.user import User
from app.schemas.user import UserCreate, UserUpdate
from fastapi import HTTPException
from fastapi.encoders import jsonable_encoder
from sqlalchemy.orm import Session


class CrudUser(CrudBase[User, UserCreate, UserUpdate]):
    def get_by_username(self, db: Session, *, username: str) -> Optional[User]:
        return db.query(User).filter(User.username == username).first()

    def create(self, db: Session, *, obj_in: UserCreate) -> User:
        db_obj = User(
            username=obj_in.username,
            phone=obj_in.phone,
            email=obj_in.email,
            hashed_password=get_password_hash(obj_in.password),
        )

        if obj_in.stations and (
            stations := db.query(Station).filter(Station.id.in_(obj_in.stations))
        ).count() == len(obj_in.stations):
            db_obj.stations.extend(stations)
        elif obj_in.stations:
            raise HTTPException(status_code=404, detail="stations not found")

        db.add(db_obj)
        db.commit()
        db.refresh(db_obj)
        return db_obj

    def create_superuser(self, db: Session, *, obj_in: UserCreate) -> User:
        db_obj = User(
            username=obj_in.username,
            phone=obj_in.phone,
            email=obj_in.email,
            hashed_password=get_password_hash(obj_in.password),
            is_superuser=True,
        )
        db.add(db_obj)
        db.commit()
        db.refresh(db_obj)
        return db_obj

    def update(
        self, db: Session, *, db_obj: User, obj_in: Union[UserUpdate, Dict[str, Any]]
    ) -> User:
        obj_data = jsonable_encoder(db_obj)

        if obj_in.stations and (
            stations := db.query(Station).filter(Station.id.in_(obj_in.stations))
        ).count() == len(obj_in.stations):
            db_obj.stations.clear()
            db_obj.stations.extend(stations)
        elif obj_in.stations:
            raise HTTPException(status_code=404, detail="stations not found")
        elif obj_in.stations == []:
            db_obj.stations.clear()

        if isinstance(obj_in, dict):
            update_data = obj_in
        else:
            update_data = obj_in.dict(exclude_unset=True)

        if update_data.get("password"):
            hashed_password = get_password_hash(update_data["password"])
            del update_data["password"]
            update_data["hashed_password"] = hashed_password

        for field in obj_data:
            if field in update_data:
                setattr(db_obj, field, update_data[field])

        db.add(db_obj)
        db.commit()
        db.refresh(db_obj)
        return db_obj

    def authenticate(
        self, db: Session, *, username: str, password: str
    ) -> Optional[User]:
        user = self.get_by_username(db, username=username)
        if not user:
            return None
        if not verify_password(password, user.hashed_password):
            return None
        return user

    def is_superuser(self, user: User) -> bool:
        return user.is_superuser


user = CrudUser(User)
