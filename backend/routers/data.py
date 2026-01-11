# Backend/routers/data.py

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from database import SessionLocal
from models.data import Class, Section, Student
from schemas.data import (
    ClassOut,
    SectionOut,
    StudentCreate,
    StudentOut,
)
from dependencies.auth import get_current_user

router = APIRouter(prefix="/data", tags=["Data"])


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


# -------- Classes --------
@router.get("/classes", response_model=list[ClassOut])
def get_classes(
    db: Session = Depends(get_db),
    _: str = Depends(get_current_user),
):
    return db.query(Class).all()


# -------- Sections --------
@router.get("/sections/{class_id}", response_model=list[SectionOut])
def get_sections(
    class_id: str,
    db: Session = Depends(get_db),
    _: str = Depends(get_current_user),
):
    return db.query(Section).filter(Section.class_id == class_id).all()


# -------- Students --------
@router.post("/students", response_model=StudentOut)
def create_student(
    student: StudentCreate,
    db: Session = Depends(get_db),
    _: str = Depends(get_current_user),
):
    exists = (
        db.query(Student)
        .filter(
            Student.section_id == student.section_id,
            Student.roll_number == student.roll_number,
        )
        .first()
    )
    if exists:
        raise HTTPException(400, "Roll number already exists")

    new_student = Student(**student.dict())
    db.add(new_student)
    db.commit()
    db.refresh(new_student)
    return new_student


@router.get("/students/{section_id}", response_model=list[StudentOut])
def get_students(
    section_id: str,
    db: Session = Depends(get_db),
    _: str = Depends(get_current_user),
):
    return db.query(Student).filter(Student.section_id == section_id).all()


@router.delete("/students/{student_id}")
def delete_student(
    student_id: str,
    db: Session = Depends(get_db),
    _: str = Depends(get_current_user),
):
    student = db.query(Student).filter(Student.id == student_id).first()
    if not student:
        raise HTTPException(404, "Student not found")

    db.delete(student)
    db.commit()
    return {"message": "Student deleted"}
