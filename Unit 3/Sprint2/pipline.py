import psycopg2
from sqlite_ex import connect_to_sqlite
import Sprint2.queries as queries
from pprint import pprint


dbname = 'hgkwzbyh'
host = 'ruby.db.elephantsql.com'
user = 'hgkwzbyh'
password = 'K0MUJyR9fRmn1XNuF7Qlu8U8svJtGfCE'


def connect_to_pg():
    return psycopg2.connect(dbname=dbname, host=host,
                            user=user, password=password)


def execute_query(conn, query):
    cursor = conn.cursor()
    cursor.execute(query)
    return cursor.fetchall()


def execute_ddl(conn, query):
    cursor = conn.cursor()
    cursor.execute(query)


def insert_character_data(conn, character_data):
    insert_query = f"""
    INSERT INTO character(
        character_id,
        name,
        level,
        exp,
        hp,
        strength,
        intelligence,
        dexterity,
        wisdom
    )
    VALUES
    {','.join([str(row) for row in character_data])}
    """
    execute_ddl(conn, insert_query)


if __name__ == '__main__':
    sqlite_conn = connect_to_sqlite()

    character_data = execute_query(sqlite_conn, queries.select_all_characters)

    pg_conn = connect_to_pg()

    execute_ddl(pg_conn, queries.create_character_table)

    insert_character_data(pg_conn, character_data)

    pg_conn.commit()
