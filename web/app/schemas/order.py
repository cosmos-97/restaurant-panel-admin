from collections import defaultdict
from copy import deepcopy
from datetime import datetime
from typing import Any, List, Optional
from uuid import UUID

from app.utils import OrderType
from pydantic import BaseModel, root_validator


class OrderBase(BaseModel):
    from .order_station_cold_side import OrderStationColdSideCreate
    from .order_station_combo import OrderStationComboCreate
    from .order_station_dessert import OrderStationDessertCreate
    from .order_station_hot_side import OrderStationHotSideCreate
    from .order_station_item import OrderStationItemCreate
    from .order_station_sauce import OrderStationSauceCreate
    from .order_station_special import OrderStationSpecialCreate

    order_type: Optional[OrderType] = None
    guest_name: Optional[str] = None
    option_id: Optional[UUID] = None
    special_instructions: Optional[str] = None
    card_number: Optional[str] = None
    card_type: Optional[str] = None
    reference_number: Optional[str] = None
    authorization: Optional[str] = None
    entry_mode: Optional[str] = None
    application_name: Optional[str] = None
    application_label: Optional[str] = None
    aid: Optional[str] = None
    tc_pimverified: Optional[str] = None
    pin_verified: Optional[bool] = None
    status: Optional[str] = None
    items: Optional[List[OrderStationItemCreate]] = None
    combos: Optional[List[OrderStationComboCreate]] = None
    cold_sides: Optional[List[OrderStationColdSideCreate]] = None
    desserts: Optional[List[OrderStationDessertCreate]] = None
    hot_sides: Optional[List[OrderStationHotSideCreate]] = None
    sauces: Optional[List[OrderStationSauceCreate]] = None
    specials: Optional[List[OrderStationSpecialCreate]] = None
    hot_sides: Optional[List[UUID]] = None
    cold_sides: Optional[List[UUID]] = None
    sauces: Optional[List[UUID]] = None
    beverages: Optional[List[UUID]] = None
    desserts: Optional[List[UUID]] = None

    class Config:
        orm_mode = True


class OrderCreate(OrderBase):
    order_type: OrderType
    guest_name: str
    card_number: str
    card_type: str
    reference_number: str
    authorization: str
    entry_mode: str
    application_name: str
    application_label: str
    aid: str
    tc_pimverified: str
    pin_verified: bool


class OrderUpdate(OrderBase):
    pass


class StationItem(BaseModel):
    from app.schemas.order_station_item import OrderStationItem

    id: Optional[UUID]
    station_name: Optional[str] = None
    items: Optional[List[OrderStationItem]]

    class Config:
        orm_mode = True


class StationCombo(BaseModel):
    from app.schemas.order_station_combo import OrderStationCombo

    id: Optional[UUID]
    station_name: Optional[str] = None
    combos: Optional[List[OrderStationCombo]]

    class Config:
        orm_mode = True


class StationHotSide(BaseModel):
    from app.schemas.order_station_hot_side import OrderStationHotSide

    id: Optional[UUID]
    station_name: Optional[str] = None
    hot_sides: Optional[List[OrderStationHotSide]]

    class Config:
        orm_mode = True


class StationColdSide(BaseModel):
    from app.schemas.order_station_cold_side import OrderStationColdSide

    id: Optional[UUID]
    station_name: Optional[str] = None
    cold_sides: Optional[List[OrderStationColdSide]]

    class Config:
        orm_mode = True


class StationSauce(BaseModel):
    from app.schemas.order_station_sauce import OrderStationSauce

    id: Optional[UUID]
    station_name: Optional[str] = None
    sauces: Optional[List[OrderStationSauce]]

    class Config:
        orm_mode = True


class StationBeverage(BaseModel):
    from app.schemas.order_station_beverage import OrderStationBeverage

    id: Optional[UUID]
    station_name: Optional[str] = None
    beverages: Optional[List[OrderStationBeverage]]

    class Config:
        orm_mode = True


class StationDessert(BaseModel):
    from app.schemas.order_station_dessert import OrderStationDessert

    id: Optional[UUID]
    station_name: Optional[str] = None
    desserts: Optional[List[OrderStationDessert]]

    class Config:
        orm_mode = True


class Order(OrderBase):
    from app.schemas.option import OptionBase

    id: Optional[int]
    option: Optional[OptionBase]
    stations: Optional[List[Any]]
    stations_item: Optional[List[StationItem]]
    stations_combo: Optional[List[StationCombo]]
    stations_hot_side: Optional[List[StationHotSide]]
    stations_cold_side: Optional[List[StationColdSide]]
    stations_sauce: Optional[List[StationSauce]]
    stations_beverage: Optional[List[StationBeverage]]
    stations_dessert: Optional[List[StationDessert]]
    created_at: Optional[datetime]

    @root_validator(skip_on_failure=True)
    def compute_stations(cls, values):
        temp = defaultdict(list)
        stations_items = deepcopy(values["stations_item"])
        stations_combos = deepcopy(values["stations_combo"])
        stations_hot_sides = deepcopy(values["stations_hot_side"])
        stations_cold_sides = deepcopy(values["stations_cold_side"])
        stations_sauces = deepcopy(values["stations_sauce"])
        stations_beverages = deepcopy(values["stations_beverage"])
        stations_desserts = deepcopy(values["stations_dessert"])

        for elem in stations_items:
            temp[(elem.id, elem.station_name)].extend(elem.items)

        for elem in stations_combos:
            temp[(elem.id, elem.station_name)].extend(elem.combos)

        for elem in stations_hot_sides:
            temp[(elem.id, elem.station_name)].extend(elem.hot_sides)

        for elem in stations_cold_sides:
            temp[(elem.id, elem.station_name)].extend(elem.cold_sides)

        for elem in stations_sauces:
            temp[(elem.id, elem.station_name)].extend(elem.sauces)

        for elem in stations_beverages:
            temp[(elem.id, elem.station_name)].extend(elem.beverages)

        for elem in stations_desserts:
            temp[(elem.id, elem.station_name)].extend(elem.desserts)

        values["stations"] = [
            {"items": y, "id": x[0], "station_name": x[1]} for x, y in temp.items()
        ]

        return values

    class Config:
        orm_mode = True
