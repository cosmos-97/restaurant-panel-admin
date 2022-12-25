from app.db.base_class import Base
from sqlalchemy import Column, DateTime, ForeignKey, String, func, text
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import relationship

from .vendor_category import vendor_category


class Vendor(Base):
    id = Column(
        UUID(as_uuid=True),
        primary_key=True,
        server_default=text("uuid_generate_v4()"),
        unique=True,
        index=True,
    )
    user_id = Column(UUID(as_uuid=True), ForeignKey("user.id"), index=True)
    name = Column(String, index=True, nullable=False)
    phone = Column(String, nullable=False)
    created_at = Column(DateTime(timezone=True), server_default=func.now())

    categories = relationship("Category", secondary=vendor_category)
    requests = relationship(
        "Request", back_populates="vendor", cascade="all, delete-orphan", uselist=True
    )

    def __init__(self, **kwargs):
        self.user_id = kwargs.get("user_id")
        self.name = kwargs.get("name")
        self.phone = kwargs.get("phone")
