from app.db.base_class import Base
from sqlalchemy import Boolean, Column, ForeignKey, String, text
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import relationship

from .combo_option import combo_option
from .item_option import item_option


class Option(Base):
    id = Column(
        UUID(as_uuid=True),
        primary_key=True,
        server_default=text("uuid_generate_v4()"),
        unique=True,
        index=True,
    )
    user_id = Column(UUID(as_uuid=True), ForeignKey("user.id"), index=True)
    option_name = Column(String, index=True, nullable=False)
    status = Column(Boolean, nullable=False, default=True)

    items = relationship("Item", secondary=item_option, back_populates="options")
    combos = relationship("Combo", secondary=combo_option, back_populates="options")
