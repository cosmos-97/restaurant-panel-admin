from typing import Any, Dict, List, Union

from app.crud.base import CrudBase
from app.models.category import Category
from app.models.cold_side import ColdSide
from app.models.hot_side import HotSide
from app.models.ingredient import Ingredient
from app.models.item import Item
from app.models.option import Option
from app.models.sauce import Sauce
from app.models.station import Station
from app.schemas.item import ItemCreate, ItemUpdate
from fastapi import HTTPException
from fastapi.encoders import jsonable_encoder
from sqlalchemy import and_, asc, func
from sqlalchemy.orm import Session


class CrudItem(CrudBase[Item, ItemCreate, ItemUpdate]):
    def get_multi(
        self,
        db: Session,
        *,
        skip: int = 0,
        limit: int = 100,
        column: str = "name",
        is_archived: bool,
    ) -> List[Item]:
        try:
            column = getattr(Item, column)
        except Exception:
            raise HTTPException(status_code=404, detail="column name not found")

        return (
            db.query(Item)
            .filter(Item.is_archived == is_archived)
            .order_by(asc(column))
            .offset(skip)
            .limit(limit)
            .all()
        ), db.query(Item).filter(Item.is_archived == is_archived).count()

    def search(
        self,
        db: Session,
        *,
        skip: int = 0,
        limit: int = 100,
        column: str = "name",
        term: str,
        is_archived: bool,
    ) -> List[Item]:
        return (
            db.query(Item)
            .filter(
                and_(
                    Item.__ts_vector__.op("@@")(func.plainto_tsquery(term)),
                    Item.is_archived == is_archived,
                )
            )
            .order_by(asc(column))
            .offset(skip)
            .limit(limit)
            .all()
        ), db.query(Item).filter(
            and_(
                Item.__ts_vector__.op("@@")(func.plainto_tsquery(term)),
                Item.is_archived == is_archived,
            )
        ).count()

    def create_with_owner(
        self, db: Session, *, obj_in: ItemCreate, user_id: int
    ) -> Item:
        obj_in_data = jsonable_encoder(obj_in)
        db_obj = self.model(**obj_in_data, user_id=user_id)

        if not db.query(Category).filter(Category.id == obj_in.category_id).count():
            raise HTTPException(status_code=404, detail="category not found")

        if not db.query(Station).filter(Station.id == obj_in.station_id).count():
            raise HTTPException(status_code=404, detail="station not found")

        if obj_in.sauces and (
            sauces := db.query(Sauce).filter(Sauce.id.in_(obj_in.sauces))
        ).count() == len(obj_in.sauces):
            db_obj.sauces.extend(sauces)
        elif obj_in.sauces:
            raise HTTPException(status_code=404, detail="sauces not found")

        if obj_in.hot_sides and (
            hot_sides := db.query(HotSide).filter(HotSide.id.in_(obj_in.hot_sides))
        ).count() == len(obj_in.hot_sides):
            db_obj.hot_sides.extend(hot_sides)
        elif obj_in.hot_sides:
            raise HTTPException(status_code=404, detail="hot_sides not found")

        if obj_in.cold_sides and (
            cold_sides := db.query(ColdSide).filter(ColdSide.id.in_(obj_in.cold_sides))
        ).count() == len(obj_in.cold_sides):
            db_obj.cold_sides.extend(cold_sides)
        elif obj_in.cold_sides:
            raise HTTPException(status_code=404, detail="cold_sides not found")

        if obj_in.ingredients and (
            ingredients := db.query(Ingredient).filter(
                Ingredient.id.in_(obj_in.ingredients)
            )
        ).count() == len(obj_in.ingredients):
            db_obj.ingredients.extend(ingredients)
        elif obj_in.ingredients:
            raise HTTPException(status_code=404, detail="ingredients not found")

        if obj_in.options and (
            options := db.query(Option).filter(Option.id.in_(obj_in.options))
        ).count() == len(obj_in.options):
            db_obj.options.extend(options)
        elif obj_in.options:
            raise HTTPException(status_code=404, detail="options not found")

        db.add(db_obj)
        db.commit()
        db.refresh(db_obj)
        return db_obj

    def update(
        self,
        db: Session,
        *,
        db_obj: Item,
        obj_in: Union[ItemUpdate, Dict[str, Any]],
    ) -> Item:
        obj_data = jsonable_encoder(db_obj)

        if (
            obj_in.category_id
            and not db.query(Category).filter(Category.id == obj_in.category_id).count()
        ):
            raise HTTPException(status_code=404, detail="category not found")

        if (
            obj_in.station_id
            and not db.query(Station).filter(Station.id == obj_in.station_id).count()
        ):
            raise HTTPException(status_code=404, detail="station not found")

        if obj_in.sauces and (
            sauces := db.query(Sauce).filter(Sauce.id.in_(obj_in.sauces))
        ).count() == len(obj_in.sauces):
            db_obj.sauces.clear()
            db_obj.sauces.extend(sauces)
        elif obj_in.sauces:
            raise HTTPException(status_code=404, detail="sauces not found")
        elif obj_in.sauces == []:
            db_obj.sauces.clear()

        if obj_in.hot_sides and (
            hot_sides := db.query(HotSide).filter(HotSide.id.in_(obj_in.hot_sides))
        ).count() == len(obj_in.hot_sides):
            db_obj.hot_sides.clear()
            db_obj.hot_sides.extend(hot_sides)
        elif obj_in.hot_sides:
            raise HTTPException(status_code=404, detail="hot_sides not found")
        elif obj_in.hot_sides == []:
            db_obj.hot_sides.clear()

        if obj_in.cold_sides and (
            cold_sides := db.query(ColdSide).filter(ColdSide.id.in_(obj_in.cold_sides))
        ).count() == len(obj_in.cold_sides):
            db_obj.cold_sides.clear()
            db_obj.cold_sides.extend(cold_sides)
        elif obj_in.cold_sides:
            raise HTTPException(status_code=404, detail="cold_sides not found")
        elif obj_in.cold_sides == []:
            db_obj.cold_sides.clear()

        if obj_in.ingredients and (
            ingredients := db.query(Ingredient).filter(
                Ingredient.id.in_(obj_in.ingredients)
            )
        ).count() == len(obj_in.ingredients):
            db_obj.ingredients.clear()
            db_obj.ingredients.extend(ingredients)
        elif obj_in.ingredients:
            raise HTTPException(status_code=404, detail="ingredients not found")
        elif obj_in.ingredients == []:
            db_obj.ingredients.clear()

        if obj_in.options and (
            options := db.query(Option).filter(Option.id.in_(obj_in.options))
        ).count() == len(obj_in.options):
            db_obj.options.clear()
            db_obj.options.extend(options)
        elif obj_in.options:
            raise HTTPException(status_code=404, detail="options not found")
        elif obj_in.options == []:
            db_obj.options.clear()

        if isinstance(obj_in, dict):
            update_data = obj_in
        else:
            update_data = obj_in.dict(exclude_unset=True)
        for field in obj_data:
            if field in update_data:
                setattr(db_obj, field, update_data[field])

        db.add(db_obj)
        db.commit()
        db.refresh(db_obj)
        return db_obj


item = CrudItem(Item)
