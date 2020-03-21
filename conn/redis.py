"""Redis module
"""
from typing import List
from decorator import singleton


@singleton
class RedisClient:
    """Asynchronous Redis Client
    """
    pool = None

    def __init__(self, async_pool):
        """bind an async redis-pool to this class instance
        """
        self.pool = async_pool

    async def get_keys(self, some_map: str) -> List[str]:
        """Get all keys from hashmap
        """
        if not some_map:
            return []

        keys = self.pool.hkeys(some_map)
        return keys
