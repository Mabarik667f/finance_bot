from datetime import datetime, timedelta

from aiogram.types import CallbackQuery, Message

from lexicon.lexicon import LEXICON
from models.methods import get_finance_request

# дата сегодняшнего дня
default_date = datetime.today().strftime('%Y-%m-%d')


def get_date(days: int) -> str:
    """Высчитывает до какого момента времени собирать данные по дате"""
    df_date = datetime.strptime(default_date, '%Y-%m-%d')
    start_d = df_date - timedelta(days=days)
    start_date_formatted = start_d.strftime('%Y-%m-%d')

    return start_date_formatted


def get_stat_data(request: (CallbackQuery, Message),
                  start_date=default_date,
                  end_date=default_date) -> None:
    """Формирует данные за определённый период для вывода сообщения"""
    total_expense, total_income = get_finance_request(request.from_user.id,
                                                      start_date=start_date,
                                                      end_date=end_date)

    # Преобразование строк в объекты datetime
    start_d = datetime.strptime(start_date, "%Y-%m-%d")
    end_d = datetime.strptime(end_date, "%Y-%m-%d")

    # Расчет разницы между датами
    delta = end_d - start_d

    # Получение количества дней (с разницей в днях)
    number_of_days = delta.days
    if number_of_days != 0:
        total_inc = total_income / number_of_days
        total_exp = total_expense / number_of_days
    else:
        total_inc = total_income
        total_exp = total_expense

    # Если нет данных
    if total_expense == 0 and total_income == 0:
        LEXICON['cur_stat'] = LEXICON['no_data']
        return

    LEXICON['cur_stat'] = f'Средний доход 💰 за день: {round(total_inc, 1)}₽\n' \
                          f'Средний расход 💳 за день: {round(total_exp, 1)}₽\n' \
                          f'\n' \
                          f'Расход: {total_expense}₽\n' \
                          f'Доход: {total_income}₽\n'
