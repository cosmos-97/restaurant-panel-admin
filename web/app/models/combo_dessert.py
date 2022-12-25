from app.db.base_class import Base
from sqlalchemy import Column, ForeignKey, Table

combo_dessert = Table(
    "combo_dessert",
    Base.metadata,
    Column("combo_id", ForeignKey("combo.id", ondelete="CASCADE"), primary_key=True),
    Column(
        "dessert_id", ForeignKey("dessert.id", ondelete="CASCADE"), primary_key=True
    ),
)
