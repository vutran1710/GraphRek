"""Initialization fastapi application
"""
from fastapi import FastAPI, Depends
from aioredis import create_redis_pool
from neomodel import db, install_all_labels

from middlewares import internal_only
from apis import demo
from conn.redis import RedisClient
from conn.db_models import *
from utils import CONFIG

app = FastAPI()


@app.on_event("startup")
async def init_conns():
    """Init external connections & middlewares
    """
    pool = await create_redis_pool(CONFIG['REDIS_URL'])
    RedisClient(pool)
    db.set_connection(CONFIG['NEO4J_URL'])
    install_all_labels()


app.include_router(
    demo.router,
    prefix="/thing",
    tags=["Thing"],
    dependencies=[Depends(internal_only)],
    responses={404: {
        "message": "Not found"
    }},
)
