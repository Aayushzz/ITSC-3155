from sqlalchemy.orm import Session
from fastapi import HTTPException, status, Response
from ..models import models, schemas

def create(db: Session, recipe: schemas.RecipeCreate):
    db_row = models.Recipe(
        sandwich_id=recipe.sandwich_id,
        resource_id=recipe.resource_id,
        amount=recipe.amount,
    )
    db.add(db_row)
    db.commit()
    db.refresh(db_row)
    return db_row

def read_all(db: Session):
    return db.query(models.Recipe).all()

def read_one(db: Session, recipe_id: int):
    return db.query(models.Recipe).filter(models.Recipe.id == recipe_id).first()

def update(db: Session, recipe_id: int, recipe: schemas.RecipeUpdate):
    q = db.query(models.Recipe).filter(models.Recipe.id == recipe_id)
    q.update(recipe.model_dump(exclude_unset=True), synchronize_session=False)
    db.commit()
    return q.first()

def delete(db: Session, recipe_id: int):
    q = db.query(models.Recipe).filter(models.Recipe.id == recipe_id)
    q.delete(synchronize_session=False)
    db.commit()
    return Response(status_code=status.HTTP_204_NO_CONTENT)
