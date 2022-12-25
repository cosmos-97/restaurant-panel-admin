from app.db.base_class import Base
from sqlalchemy import Column, ForeignKey, Table

order_dessert = Table(
    "order_dessert",
    Base.metadata,
    Column("order_id", ForeignKey("order.id", ondelete="CASCADE"), primary_key=True),
    Column(
        "dessert_id", ForeignKey("dessert.id", ondelete="CASCADE"), primary_key=True
    ),
)
