from typing import List, Optional
from uuid import UUID

from app import crud, models, schemas
from app.api import deps
from app.utils import IResponseBase
from fastapi import APIRouter, Depends, HTTPException, Query
from sqlalchemy.orm import Session

router = APIRouter()


@router.get("/", response_model=IResponseBase[List[schemas.Special]])
async def get_specials(
    *,
    db: Session = Depends(deps.get_db),
    skip: int = Query(0, ge=0),
    limit: int = Query(100, ge=1, le=100),
    column: str = "name",
    term: Optional[str] = None,
    is_archived: bool = False,
    current_user: models.User = Depends(deps.get_current_superuser),
) -> IResponseBase[List[schemas.Special]]:
    """
    Retrieve specials.
    """
    if term:
        specials, total_records_count = crud.special.search(
            db=db,
            skip=skip,
            limit=limit,
            column=column,
            term=term,
            is_archived=is_archived,
        )
    else:
        specials, total_records_count = crud.special.get_multi(
            db=db, skip=skip, limit=limit, column=column, is_archived=is_archived
        )

    return IResponseBase[List[schemas.Special]](
        records=specials,
        total_records_count=total_records_count,
        page_size=limit if limit < total_records_count else total_records_count,
        page_number=(skip / 5) + 1,
    )


@router.get("/{id}", response_model=schemas.Special)
async def get_special(
    *,
    db: Session = Depends(deps.get_db),
    id: UUID,
    current_user: models.User = Depends(deps.get_current_superuser),
) -> schemas.Special:
    """
    Get special by ID.
    """
    special = crud.special.get(db=db, id=id)
    if not special:
        raise HTTPException(status_code=404, detail="Special not found")

    return special


@router.post("/", response_model=schemas.Special)
async def create_special(
    *,
    db: Session = Depends(deps.get_db),
    special_in: schemas.SpecialCreate,
    current_user: models.User = Depends(deps.get_current_superuser),
) -> schemas.Special:
    """
    Create new special.
    """

    special = crud.special.create_with_owner(
        db, obj_in=special_in, user_id=current_user.id
    )
    return special


@router.put("/{id}", response_model=schemas.Special)
async def update_special(
    *,
    db: Session = Depends(deps.get_db),
    id: UUID,
    special_in: schemas.SpecialUpdate,
    current_user: models.User = Depends(deps.get_current_superuser),
) -> schemas.Special:
    """
    Update an special.
    """
    special = crud.special.get(db=db, id=id)

    if not special:
        raise HTTPException(status_code=404, detail="Special not found")

    special = crud.special.update(db=db, db_obj=special, obj_in=special_in)
    return special


@router.delete("/{id}", response_model=schemas.Special)
async def delete_special(
    *,
    db: Session = Depends(deps.get_db),
    id: UUID,
    current_user: models.User = Depends(deps.get_current_superuser),
) -> schemas.Special:
    """
    Delete an special.
    """
    special = crud.special.get(db=db, id=id)
    if not special:
        raise HTTPException(status_code=404, detail="Special not found")

    special = crud.special.delete(db=db, db_obj=special)
    return special
