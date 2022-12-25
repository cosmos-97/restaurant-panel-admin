from app.db.base_class import Base
from sqlalchemy import Boolean, Column, ForeignKey, String, text
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import relationship

from .combo_beverage import combo_beverage


class Beverage(Base):
    id = Column(
        UUID(as_uuid=True),
        primary_key=True,
        server_default=text("uuid_generate_v4()"),
        unique=True,
        index=True,
    )
    user_id = Column(UUID(as_uuid=True), ForeignKey("user.id"), index=True)
    station_id = Column(UUID(as_uuid=True), ForeignKey("station.id"), index=True)
    beverage_name = Column(String, index=True, nullable=False)
    status = Column(Boolean, nullable=False, default=True)

    station = relationship("Station")
    combos = relationship("Combo", secondary=combo_beverage, back_populates="beverages")
