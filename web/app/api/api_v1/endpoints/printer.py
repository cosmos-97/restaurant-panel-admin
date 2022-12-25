from typing import List
from uuid import UUID

from app import crud, models, schemas
from app.api import deps
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

router = APIRouter()


@router.get("/", response_model=List[schemas.Printer])
async def get_printers(
    db: Session = Depends(deps.get_db),
    skip: int = 0,
    limit: int = 100,
    current_user: models.User = Depends(deps.get_current_superuser),
) -> List[schemas.Printer]:
    """
    Retrieve printers.
    """
    printers = crud.printer.get_multi(db=db, skip=skip, limit=limit)

    return printers


@router.get("/{id}", response_model=schemas.Printer)
async def get_printer(
    *,
    db: Session = Depends(deps.get_db),
    id: UUID,
    current_user: models.User = Depends(deps.get_current_superuser),
) -> schemas.Printer:
    """
    Get printer by ID.
    """
    printer = crud.printer.get(db=db, id=id)
    if not printer:
        raise HTTPException(status_code=404, detail="Printer not found")

    return printer


@router.post("/", response_model=schemas.Printer)
async def create_printer(
    *,
    db: Session = Depends(deps.get_db),
    printer_in: schemas.PrinterCreate,
    current_user: models.User = Depends(deps.get_current_superuser),
) -> schemas.Printer:
    """
    Create new printer.
    """

    printer = crud.printer.create_with_owner(
        db, obj_in=printer_in, user_id=current_user.id
    )
    return printer


@router.put("/{id}", response_model=schemas.Printer)
async def update_printer(
    *,
    db: Session = Depends(deps.get_db),
    id: UUID,
    printer_in: schemas.PrinterUpdate,
    current_user: models.User = Depends(deps.get_current_superuser),
) -> schemas.Printer:
    """
    Update a printer.
    """
    printer = crud.printer.get(db=db, id=id)

    if not printer:
        raise HTTPException(status_code=404, detail="Printer not found")

    printer = crud.printer.update(db=db, db_obj=printer, obj_in=printer_in)
    return printer


@router.delete("/{id}", response_model=schemas.Printer)
async def delete_printer(
    *,
    db: Session = Depends(deps.get_db),
    id: UUID,
    current_user: models.User = Depends(deps.get_current_superuser),
) -> schemas.Printer:
    """
    Delete a printer.
    """
    printer = crud.printer.get(db=db, id=id)
    if not printer:
        raise HTTPException(status_code=404, detail="Printer not found")

    printer = crud.printer.delete(db=db, db_obj=printer)
    return printer
