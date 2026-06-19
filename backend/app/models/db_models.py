"""SQLAlchemy database models"""

from datetime import datetime

from sqlalchemy import Boolean, Column, DateTime, Float, Integer, String, Text

from app.db.database import Base


class Student(Base):
    """Student model"""

    __tablename__ = "students"

    id = Column(Integer, primary_key=True, index=True)
    student_id = Column(String(50), unique=True, index=True)
    first_name = Column(String(100))
    last_name = Column(String(100))
    email = Column(String(100), unique=True, index=True)
    major = Column(String(100))
    year = Column(Integer)
    gpa = Column(Float)
    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)


class Course(Base):
    """Course model"""

    __tablename__ = "courses"

    id = Column(Integer, primary_key=True, index=True)
    course_code = Column(String(50), unique=True, index=True)
    course_name = Column(String(200))
    description = Column(Text)
    credits = Column(Integer)
    instructor = Column(String(100))
    semester = Column(String(20))
    created_at = Column(DateTime, default=datetime.utcnow)


class Attendance(Base):
    """Attendance record model"""

    __tablename__ = "attendance"

    id = Column(Integer, primary_key=True, index=True)
    student_id = Column(String(50), index=True)
    course_id = Column(String(50), index=True)
    date = Column(DateTime)
    present = Column(Boolean, default=True)
    created_at = Column(DateTime, default=datetime.utcnow)


class ChatMessage(Base):
    """Chat message model"""

    __tablename__ = "chat_messages"

    id = Column(Integer, primary_key=True, index=True)
    student_id = Column(String(50), index=True)
    user_message = Column(Text)
    bot_response = Column(Text)
    created_at = Column(DateTime, default=datetime.utcnow)
