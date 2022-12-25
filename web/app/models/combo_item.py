from app.db.base_class import Base
from sqlalchemy import Column, ForeignKey, Table

combo_item = Table(
    "combo_item",
    Base.metadata,
    Column("combo_id", ForeignKey("combo.id", ondelete="CASCADE"), primary_key=True),
    Column("item_id", ForeignKey("item.id", ondelete="CASCADE"), primary_key=True),
)
