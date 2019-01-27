from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import os
path_dir = os.path.dirname(os.path.abspath(__file__))
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///'+path_dir+'/database.db'
db = SQLAlchemy(app)


class Githuber(db.Model):
    # id = db.Column(db.Integer, primary_key=True)
    useracc = db.Column(db.String(80), unique=True, nullable=False, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=True)
    bio = db.Column(db.String(120), unique=True, nullable=True)
    location = db.Column(db.String(80), unique=True, nullable=True)

    def __repr__(self):
        return '<User %r>' % self.useracc

if __name__ == "__main__":
    db.create_all()
    admin = Githuber(username='admin', email='admin@example.com')
    guest = Githuber(username='guest', email='guest@example.com')
    db.session.add(admin)
    db.session.add(guest)
    db.session.commit()