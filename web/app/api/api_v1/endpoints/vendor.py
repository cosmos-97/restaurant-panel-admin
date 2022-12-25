from typing import List
from uuid import UUID

from app import crud, models, schemas
from app.api import deps
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

router = APIRouter()


@router.get("/", response_model=List[schemas.Vendor])
async def get_vendors(
    db: Session = Depends(deps.get_db),
    skip: int = 0,
    limit: int = 100,
    current_user: models.User = Depends(deps.get_current_superuser),
) -> List[schemas.Vendor]:
    """
    Retrieve vendors.
    """
    vendors = crud.vendor.get_multi(db=db, skip=skip, limit=limit)

    return vendors


@router.get("/{id}", response_model=schemas.Vendor)
async def get_vendor(
    *,
    db: Session = Depends(deps.get_db),
    id: UUID,
    current_user: models.User = Depends(deps.get_current_superuser),
) -> schemas.Vendor:
    """
    Get vendor by ID.
    """
    vendor = crud.vendor.get(db=db, id=id)
    if not vendor:
        raise HTTPException(status_code=404, detail="Vendor not found")

    return vendor


@router.post("/", response_model=schemas.Vendor)
async def create_vendor(
    *,
    db: Session = Depends(deps.get_db),
    vendor_in: schemas.VendorCreate,
    current_user: models.User = Depends(deps.get_current_superuser),
) -> schemas.Vendor:
    """
    Create new vendor.
    """

    vendor = crud.vendor.create_with_owner(
        db, obj_in=vendor_in, user_id=current_user.id
    )
    return vendor


@router.put("/{id}", response_model=schemas.Vendor)
async def update_vendor(
    *,
    db: Session = Depends(deps.get_db),
    id: UUID,
    vendor_in: schemas.VendorUpdate,
    current_user: models.User = Depends(deps.get_current_superuser),
) -> schemas.Vendor:
    """
    Update a vendor.
    """
    vendor = crud.vendor.get(db=db, id=id)

    if not vendor:
        raise HTTPException(status_code=404, detail="Vendor not found")

    vendor = crud.vendor.update(db=db, db_obj=vendor, obj_in=vendor_in)
    return vendor


@router.delete("/{id}", response_model=schemas.Vendor)
async def delete_vendor(
    *,
    db: Session = Depends(deps.get_db),
    id: UUID,
    current_user: models.User = Depends(deps.get_current_superuser),
) -> schemas.Vendor:
    """
    Delete a vendor.
    """
    vendor = crud.vendor.get(db=db, id=id)
    if not vendor:
        raise HTTPException(status_code=404, detail="Vendor not found")

    vendor = crud.vendor.delete(db=db, db_obj=vendor)
    return vendor
