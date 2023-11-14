from sqlalchemy.orm import Session

from src.shemas.cat import CatModel, CatVactinatedModel
from src.database.models import Cat


async def get_cats(limit: int, offset: int, db: Session):
    cats = db.query(Cat).limit(limit).offset(offset).all()
    return cats


async def get_cat_by_id(cat_id: int, db: Session):
    cat = db.query(Cat).filter_by(id=cat_id).first()
    return cat


async def create(body: CatModel, db: Session):
    cat = Cat(**body.model_dump())
    db.add(cat)
    db.commit()
    db.refresh(cat)
    return cat


async def update(cat_id: int, body: CatModel, db: Session):
    cat = await get_cat_by_id(cat_id, db)
    if cat:
        cat.nickname = body.nickname        
        cat.age = body.age                  
        cat.description = body.description  
        cat.vaccinated = body.vaccinated    
        cat.nickname = body.nickname        
        cat.owner_id = body.owner_id        
        db.commit()
    return cat


async def delete(cat_id: int, db: Session):
    cat = await get_cat_by_id(cat_id, db)
    if cat:
        db.delete(cat)
        db.commit()
    return cat

async def set_vactinated(cat_id: int, body: CatVactinatedModel, db: Session):
    cat = await get_cat_by_id(cat_id, db)
    if cat:
        if cat.vaccinated != body.vaccinated:   # type: ignore
            cat.vaccinated = body.vaccinated    # type: ignore
            db.commit()
    return cat
