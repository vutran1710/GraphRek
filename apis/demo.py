""" Demo API
"""
from fastapi import APIRouter
from models import GetKeysPayload
from conn.redis import RedisClient

router = APIRouter()


@router.get("/get-keys", response_model=GetKeysPayload)
async def get_best_posts():
    """ Get sample keys from hashmap for demo
    """
    redis: RedisClient = RedisClient(...)
    payload = await redis.get_keys('test-map')
    return payload
