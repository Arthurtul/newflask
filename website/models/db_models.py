import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from sqlalchemy import MetaData
from website import db

convention = {
    "ix": 'ix_%(column_0_label)s',
    "uq": "uq_%(table_name)s_%(column_0_name)s",
    "ck": "ck_%(table_name)s_%(constraint_name)s",
    "fk": "fk_%(table_name)s_%(column_0_name)s_%(referred_table_name)s",
    "pk": "pk_%(table_name)s"
}

basedir = os.path.abspath(os.path.dirname(__file__))

app = Flask(__name__)

app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///"+os.path.join(basedir, "data.sqlite")
app.config["SQLALCHEMY_TRACK_MODIFICATION"] = False

metadata = MetaData(naming_convention=convention)
# db = SQLAlchemy(app, metadata=metadata)
Migrate(app, db)


class Message(db.Model):
    __tablename__ = "message"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    phone = db.Column(db.String(40), unique=True)
    message = db.Column(db.Text, nullable=False)
    one_more = db.Column(db.String(180), unique=True)

    def __init__(self, name, email, phone, message, one_more):
        self.name = name
        self.email = email
        self.phone = phone
        self.message = message
        self.one_more = one_more

    def __repr__(self):
        return f"{self.name} - {self.email}"


class Posts(db.Model):
    __tablename__ = 'Posts'
    id = db.Column(db.Integer, primary_key=True)
    data = db.Column(db.String(50), unique=False, nullable=False)
    autor = db.Column(db.String(120), unique=False, nullable=False)
    book_name = db.Column(db.String(80), unique=False)
    comment = db.Column(db.Text, unique=False, nullable=False)

    def __init__(self, data, autor, book_name, comment):
        self.data = data
        self.autor = autor
        self.book_name = book_name
        self.comment = comment

    def __repr__(self):
        return f'{self.data} - {self.autor} - {self.book_name}'

