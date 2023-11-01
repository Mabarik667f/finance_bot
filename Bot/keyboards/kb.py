from aiogram.types import (InlineKeyboardButton, KeyboardButton, ReplyKeyboardMarkup, InlineKeyboardMarkup)
from aiogram.utils.keyboard import InlineKeyboardBuilder, ReplyKeyboardBuilder
from Bot.lexicon.lexicon import LEXICON

# создание списка кнопок обычной клавиатуры
buttons_main_menu: list[KeyboardButton] = [KeyboardButton(text=LEXICON['expenses']),
                                           KeyboardButton(text=LEXICON['income'])]
kb_builder = ReplyKeyboardBuilder()

# заносим кнопки в builder
kb_builder.row(*buttons_main_menu, width=3)

# приводим builder к объекту клавиатуры
kb_main_menu_markup: ReplyKeyboardMarkup = kb_builder.as_markup(resize_keyboard=True, one_time_keyboard=True)

# создание списка кнопок inline клавиатуры для команды /stat
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

# заносим кнопки в inline_stat_builder
inline_stat_builder.row(*buttons_inline_stat, width=2)

# заносим кнопки в error_inline_builder - это inline кнопка для выхода из режимов записи
error_inline_builder.row(InlineKeyboardButton(text=LEXICON['error_format'],
                                              callback_data='cancel'))

# приводим inline_stat_builder к объекту inline клавиатуры
inline_stat_markup: InlineKeyboardMarkup = inline_stat_builder.as_markup()

# приводим error_stat_builder к объекту inline клавиатуры
error_markup: InlineKeyboardMarkup = error_inline_builder.as_markup()
