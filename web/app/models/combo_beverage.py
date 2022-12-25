from app.db.base_class import Base
from sqlalchemy import Column, ForeignKey, Table

combo_beverage = Table(
    "combo_beverage",
    Base.metadata,
    Column("combo_id", ForeignKey("combo.id", ondelete="CASCADE"), primary_key=True),
    Column(
        "beverage_id", ForeignKey("beverage.id", ondelete="CASCADE"), primary_key=True
    ),
)
