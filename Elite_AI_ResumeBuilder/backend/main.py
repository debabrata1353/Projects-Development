from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from api import users
from db.session import engine, Base

# Create DB Tables
Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="Elite AI Resume Builder & Job Tracker API",
    description="Backend API for parsing CVs, searching jobs, and generating resumes using Local OSS LLM",
    version="1.0.0"
)

# Allow React Native frontend to communicate with API
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Include Routers
app.include_router(users.router, prefix="/api/users", tags=["Users"])

@app.get("/")
def read_root():
    return {"message": "Welcome to Elite AI Backend API"}
