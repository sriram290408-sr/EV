#main.py
from fastapi import FastAPI, Depends;
from schemas import CreateBase, ResponseModel;
from sqlalchemy.orm import Session;
from database import localsession, base;
from models import StudentData;

app = FastAPI()

#Dependency for DB Session 
def get_db():
    db = localsession()
    try:
        yield db
    finally:
        db.close()

# POST - Create Datalist
@app.post("/Datalist",response_model=ResponseModel)

def Create(Data: ResponseModel, db: Session = Depends(get_db)):
    db_data = StudentData(**Data.dict())
    db.add(db_data)
    db.commit()
    db.refresh()
    return db_data