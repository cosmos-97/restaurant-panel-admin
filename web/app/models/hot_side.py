from app.db.base_class import Base
from sqlalchemy import Boolean, Column, ForeignKey, String, text
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import relationship

from .combo_hot_side import combo_hot_side
from .item_hot_side import item_hot_side


class HotSide(Base):
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
    items = relationship("Item", secondary=item_hot_side, back_populates="hot_sides")
    combos = relationship("Combo", secondary=combo_hot_side, back_populates="hot_sides")
