from datetime import datetime

from peewee import *
from config_data.config import load_config

# Загружаем конфиг
cfg = load_config()

# Инициализируем базу данных
db = MySQLDatabase(cfg.db.db_name, user=cfg.db.db_user, password=cfg.db.db_password)


class BaseDataBase(Model):
    """Базовая модель, для упрощения кода"""
    class Meta:
        database = db


class User(BaseDataBase):
    """Модель для пользователей"""
    id = IntegerField(primary_key=True)
    name = CharField(max_length=45)

    class Meta:
        table_name = 'users'


class TypeOfTransaction(BaseDataBase):
    """Модель для Типов транзакций"""
    name = CharField(max_length=20)

    class Meta:
        table_name = 'type_of_transaction'


class Transaction(BaseDataBase):
    """Модель для транзакций"""
    amount = DecimalField(10, 1)
    transaction_date = DateField(default=datetime.today().strftime('%Y-%m-%d'))
    user = ForeignKeyField(User)
    type_of_transaction = ForeignKeyField(TypeOfTransaction)

    class Meta:
        table_name = 'transactions'


db.connect()

# Создаём таблицы, если они не были созданы
db.create_tables([User, TypeOfTransaction, Transaction])

db.close()