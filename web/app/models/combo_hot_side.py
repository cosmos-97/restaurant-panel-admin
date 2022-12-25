from app.db.base_class import Base
from sqlalchemy import Column, ForeignKey, Table

combo_hot_side = Table(
    "combo_hot_side",
    Base.metadata,
    Column("combo_id", ForeignKey("combo.id", ondelete="CASCADE"), primary_key=True),
    Column(
        "hot_side_id", ForeignKey("hot_side.id", ondelete="CASCADE"), primary_key=True
    ),
)
