from app.db.base_class import Base
from sqlalchemy import Column, ForeignKey, Table

combo_option = Table(
    "combo_option",
    Base.metadata,
    Column("combo_id", ForeignKey("combo.id", ondelete="CASCADE"), primary_key=True),
    Column("option_id", ForeignKey("option.id", ondelete="CASCADE"), primary_key=True),
)
