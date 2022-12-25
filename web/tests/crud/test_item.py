from app import crud
from app.schemas.item import ItemCreate, ItemUpdate
from sqlalchemy.orm import Session
from web.tests.utils.category import create_random_category
from web.tests.utils.sauce import create_random_sauce
from web.tests.utils.user import create_random_superuser
from web.tests.utils.utils import random_lower_string, random_bool, random_number


def test_create_item(db: Session) -> None:
    name = random_lower_string()
    description = random_lower_string()
    special_instructions = random_bool()
    price = random_number()

    user = create_random_superuser(db)
    category = create_random_category(db, user_id=user.id)
    sauces = [create_random_sauce(db, user_id=user.id) for _ in range(3)]
    sauces_ids = [sauce.id for sauce in sauces]

    item_in = ItemCreate(
        name=name,
        description=description,
        category_id=category.id,
        special_instructions=special_instructions,
        price=price,
        sauces=sauces_ids,
    )
    item = crud.item.create_with_owner(db=db, obj_in=item_in, user_id=user.id)

    assert item.name == name
    assert item.description == description
    assert item.user_id == user.id


def test_get_item(db: Session) -> None:
    title = random_lower_string()
    description = random_lower_string()
    item_in = ItemCreate(title=title, description=description)
    user = create_random_superuser(db)
    item = crud.item.create_with_owner(db=db, obj_in=item_in, owner_id=user.id)
    stored_item = crud.item.get(db=db, id=item.id)
    assert stored_item
    assert item.id == stored_item.id
    assert item.title == stored_item.title
    assert item.description == stored_item.description
    assert item.owner_id == stored_item.owner_id


def test_update_item(db: Session) -> None:
    title = random_lower_string()
    description = random_lower_string()
    item_in = ItemCreate(title=title, description=description)
    user = create_random_superuser(db)
    item = crud.item.create_with_owner(db=db, obj_in=item_in, owner_id=user.id)
    description2 = random_lower_string()
    item_update = ItemUpdate(description=description2)
    item2 = crud.item.update(db=db, db_obj=item, obj_in=item_update)
    assert item.id == item2.id
    assert item.title == item2.title
    assert item2.description == description2
    assert item.owner_id == item2.owner_id


def test_delete_item(db: Session) -> None:
    title = random_lower_string()
    description = random_lower_string()
    item_in = ItemCreate(title=title, description=description)
    user = create_random_superuser(db)
    item = crud.item.create_with_owner(db=db, obj_in=item_in, owner_id=user.id)
    item2 = crud.item.remove(db=db, id=item.id)
    item3 = crud.item.get(db=db, id=item.id)
    assert item3 is None
    assert item2.id == item.id
    assert item2.title == title
    assert item2.description == description
    assert item2.owner_id == user.id
