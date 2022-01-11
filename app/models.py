from datetime import datetime
from app import db

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), index=True, unique=True)
    email = db.Column(db.String(120), index=True, unique=True)
    password_hash = db.Column(db.String(128))
    businesses = db.relationship('Businesses', backref='user', lazy='dynamic')

    def __repr__(self):
        return '<User {}>'.format(self.username)

class Businesses(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    business_name = db.Column(db.String(120), index=True, unique=True)
    acct_created = db.Column(db.DateTime, index=True, default=datetime.utcnow)
    industry = db.Column(db.String(120))
    address_building = db.Column(db.String(120))
    address_street_name = db.Column(db.String(120))
    address_city = db.Column(db.String(120))
    address_state = db.Column(db.String(2))
    address_zip = db.Column(db.String(5))
    contact_phone = db.Column(db.String(64))
    address_borough = db.Column(db.String(128))
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))

    def __repr__(self):
        return '<Business {}>'.format(self.business_name)