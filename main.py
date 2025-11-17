#main.py
from fastapi import FastAPI, Depends, HTTPException
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

@app.post("/student", response_model=ResponseModel)
def create_student(data: CreateBase, db: Session = Depends(get_db)):
    s = StudentData(**data.model_dump())
    db.add(s)
    db.commit()
    db.refresh(s)
    return s

@app.post("/student/{student_id}/marks", response_model=MarksResponse)
def add_marks(student_id: int, marks: MarksBase, db: Session = Depends(get_db)):
    if not db.query(StudentData).filter(StudentData.id == student_id).first():
        raise HTTPException(404, "Student not found")
    m = StudentMarks(student_id=student_id, **marks.model_dump())
    db.add(m)
    db.commit()
    db.refresh(m)
    return m

@app.get("/student/{student_id}", response_model=ResponseModel)
def get_student(student_id: int, db: Session = Depends(get_db)):
    s = db.query(StudentData).filter(StudentData.id == student_id).first()
    if not s:
        raise HTTPException(404, "Student not found")
    return s

@app.get("/student/{student_id}/full")
def get_student_with_marks(student_id: int, db: Session = Depends(get_db)):
    s = db.query(StudentData).filter(StudentData.id == student_id).first()
    m = db.query(StudentMarks).filter(StudentMarks.student_id == student_id).first()
    if not s:
        raise HTTPException(404, "Student not found")
    return {"student": s, "marks": m}

@app.delete("/student/{student_id}")
def delete_student(student_id: int, db: Session = Depends(get_db)):
    s = db.query(StudentData).filter(StudentData.id == student_id).first()
    if not s:
        raise HTTPException(404, "Student not found")
    db.delete(s)
    db.commit()
    return {"message": "Student deleted"}

@app.delete("/student/{student_id}/marks")
def delete_marks(student_id: int, db: Session = Depends(get_db)):
    m = db.query(StudentMarks).filter(StudentMarks.student_id == student_id).first()
    if not m:
        raise HTTPException(404, "Marks not found")
    db.delete(m)
    db.commit()
    return {"message": "Marks deleted"}
