""" Application Middlewares
"""
from fastapi import HTTPException, Header
from starlette.status import HTTP_403_FORBIDDEN
from logzero import logger


def internal_only(internal_header: str = Header(None)):
    """ Only allow internal cluster call
    """
    logger.info("ROLE = %s", internal_header)
    if internal_header != 'service':
        raise HTTPException(HTTP_403_FORBIDDEN, detail="Access denied")
