from app.db.base_class import Base
from sqlalchemy import Column, ForeignKey, Table

special_ingredient = Table(
    "special_ingredient",
    Base.metadata,
    Column(
        "special_id", ForeignKey("special.id", ondelete="CASCADE"), primary_key=True
    ),
    Column(
        "ingredient_id",
        ForeignKey("ingredient.id", ondelete="CASCADE"),
        primary_key=True,
    ),
)
