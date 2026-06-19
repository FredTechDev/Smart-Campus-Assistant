"""Pydantic schemas for request/response validation"""

from datetime import datetime
from typing import Optional

from pydantic import BaseModel, EmailStr


class StudentBase(BaseModel):
    """Base student schema"""

    student_id: str
    first_name: str
    last_name: str
    email: EmailStr
    major: str
    year: int
    gpa: Optional[float] = None


class StudentCreate(StudentBase):
    """Create student schema"""

    pass


class StudentUpdate(BaseModel):
    """Update student schema"""

    first_name: Optional[str] = None
    last_name: Optional[str] = None
    email: Optional[EmailStr] = None
    major: Optional[str] = None
    year: Optional[int] = None
    gpa: Optional[float] = None


class StudentSchema(StudentBase):
    """Student response schema"""

    id: int
    created_at: datetime
    updated_at: datetime

    class Config:
        from_attributes = True


class CourseBase(BaseModel):
    """Base course schema"""

    course_code: str
    course_name: str
    description: Optional[str] = None
    credits: int
    instructor: str
    semester: str


class CourseCreate(CourseBase):
    """Create course schema"""

    pass


class CourseSchema(CourseBase):
    """Course response schema"""

    id: int
    created_at: datetime

    class Config:
        from_attributes = True


class PerformancePredictionResponse(BaseModel):
    """Performance prediction response"""

    student_id: str
    predicted_gpa: float
    confidence: float
    risk_level: str  # low, medium, high
    recommendations: list[str]


class ChatMessageCreate(BaseModel):
    """Create chat message schema"""

    student_id: str
    message: str


class ChatMessageResponse(BaseModel):
    """Chat message response schema"""

    id: int
    student_id: str
    user_message: str
    bot_response: str
    created_at: datetime

    class Config:
        from_attributes = True
