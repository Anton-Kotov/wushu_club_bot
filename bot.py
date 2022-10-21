import asyncio

from aiogram import Bot, Dispatcher
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.contrib.fsm_storage.redis import RedisStorage2

from tg_bot.config import load_config


async def main():
    config = load_config(".env")
    bot = Bot(token=config.tg_bot.token, parse_mode="HTML")
    storage = RedisStorage2() if config.tg_bot.use_redis else MemoryStorage
    dp = Dispatcher(bot, storage=storage)
    bot['config'] = config

if __name__ == "__main__":
    try:
        asyncio.run(main())
    except (KeyboardInterrupt, SystemExit):
        pass