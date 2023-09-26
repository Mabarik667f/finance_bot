from copy import deepcopy

from aiogram import Router, F
from aiogram.filters import CommandStart, Command, StateFilter
from aiogram.fsm.state import default_state
from aiogram.types import Message, CallbackQuery
from lexicon.lexicon import LEXICON
from keyboards.kb import kb_main_menu_markup, inline_stat_markup
from bot import db, FSMWriteFinance, user_dict_template
from aiogram.fsm.context import FSMContext
import re

router = Router()


@router.message(CommandStart(), StateFilter(default_state))
async def cmd_start(message: Message):
    """Вывод Приветствия и запись пользователя в бд"""
    if message.from_user.id not in db:
        db[message.from_user.id] = deepcopy(user_dict_template)
    print(db[message.from_user.id]['income'])
    await message.answer(text=LEXICON['/start'],
                         reply_markup=kb_main_menu_markup)


@router.message(Command('help'), StateFilter(default_state))
async def cmd_help(message: Message):
    """Вывод списка команд, описание работы бота"""
    await message.answer(text=LEXICON['/help'])


@router.message(Command(commands='cancel'), StateFilter(default_state))
async def cmd_error_cancel(message: Message):

    await message.answer(text=LEXICON['error_cancel'])


@router.message(Command(commands='cancel'), ~StateFilter(default_state))
async def cmd_cancel_command_state(message: Message, state: FSMContext):
    await message.answer(
        text=LEXICON['/cancel']
    )

    await state.clear()


# Расход
@router.message(F.text == '- Статья расходов 💳')
async def cmd_expenses_process(message: Message, state: FSMContext):
    await message.answer(text=LEXICON['enter_expanses'])

    await state.set_state(FSMWriteFinance.fill_minus)


@router.message(StateFilter(FSMWriteFinance.fill_minus),
                lambda message: re.search(r'^-\s*\d+(\.\d+)?$', message.text.strip()))
async def cmd_expanses_process(message: Message):
    if db.get(message.from_user.id):
        db[message.from_user.id]['expanses'] += float(message.text[1:])

        await message.answer(text=LEXICON['add_expanses'])
    else:
        await message.answer(text=LEXICON['no_register'])


@router.message(StateFilter(FSMWriteFinance.fill_minus))
async def cmd_error_write_income(message: Message):
    await message.answer(text=LEXICON['error_add_expanses'])


# Доход
@router.message(F.text == '+ Статья доходов 💰')
async def cmd_income_process(message: Message, state: FSMContext):
    await message.answer(text=LEXICON['enter_income'])

    await state.set_state(FSMWriteFinance.fill_plus)


@router.message(StateFilter(FSMWriteFinance.fill_plus),
                       lambda message: re.search(r'^\+\s*\d+(\.\d+)?$', message.text.strip()))
async def cmd_write_income(message: Message):
    if db.get(message.from_user.id):
        db[message.from_user.id]['income'] += float(message.text[1:])

        await message.answer(text=LEXICON['add_income'])
    else:
        await message.answer(text=LEXICON['no_register'])


@router.message(StateFilter(FSMWriteFinance.fill_plus))
async def cmd_error_write_income(message: Message):
    await message.answer(text=LEXICON['error_add_income'])


# Вывод кнопок для просмотра расхода
@router.message(Command('stat'), StateFilter(default_state))
async def cmd_stat_process(message: Message):

    await message.answer(text=LEXICON['/stat'],
                         reply_markup=inline_stat_markup)


@router.callback_query(F.data == 'stat_day', StateFilter(default_state))
async def cmd_day_process(callback: CallbackQuery):
    await callback.answer()


@router.callback_query(F.data == 'stat_week', StateFilter(default_state))
async def cmd_week_process(callback: CallbackQuery):
    await callback.answer()


@router.callback_query(F.data == 'stat_month', StateFilter(default_state))
async def cmd_month_process(callback: CallbackQuery):
    await callback.answer()


@router.callback_query(F.data == 'stat_year', StateFilter(default_state))
async def cmd_year_process(callback: CallbackQuery):
    await callback.answer()