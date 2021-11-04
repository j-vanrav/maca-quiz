from app import db

class Result(db.Model):
    id          = db.Column(db.Integer, primary_key = True)
    answer      = db.Column(db.String(length=1))