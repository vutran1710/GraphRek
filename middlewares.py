from fastapi import Depends, HTTPException, Headerfrom starlette.status import HTTP_403_FORBIDDEN
from starlette.requests import Request
from utils import CONFIG
from logzero import logger


def internal_only(internal_header: str = Header(None)):
    logger.info("ROLE = %s", internal_header)
    if internal_header != 'service':
        raise HTTPException(HTTP_403_FORBIDDEN, detail="Access denied")
