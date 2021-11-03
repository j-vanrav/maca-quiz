from wtforms.validators import IPAddress
from app import db

class Result(db.Model):
    id          = db.Column(db.Integer, primary_key = True)
    ipAddress   = db.Column(db.String, unique=True)
    answer      = db.Column(db.String(length=1))