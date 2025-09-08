from sqlalchemy import MetaData, create_engine, insert
from sqlalchemy import Column, Table, Integer, String, ForeignKey
from sqlalchemy.dialects import sqlite, postgresql, mysql, oracle, mssql


engine = create_engine("sqlite+pysqlite:///:memory:", echo=True)

metadata = MetaData()

users_table = Table(
    "users",
    metadata,
    Column("id", Integer, primary_key=True, unique=True, autoincrement=True),
    Column("name", String(30)),
    Column("fullname", String),
)

addresses_table = Table(
    "addresses",
    metadata,
    Column("id", Integer, primary_key=True, unique=True, autoincrement=True),
    Column("email_addresses", String(30)),
    Column("user_id", Integer, ForeignKey("users.id")),
)

metadata.create_all(engine)

stmt = insert(users_table).values(name="Seva", fullname="Vsevolod")
stmt_wo_values = insert(users_table)

sqlite_stmt = stmt_wo_values.compile(engine, sqlite.dialect())
postgresql_stmt = stmt_wo_values.compile(engine, postgresql.dialect())
# print(stmt.compile(engine, mysql.dialect()))
# print(stmt.compile(engine, oracle.dialect()))
# print(stmt.compile(engine, mssql.dialect()))

with engine.begin() as conn:  # Connection
    result = conn.execute(
        stmt_wo_values,
        [
            {"name": "Oleg", "fullname": "Papirosov"},
            {"name": "Maria", "fullname": "Adler"},
            {"name": "Konstantin", "fullname": "Ebaklak"},
        ],
    )
