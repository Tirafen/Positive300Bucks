from sqlalchemy.orm import Session
from sqlalchemy import text
import models
import schemas
from uuid import uuid4, UUID


def get_user(db: Session, user_id: UUID):
    return db.query(models.User).filter(models.User.id == user_id).first()


def get_user_by_email(db: Session, email: str):
    return db.query(models.User).filter(models.User.email == email).first()


def get_users(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.User).offset(skip).limit(limit).all()


def create_user(db: Session, user: schemas.UserCreate):
    generated_id = uuid4()
    db_user = models.User(id=generated_id, email=user.email, name=user.name)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user


def get_items(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Orders).offset(skip).limit(limit).all()


def create_user_item(db: Session, item: schemas.OrderCreate, user_id: UUID):
    order_number = db.query(text('count(*) from orders')).first()
    if order_number is None:
        order_number = 1
    else:
        order_number = order_number[0]
        order_number += 1
    db_item = models.Orders(**item.dict(), owner_id=user_id, order_number=order_number)
    db.add(db_item)
    db.commit()
    db.refresh(db_item)
    return db_item
