from app.db.base_class import Base
from sqlalchemy import (
    Column,
    DateTime,
    ForeignKey,
    Boolean,
    func,
    BigInteger,
    Float,
    String,
)
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import relationship


class Request(Base):
    id = Column(BigInteger, primary_key=True, index=True)
    user_id = Column(
        UUID(as_uuid=True), ForeignKey("user.id"), index=True, nullable=False
    )
    vendor_id = Column(
        UUID(as_uuid=True), ForeignKey("vendor.id"), index=True, nullable=False
    )
    product = Column(String, nullable=False)
    price = Column(Float, nullable=False)
    quantity = Column(Float, nullable=False)
    unit = Column(String, nullable=False)
    status = Column(Boolean, nullable=False, default=True)
    created_at = Column(DateTime(timezone=True), server_default=func.now())

    vendor = relationship("Vendor", back_populates="requests", foreign_keys=[vendor_id])
