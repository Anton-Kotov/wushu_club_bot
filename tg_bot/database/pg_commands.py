from typing import Union

import asyncpg as asyncpg
from asyncpg import Pool, Connection

from tg_bot.config import load_config


class Database:

    def __init__(self):
        self.pool: Union[Pool, None] = None

    async def create(self):
        config = load_config(".env")
        self.pool = await asyncpg.create_pool(
            user=config.db.user,
            password=config.db.password,
            host=config.db.host,
            database=config.db.database
        )

    async def execute(self, command, *args,
                      fetch: bool = False,
                      fetchval: bool = False,
                      fetchrow: bool = False,
                      execute: bool = False
                      ):
        async with self.pool.acquire() as connection:
            connection: Connection
            async with connection.transaction():
                if fetch:
                    result = await connection.fetch(command, *args)
                elif fetchval:
                    result = await connection.fetchval(command, *args)
                elif fetchrow:
                    result = await connection.fetchrow(command, *args)
                elif execute:
                    result = await connection.execute(command, *args)
        return result

    async def create_table(self, sql):

        await self.execute(sql, execute=True)

    async def add_menu(self, MAIN_CODE, MAIN_NAME,
                       CATEGORY_CODE, CATEGORY_NAME,
                       SUBCATEGORY_CODE, SUBCATEGORY_NAME,
                       TEXT, PHOTO):

        sql = """
            INSERT INTO menu
            (MAIN_CODE, MAIN_NAME, CATEGORY_CODE,
            CATEGORY_NAME, SUBCATEGORY_CODE, SUBCATEGORY_NAME,
            TEXT, PHOTO)
            VALUES ($1, $2, $3, $4, $5, $6, $7, $8); 
        """

        return await self.execute(sql, MAIN_CODE, MAIN_NAME,
                                  CATEGORY_CODE, CATEGORY_NAME,
                                  SUBCATEGORY_CODE, SUBCATEGORY_NAME,
                                  TEXT, PHOTO, execute=True)

    async def get_main(self):

        sql = """ 
        SELECT DISTINCT MAIN_CODE, MAIN_NAME
        FROM menu; """

        return await self.execute(sql, fetch=True)

    async def get_categories(self, main):

        sql = f""" 
        SELECT DISTINCT CATEGORY_CODE, CATEGORY_NAME
        FROM menu
        WHERE MAIN_CODE = '{main}'; """

        return await self.execute(sql, fetch=True)

    async def close(self) -> None:
        if self.pool is None:
            return None

        await self.pool.close()