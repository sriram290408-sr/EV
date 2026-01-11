from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from database import SessionLocal
from models.marks import Mark
from schemas.marks import MarkCreate, MarkOut
from dependencies.auth import get_current_user

router = APIRouter(prefix="/marks", tags=["Marks"])


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@router.post("/", response_model=MarkOut)
def add_mark(
    mark: MarkCreate,
    db: Session = Depends(get_db),
    _: str = Depends(get_current_user),
):
    new_mark = Mark(**mark.dict())
    db.add(new_mark)
    db.commit()
    db.refresh(new_mark)
    return new_mark


@router.get("/{student_id}", response_model=list[MarkOut])
def get_marks(
    student_id: str,
    db: Session = Depends(get_db),
    _: str = Depends(get_current_user),
):
    return db.query(Mark).filter(Mark.student_id == student_id).all()


@router.delete("/{mark_id}")
def delete_mark(
    mark_id: str,
    db: Session = Depends(get_db),
    _: str = Depends(get_current_user),
):
    mark = db.query(Mark).filter(Mark.id == mark_id).first()
    if not mark:
        raise HTTPException(404, "Mark not found")

    db.delete(mark)
    db.commit()
    return {"message": "Mark deleted"}
