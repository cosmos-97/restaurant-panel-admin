from app.db.base_class import Base
from sqlalchemy import Column, ForeignKey, Table

special_cold_side = Table(
    "special_cold_side",
    Base.metadata,
    Column(
        "special_id", ForeignKey("special.id", ondelete="CASCADE"), primary_key=True
    ),
    Column(
        "cold_side_id", ForeignKey("cold_side.id", ondelete="CASCADE"), primary_key=True
    ),
)
