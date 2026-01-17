from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from .api.v1.endpoints import auth,users,students
from .db.base import Base, engine


app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins = ["*"],
    allow_credentials=True,
    allow_headers=["*"],
    allow_methods=["*"]
)

Base.metadata.create_all(bind=engine)



app.include_router(auth.router)
app.include_router(users.router)
app.include_router(students.router)