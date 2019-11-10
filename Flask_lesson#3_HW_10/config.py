import os


class Config:
    SECRET_KEY = "secret_key"
    DEBUG = True


class TestConfig(Config):
    SECRET_KEY = "test_key"


class ProductionConfig(Config):
    SECRET_KEY = "prod_key"


def run_config():
    env = os.environ.get('ENV')
    if env == 'TEST':
        return TestConfig
    elif env == 'PROD':
        return ProductionConfig
    else:
        return Config


