from app.db.base_class import Base
from sqlalchemy import Column, ForeignKey, Table

special_combo = Table(
    "special_combo",
    Base.metadata,
    Column(
        "special_id", ForeignKey("special.id", ondelete="CASCADE"), primary_key=True
    ),
    Column("combo_id", ForeignKey("combo.id", ondelete="CASCADE"), primary_key=True),
)
