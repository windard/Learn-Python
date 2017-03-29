# coding=utf-8

import os

# configuration
DATABASE = '/home/windard/Desktop/python/flask/flaskr.db'
DEBUG = True
SECRET_KEY = os.urandom(30)
USERNAME = 'admin'
PASSWORD = 'default'

HOST='0.0.0.0'
PORT=8888
SQLALCHEMY_DATABASE_URI = 'mysql://web:web@localhost/test'
SQLALCHEMY_TRACK_MODIFICATIONS = True
