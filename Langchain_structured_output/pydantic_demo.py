from pydantic import BaseModel, EmailStr, Field
from typing import Optional
class Student(BaseModel):
    name: str = 'Binod'
    age: Optional[int] = None
    email: EmailStr
    cgpa: float = Field(gt=0,lt=10, description="A decimal value")
new_student = {'age':32, 'email': 'abc@gmail.com', 'cgpa': 6}
student = Student(**new_student)
student_dict = dict(student)

student_json = student.model_dump_json()
print(student_json)