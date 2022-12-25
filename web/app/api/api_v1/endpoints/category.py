from typing import List
from uuid import UUID

from app import crud, models, schemas
from app.api import deps
from app.utils import IResponseBase
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

router = APIRouter()


@router.get("/", response_model=IResponseBase[List[schemas.Category]])
async def get_categories(
    db: Session = Depends(deps.get_db),
    skip: int = 0,
    limit: int = 100,
    current_user: models.User = Depends(deps.get_current_superuser),
) -> IResponseBase[List[schemas.Category]]:
    """
    Retrieve categories.
    """
    categories, total_records_count = crud.category.get_multi(
        db=db, skip=skip, limit=limit
    )

    return IResponseBase[List[schemas.Category]](
        records=categories,
        total_records_count=total_records_count,
        page_size=limit if limit < total_records_count else total_records_count,
        page_number=(skip / 5) + 1,
    )


@router.get("/{id}", response_model=schemas.Category)
async def get_category(
    *,
    db: Session = Depends(deps.get_db),
    id: UUID,
    current_user: models.User = Depends(deps.get_current_superuser),
) -> schemas.Category:
    """
    Get category by ID.
    """
    category = crud.category.get(db=db, id=id)
    if not category:
        raise HTTPException(status_code=404, detail="Category not found")

    return category


@router.post("/", response_model=schemas.Category)
async def create_category(
    *,
    db: Session = Depends(deps.get_db),
    category_in: schemas.CategoryCreate,
    current_user: models.User = Depends(deps.get_current_superuser),
) -> schemas.Category:
    """
    Create new category.
    """

    category = crud.category.create_with_owner(
        db, obj_in=category_in, user_id=current_user.id
    )
    return category


@router.put("/{id}", response_model=schemas.Category)
async def update_category(
    *,
    db: Session = Depends(deps.get_db),
    id: UUID,
    category_in: schemas.CategoryUpdate,
    current_user: models.User = Depends(deps.get_current_superuser),
) -> schemas.Category:
    """
    Update a category.
    """
    category = crud.category.get(db=db, id=id)

    if not category:
        raise HTTPException(status_code=404, detail="Category not found")

    category = crud.category.update(db=db, db_obj=category, obj_in=category_in)
    return category


@router.delete("/{id}", response_model=schemas.Category)
async def delete_category(
    *,
    db: Session = Depends(deps.get_db),
    id: UUID,
    current_user: models.User = Depends(deps.get_current_superuser),
) -> schemas.Category:
    """
    Delete a category.
    """
    category = crud.category.get(db=db, id=id)
    if not category:
        raise HTTPException(status_code=404, detail="Category not found")

    category = crud.category.delete(db=db, db_obj=category)
    return category
