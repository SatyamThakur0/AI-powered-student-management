from pydantic import BaseModel, EmailStr
from typing import Optional

class Student(BaseModel):
    name: str
    age: int
    course: str
    email: Optional[EmailStr] = None

class professor(BaseModel):
    name: str
    experience: int
    subject: str
    email: Optional[EmailStr] = None

class Feedback(BaseModel):
    text: str