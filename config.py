import os

basedir = os.path.abspath(os.path.dirname(__file__))

ENV = 'prod'
class Config(object):
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'super_secret'
    if ENV == 'dev':
        SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or 'postgresql://postgres:postgres@localhost:5432/quizzet'
        URL = 'http://localhost:5000'
    elif ENV == 'prod':
        SQLALCHEMY_DATABASE_URI = 'postgresql' + os.environ.get('DATABASE_URL')[8:] or ''
        URL = 'https://maca-quiz.herokuapp.com'
    SQLALCHEMY_TRACK_MODIFICATIONS = False