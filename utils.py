from os import environ
from logzero import logger, loglevel
from configparser import SafeConfigParser
from typing import Callable
from pydantic import BaseModel


class AppConfig(BaseModel):
    LOG_LEVEL: int
    SECRET_KEY: str
    REDIS_URL: str


def load_config() -> dict:
    config = {}
    stage = environ.get('STAGE', 'DEVELOPMENT').upper()
    parser = SafeConfigParser()
    parser.read('config.ini')

    for k, v in parser.items(stage):
        key = k.upper()
        value = v or environ.get(key)
        config.update({key: value})

    config = AppConfig(**config).dict()
    loglevel(level=config['LOG_LEVEL'])
    return config


def deprecated(describe):
    def decorator(func):
        def wrapped(*args, **kwargs):
            return None

        return wrapped

    return decorator


def shouterr(message: str):
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
