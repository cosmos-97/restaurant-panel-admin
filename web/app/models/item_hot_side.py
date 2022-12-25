from app.db.base_class import Base
from sqlalchemy import Column, ForeignKey, Table

item_hot_side = Table(
    "item_hot_side",
    Base.metadata,
    Column("item_id", ForeignKey("item.id", ondelete="CASCADE"), primary_key=True),
    Column(
        "hot_side_id", ForeignKey("hot_side.id", ondelete="CASCADE"), primary_key=True
    ),
)
