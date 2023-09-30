from datetime import datetime, timedelta

from aiogram.types import CallbackQuery, Message

from lexicon.lexicon import LEXICON
from models.methods import get_finance_request

default_date = datetime.today().strftime('%Y-%m-%d')


def get_date(days: int) -> str:
    df_date = datetime.strptime(default_date, '%Y-%m-%d')
    end_d = df_date + timedelta(days=days)
    end_date_formatted = end_d.strftime('%Y-%m-%d')

    return end_date_formatted


def get_stat_data(request: (CallbackQuery, Message),
                  start_date=default_date,
                  end_date=default_date) -> None:
    total_expense, total_income = get_finance_request(request.from_user.id,
                                                      start_date=start_date,
                                                      end_date=end_date)

    if total_expense != 0:
        ratio = total_income / total_expense
        ratio = round(ratio * 100, 2)
    else:
        ratio = 0

    if total_expense == 0 and total_income == 0:
        LEXICON['cur_stat'] = LEXICON['no_data']
        return

    LEXICON['cur_stat'] = f'Cоотношение расхода и дохода за выбранный период ⌚: {ratio}% \n' \
                          f'\n' \
                          f'Расход: {total_expense}₽\n' \
                          f'Доход: {total_income}₽\n'
