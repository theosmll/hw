from sqlalchemy.orm import Session
from .models import User, Product, Order
from .database import UserDB, ProductDB, OrderDB

def get_user(db: Session, user_id: int):
    return db.query(UserDB).filter(UserDB.id == user_id).first()

def create_user(db: Session, user: User):
    db_user = UserDB(**user.dict())
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user

def get_product(db: Session, product_id: int):
    return db.query(ProductDB).filter(ProductDB.id == product_id).first()

def create_product(db: Session, product: Product):
    db_product = ProductDB(**product.dict())
    db.add(db_product)
    db.commit()
    db.refresh(db_product)
    return db_product

def get_order(db: Session, order_id: int):
    return db.query(OrderDB).filter(OrderDB.id == order_id).first()

def create_order(db: Session, order: Order):
    db_order = OrderDB(**order.dict())
    db.add(db_order)
    db.commit()
    db.refresh(db_order)
    return db_order
