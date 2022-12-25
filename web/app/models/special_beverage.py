from app.db.base_class import Base
from sqlalchemy import Column, ForeignKey, Table

special_beverage = Table(
    "special_beverage",
    Base.metadata,
    Column(
        "special_id", ForeignKey("special.id", ondelete="CASCADE"), primary_key=True
    ),
    Column(
        "beverage_id", ForeignKey("beverage.id", ondelete="CASCADE"), primary_key=True
    ),
)
