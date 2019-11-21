import os


class Config:
    SECRET_KEY = "secret_key"
    DEBUG = True


class TestConfig(Config):
    SECRET_KEY = "test_key"


class ProductionConfig(Config):
    SECRET_KEY = "prod_key"


def run_config():
    get_env = {"TEST": TestConfig, "PROD": ProductionConfig}
    return get_env.get(os.environ.get('ENV'))
