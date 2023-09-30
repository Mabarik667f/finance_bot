from aiogram import Router, F
from aiogram.exceptions import TelegramBadRequest
from aiogram.filters import CommandStart, Command, StateFilter
from aiogram.fsm.state import default_state
from aiogram.types import Message, CallbackQuery
from lexicon.lexicon import LEXICON
from keyboards.kb import kb_main_menu_markup, inline_stat_markup, error_markup
from bot import FSMWriteFinance
from aiogram.fsm.context import FSMContext
from models.methods import get_or_create_user, add_transaction
from services.services import get_stat_data, get_date


import re

router = Router()


@router.message(CommandStart(), StateFilter(default_state))
async def cmd_start(message: Message):
    """Вывод Приветствия и запись пользователя в бд"""

    get_or_create_user(message.from_user.id, message.from_user.first_name)

    await message.answer(text=LEXICON['/start'],
                         reply_markup=kb_main_menu_markup)


@router.message(Command(commands='help'), StateFilter(default_state))
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


@router.callback_query(F.data == 'cancel', StateFilter(default_state))
async def cmd_error_cancel(callback: CallbackQuery):
    await callback.answer(text=LEXICON['error_cancel'])


@router.callback_query(F.data == 'cancel', ~StateFilter(default_state))
async def cmd_cancel_command_state(callback: CallbackQuery, state: FSMContext):
    await callback.answer(
        text=LEXICON['/cancel']
    )

    await state.clear()


@router.message(Command(commands='day'), StateFilter(default_state))
async def cmd_selected_day(message: Message, state: FSMContext):
    await message.answer(text=LEXICON['selected_day'],
                         reply_markup=error_markup)

    await state.set_state(FSMWriteFinance.fill_day)


# обработчик выбора дня
@router.message(StateFilter(FSMWriteFinance.fill_day),
                lambda message: re.search(r'^\d{4}[-.]\d{2}[-.]\d{2}$', message.text.strip()))
async def cmd_selected_day_answer(message: Message):
    get_stat_data(message, start_date=message.text.strip(), end_date=message.text.strip())

    await message.answer(text=LEXICON['cur_stat'])


@router.message(StateFilter(FSMWriteFinance.fill_day))
async def cmd_error_selected_day_answer(message: Message):
    await message.answer(text=LEXICON['error_day_format'],
                         reply_markup=error_markup)


@router.message(Command(commands='date'), StateFilter(default_state))
async def cmd_selected_day(message: Message, state: FSMContext):
    await message.answer(text=LEXICON['selected_date'],
                         reply_markup=error_markup)

    await state.set_state(FSMWriteFinance.fill_date)


# обработчик выбора периода
@router.message(StateFilter(FSMWriteFinance.fill_date),
                lambda message: re.search(r'^\d{4}[-.]\d{2}[-.]\d{2}\s*,\s*\d{4}[-.]\d{2}[-.]\d{2}$',
                                          message.text.strip()))
async def cmd_selected_day_answer(message: Message):
    start, end = message.text.strip().split(',')
    get_stat_data(message, start_date=start, end_date=end)

    await message.answer(text=LEXICON['cur_stat'])


@router.message(StateFilter(FSMWriteFinance.fill_date))
async def cmd_error_selected_day_answer(message: Message):
    await message.answer(text=LEXICON['error_date_format'],
                         reply_markup=error_markup)


# Расход
@router.message(F.text == '- Статья расходов 💳')
async def cmd_expenses_process(message: Message, state: FSMContext):
    await message.answer(text=LEXICON['enter_expanses'])

    await state.set_state(FSMWriteFinance.fill_minus)


@router.message(StateFilter(FSMWriteFinance.fill_minus),
                lambda message: re.search(r'^-\s*\d+(\.\d+)?$', message.text.strip()))
async def cmd_expanses_process(message: Message):
    add_transaction(message.from_user.id,
                    income=message.text[1:].strip(),
                    transaction=2)  # 2 is expanse

    await message.answer(text=LEXICON['add_expanses'])


@router.message(StateFilter(FSMWriteFinance.fill_minus))
async def cmd_error_write_income(message: Message):
    await message.answer(text=LEXICON['error_add_expanses'],
                         reply_markup=error_markup)


# Доход
@router.message(F.text == '+ Статья доходов 💰')
async def cmd_income_process(message: Message, state: FSMContext):
    await message.answer(text=LEXICON['enter_income'])

    await state.set_state(FSMWriteFinance.fill_plus)


@router.message(StateFilter(FSMWriteFinance.fill_plus),
                lambda message: re.search(r'^\+\s*\d+(\.\d+)?$', message.text.strip()))
async def cmd_write_income(message: Message):
    add_transaction(message.from_user.id,
                    income=message.text[1:].strip(),
                    transaction=1)  # 1 is income

    await message.answer(text=LEXICON['add_income'])


@router.message(StateFilter(FSMWriteFinance.fill_plus))
async def cmd_error_write_income(message: Message):
    await message.answer(text=LEXICON['error_add_income'],
                         reply_markup=error_markup)


# Вывод кнопок для просмотра расхода
@router.message(Command('stat'), StateFilter(default_state))
async def cmd_stat_process(message: Message):
    await message.answer(text=LEXICON['/stat'],
                         reply_markup=inline_stat_markup)


@router.callback_query(F.data.in_(
    ['stat_year',
     'stat_month',
     'stat_week',
     'stat_day']), StateFilter(default_state))
async def cmd_date_process(callback: CallbackQuery):
    try:
        if callback.data == 'stat_year':
            get_stat_data(callback, end_date=get_date(365))
        elif callback.data == 'stat_month':
            get_stat_data(callback, end_date=get_date(30))
        elif callback.data == 'stat_week':
            get_stat_data(callback, end_date=get_date(7))
        elif callback.data == 'stat_day':
            get_stat_data(callback)
        await callback.message.edit_text(text=LEXICON['cur_stat'],
                                         reply_markup=inline_stat_markup)
    except TelegramBadRequest:
        await callback.answer()
