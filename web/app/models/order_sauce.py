from app.db.base_class import Base
from sqlalchemy import Column, ForeignKey, Table

order_sauce = Table(
    "order_sauce",
    Base.metadata,
    Column("order_id", ForeignKey("order.id", ondelete="CASCADE"), primary_key=True),
    Column("sauce_id", ForeignKey("sauce.id", ondelete="CASCADE"), primary_key=True),
)
