from flask import Flask, render_template, request
from flask_restful import Api, Resource
from sqlalchemy import create_engine
from flask_restful import Api, Resource
import sqlite3
from DataBase.db_scrapping import *
# import jsonpify

class App:
    app = Flask(__name__)

    @app.route("/")
    def home():
        return render_template("home.html")

# db_connect = create_engine('sqlite:///database.db')
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
            query1 = query1.fetchall()
            query2 = c.execute("select * from Repository")
            query2 = query2.fetchall()
            query3 = c.execute("select * from Star")
            query3 = query3.fetchall()
            query4 = c.execute("select * from Follower")
            query4 = query4.fetchall()
            query5 = c.execute("select * from Following")
            query5 = query5.fetchall()
            
            return {'Githuber': query1,\
             'Repository': query2,\
              'Star': query3,\
              'Follower': query4,\
              'Following': query5}
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
        insert_data(url)
