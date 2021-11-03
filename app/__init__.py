from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from config import Config

app = Flask(__name__)
app.static_folder = 'static'
app.config.from_object(Config)
db = SQLAlchemy(app)

from app import routes

if __name__ == '__main__':
    app.run(host='127.0.0.1', debug=True)