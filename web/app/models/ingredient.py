from app.db.base_class import Base
from sqlalchemy import Float, Boolean, Column, ForeignKey, String, text
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import relationship

from .item_ingredient import item_ingredient
from .combo_ingredient import combo_ingredient


class Ingredient(Base):
    id = Column(
        UUID(as_uuid=True),
        primary_key=True,
        server_default=text("uuid_generate_v4()"),
        unique=True,
        index=True,
    )
    user_id = Column(UUID(as_uuid=True), ForeignKey("user.id"), index=True)
    ingredient_name = Column(String, index=True, nullable=False)
    measuring_unit = Column(String, nullable=False)
    quantity = Column(Float, nullable=False)
    status = Column(Boolean, nullable=False, default=True)

    items = relationship(
        "Item", secondary=item_ingredient, back_populates="ingredients"
    )
    combos = relationship(
        "Combo", secondary=combo_ingredient, back_populates="ingredients"
    )
