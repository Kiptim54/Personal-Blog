class Config:
    pass

class ProdConfig(Config):
    pass

class DevConfig(Config):
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://kiptim:jerotich@localhost/blog'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SECRET_KEY = '<Flask WTF Secret Key>'
    # WTF_CSRF_SECRET_KEY="a csrf secret key"


config_options ={"production":ProdConfig,"default":DevConfig}

