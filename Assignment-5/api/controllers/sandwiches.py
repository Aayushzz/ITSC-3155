from sqlalchemy.orm import Session
from fastapi import HTTPException, status, Response
from ..models import models, schemas

def create(db: Session, sandwich: schemas.SandwichCreate):
    db_row = models.Sandwich(
        sandwich_name=sandwich.sandwich_name,
        price=sandwich.price,
    )
    db.add(db_row)
    db.commit()
    db.refresh(db_row)
    return db_row

def read_all(db: Session):
    return db.query(models.Sandwich).all()

def read_one(db: Session, sandwich_id: int):
    return db.query(models.Sandwich).filter(models.Sandwich.id == sandwich_id).first()

def update(db: Session, sandwich_id: int, sandwich: schemas.SandwichUpdate):
    q = db.query(models.Sandwich).filter(models.Sandwich.id == sandwich_id)
    q.update(sandwich.model_dump(exclude_unset=True), synchronize_session=False)
    db.commit()
    return q.first()

def delete(db: Session, sandwich_id: int):
    q = db.query(models.Sandwich).filter(models.Sandwich.id == sandwich_id)
    q.delete(synchronize_session=False)
    db.commit()
    return Response(status_code=status.HTTP_204_NO_CONTENT)
