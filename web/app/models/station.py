from app.db.base_class import Base
from sqlalchemy import ARRAY, Column, ForeignKey, Integer, String, text
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import relationship


def channel_name(context):
    return context.get_current_parameters()["station_name"]


class Station(Base):
    id = Column(
        UUID(as_uuid=True),
        primary_key=True,
        server_default=text("uuid_generate_v4()"),
        unique=True,
        index=True,
    )
    user_id = Column(UUID(as_uuid=True), ForeignKey("user.id"), index=True)
    station_name = Column(String, index=True, nullable=False)
    channel_name = Column(String, nullable=False, default=channel_name)
    max_time = Column(Integer, nullable=False)
    statuses = Column(ARRAY(String), nullable=False)

    items = relationship("OrderStationItem", viewonly=True)
    combos = relationship("OrderStationCombo", viewonly=True)
    specials = relationship("OrderStationSpecial", viewonly=True)
    hot_sides = relationship("OrderStationHotSide", viewonly=True)
    cold_sides = relationship("OrderStationColdSide", viewonly=True)
    sauces = relationship("OrderStationSauce", viewonly=True)
    beverages = relationship("OrderStationBeverage", viewonly=True)
    desserts = relationship("OrderStationDessert", viewonly=True)
