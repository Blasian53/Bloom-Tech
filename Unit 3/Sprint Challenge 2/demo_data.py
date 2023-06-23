import sqlite3

row_count = """
    SELECT count(*)
    FROM demo
"""

xy_at_least_5 = """
    SELECT count(*)
    FROM demo
    WHERE x >= 5 and y >= 5
"""

unique_y = """
    SELECT count(DISTINCT(y))
    FROM demo
"""

create_demo_table = """
CREATE TABLE demo (
s char,
x INTEGER,
y INTEGER
)
"""

insert_into_demo_table = """
    INSERT INTO demo
    VALUES ('g', 3, 9), ('v', 5, 7), ('f', 8, 7)
"""


def connect_to_sqlite(db='demo_data.sqlite3'):
    return sqlite3.connect(db)


def execute_query(conn, query):
    cur = conn.cursor()
    cur.execute(query)
    return cur.fetchall()


if __name__ == '__main__':
    sq_conn = connect_to_sqlite()
    execute_query(sq_conn, create_demo_table)
    execute_query(sq_conn, insert_into_demo_table)
    sq_conn.commit()
