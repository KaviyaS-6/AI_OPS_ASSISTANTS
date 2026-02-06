from fastapi import FastAPI
from pydantic import BaseModel
from main import run_assistant

app = FastAPI(title="AI Ops Assistant")

# Request Schema
class TaskRequest(BaseModel):
    task: str


@app.get("/")
def home():
    return {"message": "AI Ops Assistant is running 🚀"}


@app.post("/run-task")
def run_task(request: TaskRequest):
    result = run_assistant(request.task)
    return {"result": result}
