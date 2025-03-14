from task_model import Task
from fastapi import FastAPI 

app = FastAPI()

tasks = [
    Task(),
    Task()
]

@app.get("/")
def nam ():
    return "Hello World"

@app.get("/get-tasks")
def get_all_tasks():
    return tasks

