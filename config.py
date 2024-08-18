import os

class Config:
    SQLALCHEMY_DATABASE_URI = os.getenv('DATABASE_URL', 'postgresql://postgres:99!21?80@localhost/country_finder')
    SQLALCHEMY_TRACK_MODIFICATIONS = False