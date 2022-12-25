from app.db.base_class import Base
from sqlalchemy import Column, ForeignKey, Table

combo_ingredient = Table(
    "combo_ingredient",
    Base.metadata,
    Column("combo_id", ForeignKey("combo.id", ondelete="CASCADE"), primary_key=True),
    Column(
        "ingredient_id",
        ForeignKey("ingredient.id", ondelete="CASCADE"),
        primary_key=True,
    ),
)
