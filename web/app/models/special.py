from app.db.base_class import Base
from app.utils import TSVector
from sqlalchemy import (
    Boolean,
    Column,
    Computed,
    Date,
    Float,
    ForeignKey,
    Index,
    Integer,
    String,
    Text,
    text,
)
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import relationship

from .special_beverage import special_beverage
from .special_cold_side import special_cold_side
from .special_combo import special_combo
from .special_dessert import special_dessert
from .special_hot_side import special_hot_side
from .special_ingredient import special_ingredient
from .special_item import special_item
from .special_option import special_option
from .special_sauce import special_sauce


class Special(Base):
    id = Column(
        UUID(as_uuid=True),
        primary_key=True,
        server_default=text("uuid_generate_v4()"),
        unique=True,
        index=True,
    )
    user_id = Column(UUID(as_uuid=True), ForeignKey("user.id"), index=True)
    station_id = Column(UUID(as_uuid=True), ForeignKey("station.id"), index=True)
    name = Column(String, index=True, nullable=False)
    description = Column(Text, nullable=False)
    start_date = Column(Date, nullable=False)
    end_date = Column(Date, nullable=False)
    logo_url = Column(String, nullable=False)
    category_id = Column(UUID(as_uuid=True), ForeignKey("category.id"), nullable=False)
    type = Column(String, nullable=False)
    size = Column(String, nullable=False)
    quantity_sides = Column(Integer, nullable=True)
    quantity_sauces = Column(Integer, nullable=True)
    price = Column(Float, nullable=False)
    discount_beverage = Column(Boolean, nullable=False)
    price_beverage = Column(Float, nullable=False)
    discount_dessert = Column(Boolean, nullable=False)
    price_dessert = Column(Float, nullable=False)
    special_instructions = Column(Boolean, nullable=False)
    status = Column(Boolean, nullable=False, default=True)
    is_archived = Column(Boolean, nullable=False, default=False)
    notify_after_orders = Column(Integer, nullable=False)

    __ts_vector__ = Column(
        TSVector(),
        Computed(
            "to_tsvector('english', name || ' ' || description)",
            persisted=True,
        ),
    )

    __table_args__ = (
        Index("ix_special___ts_vector__", __ts_vector__, postgresql_using="gin"),
    )

    category = relationship("Category", back_populates="specials", lazy=False)
    items = relationship("Item", secondary=special_item)
    combos = relationship("Combo", secondary=special_combo)
    sauces = relationship("Sauce", secondary=special_sauce)
    hot_sides = relationship("HotSide", secondary=special_hot_side)
    cold_sides = relationship("ColdSide", secondary=special_cold_side)
    ingredients = relationship("Ingredient", secondary=special_ingredient)
    options = relationship("Option", secondary=special_option)
    station = relationship("Station")
    beverages = relationship("Beverage", secondary=special_beverage)
    desserts = relationship("Dessert", secondary=special_dessert)

    def __init__(self, **kwargs):
        self.user_id = kwargs.get("user_id")
        self.station_id = kwargs.get("station_id")
        self.name = kwargs.get("name")
        self.description = kwargs.get("description")
        self.start_date = kwargs.get("start_date")
        self.end_date = kwargs.get("end_date")
        self.logo_url = kwargs.get("logo_url")
        self.category_id = kwargs.get("category_id")
        self.type = kwargs.get("type")
        self.size = kwargs.get("size")
        self.quantity_sides = kwargs.get("quantity_sides")
        self.quantity_sauces = kwargs.get("quantity_sauces")
        self.price = kwargs.get("price")
        self.discount_beverage = kwargs.get("discount_beverage")
        self.price_beverage = kwargs.get("price_beverage")
        self.discount_dessert = kwargs.get("discount_dessert")
        self.price_dessert = kwargs.get("price_dessert")
        self.special_instructions = kwargs.get("special_instructions")
        self.status = kwargs.get("status")
        self.notify_after_orders = kwargs.get("notify_after_orders")
