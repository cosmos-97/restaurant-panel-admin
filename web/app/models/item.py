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

from .item_cold_side import item_cold_side
from .item_hot_side import item_hot_side
from .item_ingredient import item_ingredient
from .item_option import item_option
from .item_sauce import item_sauce


class Item(Base):
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
    special_instructions = Column(Boolean, nullable=False)
    price = Column(Float, nullable=False)
    size = Column(String, nullable=True)
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
        Index("ix_item___ts_vector__", __ts_vector__, postgresql_using="gin"),
    )

    category = relationship("Category", back_populates="items", lazy=False)
    sauces = relationship("Sauce", secondary=item_sauce, back_populates="items")
    hot_sides = relationship("HotSide", secondary=item_hot_side, back_populates="items")
    cold_sides = relationship(
        "ColdSide", secondary=item_cold_side, back_populates="items"
    )
    ingredients = relationship(
        "Ingredient", secondary=item_ingredient, back_populates="items"
    )
    options = relationship("Option", secondary=item_option, back_populates="items")
    station = relationship("Station")

    def __init__(self, **kwargs):
        self.user_id = kwargs.get("user_id")
        self.station_id = kwargs.get("station_id")
        self.name = kwargs.get("name")
        self.description = kwargs.get("description")
        self.logo_url = kwargs.get("logo_url")
        self.category_id = kwargs.get("category_id")
        self.special_instructions = kwargs.get("special_instructions")
        self.price = kwargs.get("price")
        self.size = kwargs.get("size")
        self.status = kwargs.get("status")
        self.notify_after_orders = kwargs.get("notify_after_orders")
