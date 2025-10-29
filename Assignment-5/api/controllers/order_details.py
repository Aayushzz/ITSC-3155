from sqlalchemy.orm import Session
from fastapi import HTTPException, status, Response
from ..models import models, schemas

def create(db: Session, detail: schemas.OrderDetailCreate):
    db_row = models.OrderDetail(
        order_id=detail.order_id,
        sandwich_id=detail.sandwich_id,
        amount=detail.amount,
    )
    db.add(db_row)
    db.commit()
    db.refresh(db_row)
    return db_row

def read_all(db: Session):
    return db.query(models.OrderDetail).all()

def read_one(db: Session, detail_id: int):
    return db.query(models.OrderDetail).filter(models.OrderDetail.id == detail_id).first()

def update(db: Session, detail_id: int, detail: schemas.OrderDetailUpdate):
    q = db.query(models.OrderDetail).filter(models.OrderDetail.id == detail_id)
    q.update(detail.model_dump(exclude_unset=True), synchronize_session=False)
    db.commit()
    return q.first()

def delete(db: Session, detail_id: int):
    q = db.query(models.OrderDetail).filter(models.OrderDetail.id == detail_id)
    q.delete(synchronize_session=False)
    db.commit()
    return Response(status_code=status.HTTP_204_NO_CONTENT)
