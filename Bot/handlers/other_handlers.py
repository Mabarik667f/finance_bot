from aiogram import Router
from aiogram.types import Message
from Bot.lexicon.lexicon import LEXICON


router = Router()


@router.message()
async def process_unknown_command(message: Message):
    await message.answer(text=LEXICON['unknown'])
