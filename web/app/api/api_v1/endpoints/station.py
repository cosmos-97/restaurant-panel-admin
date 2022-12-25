from typing import List
from uuid import UUID

from app import crud, models, schemas
from app.api import deps
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

router = APIRouter()


@router.get("/", response_model=List[schemas.Station])
async def get_stations(
    db: Session = Depends(deps.get_db),
    skip: int = 0,
    limit: int = 100,
    current_user: models.User = Depends(deps.get_current_superuser),
) -> List[schemas.Station]:
    """
    Retrieve stations.
    """
    stations = crud.station.get_multi(db=db, skip=skip, limit=limit)

    return stations


@router.get("/{id}", response_model=schemas.Station)
async def get_station(
    *,
    db: Session = Depends(deps.get_db),
    id: UUID,
    current_user: models.User = Depends(deps.get_current_superuser),
) -> schemas.Station:
    """
    Get station by ID.
    """
    station = crud.station.get(db=db, id=id)
    if not station:
        raise HTTPException(status_code=404, detail="Station not found")

    return station


@router.post("/", response_model=schemas.Station)
async def create_station(
    *,
    db: Session = Depends(deps.get_db),
    station_in: schemas.StationCreate,
    current_user: models.User = Depends(deps.get_current_superuser),
) -> schemas.Station:
    """
    Create new station.
    """

    station = crud.station.create_with_owner(
        db, obj_in=station_in, user_id=current_user.id
    )
    return station


@router.put("/{id}", response_model=schemas.Station)
async def update_station(
    *,
    db: Session = Depends(deps.get_db),
    id: UUID,
    station_in: schemas.StationUpdate,
    current_user: models.User = Depends(deps.get_current_superuser),
) -> schemas.Station:
    """
    Update a station.
    """
    station = crud.station.get(db=db, id=id)

    if not station:
        raise HTTPException(status_code=404, detail="Station not found")

    station = crud.station.update(db=db, db_obj=station, obj_in=station_in)
    return station


@router.delete("/{id}", response_model=schemas.Station)
async def delete_station(
    *,
    db: Session = Depends(deps.get_db),
    id: UUID,
    current_user: models.User = Depends(deps.get_current_superuser),
) -> schemas.Station:
    """
    Delete a station.
    """
    station = crud.station.get(db=db, id=id)
    if not station:
        raise HTTPException(status_code=404, detail="Station not found")

    station = crud.station.delete(db=db, db_obj=station)
    return station
