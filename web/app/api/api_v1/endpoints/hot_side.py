from typing import List
from uuid import UUID

from app import crud, models, schemas
from app.api import deps
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

router = APIRouter()


@router.get("/", response_model=List[schemas.HotSide])
async def get_hot_sides(
    db: Session = Depends(deps.get_db),
    skip: int = 0,
    limit: int = 100,
    current_user: models.User = Depends(deps.get_current_superuser),
) -> List[schemas.HotSide]:
    """
    Retrieve hot_sides.
    """
    hot_sides = crud.hot_side.get_multi(db=db, skip=skip, limit=limit)

    return hot_sides


@router.get("/{id}", response_model=schemas.HotSide)
async def get_hot_side(
    *,
    db: Session = Depends(deps.get_db),
    id: UUID,
    current_user: models.User = Depends(deps.get_current_superuser),
) -> schemas.HotSide:
    """
    Get hot_side by ID.
    """
    hot_side = crud.hot_side.get(db=db, id=id)
    if not hot_side:
        raise HTTPException(status_code=404, detail="HotSide not found")

    return hot_side


@router.post("/", response_model=schemas.HotSide)
async def create_hot_side(
    *,
    db: Session = Depends(deps.get_db),
    hot_side_in: schemas.HotSideCreate,
    current_user: models.User = Depends(deps.get_current_superuser),
) -> schemas.HotSide:
    """
    Create new hot_side.
    """

    hot_side = crud.hot_side.create_with_owner(
        db, obj_in=hot_side_in, user_id=current_user.id
    )
    return hot_side


@router.put("/{id}", response_model=schemas.HotSide)
async def update_hot_side(
    *,
    db: Session = Depends(deps.get_db),
    id: UUID,
    hot_side_in: schemas.HotSideUpdate,
    current_user: models.User = Depends(deps.get_current_superuser),
) -> schemas.HotSide:
    """
    Update a hot_side.
    """
    hot_side = crud.hot_side.get(db=db, id=id)

    if not hot_side:
        raise HTTPException(status_code=404, detail="HotSide not found")

    hot_side = crud.hot_side.update(db=db, db_obj=hot_side, obj_in=hot_side_in)
    return hot_side


@router.delete("/{id}", response_model=schemas.HotSide)
async def delete_hot_side(
    *,
    db: Session = Depends(deps.get_db),
    id: UUID,
    current_user: models.User = Depends(deps.get_current_superuser),
) -> schemas.HotSide:
    """
    Delete a hot_side.
    """
    hot_side = crud.hot_side.get(db=db, id=id)
    if not hot_side:
        raise HTTPException(status_code=404, detail="HotSide not found")

    hot_side = crud.hot_side.delete(db=db, db_obj=hot_side)
    return hot_side
