from app.db.base_class import Base
from sqlalchemy import Column, ForeignKey, Table

combo_sauce = Table(
    "combo_sauce",
    Base.metadata,
    Column("combo_id", ForeignKey("combo.id", ondelete="CASCADE"), primary_key=True),
    Column("sauce_id", ForeignKey("sauce.id", ondelete="CASCADE"), primary_key=True),
)
