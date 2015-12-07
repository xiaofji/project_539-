import os


# default config
class BaseConfig(object):
    DEBUG = False
    SECRET_KEY = "\x03\x03\xfc\x02\xc2f\xf3\x84'\xa8V\x9e\x97\xc3\xe1hB\xd7\xb3\x1b\xde\xd3\x13\xa5"
    SQLALCHEMY_DATABASE_URI = os.environ['DATABASE_URL']



class DevelopmentConfig(BaseConfig):
    DEBUG = True


class ProductionConfig(BaseConfig):
    DEBUG = False
