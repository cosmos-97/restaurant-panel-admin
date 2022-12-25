from app import crud, models, schemas
from app.api import deps
from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

router = APIRouter()


@router.get("/appearance", response_model=schemas.Appearance)
async def get_appearance(
    *,
    db: Session = Depends(deps.get_db),
    current_user: models.User = Depends(deps.get_current_superuser),
) -> schemas.Appearance:
    """
    Get one appearance.
    """
    appearance = crud.appearance.get(db=db)

    return appearance


@router.put("/appearance", response_model=schemas.Appearance)
async def update_appearance(
    *,
    db: Session = Depends(deps.get_db),
    appearance_in: schemas.AppearanceUpdate,
    current_user: models.User = Depends(deps.get_current_superuser),
) -> schemas.Appearance:
    """
    Update a appearance.
    """

    appearance = crud.appearance.create_or_update(
        db, obj_in=appearance_in, user_id=current_user.id
    )
    return appearance


@router.get("/store_info", response_model=schemas.StoreInfo)
async def get_store_info(
    *,
    db: Session = Depends(deps.get_db),
    current_user: models.User = Depends(deps.get_current_superuser),
) -> schemas.StoreInfo:
    """
    Get one store_info.
    """
    store_info = crud.store_info.get(db=db)

    return store_info


@router.put("/store_info", response_model=schemas.StoreInfo)
async def update_store_info(
    *,
    db: Session = Depends(deps.get_db),
    store_info_in: schemas.StoreInfoUpdate,
    current_user: models.User = Depends(deps.get_current_superuser),
) -> schemas.StoreInfo:
    """
    Update a store_info.
    """

    store_info = crud.store_info.create_or_update(
        db, obj_in=store_info_in, user_id=current_user.id
    )
    return store_info


@router.get("/receipt", response_model=schemas.Receipt)
async def get_receipt(
    *,
    db: Session = Depends(deps.get_db),
    current_user: models.User = Depends(deps.get_current_superuser),
) -> schemas.Receipt:
    """
    Get one receipt.
    """
    receipt = crud.receipt.get(db=db)

    return receipt


@router.put("/receipt", response_model=schemas.Receipt)
async def update_receipt(
    *,
    db: Session = Depends(deps.get_db),
    receipt_in: schemas.ReceiptUpdate,
    current_user: models.User = Depends(deps.get_current_superuser),
) -> schemas.Receipt:
    """
    Update a receipt.
    """

    receipt = crud.receipt.create_or_update(
        db, obj_in=receipt_in, user_id=current_user.id
    )
    return receipt


@router.get("/sound", response_model=schemas.Sound)
async def get_sound(
    *,
    db: Session = Depends(deps.get_db),
    current_user: models.User = Depends(deps.get_current_superuser),
) -> schemas.Sound:
    """
    Get one sound.
    """
    sound = crud.sound.get(db=db)

    return sound


@router.put("/sound", response_model=schemas.Sound)
async def update_sound(
    *,
    db: Session = Depends(deps.get_db),
    sound_in: schemas.SoundUpdate,
    current_user: models.User = Depends(deps.get_current_superuser),
) -> schemas.Sound:
    """
    Update a sound.
    """

    sound = crud.sound.create_or_update(db, obj_in=sound_in, user_id=current_user.id)
    return sound
