import os


# default config
class BaseConfig(object):
    DEBUG = False
    # shortened for readability
    SECRET_KEY = "\x03\x03\xfc\x02\xc2f\xf3\x84'\xa8V\x9e\x97\xc3\xe1hB\xd7\xb3\x1b\xde\xd3\x13\xa5"
    SQLALCHEMY_DATABASE_URI = os.environ['DATABASE_URL']
    print SQLALCHEMY_DATABASE_URI



class DevelopmentConfig(BaseConfig):
    DEBUG = True


class ProductionConfig(BaseConfig):
    DEBUG = False
