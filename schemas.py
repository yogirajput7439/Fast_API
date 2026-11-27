from pydantic import BaseModel, Field, ConfigDict

class StudentCreate(BaseModel):
    name: str = Field(min_length=3)
    age: int = Field(gt=0, lt=100)
    email: str
    course: str

class StudentResponse(StudentCreate):
    id: int

    model_config = ConfigDict(from_attributes=True)

from pydantic import BaseModel, EmailStr, Field

class UserCreate(BaseModel):

    name: str = Field(min_lenght = 1, max_length = 100)

    email : EmailStr

    password : str = Field(min_lenght = 8, max_length = 128)

    
