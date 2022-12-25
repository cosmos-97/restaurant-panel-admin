from typing import Any, List
from uuid import UUID

from app import crud, models, schemas
from app.api import deps
from fastapi import APIRouter, Body, Depends, HTTPException
from fastapi.encoders import jsonable_encoder
from pydantic import EmailStr
from sqlalchemy.orm import Session

router = APIRouter()


@router.put("/me", response_model=schemas.User)
async def update_user_me(
    *,
    db: Session = Depends(deps.get_db),
    phone: str = Body(None),
    email: EmailStr = Body(None),
    password: str = Body(None),
    current_user: models.User = Depends(deps.get_current_user),
) -> Any:
    """
    Update own user.
    """
    current_user_data = jsonable_encoder(current_user)
    user_in = schemas.UserUpdate(**current_user_data)
    if password is not None:
        user_in.password = password
    if phone is not None:
        user_in.phone = phone
    if email is not None:
        user_in.email = email

    user = crud.user.update(db, db_obj=current_user, obj_in=user_in)
    return user


@router.get("/me", response_model=schemas.User)
async def read_user_me(
    current_user: models.User = Depends(deps.get_current_user),
) -> Any:
    """
    Get current user.
    """
    return current_user


@router.post("/", response_model=schemas.User)
async def create_user(
    *,
    db: Session = Depends(deps.get_db),
    user_in: schemas.UserCreate,
    current_user: models.User = Depends(deps.get_current_superuser),
) -> Any:
    """
    Create new user.
    """
    user = crud.user.get_by_username(db, username=user_in.username)
    if user:
        raise HTTPException(
            status_code=400,
            detail="The user with this username already exists in the system.",
        )
    user = crud.user.create(db, obj_in=user_in)
    return user


@router.get("/", response_model=List[schemas.User])
async def get_users(
    db: Session = Depends(deps.get_db),
    skip: int = 0,
    limit: int = 100,
    current_user: models.User = Depends(deps.get_current_superuser),
) -> List[schemas.User]:
    """
    Retrieve users.
    """
    users = crud.user.get_multi(db=db, skip=skip, limit=limit)

    return users


@router.get("/{id}", response_model=schemas.User)
async def get_user(
    *,
    db: Session = Depends(deps.get_db),
    id: UUID,
    current_user: models.User = Depends(deps.get_current_superuser),
) -> schemas.User:
    """
    Get user by ID.
    """
    user = crud.user.get(db=db, id=id)
    if not user:
        raise HTTPException(status_code=404, detail="User not found")

    return user


@router.put("/{id}", response_model=schemas.User)
async def update_user(
    *,
    db: Session = Depends(deps.get_db),
    id: UUID,
    user_in: schemas.UserUpdate,
    current_user: models.User = Depends(deps.get_current_superuser),
) -> schemas.User:
    """
    Update an user.
    """
    user = crud.user.get(db=db, id=id)

    if not user:
        raise HTTPException(status_code=404, detail="User not found")

    user_by_usename = crud.user.get_by_username(db, username=user_in.username)
    if user_by_usename and user_by_usename.username != user.username:
        raise HTTPException(
            status_code=400,
            detail="The user with this username already exists in the system.",
        )

    user = crud.user.update(db=db, db_obj=user, obj_in=user_in)
    return user


@router.delete("/{id}", response_model=schemas.User)
async def delete_user(
    *,
    db: Session = Depends(deps.get_db),
    id: UUID,
    current_user: models.User = Depends(deps.get_current_superuser),
) -> schemas.User:
    """
    Delete a user.
    """
    user = crud.user.get(db=db, id=id)
    if not user:
        raise HTTPException(status_code=404, detail="User not found")

    user = crud.user.delete(db=db, db_obj=user)
    return user
