from typing import List
from uuid import UUID

from app import crud, models, schemas
from app.api import deps
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

router = APIRouter()


@router.get("/", response_model=List[schemas.Ingredient])
async def get_ingredients(
    db: Session = Depends(deps.get_db),
    skip: int = 0,
    limit: int = 100,
    current_user: models.User = Depends(deps.get_current_superuser),
) -> List[schemas.Ingredient]:
    """
    Retrieve ingredients.
    """
    ingredients = crud.ingredient.get_multi(db=db, skip=skip, limit=limit)

    return ingredients


@router.get("/{id}", response_model=schemas.Ingredient)
async def get_ingredient(
    *,
    db: Session = Depends(deps.get_db),
    id: UUID,
    current_user: models.User = Depends(deps.get_current_superuser),
) -> schemas.Ingredient:
    """
    Get ingredient by ID.
    """
    ingredient = crud.ingredient.get(db=db, id=id)
    if not ingredient:
        raise HTTPException(status_code=404, detail="Ingredient not found")

    return ingredient


@router.post("/", response_model=schemas.Ingredient)
async def create_ingredient(
    *,
    db: Session = Depends(deps.get_db),
    ingredient_in: schemas.IngredientCreate,
    current_user: models.User = Depends(deps.get_current_superuser),
) -> schemas.Ingredient:
    """
    Create new ingredient.
    """

    ingredient = crud.ingredient.create_with_owner(
        db, obj_in=ingredient_in, user_id=current_user.id
    )
    return ingredient


@router.put("/{id}", response_model=schemas.Ingredient)
async def update_ingredient(
    *,
    db: Session = Depends(deps.get_db),
    id: UUID,
    ingredient_in: schemas.IngredientUpdate,
    current_user: models.User = Depends(deps.get_current_superuser),
) -> schemas.Ingredient:
    """
    Update a ingredient.
    """
    ingredient = crud.ingredient.get(db=db, id=id)

    if not ingredient:
        raise HTTPException(status_code=404, detail="Ingredient not found")

    ingredient = crud.ingredient.update(db=db, db_obj=ingredient, obj_in=ingredient_in)
    return ingredient


@router.delete("/{id}", response_model=schemas.Ingredient)
async def delete_ingredient(
    *,
    db: Session = Depends(deps.get_db),
    id: UUID,
    current_user: models.User = Depends(deps.get_current_superuser),
) -> schemas.Ingredient:
    """
    Delete a ingredient.
    """
    ingredient = crud.ingredient.get(db=db, id=id)
    if not ingredient:
        raise HTTPException(status_code=404, detail="Ingredient not found")

    ingredient = crud.ingredient.delete(db=db, db_obj=ingredient)
    return ingredient
