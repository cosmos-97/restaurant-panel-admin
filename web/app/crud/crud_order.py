from typing import Any, Dict, Union

from app.crud.base import CrudBase
from app.models.beverage import Beverage
from app.models.cold_side import ColdSide
from app.models.combo import Combo
from app.models.dessert import Dessert
from app.models.hot_side import HotSide
from app.models.item import Item
from app.models.option import Option
from app.models.order import Order
from app.models.order_station_item import OrderStationItem
from app.models.sauce import Sauce
from app.schemas.order import OrderCreate, OrderUpdate
from fastapi import HTTPException
from fastapi.encoders import jsonable_encoder
from sqlalchemy.orm import Session


class CrudOrder(CrudBase[Order, OrderCreate, OrderUpdate]):
    def create(self, db: Session, *, obj_in: OrderCreate) -> Order:
        obj_in_data = jsonable_encoder(obj_in)
        db_obj = self.model(**obj_in_data)

        if not db.query(Option).filter(Option.id == obj_in.option_id).count():
            raise HTTPException(status_code=404, detail="option not found")

        db.add(db_obj)
        db.flush()
        db.refresh(db_obj)

        if obj_in.items and (
            items := db.query(Item).filter(
                Item.id.in_([it.item_id for it in obj_in.items])
            )
        ).count() == len(obj_in.items):
            db_items = [
                OrderStationItem(
                    **it,
                    order_id=db_obj.id,
                    station_id=items.filter(Item.id == it["item_id"])
                    .first()
                    .stations[0]
                    .id,
                )
                for it in jsonable_encoder(obj_in.items)
            ]
        elif obj_in.items:
            raise HTTPException(status_code=404, detail="items not found")

        if obj_in.combos and (
            combos := db.query(Combo).filter(Combo.id.in_(obj_in.combos))
        ).count() == len(obj_in.combos):
            db_obj.combos.extend(combos)
        elif obj_in.combos:
            raise HTTPException(status_code=404, detail="combos not found")

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

        if obj_in.sauces and (
            sauces := db.query(Sauce).filter(Sauce.id.in_(obj_in.sauces))
        ).count() == len(obj_in.sauces):
            db_obj.sauces.extend(sauces)
        elif obj_in.sauces:
            raise HTTPException(status_code=404, detail="sauces not found")

        if obj_in.beverages and (
            beverages := db.query(Beverage).filter(Beverage.id.in_(obj_in.beverages))
        ).count() == len(obj_in.beverages):
            db_obj.beverages.extend(beverages)
        elif obj_in.beverages:
            raise HTTPException(status_code=404, detail="beverages not found")

        if obj_in.desserts and (
            desserts := db.query(Dessert).filter(Dessert.id.in_(obj_in.desserts))
        ).count() == len(obj_in.desserts):
            db_obj.desserts.extend(desserts)
        elif obj_in.desserts:
            raise HTTPException(status_code=404, detail="desserts not found")

        db.add_all([db_obj, *db_items])
        db.commit()
        db.refresh(db_obj)
        return db_obj

    def update(
        self,
        db: Session,
        *,
        db_obj: Order,
        obj_in: Union[OrderUpdate, Dict[str, Any]],
    ) -> Order:
        obj_data = jsonable_encoder(db_obj)

        if not db.query(Option).filter(Option.id == obj_in.option_id).count():
            raise HTTPException(status_code=404, detail="option not found")

        if obj_in.items and (
            items := db.query(Item).filter(Item.id.in_(obj_in.items))
        ).count() == len(obj_in.items):
            db_obj.items.clear()
            db_obj.items.extend(items)
        elif obj_in.items:
            raise HTTPException(status_code=404, detail="items not found")
        elif obj_in.items == []:
            db_obj.items.clear()

        if obj_in.combos and (
            combos := db.query(Combo).filter(Combo.id.in_(obj_in.combos))
        ).count() == len(obj_in.combos):
            db_obj.combos.clear()
            db_obj.combos.extend(combos)
        elif obj_in.combos:
            raise HTTPException(status_code=404, detail="combos not found")
        elif obj_in.combos == []:
            db_obj.combos.clear()

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

        if obj_in.sauces and (
            sauces := db.query(Sauce).filter(Sauce.id.in_(obj_in.sauces))
        ).count() == len(obj_in.sauces):
            db_obj.sauces.clear()
            db_obj.sauces.extend(sauces)
        elif obj_in.sauces:
            raise HTTPException(status_code=404, detail="sauces not found")
        elif obj_in.sauces == []:
            db_obj.sauces.clear()

        if obj_in.desserts and (
            desserts := db.query(Dessert).filter(Dessert.id.in_(obj_in.desserts))
        ).count() == len(obj_in.desserts):
            db_obj.desserts.clear()
            db_obj.desserts.extend(desserts)
        elif obj_in.desserts:
            raise HTTPException(status_code=404, detail="desserts not found")
        elif obj_in.desserts == []:
            db_obj.desserts.clear()

        if obj_in.beverages and (
            beverages := db.query(Beverage).filter(Beverage.id.in_(obj_in.beverages))
        ).count() == len(obj_in.beverages):
            db_obj.beverages.clear()
            db_obj.beverages.extend(beverages)
        elif obj_in.beverages:
            raise HTTPException(status_code=404, detail="beverages not found")
        elif obj_in.beverages == []:
            db_obj.beverages.clear()

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


order = CrudOrder(Order)
