from sqlalchemy import create_engine, text

# создаем объект для обращения к базе данных
engine = create_engine("sqlite+pysqlite:///:memory:",echo=True)

# обычный контексный менеджер к базе данных
with engine.connect() as conn:
    # создаем таблицу с колонками x,y в базе данных
    conn.execute(text("CREATE TABLE some_table (x int, y int)"))
    # добавляем в колонки x и y
    conn.execute(
        text("INSERT INTO some_table (x,y) VALUES (:x,:y)"),
        [{"x":1,"y":1},{"x":2,"y":4}],
    )
    conn.commit()
# begin делает автокоммит
with engine.begin() as conn:
    conn.execute(
        text("INSERT INTO some_table (x, y) VALUES (:x, :y)"),
        [{"x": 6, "y": 8}, {"x": 9, "y": 10}],
    )

# with engine.connect() as conn:
#     result = conn.execute(text("SELECT x, y FROM some_table"))

    # Прямая итерация по объекту Result
    # for row in result:
    #     print(f"x:{row.x} y:{row.y}")

    # Получение в виде кортежа
    # for x, y in result:
    #     print(f"x:{x} y:{y}")

    # Получение данных по индексу
    # for row in result:
    #     x = row[0]

    # Получение данных по имени
    # for row in result:
    #     y = row.y
    #     print(f"Row: {row.x} {y}")

    # Получение в виде ассоциативных массивов (карт)
    # for row in result.mappings():
    #     x = row["x"]
    #     y = row["y"]
    #     print(f"x:{x} y:{y}")

# параметризация запросов
# with engine.connect() as conn:
#     result = conn.execute(text("select x, y from some_table where y > :y"), {"y": 2})
#     for row in result:
#         print(f"x:{row.x} y:{row.y}")   

# множественная параметризация
# stmt = text("INSERT INTO some_table (x, y) VALUES (:x,:y)")
# tablet = [{"x": 11, "y": 12}, {"x": 13, "y": 14}]
# with engine.connect() as conn:
#     conn.execute(stmt,tablet,)
#     conn.commit()

# Выполнение с помощью ORM Session
from sqlalchemy.orm import Session

with Session(engine) as session:
    result = session.execute(
        # обновить в таблице  Y при определенном X
        text("UPDATE some_table SET y=:y WHERE x=:x"),
        [{"x":9,"y":11},{"x":6,"y":15}]
    )
    session.commit()
# отобразить в таблице все что больше по Y и отсортировать сначала по Y потом по X
stmt = text("SELECT x , y FROM some_table WHERE y > :y ORDER BY y , x")

with Session(engine) as session:
    result = session.execute(stmt, {"y": 0})
    for row in result:
        print(f"x: {row.x} y: {row.y}")


