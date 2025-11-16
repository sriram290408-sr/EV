# main.py
from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session
from database import SessionLocal, Base, engine
from models import StudentData
from schemas import CreateBase, ResponseModel

# Create all database tables
Base.metadata.create_all(bind=engine)

app = FastAPI()

# Dependency for DB session
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


# POST - Create Student Data
@app.post("/Datalist", response_model=ResponseModel)
def create_data(data: CreateBase, db: Session = Depends(get_db)):
    db_data = StudentData(**data.dict())
    db.add(db_data)
    db.commit()
    db.refresh(db_data)
    return db_data
