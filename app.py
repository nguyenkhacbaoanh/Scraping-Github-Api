from flask import Flask, request
from sqlalchemy import create_engine
from flask_restful import Api, Resource

db_connect = create_engine('sqlite:///database.db')
app_ = Flask(__name__)
api = Api(app_)

class GitUser(Resource):
    def get(self):
        conn = db_connect.connect()
        query =  conn.execute("select * from User, Repositories")
        return {'GitUser': query.cursor.fetchall()}

api.add_resource(GitUser,'/GitUser1')
if __name__ == "__main__":
    # from API.api import *
    # app = App().app
    app_.run(port=3000, debug=True)