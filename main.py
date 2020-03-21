"""Initialization fastapi application
"""
from fastapi import FastAPI, Depends
from middlewares import internal_only
from apis import demo
from conn.redis import RedisClient

app = FastAPI()


@app.on_event("startup")
async def init_conns():
    """Init external connections & middlewares
    """
    RedisClient(CONFIG)


app.include_router(
    demo.router,
    prefix="/thing",
    tags=["Thing"],
    dependencies=[Depends(internal_only)],
    responses={404: {
        "message": "Not found"
    }},
)
