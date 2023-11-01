from .models import *


def get_or_create_user(id_user: int, name: str) -> None:
    """Создаём пользователя в базе данных, если его там нет,
    иначе игнорируем """
    # db.connect()

    User.get_or_create(
        id=id_user,
        name=name
    )
    # db.close()


def add_transaction(id_user: int, income: (float, int), transaction) -> None:
    """Добавляем запись дохода или расхода пользователя в раздел транзакций"""
    # db.connect()

    Transaction.create(
        amount=income,
        user=id_user,
        type_of_transaction=transaction)

    # db.close()


def get_finance_request(user_id: int,
                        start_date: str,
                        end_date: str) -> tuple:
    """Забираем данные о доходе и расходе за определённое время"""
    # db.connect()

    # сумма расходов
    total_expanse = Transaction.select(fn.SUM(Transaction.amount)).where(
        (Transaction.user_id == user_id) &  # выбор нужного пользователя
        (Transaction.type_of_transaction_id == 2) &  # выбор категории расхода
        (Transaction.transaction_date >= start_date) &  # период больше или равной начальной дате
        (Transaction.transaction_date <= end_date)).scalar() or 0  # период меньше или равной начальной дате

    # сумма доходов
    total_income = Transaction.select(fn.SUM(Transaction.amount)).where(
        (Transaction.user_id == user_id) &  # выбор нужного пользователя
        (Transaction.type_of_transaction_id == 1) &  # выбор категории дохода
        (Transaction.transaction_date >= start_date) &  # период больше или равной начальной дате
        (Transaction.transaction_date <= end_date)).scalar() or 0  # период меньше или равной начальной дате

    # db.close()

    return total_expanse, total_income
