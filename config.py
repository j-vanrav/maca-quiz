import os

basedir = os.path.abspath(os.path.dirname(__file__))

ENV = 'dev'
class Config(object):
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'super_secret'
    if ENV == 'dev':
        SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or 'postgresql://postgres:postgres@localhost:5432/quizzet'
    elif ENV == 'prod':
        SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or ''
    SQLALCHEMY_TRACK_MODIFICATIONS = False