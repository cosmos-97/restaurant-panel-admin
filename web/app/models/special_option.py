from app.db.base_class import Base
from sqlalchemy import Column, ForeignKey, Table

special_option = Table(
    "special_option",
    Base.metadata,
    Column(
        "special_id", ForeignKey("special.id", ondelete="CASCADE"), primary_key=True
    ),
    Column("option_id", ForeignKey("option.id", ondelete="CASCADE"), primary_key=True),
)
