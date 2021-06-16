from re import S
from flask.app import Flask
from flask_sqlalchemy import SQLAlchemy


class Server():
    app = Flask(__name__)
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
    app.config["SQLALCHEMY_DATABASE_URI"] = 'mysql://youruser@youruser:passwrd@svname:port(3306?)/database'
    db = SQLAlchemy(app)
