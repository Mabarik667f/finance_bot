import asyncio
import os

from dotenv import load_dotenv
from aiogram import Bot, Dispatcher
from handlers import handlers

load_dotenv()


async def main():
    bot = Bot(token=os.getenv('BOT_TOKEN'))
    dp = Dispatcher()
    dp.include_router(handlers.router)
    await dp.start_polling(bot)

if __name__ == '__main__':
    asyncio.run(main())