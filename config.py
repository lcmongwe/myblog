import os


class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    # SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://lucy:4444@localhost/myblog'
    

class ProdConfig(Config):
   pass

class TestConfig(Config):

    pass

class DevConfig(Config):
    # SQLALCHEMY_DATABASE_URI = os.environ.get('SQLALCHEMY_DATABASE_URI')
    SQLALCHEMY_DATABASE_URI='postgresql+psycopg2://lucy:4444@localhost/myblog'
    DEBUG = True

config_options = {
'development':DevConfig,
'production':ProdConfig,
'test':TestConfig
}

