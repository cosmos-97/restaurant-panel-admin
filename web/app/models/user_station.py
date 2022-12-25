from app.db.base_class import Base
from sqlalchemy import Column, ForeignKey, Table

user_station = Table(
    "user_station",
    Base.metadata,
    Column("user_id", ForeignKey("user.id", ondelete="CASCADE"), primary_key=True),
    Column(
        "station_id", ForeignKey("station.id", ondelete="CASCADE"), primary_key=True
    ),
)
