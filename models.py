from pydantic import BaseModel, EmailStr
from typing import Optional

class Student(BaseModel):
    id: int
    name: str
    age: int
    course: str
    email: Optional[EmailStr] = None

class professor(BaseModel):
    p_id: int
    name: str
    experience: int
    subject: str
    email: Optional[EmailStr] = None

class Feedback(BaseModel):
    text: str