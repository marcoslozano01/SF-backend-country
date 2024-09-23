from app.db import db

class Country(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    country = db.Column(db.String(100), nullable=False, unique=True)
    population = db.Column(db.Integer, nullable=True)