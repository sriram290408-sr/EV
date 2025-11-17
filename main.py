from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session
from database import SessionLocal, Base, engine
from models import StudentData, StudentMarks
from schemas import CreateBase, ResponseModel, MarksBase, MarksResponse

Base.metadata.create_all(bind=engine)

app = FastAPI()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


# POST: Create Student
@app.post("/student", response_model=ResponseModel)
def create_student(data: CreateBase, db: Session = Depends(get_db)):
    db_student = StudentData(**data.dict())
    db.add(db_student)
    db.commit()
    db.refresh(db_student)
    return db_student


# POST: Add Marks for a Student
@app.post("/student/{student_id}/marks", response_model=MarksResponse)
def add_marks(student_id: int, marks: MarksBase, db: Session = Depends(get_db)):
    db_marks = StudentMarks(student_id=student_id, **marks.dict())
    db.add(db_marks)
    db.commit()
    db.refresh(db_marks)
    return db_marks
