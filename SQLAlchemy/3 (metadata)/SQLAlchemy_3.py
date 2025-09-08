# Настройка метаданных с объектами таблиц
from sqlalchemy import MetaData
from sqlalchemy import Table, Column, Integer, String, ForeignKey
from sqlalchemy import create_engine

engine = create_engine("sqlite+pysqlite:///:memory:",echo=True)

metadata_obj = MetaData()

user_table = Table(
    "user_account",
    metadata_obj,
    Column("id",Integer,primary_key=True),
    Column("name",String(30)),
    Column("fullname",String),
)

# Column("name", String(length=30), table=<user_account>)
# user_table.c.name
# user_table.c.keys()

address_table = Table(
    "adress",
    metadata_obj,
    Column("id",Integer,primary_key=True),
    Column("user_id", ForeignKey("user_account.id"),nullable=False),
    Column("email_address",String,nullable=False),
)

# вызываем метод create_all в нашем объекте metadata_obj
metadata_obj.create_all(engine)
print(address_table.c.id)
# удаляет в обратном порядке
metadata_obj.drop_all(engine)
# функции CREATE/DROP ALL полезны для тестов,
# маленьких приложений, либо для приложений с короткоживущей
# базой данных. Для работы с уже более сложными базами данных
# строго рекомендуется использовать такую утилиту для миграций как
# Alembic.
