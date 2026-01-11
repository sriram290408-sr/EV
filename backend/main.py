from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from dotenv import load_dotenv

from routers import users, data, marks, attendance, login_logs

load_dotenv()

app = FastAPI(title="EduVerse API")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(users.router)
app.include_router(data.router)
app.include_router(marks.router)
app.include_router(attendance.router)
app.include_router(login_logs.router)

@app.get("/health")
def health():
    return {"status": "ok"}
