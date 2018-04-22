import os 

class Config:
    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://kiptim:jerotich@localhost/blog'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SECRET_KEY = 'kenani'
    # WTF_CSRF_SECRET_KEY="a csrf secret key"
    #  email configurations
    MAIL_SERVER = 'smtp.googlemail.com'
    MAIL_PORT = 587
    MAIL_USE_TLS = True
    MAIL_USERNAME = os.environ.get("Brenda Kiptim")
    MAIL_PASSWORD = os.environ.get("jerotich")
    UPLOADED_PHOTOS_DEST ='app/static/photos'
     # simple mde  configurations
    SIMPLEMDE_JS_IIFE = True
    SIMPLEMDE_USE_CDN = True
class TestConfig(Config):
    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://kiptim:jerotich@localhost/blog_test'


class ProdConfig(Config):
    pass

class DevConfig(Config):
    DEBUG = True
    
config_options ={"production":ProdConfig,"default":DevConfig}

