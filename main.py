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