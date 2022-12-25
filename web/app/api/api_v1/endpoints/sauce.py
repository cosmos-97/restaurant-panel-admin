from typing import List
from uuid import UUID

from app import crud, models, schemas
from app.api import deps
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

router = APIRouter()


@router.get("/", response_model=List[schemas.Sauce])
async def get_sauces(
    db: Session = Depends(deps.get_db),
    skip: int = 0,
    limit: int = 100,
    current_user: models.User = Depends(deps.get_current_superuser),
) -> List[schemas.Sauce]:
    """
    Retrieve sauces.
    """
    sauces = crud.sauce.get_multi(db=db, skip=skip, limit=limit)

    return sauces


@router.get("/{id}", response_model=schemas.Sauce)
async def get_sauce(
    *,
    db: Session = Depends(deps.get_db),
    id: UUID,
    current_user: models.User = Depends(deps.get_current_superuser),
) -> schemas.Sauce:
    """
    Get sauce by ID.
    """
    sauce = crud.sauce.get(db=db, id=id)
    if not sauce:
        raise HTTPException(status_code=404, detail="Sauce not found")

    return sauce


@router.post("/", response_model=schemas.Sauce)
async def create_sauce(
    *,
    db: Session = Depends(deps.get_db),
    sauce_in: schemas.SauceCreate,
    current_user: models.User = Depends(deps.get_current_superuser),
) -> schemas.Sauce:
    """
    Create new sauce.
    """

    sauce = crud.sauce.create_with_owner(db, obj_in=sauce_in, user_id=current_user.id)
    return sauce


@router.put("/{id}", response_model=schemas.Sauce)
async def update_sauce(
    *,
    db: Session = Depends(deps.get_db),
    id: UUID,
    sauce_in: schemas.SauceUpdate,
    current_user: models.User = Depends(deps.get_current_superuser),
) -> schemas.Sauce:
    """
    Update a sauce.
    """
    sauce = crud.sauce.get(db=db, id=id)

    if not sauce:
        raise HTTPException(status_code=404, detail="Sauce not found")

    sauce = crud.sauce.update(db=db, db_obj=sauce, obj_in=sauce_in)
    return sauce


@router.delete("/{id}", response_model=schemas.Sauce)
async def delete_sauce(
    *,
    db: Session = Depends(deps.get_db),
    id: UUID,
    current_user: models.User = Depends(deps.get_current_superuser),
) -> schemas.Sauce:
    """
    Delete a sauce.
    """
    sauce = crud.sauce.get(db=db, id=id)
    if not sauce:
        raise HTTPException(status_code=404, detail="Sauce not found")

    sauce = crud.sauce.delete(db=db, db_obj=sauce)
    return sauce
