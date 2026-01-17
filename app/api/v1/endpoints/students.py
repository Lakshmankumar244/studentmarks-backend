from fastapi import APIRouter, Depends
from typing import Annotated
from starlette import status
from ...deps import get_db
from .auth import get_current_active_user
from app.models.user import StudentData
from app.schemas.user import CreateStudentRequest


router = APIRouter(
    tags=['students']
)


@router.post('/createStudent', status_code=status.HTTP_201_CREATED)
async def createStudent(db: get_db, create_student_request: CreateStudentRequest):
    create_student_model = StudentData(
        studentID = create_student_request.studentID,
        studentFirstName = create_student_request.studentFirstName,
        studentLastName = create_student_request.studentLastName,
        mobile = create_student_request.mobile,
        email = create_student_request.email,
        department = create_student_request.department,
        section = create_student_request.section
    )
    db.add(create_student_model)
    db.commit()

@router.get('/students', status_code=status.HTTP_200_OK)
async def getStudents(db:get_db, user: Annotated[dict, Depends(get_current_active_user)]):
    if user:
        students = db.query(StudentData).all()
        return students
    

