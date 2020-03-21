""" Utils & setups
"""
from typing import Callable
from os import environ
from configparser import ConfigParser
from logzero import logger, loglevel
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


def deprecated(_describe):
    """ Annotation for deprecated functions
    """
    def decorator(_func):
        def wrapped(*_args, **_kwargs):
            return None

        return wrapped

    return decorator


def shouterr(message: str):
    """ Annotate err log on Exception
    """
    def decorator(func: Callable):
        def wrapped(*args, **kwargs):
            try:
                return func(*args, **kwargs)
            except Exception as err:
                logger.error('<<< %s >>', message.upper())
                logger.error(err)
                return None

        return wrapped

    return decorator


CONFIG = load_config()
