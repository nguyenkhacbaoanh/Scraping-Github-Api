from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import os
path_dir = os.path.dirname(os.path.abspath(__file__))
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///'+path_dir+'/database.db'
db = SQLAlchemy(app)

# import module interne
from ScrappingGithub.scrapping import AutoScrapping


class Githuber(db.Model):
    __tablename__ = "User"
    # id = db.Column(db.Integer, primary_key=True)
    useracc = db.Column(db.String(80), unique=True, nullable=False, primary_key=True)
    username = db.Column(db.String(80), unique=False, nullable=True)
    bio = db.Column(db.String(120), unique=False, nullable=True)
    location = db.Column(db.String(80), unique=False, nullable=True)

    # def __repr__(self):
    #     return '<User %r>' % self.useracc

class Repository(db.Model):
    __tablename__ = "Repositories"
    id = db.Column(db.Integer, primary_key=True)
    repo = db.Column(db.String(80), nullable=True)
    used_lang = db.Column(db.String(10), nullable=True)
    # user = db.Column(db.String(80), db.ForeignKey('User.useracc'), nullable=False)
    # user_github = db.relationship('Githuber')


if __name__ == "__main__":
    # url scrapped
    url = "https://github.com/supig"
    # instancie
    cp = AutoScrapping(url)
    useracc, username, bio, location = cp.infoPerso()
    # ---
    repo, used_lang = cp.repoScrapping()
    # create database
    db.create_all()
    someone = Githuber(useracc=useracc, username=username, bio=bio, location=location)
    db.session.add(someone)
    for i in range(len(repo)):
        repo_someone = Repository(repo=repo[i], used_lang=used_lang[i])
        db.session.add(repo_someone)
    db.session.commit()