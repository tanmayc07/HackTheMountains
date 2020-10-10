from app import db
from sqlalchemy import Column, Integer, String, ForeignKey, Date
from sqlalchemy.orm import relationship
import datetime

class user(db.Model):
    id = db.Column(Integer, primary_key=True)
    name =  db.Column(String(150), unique = True, nullable=False)
    phone = db.Column(String(20))
    password = db.Column(String(10), nullable=False)
    created_at = db.Column(db.Datetime, nullable=False, default=datetime.utcnow)
    email = db.Column(String(50), nullable=False)
    token = db.relationship('Token', backref='token', lazy=True)
    medicine = db.relationship('Medicine', backref='Medinfo', lazy=True)

    def repr(self):
        return self.name

class token(db.Model):
    id = db.Column(Integer, primary_key=True)
    created_at = db.Column(db.Datetime, nullable=False, default=datetime.utcnow)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)

class Medinfo(db.Model):
    id = db.Column(Integer, primary_key=True)
    name = db.Column(String(150))
    time_interval = db.Column(db.Datetime, nullable=False, default=datetime.utcnow)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)



