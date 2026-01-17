from app.db.base import Base
from sqlalchemy import Column, Integer, String, Boolean, ForeignKey, JSON, Float

class StudentData(Base):
    __tablename__ = "StudentData"

    studentID = Column(Integer, primary_key=True)
    studentFirstName = Column(String, nullable=False)
    studentLastName = Column(String, nullable=False)
    gender = Column(String, nullable=False)
    mobile = Column(String, nullable=False,unique=True)
    email = Column(String, nullable=False,unique=True)
    department = Column(String, nullable=False)
    section = Column(String, nullable=False)

class FacultyData(Base):
    __tablename__ = 'FacultyData'

    facultyId = Column(Integer,primary_key=True)
    facultyFirstName = Column(String, nullable=False)
    facultyLastName = Column(String, nullable=False)
    mobile = Column(String, nullable=False, unique=True)
    email = Column(String, nullable=False, unique=True)
    department = Column(JSON, nullable=False)
    section = Column(JSON, nullable=False)
    subjectName = Column(String, nullable=False)
    subjectCode = Column(String, nullable=False)

class CourseStructure(Base):
    __tablename__ = 'CourseStructure'

    SNo = Column(Integer, primary_key=True)
    courseCode = Column(String(20), nullable=False, unique=True)
    subject = Column(String(255), nullable=False)
    credits = Column(Float, nullable=False)
    year = Column(String(10), nullable=False)       # e.g., "I"
    semester = Column(String(10), nullable=False)

class User(Base):
    __tablename__ = 'User'

    SNo = Column(Integer, primary_key=True)
    username = Column(String, nullable=False)
    password = Column(String, nullable=False)
    isActive = Column(Boolean, nullable=False, default=True)
    isStudent = Column(Boolean, nullable=False)
