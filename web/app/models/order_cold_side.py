from app.db.base_class import Base
from sqlalchemy import Column, ForeignKey, Table

order_cold_side = Table(
    "order_cold_side",
    Base.metadata,
    Column("order_id", ForeignKey("order.id", ondelete="CASCADE"), primary_key=True),
    Column(
        "coldside_id", ForeignKey("coldside.id", ondelete="CASCADE"), primary_key=True
    ),
)
