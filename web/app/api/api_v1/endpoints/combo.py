from typing import List, Optional
from uuid import UUID

from app import crud, models, schemas
from app.api import deps
from app.utils import IResponseBase
from fastapi import APIRouter, Depends, HTTPException, Query
from sqlalchemy.orm import Session

router = APIRouter()


@router.get("/", response_model=IResponseBase[List[schemas.Combo]])
async def get_combos(
    *,
    db: Session = Depends(deps.get_db),
    skip: int = Query(0, ge=0),
    limit: int = Query(100, ge=1, le=100),
    column: str = "name",
    term: Optional[str] = None,
    is_archived: bool = False,
    current_user: models.User = Depends(deps.get_current_superuser),
) -> IResponseBase[List[schemas.Combo]]:
    """
    Retrieve combos.
    """
    if term:
        combos, total_records_count = crud.combo.search(
            db=db,
            skip=skip,
            limit=limit,
            column=column,
            term=term,
            is_archived=is_archived,
        )
    else:
        combos, total_records_count = crud.combo.get_multi(
            db=db, skip=skip, limit=limit, column=column, is_archived=is_archived
        )

    return IResponseBase[List[schemas.Combo]](
        records=combos,
        total_records_count=total_records_count,
        page_size=limit if limit < total_records_count else total_records_count,
        page_number=(skip / 5) + 1,
    )


@router.get("/{id}", response_model=schemas.Combo)
async def get_combo(
    *,
    db: Session = Depends(deps.get_db),
    id: UUID,
    current_user: models.User = Depends(deps.get_current_superuser),
) -> schemas.Combo:
    """
    Get combo by ID.
    """
    combo = crud.combo.get(db=db, id=id)
    if not combo:
        raise HTTPException(status_code=404, detail="Combo not found")

    return combo


@router.post("/", response_model=schemas.Combo)
async def create_combo(
    *,
    db: Session = Depends(deps.get_db),
    combo_in: schemas.ComboCreate,
    current_user: models.User = Depends(deps.get_current_superuser),
) -> schemas.Combo:
    """
    Create new combo.
    """

    combo = crud.combo.create_with_owner(db, obj_in=combo_in, user_id=current_user.id)
    return combo


@router.put("/{id}", response_model=schemas.Combo)
async def update_combo(
    *,
    db: Session = Depends(deps.get_db),
    id: UUID,
    combo_in: schemas.ComboUpdate,
    current_user: models.User = Depends(deps.get_current_superuser),
) -> schemas.Combo:
    """
    Update an combo.
    """
    combo = crud.combo.get(db=db, id=id)

    if not combo:
        raise HTTPException(status_code=404, detail="Combo not found")

    combo = crud.combo.update(db=db, db_obj=combo, obj_in=combo_in)
    return combo


@router.delete("/{id}", response_model=schemas.Combo)
async def delete_combo(
    *,
    db: Session = Depends(deps.get_db),
    id: UUID,
    current_user: models.User = Depends(deps.get_current_superuser),
) -> schemas.Combo:
    """
    Delete an combo.
    """
    combo = crud.combo.get(db=db, id=id)
    if not combo:
        raise HTTPException(status_code=404, detail="Combo not found")

    combo = crud.combo.delete(db=db, db_obj=combo)
    return combo
