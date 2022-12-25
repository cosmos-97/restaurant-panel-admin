from app.db.base_class import Base
from sqlalchemy import Column, ForeignKey, Table

vendor_category = Table(
    "vendor_category",
    Base.metadata,
    Column("vendor_id", ForeignKey("vendor.id", ondelete="CASCADE"), primary_key=True),
    Column(
        "category_id", ForeignKey("category.id", ondelete="CASCADE"), primary_key=True
    ),
)
