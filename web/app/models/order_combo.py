from app.db.base_class import Base
from sqlalchemy import Column, ForeignKey, Table

order_combo = Table(
    "order_combo",
    Base.metadata,
    Column("order_id", ForeignKey("order.id", ondelete="CASCADE"), primary_key=True),
    Column("combo_id", ForeignKey("combo.id", ondelete="CASCADE"), primary_key=True),
)
