from typing import List
from uuid import UUID

from app import crud, models, schemas
from app.api import deps
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

router = APIRouter()


@router.get("/", response_model=List[schemas.Request])
async def get_requests(
    db: Session = Depends(deps.get_db),
    skip: int = 0,
    limit: int = 100,
    current_user: models.User = Depends(deps.get_current_superuser),
) -> List[schemas.Request]:
    """
    Retrieve requests.
    """
    requests = crud.request.get_multi(db=db, skip=skip, limit=limit)

    return requests


@router.get("/{id}", response_model=schemas.Request)
async def get_request(
    *,
    db: Session = Depends(deps.get_db),
    id: UUID,
    current_user: models.User = Depends(deps.get_current_superuser),
) -> schemas.Request:
    """
    Get request by ID.
    """
    request = crud.request.get(db=db, id=id)
    if not request:
        raise HTTPException(status_code=404, detail="Request not found")

    return request


@router.post("/", response_model=schemas.Request)
async def create_request(
    *,
    db: Session = Depends(deps.get_db),
    request_in: schemas.RequestCreate,
    current_user: models.User = Depends(deps.get_current_superuser),
) -> schemas.Request:
    """
    Create new request.
    """

    request = crud.request.create_with_owner(
        db, obj_in=request_in, user_id=current_user.id
    )
    return request


@router.put("/{id}", response_model=schemas.Request)
async def update_request(
    *,
    db: Session = Depends(deps.get_db),
    id: UUID,
    request_in: schemas.RequestUpdate,
    current_user: models.User = Depends(deps.get_current_superuser),
) -> schemas.Request:
    """
    Update a request.
    """
    request = crud.request.get(db=db, id=id)

    if not request:
        raise HTTPException(status_code=404, detail="Request not found")

    request = crud.request.update(db=db, db_obj=request, obj_in=request_in)
    return request


@router.delete("/{id}", response_model=schemas.Request)
async def delete_request(
    *,
    db: Session = Depends(deps.get_db),
    id: UUID,
    current_user: models.User = Depends(deps.get_current_superuser),
) -> schemas.Request:
    """
    Delete a request.
    """
    request = crud.request.get(db=db, id=id)
    if not request:
        raise HTTPException(status_code=404, detail="Request not found")

    request = crud.request.delete(db=db, db_obj=request)
    return request
