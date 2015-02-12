from flask.ext.sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(254), unique=True)
    password = db.Column(db.String(60))
    sessions = db.relationship('Session', backref='person', lazy='dynamic')

class Session(db.Model):
    key = db.Column(db.String(32), primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
