from pydantic import BaseModel, Field, ConfigDict

class StudentCreate(BaseModel):
    name: str = Field(min_length=3)
    age: int = Field(gt=0, lt=100)
    email: str
    course: str

class StudentResponse(StudentCreate):
    id: int

    model_config = ConfigDict(from_attributes=True)