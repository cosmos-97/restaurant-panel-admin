from app.db.base_class import Base
from sqlalchemy import Column, ForeignKey, Table

special_item = Table(
    "special_item",
    Base.metadata,
    Column(
        "special_id", ForeignKey("special.id", ondelete="CASCADE"), primary_key=True
    ),
    Column("item_id", ForeignKey("item.id", ondelete="CASCADE"), primary_key=True),
)
