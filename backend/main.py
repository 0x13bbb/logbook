import asyncio
from fastapi import FastAPI, HTTPException
from db import db
from pydantic import BaseModel, validator

app = FastAPI()

@app.on_event("startup")
def startup():
    db.init_db()
    
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
        return v.strip().lower()

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

class NameQuery(BaseModel):
    name: str
    
    @validator('name')
    def validate_name(cls, v):
        if not v.strip():
            raise ValueError('Name cannot be empty')
        return v.strip().lower() 

@app.get("/mood/{name}")
def get_mood(name: str):
    query = NameQuery(name=name)
    
    moods = db.get_mood(query.name)
    if moods is None:
        raise HTTPException(
            status_code=404,
            detail=f"No mood entries found for name: {name}"
        )
    return moods

class HabitCreate(BaseModel):
    name: str
    completed: str

    @validator('completed')
    def validate_completed(cls, v):
        if v not in ["yes", "no", "unable"]:
            raise ValueError('Completed must be yes, no or unable.')
        return v

    @validator('name')
    def validate_name(cls, v):
        if not v.strip():
            raise ValueError('Name cannot be empty')
        return v.strip().lower()

@app.post("/habits")
def insert_habit(habit: HabitCreate):
    created_habit = db.insert_habit(habit.name, habit.completed)
    if not created_habit:
        raise HTTPException(
            status_code=500,
            detail="Failed to create habit entry"
        )

    return {
        "id": created_habit["id"],
        "name": created_habit["name"],
        "completed": created_habit["completed"],
        "time": created_habit["time"]
    }

@app.get("/habits/{name}")
def get_habits(name: str):
    query = NameQuery(name=name)
    
    habits = db.get_habits(query.name)
    if habits is None:
        raise HTTPException(
            status_code=404,
            detail=f"No habit entries found for name: {name}"
        )
    return habits

class MilestoneCreate(BaseModel):
    habit_name: str 
    streak_target: int
    reward: str

    @validator('habit_name')
    def validate_habit_name(cls, v):
        if not v.strip():
            raise ValueError('Habit name cannot be empty')
        return v.strip().lower()

    @validator('streak_target')
    def validate_streak_target(cls, v):
        if v < 1:
            raise ValueError('Streak target must be at least 1')
        return v

    @validator('reward')
    def validate_reward(cls, v):
        if not v.strip():
            raise ValueError('Reward cannot be empty')
        return v.strip()

@app.post("/milestones")
def insert_milestone(milestone: MilestoneCreate):
    created_milestone = db.insert_milestone(
        milestone.habit_name,
        milestone.streak_target,
        milestone.reward
    )
    if not created_milestone:
        raise HTTPException(
            status_code=500, 
            detail="Failed to create milestone"
        )

    return {
        "id": created_milestone["id"],
        "habit_name": created_milestone["habit_name"],
        "streak_target": created_milestone["streak_target"],
        "reward": created_milestone["reward"]
    }

@app.get("/milestones/{habit_name}")
def get_milestones(habit_name: str):
    query = NameQuery(name=habit_name)
    
    milestones = db.get_milestones(query.name)
    if milestones is None:
        raise HTTPException(
            status_code=404,
            detail=f"No milestones found for habit: {habit_name}"
        )
    return milestones