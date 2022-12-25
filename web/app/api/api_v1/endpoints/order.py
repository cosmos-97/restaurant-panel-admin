from typing import List

from app import crud, models, schemas
from app.api import deps
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

router = APIRouter()


@router.get(
    "/",
    response_model=List[schemas.Order],
    response_model_exclude=[
        "stations_item",
        "stations_combo",
        "stations_special",
        "stations_hot_side",
        "stations_cold_side",
        "stations_sauce",
        "stations_beverage",
        "stations_dessert",
    ],
)
async def get_orders(
    db: Session = Depends(deps.get_db),
    skip: int = 0,
    limit: int = 100,
    current_user: models.User = Depends(deps.get_current_superuser),
) -> List[schemas.Order]:
    """
    Retrieve orders.
    """
    orders = crud.order.get_multi(db=db, skip=skip, limit=limit)

    return orders


@router.get(
    "/{id}",
    response_model=schemas.Order,
    response_model_exclude=[
        "stations_item",
        "stations_combo",
        "stations_special",
        "stations_hot_side",
        "stations_cold_side",
        "stations_sauce",
        "stations_beverage",
        "stations_dessert",
    ],
)
async def get_order(
    *,
    db: Session = Depends(deps.get_db),
    id: int,
    current_user: models.User = Depends(deps.get_current_superuser),
) -> schemas.Order:
    """
    Get order by ID.
    """
    order = crud.order.get(db=db, id=id)
    if not order:
        raise HTTPException(status_code=404, detail="Order not found")

    return order


@router.post("/", response_model=schemas.Order)
async def create_order(
    *,
    db: Session = Depends(deps.get_db),
    order_in: schemas.OrderCreate,
    current_user: models.User = Depends(deps.get_current_superuser),
) -> schemas.Order:
    """
    Create new order.
    """

    order = crud.order.create(db, obj_in=order_in)
    return order


@router.put("/{id}", response_model=schemas.Order)
async def update_order(
    *,
    db: Session = Depends(deps.get_db),
    id: int,
    order_in: schemas.OrderUpdate,
    current_user: models.User = Depends(deps.get_current_superuser),
) -> schemas.Order:
    """
    Update an order.
    """
    order = crud.order.get(db=db, id=id)

    if not order:
        raise HTTPException(status_code=404, detail="Order not found")

    order = crud.order.update(db=db, db_obj=order, obj_in=order_in)
    return order


@router.delete("/{id}", response_model=schemas.Order)
async def delete_order(
    *,
    db: Session = Depends(deps.get_db),
    id: int,
    current_user: models.User = Depends(deps.get_current_superuser),
) -> schemas.Order:
    """
    Delete an order.
    """
    order = crud.order.get(db=db, id=id)
    if not order:
        raise HTTPException(status_code=404, detail="Order not found")

    order = crud.order.delete(db=db, db_obj=order)
    return order
