from app.db.base_class import Base
from sqlalchemy import Column, ForeignKey, Table

special_dessert = Table(
    "special_dessert",
    Base.metadata,
    Column(
        "special_id", ForeignKey("special.id", ondelete="CASCADE"), primary_key=True
    ),
    Column(
        "dessert_id", ForeignKey("dessert.id", ondelete="CASCADE"), primary_key=True
    ),
)
