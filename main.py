from fastapi import Depends, FastAPI
from sqlalchemy import create_engine
from sqlalchemy.orm import Session, sessionmaker
from starlette.requests import Request
from starlette.responses import Response
from DataBase.db_scrapping import Githuber, Repository, Star, Follower, Following, insert_data

from DataBase.db_scrapping import insert_data

import json

SQLALCHEMY_DATABASE_URI = 'sqlite:///databases.db'

engine = create_engine(
    SQLALCHEMY_DATABASE_URI, connect_args={"check_same_thread": False}
)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# db_session = SessionLocal()

# Utility
def get_user(db_session: Session, user_acc: str):
    user = db_session.query(Githuber).filter(Githuber.useracc == user_acc).first()
    repository = db_session.query(Repository).filter(Repository.useracc_id == user_acc).all()
    stars = db_session.query(Star).filter(Star.useracc_id == user_acc).all()
    followers = db_session.query(Follower).filter(Follower.useracc_id == user_acc).all()
    followings = db_session.query(Following).filter(Following.useracc_id == user_acc).all()
    obj = {
        "githuber": user,
        "repository": repository,
        "stars": stars,
        "followers": followers,
        "followings": followings,
    }
    return obj
def get_repo(db_session: Session, user_acc: str):
    return db_session.query(Repository).filter(Repository.useracc_id == user_acc).all()


# Dependency
def get_db(request: Request):
    return request.state.db


# FastAPI specific code
app = FastAPI()

@app.get("/githubers/{user_acc}")
def read_user(user_acc: str, db: Session = Depends(get_db)):
    user = get_user(db, user_acc=user_acc)
    return user
@app.get("/repository/{user_acc}")
def read_repository(user_acc: str, db: Session = Depends(get_db)):
    repo = get_repo(db, user_acc=user_acc)
    return repo

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

# from typing import List, Set

# from fastapi import FastAPI
# from pydantic import BaseModel, UrlStr

# app = FastAPI()


# class Repository(BaseModel):
#     repo : str
#     used_lang : str
#     user_acc : str
# class Star(BaseModel):
#     repo_starred : str
#     used_lang_starred : str
#     user_acc : str
# class Follower(BaseModel):
#     useracc : str
#     username : str
#     bio : str
#     location : str
# class Following(BaseModel):
#     useracc : str
#     username : str
#     bio : str
#     location : str


# class Githuber(BaseModel):
#     # name: str
#     # description: str = None
#     # price: float
#     # tax: float = None
#     # tags: Set[str] = []
#     # images: List[Image] = None
#     useracc : str
#     username : str
#     bio : str
#     location : str
#     repository : List[Repository] = None
#     star : List[Star] = None
#     follower : List[Follower] = None
#     following : List[Following] = None


# @app.put("/items/{item_id}")
# async def update_item(*, item_id: int, item: Item):
#     results = {"item_id": item_id, "item": item}
#     return results