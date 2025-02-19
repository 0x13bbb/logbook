import asyncio
from fastapi import FastAPI
from db import db
from pydantic import BaseModel, validator

app = FastAPI()

@app.on_event("startup")
def startup():
    db.init_db()

@app.get("/")
def read_root():
    return {"Hello": "World"}
    
class MoodCreate(BaseModel):
    name: str
    score: int

    @validator('score')
    def validate_score(cls, v):
        if not 1 <= v <= 5:
            raise ValueError('Score must be between 1 and 5')
        return v

    @validator('name')
    def validate_name(cls, v):
        if not v.strip():
            raise ValueError('Name cannot be empty')
        return v.strip()

@app.post("/mood")
def insert_mood(mood: MoodCreate):
    created_mood = db.insert_mood(mood.name, mood.score)
    if not created_mood:
        raise HTTPException(
            status_code=500,
            detail="Failed to create mood entry"
        )
    return {
        "id": created_mood["id"],
        "name": created_mood["name"],
        "score": created_mood["score"],
        "time": created_mood["time"]
    }