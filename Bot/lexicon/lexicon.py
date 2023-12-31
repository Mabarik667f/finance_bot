LEXICON: dict[str: str] = {
    'unknown': 'Я тебя не понимаю\n'
               '\n'
               'Нажми /help или загляни в меню,\n'
               'чтобы узнать, что я умею',
    '/start': 'Привет! Я твой личный финансовый помощник!\n'
              '\n'
              'Нажми /help или загляни в меню,\n'
              'чтобы узнать, что я умею',
    '/help': 'Вот что я умею:\n'
             '\n'
             '/help - Помощь\n'
             '/cancel - Выход из режима записи\n'
             '/stat - Выбор категорию просмотра статистики\n'
             '/day - Выбор дня для просмотра статистики\n'
             '/date - Выбор даты для просмотра статистики',
    '/stat': 'Выберите за какой период вывести соотношение расхода и дохода',
    '/cancel': '✅ Вы вышли из режима записи',
    'income': '+ Статья доходов 💰',
    'enter_income': '💰 Напишите статью дохода в формате: <b><i>+число</i></b>',
    'add_income': 'Доход обновлен',
    'expenses': '- Статья расходов 💳',
    'enter_expanses': '💳 Напишите статью расхода в формате: <b><i>-число</i></b>',
    'add_expanses': 'Расход обновлен',
    'stat_day': 'День ✅',
    'stat_week': 'Неделя ✅',
    'stat_month': 'Месяц ✅',
    'stat_year': 'Год ✅',
    'selected_day': 'Напишите день в формате <b><i>год-месяц-день</i></b>\n'
                    '\n'
                    'Например: <b><i>2023-09-30</i></b>',
    'selected_date': 'Напишите дату в формате <b><i>год-месяц-день, год-месяц-день</i></b>\n'
                    '\n'
                    'Например: <b><i>2022-07-12, 2023-05-30</i></b>\n',
    'no_register': '❌ Вы не зарегистрировались в базе данных.\n'
                   '\n'
                   '/cancel чтобы выйти из режима записи дохода и расхода\n'
                   '/start регистрация в бд\n',
    'error_add_income': '❌ Вы записываете доход в неправильном формате.\n'
                        'Используйте формат <b><i>+число</i></b>\n'
                        '\n'
                        'Нажмите на кнопку или введите команду /cancel,\n'
                        'чтобы выйти из режима записи',
    'error_add_expanses': '❌ Вы записываете расход в неправильном формате.\n'
                          'Используйте формат <b><i>-число</i></b>\n'
                          '\n'
                          'Нажмите на кнопку или введите команду /cancel,\n'
                          'чтобы выйти из режима записи',
    'no_data': '❌ Нет данных за указанный период',
    'error_cancel': '❌ Вы не находитесь в режиме записи\n',
    'error_day_format': '❌ Вы записываете день в неправильном формате.\n'
                        '\n'
                        'Используйте формат <b><i>год-месяц-день</i></b>\n'
                        'Например: <b><i>2023-09-30</i></b>\n'
                        '\n'
                        'Нажмите на кнопку или введите команду /cancel,\n'
                        'чтобы выйти из режима записи',
    'error_date_format': '❌ Вы записываете дату в неправильном формате.\n'
                         '\n'
                         'Используйте формат <b><i>год-месяц-день, год-месяц-день</i></b>\n'
                         'Например: <b><i>2022-07-12, 2023-05-30</i></b>\n'
                         '\n'
                         'Нажмите на кнопку или введите команду /cancel,\n'
                         'чтобы выйти из режима записи',
    'error_format': '❌ Выйти из режима записи',
    'cur_stat': '',
}

LEXICON_COMMANDS: dict[str: str] = {

    '/help': 'Справка по работе бота',
    '/cancel': 'Выход из режима учёта доходов и расходов',
    '/stat': 'Просмотр статистики за выбранный период',
    '/day': 'Выбор дня для просмотра статистики',
    '/date': 'Выбор даты для просмотра статистики',

}
