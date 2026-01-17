from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from dotenv import load_dotenv
import os

load_dotenv()

DB_URL = os.getenv("DB_URL")
connect_args = {}

if DB_URL.startswith("sqlite"):
    connect_args={"check_same_thread": False}

engine = create_engine(DB_URL,connect_args=connect_args)

session_local = sessionmaker(autocommit=False,autoflush=False,bind=engine)

Base = declarative_base()