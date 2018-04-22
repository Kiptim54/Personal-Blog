import os 

class Config:
    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://kiptim:jerotich@localhost/blog'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SECRET_KEY = 'kenani'
    #  email configurations
    MAIL_SERVER = 'smtp.gmail.com'
    MAIL_PORT = 587
    MAIL_USE_TLS = True
    MAIL_USERNAME = os.environ.get("kiptim54@gmail.com")
    MAIL_PASSWORD = os.environ.get("jerotich")
    UPLOADED_PHOTOS_DEST ='app/static/photos'
     # simple mde  configurations
    SIMPLEMDE_JS_IIFE = True
    SIMPLEMDE_USE_CDN = True


class ProdConfig(Config):
    SQLALCHEMY_DATABASE_URI = os.environ.get("DATABASE_URL")
    DEBUG = True
class DevConfig(Config):
    DEBUG = True
    

config_options ={"production":ProdConfig,"default":DevConfig}

