from fastapi import HTTPException, status
from sqlalchemy.orm import Session

from src.shemas.owner import OwnerModel
from src.database.models import Owner


async def get_owners(db: Session) -> list[Owner]:
    print("get_owners")
    owners: list[Owner] = []
    try:
        owners = db.query(Owner).all()
    except Exception as err:
        print("ERROR: db.query get_owners")
    return owners


async def get_owner_by_id(owner_id: int, db: Session):
    owner = None
    try:
        owner = db.query(Owner).filter_by(id=owner_id).first()
    except Exception as err:
        print("ERROR: db.query get_owner_by_id")
    return owner


async def get_owner_by_email(email: str, db: Session):
    owner = None
    try:
        owner = db.query(Owner).filter_by(email=email).first()
    except Exception as err:
        print("ERROR: db.query get_owner_by_email")
    return owner


async def create(body: OwnerModel, db: Session):
    owner = None
    try:
        owner = Owner(**body.model_dump())
        db.add(owner)
        db.commit()
        db.refresh(owner)
    except Exception as err:
        print("ERROR: db.query create")
    return owner


async def update(owner_id: int, body: OwnerModel, db: Session):
    owner: Owner | None = None
    try:
        owner = await get_owner_by_id(owner_id, db)
        if owner:
            owner.email = body.email    # type: ignore
            db.commit()
    except Exception as err:
        print("ERROR: db.query update")    
    return owner


async def delete(owner_id: int, db: Session):
    owner: Owner | None = None
    try:
        owner = await get_owner_by_id(owner_id, db)
        if owner:
            db.delete(owner)
            db.commit()
    except Exception as err:
        print("ERROR: db.query delete")    
    return owner
