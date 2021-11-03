import os

basedir = os.path.abspath(os.path.dirname(__file__))

ENV = 'dev'
class Config(object):
    if ENV == 'dev':
        SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or 'postgresql://postgres:postgres@localhost:5432/app'
    elif ENV == 'prod':
        SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or ''
    SQLALCHEMY_TRACK_MODIFICATIONS = False