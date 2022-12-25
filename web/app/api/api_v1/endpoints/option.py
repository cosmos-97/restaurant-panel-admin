from typing import List
from uuid import UUID

from app import crud, models, schemas
from app.api import deps
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

router = APIRouter()


@router.get("/", response_model=List[schemas.Option])
async def get_options(
    db: Session = Depends(deps.get_db),
    skip: int = 0,
    limit: int = 100,
    current_user: models.User = Depends(deps.get_current_superuser),
) -> List[schemas.Option]:
    """
    Retrieve options.
    """
    options = crud.option.get_multi(db=db, skip=skip, limit=limit)

    return options


@router.get("/{id}", response_model=schemas.Option)
async def get_option(
    *,
    db: Session = Depends(deps.get_db),
    id: UUID,
    current_user: models.User = Depends(deps.get_current_superuser),
) -> schemas.Option:
    """
    Get option by ID.
    """
    option = crud.option.get(db=db, id=id)
    if not option:
        raise HTTPException(status_code=404, detail="Option not found")

    return option


@router.post("/", response_model=schemas.Option)
async def create_option(
    *,
    db: Session = Depends(deps.get_db),
    option_in: schemas.OptionCreate,
    current_user: models.User = Depends(deps.get_current_superuser),
) -> schemas.Option:
    """
    Create new option.
    """

    option = crud.option.create_with_owner(
        db, obj_in=option_in, user_id=current_user.id
    )
    return option


@router.put("/{id}", response_model=schemas.Option)
async def update_option(
    *,
    db: Session = Depends(deps.get_db),
    id: UUID,
    option_in: schemas.OptionUpdate,
    current_user: models.User = Depends(deps.get_current_superuser),
) -> schemas.Option:
    """
    Update a option.
    """
    option = crud.option.get(db=db, id=id)

    if not option:
        raise HTTPException(status_code=404, detail="Option not found")

    option = crud.option.update(db=db, db_obj=option, obj_in=option_in)
    return option


@router.delete("/{id}", response_model=schemas.Option)
async def delete_option(
    *,
    db: Session = Depends(deps.get_db),
    id: UUID,
    current_user: models.User = Depends(deps.get_current_superuser),
) -> schemas.Option:
    """
    Delete a option.
    """
    option = crud.option.get(db=db, id=id)
    if not option:
        raise HTTPException(status_code=404, detail="Option not found")

    option = crud.option.delete(db=db, db_obj=option)
    return option
