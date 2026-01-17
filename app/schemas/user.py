from pydantic import BaseModel

class Token(BaseModel):
    access_token: str
    token_type: str


class CreateUserRequest(BaseModel):
    username: str
    password: str 
    isStudent: bool

class CreateStudentRequest(BaseModel):
    studentID: int
    studentFirstName: str
    studentLastName: str
    gender: str
    mobile: str
    email: str
    department: str
    section: str