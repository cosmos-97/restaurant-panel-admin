from app.db.base_class import Base
from sqlalchemy import Column, ForeignKey, Table

special_hot_side = Table(
    "special_hot_side",
    Base.metadata,
    Column(
        "special_id", ForeignKey("special.id", ondelete="CASCADE"), primary_key=True
    ),
    Column(
        "hot_side_id", ForeignKey("hot_side.id", ondelete="CASCADE"), primary_key=True
    ),
)
