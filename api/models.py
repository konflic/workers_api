from enum import Enum
from datetime import date
from typing import Optional

from pydantic import BaseModel, validator


grades = range(1, 10 + 1)


class Department(str, Enum):
    IT = "IT"
    Accounting = "Accounting"
    Sales = "Sales"
    Management = "Management"
    Office = "Office"


class Gender(str, Enum):
    male = "male"
    female = "female"
    other = "other"


class Worker(BaseModel):
    name: str
    department: Department
    position: str
    grade: int
    birthday: date
    gender: Gender

    @validator("grade")
    def grade_range(cls, v):
        if v not in grades:
            raise ValueError("Range must be from 1 to 10")
        return v


class UpdateWorker(BaseModel):
    name: Optional[str] = None
    department: Optional[Department] = None
    position: Optional[str] = None
    grade: Optional[int] = None
    birthday: Optional[date] = None
    gender: Optional[Gender] = None

    @validator("grade")
    def grade_range(cls, v):
        if v is not None and v not in grades:
            raise ValueError("Range must be from 1 to 10")
        return v
