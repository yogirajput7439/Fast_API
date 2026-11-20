from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def home():
    return {
        "message": "Welcome to FastAPI",
        "developer": "Python Developer"
    }

@app.get("/about")
def about():
    return {
        "name": "FastAPI",
        "framework": "Python"
    }

# All the methods used in FastAPI

@app.get("/students")
def get_students():
    return {"message": "Get students"}

@app.post("/students")
def create_student():
    return {"message": "Student created"}

@app.put("/students/{student_id}")
def update_student(student_id: int):
    return {"message": f"Student {student_id} updated"}

@app.delete("/students/{student_id}")
def delete_student(student_id: int):
    return {"message": f"Student {student_id} deleted"}

# Data Validation using Pydantic

from fastapi import FastAPI
from pydantic import BaseModel, Field

app = FastAPI()

class Student(BaseModel):
    name: str = Field(min_lenght = 1, max_length = 30) # for the limit of the name, email, and all input
    age: int = Field(gt =0, lt=100)
    email: str 
    course: str

@app.post("/students")
def create_student(student: Student):

    return {
        "message": "Student created successfully",
        "data": student
    }