from aiogram import Router
from aiogram.filters import CommandStart, Command
from aiogram.types import Message

router = Router()


@router.message(CommandStart())
async def cmd_start(message: Message):
    """Вывод Приветствия и запись пользователя в бд"""
    await message.answer('Привет!')


@router.message(Command('help'))
async def cmd_help(message: Message):
    """Вывод списка команд, описание работы бота"""
    await message.answer('Вот что я умею: \n/start')
