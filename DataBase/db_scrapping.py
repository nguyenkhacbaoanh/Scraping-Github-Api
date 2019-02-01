from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import os
path_dir = os.path.dirname(os.path.abspath(__file__))
base_dir = os.path.dirname(path_dir)
# print(base_dir)
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///'+base_dir+'/database.db'
db = SQLAlchemy(app)

# import module interne
from ScrappingGithub.scrapping import AutoScrapping


class Githuber(db.Model):
    # __tablename__ = "Users"
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    useracc = db.Column(db.String(80), unique=False, nullable=False)
    username = db.Column(db.String(80), unique=False, nullable=True)
    bio = db.Column(db.String(120), unique=False, nullable=True)
    location = db.Column(db.String(80), unique=False, nullable=True)
    # repos = db.relationship('Repository', backref='githuber', lazy=True)
    # stars = db.relationship('Star', backref='githuber', lazy=True)
    # followers = db.relationship('Follower', backref='githuber', lazy=True)
    # followings = db.relationship('Following', backref='githuber', lazy=True)
    # def __repr__(self):
    #     return '<User %r>' % self.useracc

class Repository(db.Model):
    # __tablename__ = "Repositories"
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    repo = db.Column(db.String(80), nullable=True)
    used_lang = db.Column(db.String(10), nullable=True)
    user_acc = db.Column(db.String(80), nullable=False)


class Star(db.Model):
    # __tablename__ = "Stars"
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    repo_starred = db.Column(db.String(80), nullable=True)
    used_lang_starred = db.Column(db.String(10), nullable=True)
    user_acc = db.Column(db.String(80), nullable=False)

class Follower(db.Model):
    # __tablename__ = "Followers"
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    followers_acc = db.Column(db.String(80), unique=False, nullable=False)
    followers_name = db.Column(db.String(80), unique=False, nullable=True)
    followers_bio = db.Column(db.String(120), unique=False, nullable=True)
    followers_location = db.Column(db.String(80), unique=False, nullable=True)
    user_acc = db.Column(db.String(80), nullable=False)

class Following(db.Model):
    # __tablename__ = "Followings"
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    following_acc = db.Column(db.String(80), unique=False, nullable=False)
    following_name = db.Column(db.String(80), unique=False, nullable=True)
    following_bio = db.Column(db.String(120), unique=False, nullable=True)
    following_location = db.Column(db.String(80), unique=False, nullable=True)
    user_acc = db.Column(db.String(80), nullable=False)

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
    # db.create_all()

    # insert in database

    # infoPerson
    someone = Githuber(useracc=useracc, username=username, bio=bio, location=location)
    db.session.add(someone)
    print("info done")
    # repo
    for i in range(len(repo)):
        repo_someone = Repository(repo=repo[i], used_lang=used_lang[i],user_acc=useracc)
        db.session.add(repo_someone)
    print("repo done")
    # star
    for i in range(len(repo_starred)):
        repo_starred_ = Star(repo_starred=repo_starred[i], used_lang_starred=used_lang_starred[i],user_acc=useracc)
        db.session.add(repo_starred_)
    print("star done")
    # follower
    for i in range(len(followers_acc)):
        follower_ = Follower(followers_name=followers_name[i], followers_acc=followers_acc[i], followers_bio=followers_bio[i], followers_location=followers_location[i],user_acc=useracc)
        db.session.add(follower_)
    print("follower done")
    # following
    for i in range(len(following_acc)):
        following_ = Following(following_name=following_name[i], following_acc=following_acc[i], following_bio=following_bio[i], following_location=following_location[i],user_acc=useracc)
        db.session.add(following_)
    print("following done")
    db.session.commit()

if __name__ == "__main__":
    # url scrapped
    url = "https://github.com/supig"
    insert_data(url)
    