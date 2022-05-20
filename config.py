import os


class Config:
    """
    general configuration parent class
    """

    SECRET_KEY = os.environ.get('SECRET_KEY')

    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://benie:12345@localhost/food'
    SQLALCHEMY_TRACK_MODIFICATIONS = True

    UPLOADED_PHOTOS_DEST = 'app/static/photos'

    # email config_options
    MAIL_SERVER = 'smtp.googlemail.com'
    MAIL_PORT = 587
    MAIL_USE_TLS = True
    MAIL_USERNAME = 'davinci.monalissa3@gmail.com'
    # MAIL_PASSWORD = os.environ.get("MAIL_PASSWORD")
    MAIL_PASSWORD = 'beenieman'
    SUBJECT_PREFIX = 'thePitcher'
    SENDER_EMAIL = 'davinci.monalissa3@gmail.com'


class ProdConfig(Config):
    """
    production configuration child class
    """

    # SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL').replace("://", "ql://", 1)

    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://benie:12345@localhost/food'

    DEBUG = True


class DevConfig(Config):
    """
    development configuration child class
    """

    DEBUG = True

    # SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL').replace("://", "ql://", 1)

    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://benie:12345@localhost/food'


config_options = {
'development':DevConfig,
'production':ProdConfig
}