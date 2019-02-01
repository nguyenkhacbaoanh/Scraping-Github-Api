from flask import Flask, request
from sqlalchemy import create_engine
from flask_restful import Api, Resource
# from sqlalchemy import create_engine
# from sqlalchemy import MetaData
# from sqlalchemy import Table
# from sqlalchemy import Column
# from sqlalchemy import Integer
# from sqlalchemy import String
# from sqlalchemy import select
import sqlite3

db_connect = create_engine('sqlite:///database.db')
# engine = create_engine('sqlite:///database.db')
# meta = MetaData(engine, reflect=True)
# app_ = Flask(__name__)
# api = Api(app_)
test = {}
class GitUser(Resource):
    def get(self, nameacc):
        conn = sqlite3.connect("database.db")
        c = conn.cursor()
        # githuber = meta.tables['githuber']
        # repo = meta.tables['repository']
        # star = meta.tables['star']
        # follower = meta.tables['follower']
        # following = meta.tables['following']
        if nameacc == "all":
            query1 =  c.execute(f"select distinct * from Githuber")
            # query2 = c.execute("select * from Repository")
            # query3 = c.execute("select * from Star")
            # query4 = c.execute("select * from Follower")
            # query5 = c.execute("select * from Following")
            
            return {'Githuber': query1.fetchall()}
            # ,\
            #  'Repository': query2.cursor.fetchall(),\
            #   'Star': query3.cursor.fetchall(),\
            #   'Follower': query4.cursor.fetchall(),\
            #   'Following': query5.cursor.fetchall()}
        else:
            query1 =  c.execute(f"select * from Githuber where Githuber.useracc='{nameacc}'")
            query1 = query1.fetchall()
            query2 = c.execute(f"select * from Repository where Repository.user_acc='{nameacc}'")
            query2 = query2.fetchall()
            query3 = c.execute(f"select * from Star where Star.user_acc='{nameacc}'")
            query3 = query3.fetchall()
            query4 = c.execute(f"select * from Follower where Follower.user_acc='{nameacc}'")
            query4 = query4.fetchall()
            query5 = c.execute(f"select * from Following where Following.user_acc='{nameacc}'")
            query5 = query5.fetchall()
            return {'Githuber': query1,\
             'Repository': query2,\
              'Star': query3,\
              'Follower': query4,\
              'Following': query5}
    def put(self, nameacc):
        url = "https://github.com/" + str(nameacc)
        # cp = AutoScrapping(url)
        # return url
        # db.create_all()
        insert_data(url)
        # cp = AutoScrapping(url)
        # useracc, username, bio, location = cp.infoPerso()
        # # ---
        # repo, used_lang = cp.repoScrapping()
        # # ---
        # repo_starred, used_lang_starred = cp.starScrapping()
        # # ---
        # followers_name, followers_acc, followers_bio, followers_location = cp.followerScrapping()
        # # ---
        # following_name, following_acc, following_bio, following_location =  cp.followingScrapping()
        # # conn = sqlite3.connect("database.db")
        # # c = conn.cursor()
        # # c.execute(f"insert into Githuber values (?,?,?,?)", (acc, name, bio, loc))
        # # c.execute(f"insert into Repository values (?,?,?)", (repo, used_lang, acc))
        # # c.execute(f"insert into Star values (?,?,?)",(repo_starred, used_lang_starred, acc))
        # # c.execute(f"insert into Follower values (?,?,?,?,?)",(followers_name, followers_acc, followers_bio, followers_location, acc))
        # # c.execute(f"insert into Following values (?,?,?,?,?)",(following_name, following_acc, following_bio, following_location, acc))
        # # c.commit()
        # # # conn.close()

        # # q = c.execute("select * from Githuber")
        # # return q.fetchall()
        # # insert in database

        # # infoPerson
        # someone = Githuber(useracc=useracc, username=username, bio=bio, location=location)
        # db.session.add(someone)
        # print("info done")
        # # repo
        # for i in range(len(repo)):
        #     repo_someone = Repository(repo=repo[i], used_lang=used_lang[i],user_acc=useracc)
        #     db.session.add(repo_someone)
        # print("repo done")
        # # star
        # for i in range(len(repo_starred)):
        #     repo_starred_ = Star(repo_starred=repo_starred[i], used_lang_starred=used_lang_starred[i],user_acc=useracc)
        #     db.session.add(repo_starred_)
        # print("star done")
        # # follower
        # for i in range(len(followers_acc)):
        #     follower_ = Follower(followers_name=followers_name[i], followers_acc=followers_acc[i], followers_bio=followers_bio[i], followers_location=followers_location[i],user_acc=useracc)
        #     db.session.add(follower_)
        # print("follower done")
        # # following
        # for i in range(len(following_acc)):
        #     following_ = Following(following_name=following_name[i], following_acc=following_acc[i], following_bio=following_bio[i], following_location=following_location[i],user_acc=useracc)
        #     db.session.add(following_)
        # print("following done")
        # db.session.commit()
# api.add_resource(GitUser,'/GitUser1')
if __name__ == "__main__":
    from DataBase.db_scrapping import * 
    from ScrappingGithub.scrapping import *
    from API.api import *
    # url scrapped
    # url = "https://github.com/supig"
    # url = str(input("Url: "))
    # instancie
    # cp = AutoScrapping(url)

    # # scrapping
    # useracc, username, bio, location = cp.infoPerso()
    # # ---
    # repo, used_lang = cp.repoScrapping()
    # # ---
    # repo_starred, used_lang_starred = cp.starScrapping()
    # # # ---
    # followers_name, followers_acc, followers_bio, followers_location = cp.followerScrapping()
    # # ---
    # following_name, following_acc, following_bio, following_location =  cp.followingScrapping()

    # # create database
    
    # # insert in database

    # # infoPerson
    # someone = Githuber(useracc=useracc, username=username, bio=bio, location=location)
    # db.session.add(someone)

    # # repo
    # for i in range(len(repo)):
    #     repo_someone_ = Repository(repo=repo[i], used_lang=used_lang[i])
    #     db.session.add(repo_someone_)
    
    # # # star
    # for i in range(len(repo_starred)):
    #     repo_starred_ = Star(repo_starred=repo_starred[i], used_lang_starred=used_lang_starred[i])
    #     db.session.add(repo_starred_)

    # # # follower
    # for i in range(len(followers_acc)):
    #     follower_ = Follower(followers_acc=followers_acc[i], followers_name=followers_name[i], followers_bio=followers_bio[i], followers_location=followers_location[i])
    #     db.session.add(follower_)

    # # # # following
    # for i in range(len(following_acc)):
    #     following_ = Following(following_name=following_name[i], following_acc=following_acc[i], following_bio=following_bio[i], following_location=following_location[i])
    #     db.session.add(following_)
    # db.session.commit()
    # -------------------
    app = App().app
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///'+base_dir+'/database.db'
    db = SQLAlchemy(app)
    db.init_app(app)
    api = Api(app)
    api.add_resource(GitUser,'/<string:nameacc>')
    app.run(port=3000, debug=True)