from app.db.base_class import Base
from sqlalchemy import Column, ForeignKey, Table

combo_cold_side = Table(
    "combo_cold_side",
    Base.metadata,
    Column("combo_id", ForeignKey("combo.id", ondelete="CASCADE"), primary_key=True),
    Column(
        "cold_side_id", ForeignKey("cold_side.id", ondelete="CASCADE"), primary_key=True
    ),
)
