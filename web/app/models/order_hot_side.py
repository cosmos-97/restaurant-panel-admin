from app.db.base_class import Base
from sqlalchemy import Column, ForeignKey, Table

order_hot_side = Table(
    "order_hot_side",
    Base.metadata,
    Column("order_id", ForeignKey("order.id", ondelete="CASCADE"), primary_key=True),
    Column(
        "hotside_id", ForeignKey("hotside.id", ondelete="CASCADE"), primary_key=True
    ),
)
