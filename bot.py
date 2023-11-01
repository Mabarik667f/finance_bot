import asyncio
import logging


from aiogram.fsm.storage.redis import RedisStorage, Redis
from Bot.config_data.config import Config, load_config
from aiogram import Bot, Dispatcher
from Bot.handlers import user_handlers, other_handlers
from Bot.keyboards.main_menu import set_main_menu
from aiogram.fsm.state import State, StatesGroup
from aiogram.fsm.storage.memory import MemoryStorage


# Инициализируем logger
logger = logging.getLogger(__name__)


class FSMWriteFinance(StatesGroup):
    """Инициализируем состояния для машины состояния"""
    fill_minus = State()  # режим записи расхода
    fill_plus = State()  # режим записи дохода
    fill_day = State()  # режим просмотра статистики за выбранный день
    fill_date = State()  # режим просмотра статистики за выбранный период времени


cfg: Config = load_config()  # загрузка конфига


redis = Redis(host=cfg.db.db_host)

storage = RedisStorage(redis=redis)


async def main():
    """Основные команды для запуска бота"""

    # Конфигурируем логирование
    logging.basicConfig(
        level=logging.INFO,
        format='%(filename)s:%(lineno)d #%(levelname)-8s '
               '[%(asctime)s] - %(name)s - %(message)s'
    )

    # Стартовое сообщение о начала логирования
    logger.info('Starting bot')

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
