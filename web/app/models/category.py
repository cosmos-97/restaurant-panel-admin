from app.db.base_class import Base
from sqlalchemy import Boolean, Column, ForeignKey, String, text
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import relationship


class Category(Base):
    id = Column(
        UUID(as_uuid=True),
        primary_key=True,
        server_default=text("uuid_generate_v4()"),
        unique=True,
        index=True,
    )
    user_id = Column(UUID(as_uuid=True), ForeignKey("user.id"), index=True)
    category_name = Column(String, index=True, nullable=False)
    logo_url = Column(String, nullable=False)
    status = Column(Boolean, nullable=False, default=True)

    items = relationship(
        "Item", back_populates="category", cascade="all, delete-orphan", uselist=True
    )
    combos = relationship(
        "Combo", back_populates="category", cascade="all, delete-orphan", uselist=True
    )
    specials = relationship(
        "Special", back_populates="category", cascade="all, delete-orphan", uselist=True
    )
