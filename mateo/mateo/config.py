import os
import datetime
from dotenv import load_dotenv

load_dotenv()

class Config: 
    SQLALCHEMY_DATABASE_URI = os.environ.get('SQLALCHEMY_DATABASE_URI', "postgresql://admin:password@localhost:5432/mateo")
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    #JWT_EXPIRATION_DELTA = datetime.timedelta(days=1)
    JWT_SECRET_KEY = os.environ.get('JWT_SECRET_KEY') 
    JWT_TOKEN_LOCATION = ['headers', 'cookies']
