from app.db.base_class import Base
from sqlalchemy import Column, ForeignKey, Table

item_ingredient = Table(
    "item_ingredient",
    Base.metadata,
    Column("item_id", ForeignKey("item.id", ondelete="CASCADE"), primary_key=True),
    Column(
        "ingredient_id",
        ForeignKey("ingredient.id", ondelete="CASCADE"),
        primary_key=True,
    ),
)
