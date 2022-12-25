from typing import List
from uuid import UUID

from app import crud, models, schemas
from app.api import deps
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

router = APIRouter()


@router.get("/", response_model=List[schemas.Dessert])
async def get_desserts(
    db: Session = Depends(deps.get_db),
    skip: int = 0,
    limit: int = 100,
    current_user: models.User = Depends(deps.get_current_superuser),
) -> List[schemas.Dessert]:
    """
    Retrieve desserts.
    """
    desserts = crud.dessert.get_multi(db=db, skip=skip, limit=limit)

    return desserts


@router.get("/{id}", response_model=schemas.Dessert)
async def get_dessert(
    *,
    db: Session = Depends(deps.get_db),
    id: UUID,
    current_user: models.User = Depends(deps.get_current_superuser),
) -> schemas.Dessert:
    """
    Get dessert by ID.
    """
    dessert = crud.dessert.get(db=db, id=id)
    if not dessert:
        raise HTTPException(status_code=404, detail="Dessert not found")

    return dessert


@router.post("/", response_model=schemas.Dessert)
async def create_dessert(
    *,
    db: Session = Depends(deps.get_db),
    dessert_in: schemas.DessertCreate,
    current_user: models.User = Depends(deps.get_current_superuser),
) -> schemas.Dessert:
    """
    Create new dessert.
    """

    dessert = crud.dessert.create_with_owner(
        db, obj_in=dessert_in, user_id=current_user.id
    )
    return dessert


@router.put("/{id}", response_model=schemas.Dessert)
async def update_dessert(
    *,
    db: Session = Depends(deps.get_db),
    id: UUID,
    dessert_in: schemas.DessertUpdate,
    current_user: models.User = Depends(deps.get_current_superuser),
) -> schemas.Dessert:
    """
    Update a dessert.
    """
    dessert = crud.dessert.get(db=db, id=id)

    if not dessert:
        raise HTTPException(status_code=404, detail="Dessert not found")

    dessert = crud.dessert.update(db=db, db_obj=dessert, obj_in=dessert_in)
    return dessert


@router.delete("/{id}", response_model=schemas.Dessert)
async def delete_dessert(
    *,
    db: Session = Depends(deps.get_db),
    id: UUID,
    current_user: models.User = Depends(deps.get_current_superuser),
) -> schemas.Dessert:
    """
    Delete a dessert.
    """
    dessert = crud.dessert.get(db=db, id=id)
    if not dessert:
        raise HTTPException(status_code=404, detail="Dessert not found")

    dessert = crud.dessert.delete(db=db, db_obj=dessert)
    return dessert
