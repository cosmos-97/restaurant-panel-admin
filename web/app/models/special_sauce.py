from app.db.base_class import Base
from sqlalchemy import Column, ForeignKey, Table

special_sauce = Table(
    "special_sauce",
    Base.metadata,
    Column(
        "special_id", ForeignKey("special.id", ondelete="CASCADE"), primary_key=True
    ),
    Column("sauce_id", ForeignKey("sauce.id", ondelete="CASCADE"), primary_key=True),
)
