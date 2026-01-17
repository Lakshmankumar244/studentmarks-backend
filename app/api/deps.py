from ..db.session import get_db_session
# from .v1.endpoints.auth import get_current_active_user
from typing import Annotated
from sqlalchemy.orm import session
from fastapi import Depends


get_db = Annotated[session,Depends(get_db_session)]

# get_active_user = Annotated[dict,Depends(get_current_active_user)]





