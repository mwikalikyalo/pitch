import os

class Config:
    '''
    General configuration parent class
    ''' 
    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://moringa:0000@localhost/pitch'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SECRET_KEY = os.environ.get('SECRET_KEY') 
    UPLOADED_PHOTOS_DEST = 'app/static/photos' 

     #email configurations
    MAIL_SERVER = 'smtp.googlemail.com'
    MAIL_PORT = 587
    MAIL_USE_TLS = True
    MAIL_USERNAME = os.environ.get("MAIL_USERNAME")
    MAIL_PASSWORD = os.environ.get("MAIL_PASSWORD")

    # simple mde  configurations
    SIMPLEMDE_JS_IIFE = True
    SIMPLEMDE_USE_CDN = True

class ProdConfig(Config):
  '''Production configuration class'''
  # SQLALCHEMY_DATABASE_URI = os.environ.get("DATABASE_URL")
  pass

class TestConfig(Config):
    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://moringa:0000@localhost/pitch_test'
    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://moringa:0000@localhost/comment_test'
    
class DevConfig(Config):
    '''
    Development configuration child class 
    '''
    # SQLALCHEMY_DATABASE_URI = 'postgres://yazapgyjbvarxf:0cbebb20130fbc21aa10981fcaaa57f447dbbaba3732c1bcf4c6d0e7c95dc898@ec2-54-209-221-231.compute-1.amazonaws.com:5432/d5ua106brjlq78'
    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://moringa:0000@localhost/pitch'
    DEBUG = True

config_options = {
  'development': DevConfig,
  'production': ProdConfig,
  'test': TestConfig
}    