""" Utils & setups
"""
from os import environ
from configparser import ConfigParser
from logzero import loglevel
from pydantic import BaseModel


class AppConfig(BaseModel):
    """ Defined required & config Fields for EnvVars
    """
    LOG_LEVEL: int
    NEO4J_URL: str
    REDIS_URL: str


def load_config() -> dict:
    """ Load config from Env
    """
    config = {}
    stage = environ.get('STAGE', 'DEVELOPMENT').upper()
    parser = ConfigParser()
    parser.read('config.ini')

    for k, v in parser.items(stage):
        key = k.upper()
        value = v or environ.get(key)
        config.update({key: value})

    config = AppConfig(**config).dict()
    loglevel(level=config['LOG_LEVEL'])
    return config


CONFIG = load_config()
