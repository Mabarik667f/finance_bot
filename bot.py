import asyncio
import os
# import pymysql.cursors

from config_data.config import Config, load_config
from aiogram import Bot, Dispatcher
from handlers import user_handlers, other_handlers
from keyboards.main_menu import set_main_menu
from aiogram.fsm.state import State, StatesGroup
from aiogram.fsm.storage.memory import MemoryStorage


class FSMWriteFinance(StatesGroup):
    fill_minus = State()
    fill_plus = State()

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


cfg: Config = load_config()

db: dict[int: dict[str: float]] = {}


async def main():

    bot = Bot(token=cfg.tg_bot.token, parse_mode='HTML')

    state = MemoryStorage()

    dp = Dispatcher(state=state)

    dp.include_router(user_handlers.router)
    dp.include_router(other_handlers.router)

    await set_main_menu(bot)
    await dp.start_polling(bot)

if __name__ == '__main__':
    asyncio.run(main())