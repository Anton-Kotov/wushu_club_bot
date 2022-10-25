import asyncio

import psycopg2
from aiogram import Bot, Dispatcher
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.contrib.fsm_storage.redis import RedisStorage2

from tg_bot.config import load_config


# def register_all_middlewares(dp):
#     dp.setup_middleware()


# def register_all_filters(dp):
#     dp.filters_factory.bind()
from tg_bot.handlers.start import register_start



def register_all_handlers(dp):
    register_start(dp)



async def main():
    config = load_config(".env")
    bot = Bot(token=config.tg_bot.token, parse_mode="HTML")
    storage = RedisStorage2() if config.tg_bot.use_redis else MemoryStorage()
    dp = Dispatcher(bot, storage=storage)

    connection = psycopg2.connect(dbname=config.db.database, user=config.db.user,
                                  password=config.db.password, host=config.db.host,
                                  port="5432")
    cursor = connection.cursor()
    # cursor.execute(''' DROP TABLE IF EXISTS master ''')

    bot['connection'] = connection
    bot['cursor'] = cursor


    # register_all_middlewares(dp)
    # register_all_filters(dp)
    register_all_handlers(dp)


    try:
        await dp.start_polling()
    finally:
        cursor.close()
        connection.close()
        await dp.storage.close()
        await dp.storage.wait_closed()
        await bot.session.close()


if __name__ == "__main__":
    try:
        asyncio.run(main())
    except (KeyboardInterrupt, SystemExit):
        pass