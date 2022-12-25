from typing import List, Optional
from uuid import UUID

from app import crud, models, schemas
from app.api import deps
from app.utils import IResponseBase
from fastapi import APIRouter, Depends, HTTPException, Query
from sqlalchemy.orm import Session

router = APIRouter()


@router.get("/", response_model=IResponseBase[List[schemas.Item]])
async def get_items(
    *,
    db: Session = Depends(deps.get_db),
    skip: int = Query(0, ge=0),
    limit: int = Query(100, ge=1, le=100),
    column: str = "name",
    term: Optional[str] = None,
    is_archived: bool = False,
    current_user: models.User = Depends(deps.get_current_superuser),
) -> IResponseBase[List[schemas.Item]]:
    """
    Retrieve items.
    """
    if term:
        items, total_records_count = crud.item.search(
            db=db,
            skip=skip,
            limit=limit,
            column=column,
            term=term,
            is_archived=is_archived,
        )
    else:
        items, total_records_count = crud.item.get_multi(
            db=db, skip=skip, limit=limit, column=column, is_archived=is_archived
        )

    return IResponseBase[List[schemas.Item]](
        records=items,
        total_records_count=total_records_count,
        page_size=limit if limit < total_records_count else total_records_count,
        page_number=(skip / 5) + 1,
    )


@router.get("/{id}", response_model=schemas.Item)
async def get_item(
    *,
    db: Session = Depends(deps.get_db),
    id: UUID,
    current_user: models.User = Depends(deps.get_current_superuser),
) -> schemas.Item:
    """
    Get item by ID.
    """
    item = crud.item.get(db=db, id=id)
    if not item:
        raise HTTPException(status_code=404, detail="Item not found")

    return item


@router.post("/", response_model=schemas.Item)
async def create_item(
    *,
    db: Session = Depends(deps.get_db),
    item_in: schemas.ItemCreate,
    current_user: models.User = Depends(deps.get_current_superuser),
) -> schemas.Item:
    """
    Create new item.
    """

    item = crud.item.create_with_owner(db, obj_in=item_in, user_id=current_user.id)
    return item


@router.put("/{id}", response_model=schemas.Item)
async def update_item(
    *,
    db: Session = Depends(deps.get_db),
    id: UUID,
    item_in: schemas.ItemUpdate,
    current_user: models.User = Depends(deps.get_current_superuser),
) -> schemas.Item:
    """
    Update an item.
    """
    item = crud.item.get(db=db, id=id)

    if not item:
        raise HTTPException(status_code=404, detail="Item not found")

    item = crud.item.update(db=db, db_obj=item, obj_in=item_in)
    return item


@router.delete("/{id}", response_model=schemas.Item)
async def delete_item(
    *,
    db: Session = Depends(deps.get_db),
    id: UUID,
    current_user: models.User = Depends(deps.get_current_superuser),
) -> schemas.Item:
    """
    Delete an item.
    """
    item = crud.item.get(db=db, id=id)
    if not item:
        raise HTTPException(status_code=404, detail="Item not found")

    item = crud.item.delete(db=db, db_obj=item)
    return item
