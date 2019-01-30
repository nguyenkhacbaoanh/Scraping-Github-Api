from flask import Flask, render_template, request
from flask_restful import Api, Resource
from flask_sqlalchemy import SQLAlchemy
import os
path_dir = os.path.dirname(os.path.abspath(__file__))
# base_dir = os.path.dirname(path_dir)
# print(base_dir)
# import module interne
from ScrappingGithub.scrapping import AutoScrapping
from DataBase.db_scrapping import *

# insert database
def database_launch(url):
    # url scrapped
    # url = "https://github.com/supig"
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
    db.create_all()

    # insert in database

    # infoPerson
    someone = Githuber(useracc=useracc, username=username, bio=bio, location=location)
    db.session.add(someone)
    print("info done")
    # repo
    for i in range(len(repo)):
        repo_someone = Repository(repo=repo[i], used_lang=used_lang[i])
        db.session.add(repo_someone)
    print("repo done")
    # star
    for i in range(len(repo_starred)):
        repo_starred_ = Star(repo_starred=repo_starred[i], used_lang_starred=used_lang_starred[i])
        db.session.add(repo_starred_)
    print("star done")
    # follower
    for i in range(len(followers_acc)):
        follower_ = Follower(followers_name=followers_name[i], followers_acc=followers_acc[i], followers_bio=followers_bio[i], followers_location=followers_location[i])
        db.session.add(follower_)
    print("follower done")
    # following
    for i in range(len(following_acc)):
        following_ = Following(following_name=following_name[i], following_acc=following_acc[i], following_bio=following_bio[i], following_location=following_location[i])
        db.session.add(following_)
    print("following done")
    db.session.commit()

def database_fetch():
    db_connect = create_engine('sqlite:///database.db')

class GitUser(Resource):
    def get(self):
        conn = db_connect.connect()
        query1 =  conn.execute("select * from User")
        query2 = conn.execute("select * from Repositories")
        # query3 = conn.execute("select * from Stars")
        # query4 = conn.execute("select * from Followers")
        # query5 = conn.execute("select * from Followings")
        return {'Githuber': query1.cursor.fetchall()[0], 'Repository': query2.cursor.fetchall()}

class App:
    app = Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///'+path_dir+'/database.db'
    db = SQLAlchemy(app)

    @app.route("/")
    def home():
        return render_template("home.html")
    @app.route("/api")
    def 
