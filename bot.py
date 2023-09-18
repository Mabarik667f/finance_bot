import asyncio
import os
# import pymysql.cursors

from dotenv import load_dotenv
from aiogram import Bot, Dispatcher
import handlers

#
load_dotenv()

# try:
#     connection = pymysql.connect(
#         host='127.0.0.1',
#         port=3306,
#         user=os.getenv('USER'),
#         password=os.getenv('PASSWORD'),
#         database=os.getenv('NAME'),
#         cursorclass=pymysql.cursors.DictCursor)
#     print('Успешно')
# except Exception as ex:
#     print('Ошибка')
#     print(ex)


async def main():
    bot = Bot(token=os.getenv('BOT_TOKEN'))
    dp = Dispatcher()
    dp.include_router(handlers.router)
    await dp.start_polling(bot)

if __name__ == '__main__':
    asyncio.run(main())