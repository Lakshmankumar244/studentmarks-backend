from fastapi import APIRouter, HTTPException, Depends
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from jose import jwt, JWTError
from datetime import timedelta,timezone,datetime
from typing import Annotated

from app.schemas.user import CreateUserRequest,Token
from app.models.user import User
from passlib.context import CryptContext 
from starlette import status
from ...deps import get_db


router = APIRouter(
    prefix='/auth'
)


SECRET_KEY = "08s4wu098047384l3kh62l3j62gkj234g2jh3gj"
ALGORITHM = "HS256"

# db_dependency = Annotated[session, Depends(get_db_session)]
bcrypt_context = CryptContext(schemes=['bcrypt'],deprecated='auto')

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/auth/token")




def verify_password(password: str,hashed_password: str):
    return bcrypt_context.verify(password,hashed_password)

def authenticate_user(username: str, password: str, db: get_db):
    user = db.query(User).filter(User.username == username).first()
    if not user:
        return False
    if not verify_password(password, user.password):
        return False
    return user

def create_access_token(username: str, sno: str, expires_delta: timedelta):
    encode = {'sub':username,'id':sno}
    expires = datetime.now(timezone.utc) + expires_delta
    encode.update({'exp': expires})
    return jwt.encode(encode,SECRET_KEY,algorithm=ALGORITHM)

async def get_current_user(token: Annotated[str,Depends(oauth2_scheme)]):

    try:
        payload = jwt.decode(token,SECRET_KEY,algorithms=ALGORITHM)
        username = payload.get('sub')
        sno = payload.get('id')
        if username is None or sno is None:
            raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED,
                            detail='Could not validate the user')
        return {'username': username,'sno': sno}
    except JWTError:
        raise HTTPException(status_code= status.HTTP_401_UNAUTHORIZED,
                                detail = 'could not validate user' )

def get_current_active_user(current_user: Annotated[dict, Depends(get_current_user)]):
    if current_user is None:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail='Authentication Failed')
    return current_user




@router.post("/token")
async def login_for_access_token(form_data: Annotated[OAuth2PasswordRequestForm, Depends()], db:get_db) -> Token:
    user = authenticate_user(form_data.username, form_data.password, db)
    if not user:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED,
                            detail="Could not validate the user")
    token = create_access_token(user.username, user.SNo, timedelta(minutes=20))
    return Token(access_token=token, token_type="bearer")