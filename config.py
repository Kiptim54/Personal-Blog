import os 

class Config:
    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://kiptim:jerotich@localhost/blog'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SECRET_KEY = '<Flask WTF Secret Key>'
    # WTF_CSRF_SECRET_KEY="a csrf secret key"
    #  email configurations
    MAIL_SERVER = 'smtp.googlemail.com'
    MAIL_PORT = 587
    MAIL_USE_TLS = True
    MAIL_USERNAME = os.environ.get("Brenda Kiptim")
    MAIL_PASSWORD = os.environ.get("jerotich")
    UPLOADED_PHOTOS_DEST ='app/static/photos'


class ProdConfig(Config):
    pass

class DevConfig(Config):
    DEBUG = True
    
config_options ={"production":ProdConfig,"default":DevConfig}

