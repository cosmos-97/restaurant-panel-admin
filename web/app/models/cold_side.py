from app.db.base_class import Base
from sqlalchemy import Boolean, Column, ForeignKey, String, text
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import relationship

from .combo_cold_side import combo_cold_side
from .item_cold_side import item_cold_side


class ColdSide(Base):
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
    status = Column(Boolean, nullable=False, default=True)

    station = relationship("Station")
    items = relationship("Item", secondary=item_cold_side, back_populates="cold_sides")
    combos = relationship(
        "Combo", secondary=combo_cold_side, back_populates="cold_sides"
    )
