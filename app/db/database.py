import databases
import sqlalchemy
from settings import DATABASE_URI

database = databases.Database(DATABASE_URI)
metadata = sqlalchemy.MetaData()


async def create_connection():
    await database.connect()


async def disconnect():
    await database.disconnect()


import aioredis
# import asyncio_redis

# async def redis_connection():
#     redis_db1 = await aioredis.create_redis_pool("redis://localhost/15672//")
#     return redis_db1
