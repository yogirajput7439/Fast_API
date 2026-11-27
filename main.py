# from fastapi import FastAPI

# app = FastAPI()

# @app.get("/")
# def home():
#     return {
#         "message": "Welcome to FastAPI",
#         "developer": "Python Developer"
#     }

# @app.get("/about")
# def about():
#     return {
#         "name": "FastAPI",
#         "framework": "Python"
#     }

# # All the methods used in FastAPI

# @app.get("/students")
# def get_students():
#     return {"message": "Get students"}

# @app.post("/students")
# def create_student():
#     return {"message": "Student created"}

# @app.put("/students/{student_id}")
# def update_student(student_id: int):
#     return {"message": f"Student {student_id} updated"}

# @app.delete("/students/{student_id}")
# def delete_student(student_id: int):
#     return {"message": f"Student {student_id} deleted"}

# # Data Validation using Pydantic

# from fastapi import FastAPI, status
# from pydantic import BaseModel, Field

# app = FastAPI()

# # class Student(BaseModel):
# #     name: str = Field(min_lenght = 1, max_length = 30) # for the limit of the name, email, and all input
# #     age: int = Field(gt =0, lt=100)
# #     email: str 
# #     course: str

# # class Student(BaseModel):
# #     name : str = Field(min_lenght= 1, max_length = 40)
# #     age : int  = Field(gt =17, lt = 60)
# #     email : str
# #     course : str 
# #     city : str

# # @app.post("/students", status_code = status.HTTP_201_CREATED)
# # def create_student(student: Student):

# #     return {
# #         "message": "Student created successfully",
# #         "data": student
# #     }



# from fastapi import Depends
# from database import engine, SessionLocal, Base

# import models

# app = FastAPI()

# Base.metadata.create_all(bind = engine)

# def get_db():
#     db = SessionLocal()

#     try:
#         yield db
#     finally:
#         db.close()


# from schemas import StudentCreate, StudentResponse
# from sqlalchemy.orm import Session

# @app.post("/students", response_model=StudentResponse, status_code=201)
# def create_student(
#     student: StudentCreate,
#     db: Session = Depends(get_db)
# ):
#     new_student = models.Student(**student.model_dump())

#     db.add(new_student)
#     db.commit()
#     db.refresh(new_student)

#     return new_student

# @app.get("/students", response_model=list[StudentResponse])
# def get_students(db: Session = Depends(get_db)):

#     students = db.query(models.Student).all()

#     return students

from fastapi import FastAPI, Depends, HTTPException, status
from sqlalchemy.orm import Session
from sqlalchemy.exc import IntegrityError

from database import Base, engine, get_db
import models, schemas
from security import hash_password

app = FastAPI(title="JobSeeker API", version="1.0.0")

Base.metadata.create_all(bind=engine)


@app.get("/")
def home():
    return {"message": "JobSeeker API Running"}


@app.post("/register", status_code=status.HTTP_201_CREATED)
def register_user(
    user: schemas.UserCreate,
    db: Session = Depends(get_db)
):
    existing_user = db.query(models.User).filter(
        models.User.email == user.email
    ).first()

    if existing_user:
        raise HTTPException(
            status_code=status.HTTP_409_CONFLICT,
            detail="Email already registered"
        )

    hashed_password = hash_password(user.password)

    new_user = models.User(
        name=user.name,
        email=user.email,
        password=hashed_password,
        role="job_seeker"
    )

    try:
        db.add(new_user)
        db.commit()
        db.refresh(new_user)

    except IntegrityError:
        db.rollback()
        raise HTTPException(
            status_code=status.HTTP_409_CONFLICT,
            detail="Email already registered"
        )

    return {
        "message": "User registered successfully",
        "user_id": new_user.id,
        "name": new_user.name,
        "email": new_user.email,
        "role": new_user.role
    }

from models import User

@app.get("/user/{user_id}")
def get_user(user_id : int, db : Session = Depends(get_db)):

    user = db.query(User).filter(User.id == user_id).first()

    if user is None:
        raise HTTPException(
            status_code = 404,
            detail = "User Not Found"
        )

    return user