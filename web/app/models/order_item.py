from app.db.base_class import Base
from sqlalchemy import Column, ForeignKey, Table

order_item = Table(
    "order_item",
    Base.metadata,
    Column("order_id", ForeignKey("order.id", ondelete="CASCADE"), primary_key=True),
    Column("item_id", ForeignKey("item.id", ondelete="CASCADE"), primary_key=True),
)
