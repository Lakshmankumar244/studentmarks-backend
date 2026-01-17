from app.db.base import session_local

def get_db_session():
    db = session_local()
    try:
        yield db
    finally:
        db.close()