""" Most used decorators
"""
from typing import Callable
from logzero import logger


def singleton(some_class):
    """ Make a Class Singleton
    """
    def on_call(*args, **kwargs):
        if on_call.instance is None:
            on_call.instance = some_class(*args, **kwargs)
        return on_call.instance

    on_call.instance = None
    return on_call


def deprecated(_describe):
    """ Annotation for deprecated functions
    """
    def decorator(_func):
        def wrapped(*_args, **_kwargs):
            return None

        return wrapped

    return decorator


def shout_err(message: str):
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
