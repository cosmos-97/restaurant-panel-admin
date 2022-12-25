from app.db.base_class import Base
from sqlalchemy import Boolean, Column, ForeignKey, String, text
from sqlalchemy.dialects.postgresql import UUID


class Printer(Base):
    id = Column(
        UUID(as_uuid=True),
        primary_key=True,
        server_default=text("uuid_generate_v4()"),
        unique=True,
        index=True,
    )
    user_id = Column(UUID(as_uuid=True), ForeignKey("user.id"), index=True)
    remote_printer_ip = Column(String, nullable=True)
    port_number = Column(String, nullable=True)
    queue_name = Column(String, nullable=True)
    status = Column(Boolean, nullable=False, default=True)
