import os


base_dir = os.path.abspath(os.path.dirname(__file__))
CODE_BASE = 'TNAFD'


class DatabaseConfig:
    REGISTRATION_COL = 'app_users'
    

class BaseConfig(DatabaseConfig):
    """
    Base application configuration
    """
    DEBUG = False
    TESTING = False
    SECRET_KEY = os.getenv('SECRET_KEY', 'you should change this')
    JWT_SECRET_KEY = 'super-secret'
    AUTH_TOKEN_EXPIRY_SECONDS = 500
    SUCCESS_MESSAGE = "Success"
    SUCCESS_MESSAGE_200 = "Success"
    FAILURE_MESSAGE_301 = "Moved Permanently"
    FAILURE_MESSAGE_400 = "Bad Request"
    FAILURE_MESSAGE_401 = "Unauthorized Request"
    FAILURE_MESSAGE_403 = "Forbidden Request"
    FAILURE_MESSAGE_404 = "Resource Not Found"
    FAILURE_MESSAGE_409 = "Resource Already Exists"
    FAILURE_MESSAGE_422 = "Invalid Input Payload"
    FAILURE_MESSAGE_500 = "Internal Server Error"
    FAILURE_MESSAGE = "Failed"
    # success and failure messages
    
    LOG_LOCATION = os.path.join(base_dir, CODE_BASE, 'Logs')
    if not os.path.exists(LOG_LOCATION):
        os.makedirs(LOG_LOCATION)


class DevelopmentConfig(BaseConfig):
    """
    Development application configuration
    """
    DEBUG = True
    MYSQL_HOST = '*****'
    MYSQL_USER = '*******'
    MYSQL_PASSWORD = '*******'
    MYSQL_DB = '*******'
    MAIL_SERVER = 'smtp.gmail.com'
    MAIL_PORT = 465
    MAIL_USERNAME = '********'
    MAIL_PASSWORD = '***********'
    MAIL_USE_TLS = False
    MAIL_USE_SSL = True
    MONGO_DB = 'btkguzctt6o97cb'
    # MONGO_URI = f'mongodb://ufumtyzgd9ji6x7g50f8:VJxXRkNWzzZq1EeokkGK@btkguzctt6o97cb-mongodb.services.clever-cloud.com:27017/btkguzctt6o97cb'
    MONGO_URI = os.environ['MONGO_URI']
    SECRET_KEY = 'a5ea0c77491f965420dfa379ddb6105adb0e3e88'
    JWT_SECRET_KEY = 'super-secret'


class TestingConfig(BaseConfig):
    """
    Testing application configuration
    """
    TESTING = True


class ProductionConfig(BaseConfig):
    """
    Production application configuration
    """
    DEBUG = True

