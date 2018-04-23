from flask import Flask
from config import config_options
from flask_bootstrap import Bootstrap
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from flask_admin import Admin
from flask_mail import Mail
from flask_uploads import UploadSet,configure_uploads,IMAGES
from flask_simplemde import SimpleMDE
from flask_basicauth import BasicAuth

login_manager = LoginManager()
login_manager.session_protection = 'strong'
login_manager.login_view = 'auth.login'

db = SQLAlchemy()
bootstrap = Bootstrap()
admin = Admin()
mail = Mail()
photos = UploadSet('photos',IMAGES)
simple = SimpleMDE()
basic_auth= BasicAuth()




def create_app(config_state):
    
    app = Flask(__name__)
    app.config.from_object(config_options[config_state])

    db.init_app(app)
    bootstrap.init_app(app)
   
    login_manager.init_app(app)
    admin.init_app(app)
    mail.init_app(app)
    simple.init_app(app)
    basic_auth.init_app(app)
      # configure UploadSet
    configure_uploads(app,photos)

    

    from .main import main as main_blueprint
    app.register_blueprint(main_blueprint)

    from .auth import auth as auth_blueprint
    app.register_blueprint(auth_blueprint , url_prefix = '/authenticate')

    return app
