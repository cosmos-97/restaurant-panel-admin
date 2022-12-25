from app.db.base_class import Base
from sqlalchemy import Boolean, Column, ForeignKey, Integer, text
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import relationship


class OrderStationCombo(Base):
    id = Column(
        UUID(as_uuid=True),
        primary_key=True,
        server_default=text("uuid_generate_v4()"),
        unique=True,
        index=True,
    )
    order_id = Column(ForeignKey("order.id", ondelete="CASCADE"), primary_key=True)
    station_id = Column(ForeignKey("station.id", ondelete="CASCADE"), primary_key=True)
    combo_id = Column(ForeignKey("combo.id", ondelete="CASCADE"), primary_key=True)
    count = Column(Integer, nullable=False, default=1)
    status = Column(Boolean, nullable=True)

    combo = relationship("Combo")

    def __init__(self, **kwargs) -> None:
        self.order_id = kwargs.get("order_id")
        self.station_id = kwargs.get("station_id")
        self.combo_id = kwargs.get("combo_id")
        self.count = kwargs.get("count")
        self.status = kwargs.get("status")
