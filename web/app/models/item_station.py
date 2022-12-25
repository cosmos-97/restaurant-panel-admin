from app.db.base_class import Base
from sqlalchemy import Column, ForeignKey, Table

item_station = Table(
    "item_station",
    Base.metadata,
    Column("item_id", ForeignKey("item.id", ondelete="CASCADE"), primary_key=True),
    Column(
        "station_id", ForeignKey("station.id", ondelete="CASCADE"), primary_key=True
    ),
)
