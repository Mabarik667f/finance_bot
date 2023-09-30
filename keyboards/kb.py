from aiogram.filters.callback_data import CallbackData
from aiogram.types import (InlineKeyboardButton, InlineKeyboardMarkup,
                           KeyboardButton, ReplyKeyboardMarkup)
from aiogram.utils.keyboard import InlineKeyboardBuilder, ReplyKeyboardBuilder
from lexicon.lexicon import LEXICON

buttons_main_menu: list[KeyboardButton] = [KeyboardButton(text=LEXICON['expenses']),
                                           KeyboardButton(text=LEXICON['income'])]
kb_builder = ReplyKeyboardBuilder()

kb_builder.row(*buttons_main_menu, width=3)

kb_main_menu_markup: ReplyKeyboardMarkup = kb_builder.as_markup(resize_keyboard=True, one_time_keyboard=True)

buttons_inline_stat: list[InlineKeyboardButton] = [InlineKeyboardButton(text=LEXICON['stat_day'],
                                                                        callback_data='stat_day'),
                                                   InlineKeyboardButton(text=LEXICON['stat_week'],
                                                                        callback_data='stat_week'),
                                                   InlineKeyboardButton(text=LEXICON['stat_month'],
                                                                        callback_data='stat_month'),
                                                   InlineKeyboardButton(text=LEXICON['stat_year'],
                                                                        callback_data='stat_year'),

                                                   ]

inline_stat_builder = InlineKeyboardBuilder()
error_inline_builder = InlineKeyboardBuilder()

inline_stat_builder.row(*buttons_inline_stat, width=2)
error_inline_builder.row(InlineKeyboardButton(text=LEXICON['error_format'],
                                              callback_data='cancel'))

inline_stat_markup = inline_stat_builder.as_markup()
error_markup = error_inline_builder.as_markup()
