""" Demo API
"""
from typing import List
from fastapi import APIRouter
from models import GetKeysPayload
from conn.redis import RedisClient

router = APIRouter()


@router.get("/get-keys", response_model=GetKeysPayload)
async def get_best_posts():
    """ Get sample keys from hashmap for demo
    """
    redis: RedisClient = RedisClient(...)
    payload: List[str] = await redis.get_keys('test-map')
    return {'data': payload}
