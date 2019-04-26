# from flask import Flask
# from flask_sqlalchemy import SQLAlchemy
import os
path_dir = os.path.dirname(os.path.abspath(__file__))
base_dir = os.path.dirname(path_dir)
SQLALCHEMY_DATABASE_URI = 'sqlite:///'+base_dir+'/databases.db'
# # print(base_dir)
# app = Flask(__name__)
# app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///'+base_dir+'/database.db'
# db = SQLAlchemy(app)

from sqlalchemy import Boolean, Column, Integer, String, create_engine
from sqlalchemy.ext.declarative import declarative_base, declared_attr
from sqlalchemy.orm import sessionmaker

# import module interne
from ScrappingGithub.scrapping import AutoScrapping

engine = create_engine(
    SQLALCHEMY_DATABASE_URI, connect_args={"check_same_thread": False}
)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)


class CustomBase:
    # Generate __tablename__ automatically
    @declared_attr
    def __tablename__(cls):
        return cls.__name__.lower()


Base = declarative_base(cls=CustomBase)

class Githuber(Base):
    # __tablename__ = "Users"
    id = Column(Integer, primary_key=True, autoincrement=True)
    useracc = Column(String(80), unique=False, nullable=False)
    username = Column(String(80), unique=False, nullable=True)
    bio = Column(String(120), unique=False, nullable=True)
    location = Column(String(80), unique=False, nullable=True)
    # repos = relationship('Repository', backref='githuber', lazy=True)
    # stars = relationship('Star', backref='githuber', lazy=True)
    # followers = relationship('Follower', backref='githuber', lazy=True)
    # followings = relationship('Following', backref='githuber', lazy=True)
    # def __repr__(self):
    #     return '<User %r>' % self.useracc

class Repository(Base):
    # __tablename__ = "Repositories"
    id = Column(Integer, primary_key=True, autoincrement=True)
    repo = Column(String(80), nullable=True)
    used_lang = Column(String(10), nullable=True)
    user_acc = Column(String(80), nullable=False)


class Star(Base):
    # __tablename__ = "Stars"
    id = Column(Integer, primary_key=True, autoincrement=True)
    repo_starred = Column(String(80), nullable=True)
    used_lang_starred = Column(String(10), nullable=True)
    user_acc = Column(String(80), nullable=False)

class Follower(Base):
    # __tablename__ = "Followers"
    id = Column(Integer, primary_key=True, autoincrement=True)
    followers_acc = Column(String(80), unique=False, nullable=False)
    followers_name = Column(String(80), unique=False, nullable=True)
    followers_bio = Column(String(120), unique=False, nullable=True)
    followers_location = Column(String(80), unique=False, nullable=True)
    user_acc = Column(String(80), nullable=False)

class Following(Base):
    # __tablename__ = "Followings"
    id = Column(Integer, primary_key=True, autoincrement=True)
    following_acc = Column(String(80), unique=False, nullable=False)
    following_name = Column(String(80), unique=False, nullable=True)
    following_bio = Column(String(120), unique=False, nullable=True)
    following_location = Column(String(80), unique=False, nullable=True)
    user_acc = Column(String(80), nullable=False)

def insert_data(url):
    # instancie
    cp = AutoScrapping(url)

    # scrapping
    useracc, username, bio, location = cp.infoPerso()
    # ---
    repo, used_lang = cp.repoScrapping()
    # ---
    repo_starred, used_lang_starred = cp.starScrapping()
    # ---
    followers_name, followers_acc, followers_bio, followers_location = cp.followerScrapping()
    # ---
    following_name, following_acc, following_bio, following_location =  cp.followingScrapping()

    # create database
    # create_all()

    Base.metadata.create_all(bind=engine)

    db_session = SessionLocal()

    # insert in database

    # infoPerson
    someone = Githuber(useracc=useracc, username=username, bio=bio, location=location)
    db_session.add(someone)
    db_session.commit()
    print("info done")
    # repo
    for i in range(len(repo)):
        repo_someone = Repository(repo=repo[i], used_lang=used_lang[i],user_acc=useracc)
        db_session.add(repo_someone)
        db_session.commit()
    print("repo done")
    # star
    for i in range(len(repo_starred)):
        repo_starred_ = Star(repo_starred=repo_starred[i], used_lang_starred=used_lang_starred[i],user_acc=useracc)
        db_session.add(repo_starred_)
        db_session.commit()
    print("star done")
    # follower
    for i in range(len(followers_acc)):
        follower_ = Follower(followers_name=followers_name[i], followers_acc=followers_acc[i], followers_bio=followers_bio[i], followers_location=followers_location[i],user_acc=useracc)
        db_session.add(follower_)
        db_session.commit()
    print("follower done")
    # following
    for i in range(len(following_acc)):
        following_ = Following(following_name=following_name[i], following_acc=following_acc[i], following_bio=following_bio[i], following_location=following_location[i],user_acc=useracc)
        db_session.add(following_)
        db_session.commit()
    print("following done")
    # session.commit()
    db_session.close()

if __name__ == "__main__":
    # url scrapped
    url = "https://github.com/nguyenkhacbaoanh"
    insert_data(url)
    