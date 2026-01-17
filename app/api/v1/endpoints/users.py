from fastapi import APIRouter, Depends
from starlette import status
from app.schemas.user import CreateUserRequest
from passlib.context import CryptContext
from typing import Annotated
from ...deps import get_db
from .auth import get_current_active_user
from app.models.user import User

# from pydantic import 

router = APIRouter(
    tags= ['users']
)

bcrypt_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

@router.post('/createUser', status_code=status.HTTP_201_CREATED)
async def create_user(db:get_db, create_user_request: CreateUserRequest):
    create_user_model = User(
        username = create_user_request.username,
        password = bcrypt_context.hash(create_user_request.password),
        isStudent = create_user_request.isStudent,
        isActive = True
    )
    db.add(create_user_model)
    db.commit()

@router.get('/users')
async def GetUsers(db: get_db, user: Annotated[dict, Depends(get_current_active_user)]):
    
    if user:
        users = db.query(User).all()
        return users


    

    
