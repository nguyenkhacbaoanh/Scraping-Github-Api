from flask import Flask, render_template, request
from flask_restful import Api, Resource
# import jsonpify

class App:
    app = Flask(__name__)

    @app.route("/")
    def home():
        return render_template("home.html")
