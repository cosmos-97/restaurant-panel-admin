from app import crud
from app.core.security import verify_password
from app.schemas.user import UserCreate, UserUpdate
from fastapi.encoders import jsonable_encoder
from sqlalchemy.orm import Session
from web.tests.utils.utils import random_lower_string


def test_create_user(db: Session) -> None:
    username = random_lower_string()
    station = random_lower_string()
    password = random_lower_string()

    user_in = UserCreate(username=username, station=station, password=password)
    user = crud.user.create(db, obj_in=user_in)
    assert user.username == username
    assert user.station == station
    assert hasattr(user, "hashed_password")
    assert user.is_superuser is False


def test_authenticate_user(db: Session) -> None:
    username = random_lower_string()
    station = random_lower_string()
    password = random_lower_string()

    user_in = UserCreate(username=username, station=station, password=password)
    user = crud.user.create(db, obj_in=user_in)
    authenticated_user = crud.user.authenticate(
        db, username=username, password=password
    )
    assert authenticated_user
    assert user.username == authenticated_user.username


def test_not_authenticate_user(db: Session) -> None:
    username = random_lower_string()
    password = random_lower_string()

    user = crud.user.authenticate(db, username=username, password=password)
    assert user is None


def test_check_if_user_is_superuser(db: Session) -> None:
    username = random_lower_string()
    password = random_lower_string()

    user_in = UserCreate(username=username, password=password)
    user = crud.user.create_superuser(db, obj_in=user_in)

    assert user.username == username
    assert user.station is None
    assert hasattr(user, "hashed_password")

    is_superuser = crud.user.is_superuser(user)
    assert is_superuser is True


def test_check_if_user_is_normal_user(db: Session) -> None:
    username = random_lower_string()
    password = random_lower_string()

    user_in = UserCreate(username=username, password=password)
    user = crud.user.create(db, obj_in=user_in)

    is_superuser = crud.user.is_superuser(user)
    assert is_superuser is False


def test_get_user(db: Session) -> None:
    password = random_lower_string()
    username = random_lower_string()

    user_in = UserCreate(username=username, password=password)
    user = crud.user.create(db, obj_in=user_in)
    user_2 = crud.user.get(db, id=user.id)

    assert user_2
    assert user.username == user_2.username
    assert jsonable_encoder(user) == jsonable_encoder(user_2)


def test_update_user(db: Session) -> None:
    password = random_lower_string()
    username = random_lower_string()

    user_in = UserCreate(username=username, password=password)
    user = crud.user.create(db, obj_in=user_in)

    new_password = random_lower_string()

    user_in_update = UserUpdate(password=new_password)
    crud.user.update(db, db_obj=user, obj_in=user_in_update)
    user_2 = crud.user.get(db, id=user.id)

    assert user_2
    assert user.username == user_2.username
    assert verify_password(new_password, user_2.hashed_password)
