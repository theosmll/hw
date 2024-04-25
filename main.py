from fastapi import FastAPI, HTTPException, Depends
from sqlalchemy.orm import Session
from .models import User, Product, Order
from .crud import get_user, create_user, get_product, create_product, get_order, create_order
from .database import SessionLocal, engine, database

app = FastAPI()

# Dependency to get the database session
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.on_event("startup")
async def startup():
    await database.connect()

@app.on_event("shutdown")
async def shutdown():
    await database.disconnect()

@app.post("/users/", response_model=User)
def create_new_user(user: User, db: Session = Depends(get_db)):
    db_user = get_user(db, user.id)
    if db_user:
        raise HTTPException(status_code=400, detail="User already registered")
    return create_user(db, user)

@app.get("/users/{user_id}", response_model=User)
def read_user(user_id: int, db: Session = Depends(get_db)):
    db_user = get_user(db, user_id)
    if db_user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return db_user

@app.post("/products/", response_model=Product)
def create_new_product(product: Product, db: Session = Depends(get_db)):
    db_product = get_product(db, product.id)
    if db_product:
        raise HTTPException(status_code=400, detail="Product already exists")
    return create_product(db, product)

@app.get("/products/{product_id}", response_model=Product)
def read_product(product_id: int, db: Session = Depends(get_db)):
    db_product = get_product(db, product_id)
    if db_product is None:
        raise HTTPException(status_code=404, detail="Product not found")
    return db_product

@app.post("/orders/", response_model=Order)
def create_new_order(order: Order, db: Session = Depends(get_db)):
    return create_order(db, order)

@app.get("/orders/{order_id}", response_model=Order)
def read_order(order_id: int, db: Session = Depends(get_db)):
    db_order = get_order(db, order_id)
    if db_order is None:
        raise HTTPException(status_code=404, detail="Order not found")
    return db_order

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8000)
