from app.db.base_class import Base
from sqlalchemy import Column, ForeignKey, Table

item_sauce = Table(
    "item_sauce",
    Base.metadata,
    Column("item_id", ForeignKey("item.id", ondelete="CASCADE"), primary_key=True),
    Column("sauce_id", ForeignKey("sauce.id", ondelete="CASCADE"), primary_key=True),
)
