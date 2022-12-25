from typing import Any
from re import sub
from sqlalchemy.ext.declarative import as_declarative, declared_attr


@as_declarative()
class Base:
    id: Any
    __name__: str

    @declared_attr
    def __tablename__(cls) -> str:
        return "_".join(
            sub(
                "([A-Z][a-z]+)",
                r" \1",
                sub("([A-Z]+)", r" \1", cls.__name__.replace("-", " ")),
            ).split()
        ).lower()
