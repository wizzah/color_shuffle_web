import os

class Config(object):
    DEBUG = False
    TESTING = False
    DATABASE_URI = 'sqlite://:memory:'

class ProductionConfig(Config):
    DATABASE_URI = 'mysql://user@localhost/foo'

class DevelopmentConfig(Config):
    DEBUG = True
    DIRECTORY = os.getcwd()+"/static"
    PROCESSING_DIRECTORY = os.getcwd()+"/static/processing"
    OUTPUT_DIRECTORY = os.getcwd()+"/static/output/"
    INPUT_FILETYPE = ".gif"
    ATTEMPTED_OUTPUT_FILENAME = "itried.gif"

class TestingConfig(Config):
    TESTING = True