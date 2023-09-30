from .models import *


def get_or_create_user(id_user: int, name: str) -> None:

    db.connect()

    User.get_or_create(
        id=id_user,
        name=name
    )
    db.close()


def add_transaction(id_user: int, income: (float, int), transaction) -> None:

    db.connect()

    Transaction.create(
        amount=income,
        user=id_user,
        type_of_transaction=transaction)

    db.close()


def get_finance_request(user_id: int,
                        start_date: str,
                        end_date: str) -> tuple:
    db.connect()

    total_expanse = Transaction.select(fn.SUM(Transaction.amount)).where(
        (Transaction.user_id == user_id) &
        (Transaction.type_of_transaction_id == 2) &
        (Transaction.transaction_date >= start_date) &
        (Transaction.transaction_date <= end_date)).scalar() or 0

    total_income = Transaction.select(fn.SUM(Transaction.amount)).where(
        (Transaction.user_id == 1575269140) &
        (Transaction.type_of_transaction_id == 1) &
        (Transaction.transaction_date >= start_date) &
        (Transaction.transaction_date <= end_date)).scalar() or 0

    db.close()

    return total_expanse, total_income
