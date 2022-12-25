from typing import List
from uuid import UUID

from app import crud, models, schemas
from app.api import deps
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

router = APIRouter()


@router.get("/", response_model=List[schemas.Alert])
async def get_alerts(
    db: Session = Depends(deps.get_db),
    skip: int = 0,
    limit: int = 100,
    current_user: models.User = Depends(deps.get_current_superuser),
) -> List[schemas.Alert]:
    """
    Retrieve alerts.
    """
    alerts = crud.alert.get_multi(db=db, skip=skip, limit=limit)

    return alerts


@router.get("/{id}", response_model=schemas.Alert)
async def get_alert(
    *,
    db: Session = Depends(deps.get_db),
    id: UUID,
    current_user: models.User = Depends(deps.get_current_superuser),
) -> schemas.Alert:
    """
    Get alert by ID.
    """
    alert = crud.alert.get(db=db, id=id)
    if not alert:
        raise HTTPException(status_code=404, detail="Alert not found")

    return alert


@router.post("/", response_model=schemas.Alert)
async def create_alert(
    *,
    db: Session = Depends(deps.get_db),
    alert_in: schemas.AlertCreate,
    current_user: models.User = Depends(deps.get_current_superuser),
) -> schemas.Alert:
    """
    Create new alert.
    """

    alert = crud.alert.create_with_owner(db, obj_in=alert_in, user_id=current_user.id)
    return alert


@router.put("/{id}", response_model=schemas.Alert)
async def update_alert(
    *,
    db: Session = Depends(deps.get_db),
    id: UUID,
    alert_in: schemas.AlertUpdate,
    current_user: models.User = Depends(deps.get_current_superuser),
) -> schemas.Alert:
    """
    Update an alert.
    """
    alert = crud.alert.get(db=db, id=id)

    if not alert:
        raise HTTPException(status_code=404, detail="Alert not found")

    alert = crud.alert.update(db=db, db_obj=alert, obj_in=alert_in)
    return alert


@router.delete("/{id}", response_model=schemas.Alert)
async def delete_alert(
    *,
    db: Session = Depends(deps.get_db),
    id: UUID,
    current_user: models.User = Depends(deps.get_current_superuser),
) -> schemas.Alert:
    """
    Delete an alert.
    """
    alert = crud.alert.get(db=db, id=id)
    if not alert:
        raise HTTPException(status_code=404, detail="Alert not found")

    alert = crud.alert.delete(db=db, db_obj=alert)
    return alert
