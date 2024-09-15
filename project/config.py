import os
from dotenv import load_dotenv
load_dotenv()

DEBUG = True
TESTING = False
SECRET_KEY = os.getenv('SECRET_KEY', 'fallback_secret_key')
SESSION_PERMANENT = False
SESSION_TYPE = 'filesystem'
SQLALCHEMY_DATABASE_URI = 'sqlite:///../instance/book.db'
SQLALCHEMY_TRACK_MODIFICATIONS = True