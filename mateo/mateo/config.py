import os
import datetime
from dotenv import load_dotenv

load_dotenv()

class Config: 
    SQLALCHEMY_DATABASE_URI = os.environ.get('SQLALCHEMY_DATABASE_URI', "postgresql://admin:password@localhost:5432/mateo")
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    #JWT_EXPIRATION_DELTA = datetime.timedelta(days=1)
    JWT_SECRET_KEY = os.environ.get('JWT_SECRET_KEY') 
    JWT_ACCESS_COOKIE_PATH = '/api/'
    JWT_REFRESH_COOKIE_PATH = '/auth/refresh'
    JWT_TOKEN_LOCATION = ['cookies']
    JWT_COOKIE_CSRF_PROTECT = True
    JWT_CSRF_IN_COOKIES = False
    JWT_ACCESS_COOKIE_NAME = 'access_token'
    JWT_REFRESH_COOKIE_NAME = 'refresh_token'
    JWT_ACCESS_CSRF_HEADER_NAME = 'X-CSRF-Token'
    JWT_REFRESH_CSRF_HEADER_NAME = 'X-CSRF-Token'
    JWT_COOKIE_SECURE = False
