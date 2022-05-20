from flask import Flask
from flask_bootstrap import Bootstrap
from config import config_options
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from flask_uploads import UploadSet,configure_uploads,IMAGES
from flask_mail import Mail


bootstrap = Bootstrap()
db = SQLAlchemy()

login_manager = LoginManager()
login_manager.session_protection = 'strong'
login_manager.login_view = 'auth.login'

photos = UploadSet('photos',IMAGES)
mail = Mail()


def create_app(config_name):
    # initialize app
    app = Flask(__name__)

    # create app configs
    app.config.from_object(config_options[config_name])

    app.config.from_object(['MAIL_PASSWORD'])

    # initialize Flask extensions
    bootstrap.init_app(app)
    db.init_app(app)
    login_manager.init_app(app)
    mail.init_app(app)

    # configure UploadSet
    configure_uploads(app, photos)

    # register blueprint
    from .main import main as main_blueprint
    app.register_blueprint(main_blueprint)

    # register auth Blueprint
    from .auth import auth as auth_blueprint
    app.register_blueprint(auth_blueprint, url_prefix='/authenticate')

    return app
