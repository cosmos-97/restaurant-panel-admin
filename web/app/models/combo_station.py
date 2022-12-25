from app.db.base_class import Base
from sqlalchemy import Column, ForeignKey, Table

combo_station = Table(
    "combo_station",
    Base.metadata,
    Column("combo_id", ForeignKey("combo.id", ondelete="CASCADE"), primary_key=True),
    Column(
        "station_id", ForeignKey("station.id", ondelete="CASCADE"), primary_key=True
    ),
)
