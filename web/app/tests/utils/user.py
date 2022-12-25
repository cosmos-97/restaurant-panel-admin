from typing import Dict

from app import crud
from app.core.config import settings
from app.models.user import User
from app.schemas.user import UserCreate, UserUpdate
from fastapi.testclient import TestClient
from sqlalchemy.orm import Session
from app.tests.utils.utils import random_lower_string


def user_authentication_headers(
    *, client: TestClient, username: str, password: str
) -> Dict[str, str]:
    data = {"username": username, "password": password}

    r = client.post(f"{settings.API_V1_STR}/login/access-token", data=data)
    response = r.json()
    auth_token = response["access_token"]
    headers = {"Authorization": f"Bearer {auth_token}"}
    return headers


def create_random_superuser(db: Session) -> User:
    username = random_lower_string()
    phone = random_lower_string()
    email = f"{random_lower_string()}@email.com"
    password = random_lower_string()

    user_in = UserCreate(username=username, phone=phone, email=email, password=password)
    user = crud.user.create_superuser(db=db, obj_in=user_in)

    return user


def authentication_token_from_username(
    *, client: TestClient, username: str, db: Session
) -> Dict[str, str]:
    password = random_lower_string()
    user = crud.user.get_by_username(db, username=username)
    if not user:
        user_in_create = UserCreate(username=username, password=password)
        user = crud.user.create(db, obj_in=user_in_create)
    else:
        user_in_update = UserUpdate(password=password)
        user = crud.user.update(db, db_obj=user, obj_in=user_in_update)

    return user_authentication_headers(
        client=client, username=username, password=password
    )
