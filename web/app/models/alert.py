from app.db.base_class import Base
from sqlalchemy import Boolean, Column, ForeignKey, String, text, Float, Text
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import relationship

from .user_alert import user_alert


class Alert(Base):
    id = Column(
        UUID(as_uuid=True),
        primary_key=True,
        server_default=text("uuid_generate_v4()"),
        unique=True,
        index=True,
    )
    user_id = Column(UUID(as_uuid=True), ForeignKey("user.id"), index=True)
    item_name = Column(String, index=True, nullable=False)
    unit = Column(String, nullable=False)
    time = Column(Float, nullable=False)
    action_needed = Column(Text, nullable=False)
    automatic_ordering = Column(Boolean, nullable=False)

    users = relationship("User", secondary=user_alert)

    def __init__(self, **kwargs):
        self.user_id = kwargs.get("user_id")
        self.item_name = kwargs.get("item_name")
        self.unit = kwargs.get("unit")
        self.time = kwargs.get("time")
        self.action_needed = kwargs.get("action_needed")
        self.automatic_ordering = kwargs.get("automatic_ordering")
