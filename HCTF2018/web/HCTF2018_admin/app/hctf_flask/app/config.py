import os

class Config(object):
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'ckj123'
    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://root:root@localhost:3306/test'
    SQLALCHEMY_TRACK_MODIFICATIONS = True