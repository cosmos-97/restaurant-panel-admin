from app.db.base_class import Base
from sqlalchemy import Column, Float, ForeignKey, String, Text, text
from sqlalchemy.dialects.postgresql import UUID


class Appearance(Base):
    id = Column(
        UUID(as_uuid=True),
        primary_key=True,
        server_default=text("uuid_generate_v4()"),
        unique=True,
        index=True,
    )
    user_id = Column(UUID(as_uuid=True), ForeignKey("user.id"), index=True)
    welcome_screen_url = Column(String, nullable=True)
    logo_url = Column(String, nullable=True)
    title_1 = Column(String, nullable=True)
    title_2 = Column(String, nullable=True)


class StoreInfo(Base):
    id = Column(
        UUID(as_uuid=True),
        primary_key=True,
        server_default=text("uuid_generate_v4()"),
        unique=True,
        index=True,
    )
    user_id = Column(UUID(as_uuid=True), ForeignKey("user.id"), index=True)
    name = Column(String, nullable=True)
    telephone = Column(String, nullable=True)
    city = Column(String, nullable=True)
    address_1 = Column(String, nullable=True)
    address_2 = Column(String, nullable=True)
    state = Column(String, nullable=True)
    zip_code = Column(String, nullable=True)
    tax_id = Column(String, nullable=True)
    store_id = Column(String, nullable=True)


class Receipt(Base):
    id = Column(
        UUID(as_uuid=True),
        primary_key=True,
        server_default=text("uuid_generate_v4()"),
        unique=True,
        index=True,
    )
    user_id = Column(UUID(as_uuid=True), ForeignKey("user.id"), index=True)
    address_1 = Column(String, nullable=True)
    address_2 = Column(String, nullable=True)
    tax_amount = Column(Float, nullable=True)
    other_charges = Column(Float, nullable=True)
    message = Column(Text, nullable=True)


class Sound(Base):
    id = Column(
        UUID(as_uuid=True),
        primary_key=True,
        server_default=text("uuid_generate_v4()"),
        unique=True,
        index=True,
    )
    user_id = Column(UUID(as_uuid=True), ForeignKey("user.id"), index=True)
    incoming_order = Column(String, nullable=True)
    ready_order = Column(String, nullable=True)
