import os

class Config(object):
    PROJECT_ID = 'Project2STAC'
    DATA_BACKEND = 'mongodb'
    MONGO_URI = 'mongodb+srv://teamname:teamname@project2-stacdata-osuhm.gcp.mongodb.net/test?retryWrites=true'
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'you-will-never-guess'