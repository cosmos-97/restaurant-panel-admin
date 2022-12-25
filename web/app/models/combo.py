from app.db.base_class import Base
from app.utils import TSVector
from sqlalchemy import (
    Boolean,
    Column,
    Computed,
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

from .combo_beverage import combo_beverage
from .combo_cold_side import combo_cold_side
from .combo_dessert import combo_dessert
from .combo_hot_side import combo_hot_side
from .combo_ingredient import combo_ingredient
from .combo_item import combo_item
from .combo_option import combo_option
from .combo_sauce import combo_sauce


class Combo(Base):
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
    logo_url = Column(String, nullable=False)
    category_id = Column(UUID(as_uuid=True), ForeignKey("category.id"), nullable=False)
    type = Column(String, nullable=False)
    price = Column(Float, nullable=False)
    size = Column(String, nullable=True)
    quantity_sides = Column(Integer, nullable=True)
    quantity_sauces = Column(Integer, nullable=True)
    discount_beverage = Column(Boolean, nullable=False)
    price_beverage = Column(Float, nullable=True)
    discount_dessert = Column(Boolean, nullable=False)
    price_dessert = Column(Float, nullable=True)
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
        Index("ix_combo___ts_vector__", __ts_vector__, postgresql_using="gin"),
    )

    category = relationship("Category", back_populates="combos", lazy=False)
    items = relationship("Item", secondary=combo_item)
    sauces = relationship("Sauce", secondary=combo_sauce, back_populates="combos")
    hot_sides = relationship(
        "HotSide", secondary=combo_hot_side, back_populates="combos"
    )
    cold_sides = relationship(
        "ColdSide", secondary=combo_cold_side, back_populates="combos"
    )
    ingredients = relationship(
        "Ingredient", secondary=combo_ingredient, back_populates="combos"
    )
    options = relationship("Option", secondary=combo_option, back_populates="combos")
    station = relationship("Station")
    beverages = relationship(
        "Beverage", secondary=combo_beverage, back_populates="combos"
    )
    desserts = relationship("Dessert", secondary=combo_dessert, back_populates="combos")

    def __init__(self, **kwargs):
        self.user_id = kwargs.get("user_id")
        self.station_id = kwargs.get("station_id")
        self.name = kwargs.get("name")
        self.description = kwargs.get("description")
        self.logo_url = kwargs.get("logo_url")
        self.category_id = kwargs.get("category_id")
        self.type = kwargs.get("type")
        self.price = kwargs.get("price")
        self.size = kwargs.get("size")
        self.quantity_sides = kwargs.get("quantity_sides")
        self.quantity_sauces = kwargs.get("quantity_sauces")
        self.discount_beverage = kwargs.get("discount_beverage")
        self.price_beverage = kwargs.get("price_beverage")
        self.discount_dessert = kwargs.get("discount_dessert")
        self.price_dessert = kwargs.get("price_dessert")
        self.special_instructions = kwargs.get("special_instructions")
        self.status = kwargs.get("status")
        self.notify_after_orders = kwargs.get("notify_after_orders")
