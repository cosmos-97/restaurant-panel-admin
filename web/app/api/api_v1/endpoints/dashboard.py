from datetime import datetime

from app import crud, models, schemas
from app.api import deps
from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

router = APIRouter()


@router.get("/orders_count", response_model=schemas.OrdersCount)
async def get_total_orders_count(
    db: Session = Depends(deps.get_db),
    current_user: models.User = Depends(deps.get_current_superuser),
) -> schemas.OrdersCount:
    """
    Retrieve orders count.
    """
    orders_count = crud.dashboard.get_total_orders_count(db=db)

    return {"orders_count": orders_count}


@router.get("/orders_count_per_datatime", response_model=schemas.OrdersCount)
async def get_orders_count_per_datatime(
    *,
    db: Session = Depends(deps.get_db),
    start_datetime: datetime,
    end_datetime: datetime,
    current_user: models.User = Depends(deps.get_current_superuser),
) -> schemas.OrdersCount:
    """
    Retrieve orders count per datetime.
    """
    orders_count = crud.dashboard.get_orders_count_per_datatime(
        db=db, start_datetime=start_datetime, end_datetime=end_datetime
    )

    return {"orders_count": orders_count}
