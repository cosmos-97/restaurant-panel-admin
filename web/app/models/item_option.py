from app.db.base_class import Base
from sqlalchemy import Column, ForeignKey, Table

item_option = Table(
    "item_option",
    Base.metadata,
    Column("item_id", ForeignKey("item.id", ondelete="CASCADE"), primary_key=True),
    Column("option_id", ForeignKey("option.id", ondelete="CASCADE"), primary_key=True),
)
