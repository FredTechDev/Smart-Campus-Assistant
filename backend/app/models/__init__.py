"""Models package"""

from app.models.db_models import Student, Course, Attendance, ChatMessage
from app.models.schemas import StudentSchema, CourseSchema

__all__ = [
    "Student",
    "Course",
    "Attendance",
    "ChatMessage",
    "StudentSchema",
    "CourseSchema",
]
