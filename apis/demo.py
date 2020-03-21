""" Demo API
"""
from typing import List
from fastapi import APIRouter, Query
from models import GetKeysPayload, PostMeta
from conn.redis import RedisClient
from conn.neo4j import NeoClient

router = APIRouter()


@router.get("/get-keys", response_model=GetKeysPayload)
async def get_best_posts():
    """ Get sample keys from hashmap for demo
    """
    redis: RedisClient = RedisClient(...)
    payload: List[str] = await redis.get_keys('test-map')
    return {'data': payload}


@router.put("/create-labels")
async def create_label(labels: List[str] = Query(None)):
    """ create label with post
    """
    neo: NeoClient = NeoClient(...)
    count = neo.create_labels(labels)
    return count


@router.put("/create-posts")
async def create_posts(label: str, posts: List[PostMeta]):
    """ create posts
    """
    neo: NeoClient = NeoClient(...)
    count = neo.create_posts(posts, label)
    return count
