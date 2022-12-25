from app.db.base_class import Base
from app.utils import OrderType
from sqlalchemy import (
    BigInteger,
    Column,
    Enum,
    ForeignKey,
    Numeric,
    String,
    DateTime,
    func,
    Boolean,
)
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import relationship


class Order(Base):
    id = Column(BigInteger, primary_key=True, index=True)
    order_type = Column(Enum(OrderType), nullable=False)
    guest_name = Column(String, index=True, nullable=False)
    option_id = Column(UUID(as_uuid=True), ForeignKey("option.id"), nullable=True)
    special_instructions = Column(String, nullable=True)
    card_number = Column(Numeric, nullable=False)
    card_type = Column(String, nullable=False)
    reference_number = Column(String, nullable=False)
    authorization = Column(String, nullable=False)
    entry_mode = Column(String, nullable=False)
    application_name = Column(String, nullable=False)
    application_label = Column(String, nullable=False)
    aid = Column(String, nullable=False)
    tc_pimverified = Column(String, nullable=False)
    pin_verified = Column(Boolean, nullable=False)
    status = Column(String, nullable=True)
    created_at = Column(DateTime(timezone=True), server_default=func.now())

    option = relationship("Option")

    stations_item = relationship("Station", secondary="order_station_item")
    stations_combo = relationship("Station", secondary="order_station_combo")
    stations_special = relationship("Station", secondary="order_station_special")
    stations_hot_side = relationship("Station", secondary="order_station_hot_side")
    stations_cold_side = relationship("Station", secondary="order_station_cold_side")
    stations_sauce = relationship("Station", secondary="order_station_sauce")
    stations_beverage = relationship("Station", secondary="order_station_beverage")
    stations_dessert = relationship("Station", secondary="order_station_dessert")

    def __init__(self, **kwargs):
        self.order_type = kwargs.get("order_type")
        self.guest_name = kwargs.get("guest_name")
        self.option_id = kwargs.get("option_id")
        self.special_instructions = kwargs.get("special_instructions")
        self.card_number = kwargs.get("card_number")
        self.card_type = kwargs.get("card_type")
        self.reference_number = kwargs.get("reference_number")
        self.authorization = kwargs.get("authorization")
        self.entry_mode = kwargs.get("entry_mode")
        self.application_name = kwargs.get("application_name")
        self.application_label = kwargs.get("application_label")
        self.aid = kwargs.get("aid")
        self.tc_pimverified = kwargs.get("tc_pimverified")
        self.pin_verified = kwargs.get("pin_verified")
