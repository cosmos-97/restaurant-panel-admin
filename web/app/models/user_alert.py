from app.db.base_class import Base
from sqlalchemy import Column, ForeignKey, Table

user_alert = Table(
    "user_alert",
    Base.metadata,
    Column("user_id", ForeignKey("user.id", ondelete="CASCADE"), primary_key=True),
    Column("alert_id", ForeignKey("alert.id", ondelete="CASCADE"), primary_key=True),
)
