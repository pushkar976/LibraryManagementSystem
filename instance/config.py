import os

BASE_DIR = os.path.abspath(os.path.dirname(__file__))

SQLALCHEMY_DATABASE_URI = f'mysql://root:root@localhost/library'
SQLALCHEMY_TRACK_MODIFICATIONS = False