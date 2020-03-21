"""Initialization fastapi application
"""
from fastapi import FastAPI, Depends
from aioredis import create_redis_pool
from neo4j import GraphDatabase, basic_auth

from utils import CONFIG
from conn.redis import RedisClient
from conn.neo4j import NeoClient
from apis import demo
from middlewares import internal_only

app = FastAPI()


@app.on_event("startup")
async def init_conns():
    """Init external connections & middlewares
    """
    pool = await create_redis_pool(CONFIG['REDIS_URL'])
    RedisClient(pool)
    neourl = CONFIG['NEO4J_URL']
    driver = GraphDatabase.driver(
        neourl,
        auth=basic_auth("neo4j", "test"),
        encrypted=False,
    )
    NeoClient(driver)


app.include_router(
    demo.router,
    prefix="/thing",
    tags=["Thing"],
    # dependencies=[Depends(internal_only)],
    responses={404: {
        "message": "Not found"
    }},
)
