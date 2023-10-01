import asyncio

from config_data.config import Config, load_config
from aiogram import Bot, Dispatcher
from handlers import user_handlers, other_handlers
from keyboards.main_menu import set_main_menu
from aiogram.fsm.state import State, StatesGroup
from aiogram.fsm.storage.memory import MemoryStorage


class FSMWriteFinance(StatesGroup):
    """Инициализируем состояния для машины состояния"""
    fill_minus = State()  # режим записи расхода
    fill_plus = State()  # режим записи дохода
    fill_day = State()  # режим просмотра статистики за выбранный день
    fill_date = State()  # режим просмотра статистики за выбранный период времени


cfg: Config = load_config()  # загрузка конфига


async def main():
    """Основные команды для запуска бота"""

    bot = Bot(token=cfg.tg_bot.token, parse_mode='HTML')

    state = MemoryStorage()  # создаём хранилище состояний

    dp = Dispatcher(state=state)

    # подключаем роутеры хендлеров к боту
    dp.include_router(user_handlers.router)
    dp.include_router(other_handlers.router)

    await set_main_menu(bot)  # подключаем меню
    await dp.start_polling(bot)  # подключаем опрос telegram requests


if __name__ == '__main__':
    asyncio.run(main())  # запуск бота
