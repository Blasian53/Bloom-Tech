from pprint import pprint
import sqlite3
from unittest import result
import queries


def connect_to_sqlite(db="rpg_db.sqlite3"):
    return sqlite3.connect(db)


def execute_query(conn, query):
    cursor = conn.cursor()
    cursor.execute(query)
    results = cursor.fetchall()
    return results



if __name__ == '__main__':
    conn = connect_to_sqlite()
    results = execute_query(conn, queries.select_all_characters)
    pprint(results)
