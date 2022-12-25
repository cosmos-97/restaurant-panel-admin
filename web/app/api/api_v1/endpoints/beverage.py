from typing import List
from uuid import UUID

from app import crud, models, schemas
from app.api import deps
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

router = APIRouter()


@router.get("/", response_model=List[schemas.Beverage])
async def get_beverages(
    db: Session = Depends(deps.get_db),
    skip: int = 0,
    limit: int = 100,
    current_user: models.User = Depends(deps.get_current_superuser),
) -> List[schemas.Beverage]:
    """
    Retrieve beverages.
    """
    beverages = crud.beverage.get_multi(db=db, skip=skip, limit=limit)

    return beverages


@router.get("/{id}", response_model=schemas.Beverage)
async def get_beverage(
    *,
    db: Session = Depends(deps.get_db),
    id: UUID,
    current_user: models.User = Depends(deps.get_current_superuser),
) -> schemas.Beverage:
    """
    Get beverage by ID.
    """
    beverage = crud.beverage.get(db=db, id=id)
    if not beverage:
        raise HTTPException(status_code=404, detail="Beverage not found")

    return beverage


@router.post("/", response_model=schemas.Beverage)
async def create_beverage(
    *,
    db: Session = Depends(deps.get_db),
    beverage_in: schemas.BeverageCreate,
    current_user: models.User = Depends(deps.get_current_superuser),
) -> schemas.Beverage:
    """
    Create new beverage.
    """

    beverage = crud.beverage.create_with_owner(
        db, obj_in=beverage_in, user_id=current_user.id
    )
    return beverage


@router.put("/{id}", response_model=schemas.Beverage)
async def update_beverage(
    *,
    db: Session = Depends(deps.get_db),
    id: UUID,
    beverage_in: schemas.BeverageUpdate,
    current_user: models.User = Depends(deps.get_current_superuser),
) -> schemas.Beverage:
    """
    Update a beverage.
    """
    beverage = crud.beverage.get(db=db, id=id)

    if not beverage:
        raise HTTPException(status_code=404, detail="Beverage not found")

    beverage = crud.beverage.update(db=db, db_obj=beverage, obj_in=beverage_in)
    return beverage


@router.delete("/{id}", response_model=schemas.Beverage)
async def delete_beverage(
    *,
    db: Session = Depends(deps.get_db),
    id: UUID,
    current_user: models.User = Depends(deps.get_current_superuser),
) -> schemas.Beverage:
    """
    Delete a beverage.
    """
    beverage = crud.beverage.get(db=db, id=id)
    if not beverage:
        raise HTTPException(status_code=404, detail="Beverage not found")

    beverage = crud.beverage.delete(db=db, db_obj=beverage)
    return beverage
