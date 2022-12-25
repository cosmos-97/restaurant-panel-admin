from typing import List
from uuid import UUID

from app import crud, models, schemas
from app.api import deps
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

router = APIRouter()


@router.get("/", response_model=List[schemas.ColdSide])
async def get_cold_sides(
    db: Session = Depends(deps.get_db),
    skip: int = 0,
    limit: int = 100,
    current_user: models.User = Depends(deps.get_current_superuser),
) -> List[schemas.ColdSide]:
    """
    Retrieve cold_sides.
    """
    cold_sides = crud.cold_side.get_multi(db=db, skip=skip, limit=limit)

    return cold_sides


@router.get("/{id}", response_model=schemas.ColdSide)
async def get_cold_side(
    *,
    db: Session = Depends(deps.get_db),
    id: UUID,
    current_user: models.User = Depends(deps.get_current_superuser),
) -> schemas.ColdSide:
    """
    Get cold_side by ID.
    """
    cold_side = crud.cold_side.get(db=db, id=id)
    if not cold_side:
        raise HTTPException(status_code=404, detail="ColdSide not found")

    return cold_side


@router.post("/", response_model=schemas.ColdSide)
async def create_cold_side(
    *,
    db: Session = Depends(deps.get_db),
    cold_side_in: schemas.ColdSideCreate,
    current_user: models.User = Depends(deps.get_current_superuser),
) -> schemas.ColdSide:
    """
    Create new cold_side.
    """

    cold_side = crud.cold_side.create_with_owner(
        db, obj_in=cold_side_in, user_id=current_user.id
    )
    return cold_side


@router.put("/{id}", response_model=schemas.ColdSide)
async def update_cold_side(
    *,
    db: Session = Depends(deps.get_db),
    id: UUID,
    cold_side_in: schemas.ColdSideUpdate,
    current_user: models.User = Depends(deps.get_current_superuser),
) -> schemas.ColdSide:
    """
    Update a cold_side.
    """
    cold_side = crud.cold_side.get(db=db, id=id)

    if not cold_side:
        raise HTTPException(status_code=404, detail="ColdSide not found")

    cold_side = crud.cold_side.update(db=db, db_obj=cold_side, obj_in=cold_side_in)
    return cold_side


@router.delete("/{id}", response_model=schemas.ColdSide)
async def delete_cold_side(
    *,
    db: Session = Depends(deps.get_db),
    id: UUID,
    current_user: models.User = Depends(deps.get_current_superuser),
) -> schemas.ColdSide:
    """
    Delete a cold_side.
    """
    cold_side = crud.cold_side.get(db=db, id=id)
    if not cold_side:
        raise HTTPException(status_code=404, detail="ColdSide not found")

    cold_side = crud.cold_side.delete(db=db, db_obj=cold_side)
    return cold_side
