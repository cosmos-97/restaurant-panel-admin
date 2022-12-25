from app.db.base_class import Base
from sqlalchemy import Boolean, Column, String, text
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import relationship

from .user_station import user_station


class User(Base):
    id = Column(
        UUID(as_uuid=True),
        primary_key=True,
        server_default=text("uuid_generate_v4()"),
        unique=True,
        index=True,
    )
    username = Column(String, unique=True, index=True, nullable=False)
    phone = Column(String, nullable=False)
    email = Column(String, nullable=False)
    hashed_password = Column(String, nullable=False)
    is_superuser = Column(Boolean, default=False)

    stations = relationship("Station", secondary=user_station)
