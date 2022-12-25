from app.db.base_class import Base
from sqlalchemy import Column, ForeignKey, Table

order_beverage = Table(
    "order_beverage",
    Base.metadata,
    Column("order_id", ForeignKey("order.id", ondelete="CASCADE"), primary_key=True),
    Column(
        "beverage_id", ForeignKey("beverage.id", ondelete="CASCADE"), primary_key=True
    ),
)
