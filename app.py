from flask import Flask, request
from sqlalchemy import create_engine
from flask_restful import Api, Resource

from flask import jsonify

db_connect = create_engine('sqlite:///database.db')
# app_ = Flask(__name__)
# api = Api(app_)

class GitUser(Resource):
    def get(self):
        conn = db_connect.connect()
        query1 =  conn.execute("select * from Githuber")
        query2 = conn.execute("select * from Repository")
        query3 = conn.execute("select * from Star")
        query4 = conn.execute("select * from Follower")
        query5 = conn.execute("select * from Following")
        return {'Githuber': query1.cursor.fetchall()[0],\
         'Repository': query2.cursor.fetchall(),\
          'Star': query3.cursor.fetchall(),\
          'Follower': query4.cursor.fetchall(),\
          'Following': query5.cursor.fetchall()}

from DataBase.db_scrapping import * 
from ScrappingGithub.scrapping import *
from API.api import *
# url scrapped
url = "https://github.com/supig"
# url = str(input("Url: "))
# instancie
cp = AutoScrapping(url)

# scrapping
useracc, username, bio, location = cp.infoPerso()
# ---
repo, used_lang = cp.repoScrapping()
# ---
repo_starred, used_lang_starred = cp.starScrapping()
# # ---
followers_name, followers_acc, followers_bio, followers_location = cp.followerScrapping()
# ---
following_name, following_acc, following_bio, following_location =  cp.followingScrapping()

# create database
db.create_all()
# api.add_resource(GitUser,'/GitUser1')
if __name__ == "__main__":
    # scrapping
    useracc, username, bio, location = cp.infoPerso()
    # ---
    repo, used_lang = cp.repoScrapping()
    # insert in database

    # infoPerson
    someone = Githuber(useracc=useracc, username=username, bio=bio, location=location)
    db.session.add(someone)

    # repo
    for i in range(len(repo)):
        repo_someone_ = Repository(repo=repo[i], used_lang=used_lang[i])
        db.session.add(repo_someone_)
    
    # # star
    for i in range(len(repo_starred)):
        repo_starred_ = Star(repo_starred=repo_starred[i], used_lang_starred=used_lang_starred[i])
        db.session.add(repo_starred_)

    # # follower
    for i in range(len(followers_acc)):
        follower_ = Follower(followers_acc=followers_acc[i], followers_name=followers_name[i], followers_bio=followers_bio[i], followers_location=followers_location[i])
        db.session.add(follower_)

    # # following
    for i in range(len(following_acc)):
        following_ = Following(following_name=following_name[i], following_acc=following_acc[i], following_bio=following_bio[i], following_location=following_location[i])
        db.session.add(following_)
    db.session.commit()
    # -------------------
    app = App().app
    api = Api(app)
    api.add_resource(GitUser,'/GitUser1')
    app.run(port=3000, debug=True)