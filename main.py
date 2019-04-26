from fastapi import Depends, FastAPI
from sqlalchemy import create_engine
from sqlalchemy.orm import Session, sessionmaker
from starlette.requests import Request
from starlette.responses import Response
from DataBase.db_scrapping import Githuber, Repository, Star, Follower, Following, insert_data

from DataBase.db_scrapping import insert_data


SQLALCHEMY_DATABASE_URI = 'sqlite:///databases.db'

engine = create_engine(
    SQLALCHEMY_DATABASE_URI, connect_args={"check_same_thread": False}
)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# db_session = SessionLocal()

# Utility
def get_user(db_session: Session, user_acc: str):
    return db_session.query(Githuber).filter(Githuber.useracc == user_acc).first()


# Dependency
def get_db(request: Request):
    return request.state.db


# FastAPI specific code
app = FastAPI()


@app.get("/githubers/{user_acc}")
def read_user(user_acc: str, db: Session = Depends(get_db)):
    user = get_user(db, user_acc=user_acc)
    return user

@app.post("/githubers/{user_acc}")
def create_user(user_acc: str):
    url = "https://github.com/" + user_acc
    insert_data(url)

@app.middleware("http")
async def db_session_middleware(request: Request, call_next):
    response = Response("Internal server error", status_code=500)
    try:
        request.state.db = SessionLocal()
        response = await call_next(request)
    finally:
        request.state.db.close()
    return response