from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from dotenv import load_dotenv

from routers import users, data, marks, attendance, login_logs
from database import Base, engine

from models.users import User
from models.login_log import LoginLog
from models.marks import Mark
from models.attendance import Attendance

load_dotenv()

app = FastAPI(title="EduVerse API")


@app.on_event("startup")
def create_tables():
    Base.metadata.create_all(bind=engine)


app.include_router(users.router)
app.include_router(data.router)
app.include_router(marks.router)
app.include_router(attendance.router)
app.include_router(login_logs.router)


@app.get("/")
def home():
    return {"message": "Backend Running Successfully"}


@app.get("/health")
def health():
    return {"status": "ok"}
