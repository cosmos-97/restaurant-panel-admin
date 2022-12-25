from app.db.base_class import Base
from sqlalchemy import Column, ForeignKey, Table

item_cold_side = Table(
    "item_cold_side",
    Base.metadata,
    Column("item_id", ForeignKey("item.id", ondelete="CASCADE"), primary_key=True),
    Column(
        "cold_side_id", ForeignKey("cold_side.id", ondelete="CASCADE"), primary_key=True
    ),
)
