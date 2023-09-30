from datetime import datetime

from peewee import *
from config_data.config import load_config

cfg = load_config()

db = MySQLDatabase(cfg.db.db_name, user=cfg.db.db_user, password=cfg.db.db_password)


class BaseDataBase(Model):

    class Meta:
        database = db


class User(BaseDataBase):
    id = IntegerField(primary_key=True)
    name = CharField(max_length=45)

    class Meta:
        table_name = 'users'


class TypeOfTransaction(BaseDataBase):
    name = CharField(max_length=20)

    class Meta:
        table_name = 'type_of_transaction'


class Transaction(BaseDataBase):
    amount = DecimalField(10, 2)
    transaction_date = DateField(default=datetime.today().strftime('%Y-%m-%d'))
    user = ForeignKeyField(User)
    type_of_transaction = ForeignKeyField(TypeOfTransaction)

    class Meta:
        table_name = 'transactions'

#
# db.connect()
#
# db.create_tables([User, TypeOfTransaction, Transaction])
