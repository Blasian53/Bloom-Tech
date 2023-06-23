import psycopg2
import queries
from sqlite_ex import connect_to_sqlite


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


def insert_titanic_data(conn, titanic_data):
    insert_query = f"""
    INSERT INTO titanic (
        survived,
        pclass,
        name,
        sex,
        age,
        sib_spouses,
        par_children,
        fare
    VALUES
    {','.join([str(row) for row in titanic_data])}
    )
    """
    for index, row in df.iterrows():
        row_tuple = (
            row['Survived'],
            row['Pclass'],
            row['Name'],
            row['Sex'],
            row['Age'],
            row['Siblings/Spouses Aboard'],
            row['Parents/Children Aboard'],
            row['Fare']
        )

    execute_ddl(conn, insert_query)


if __name__ == '__main__':
    sqlite_conn = connect_to_sqlite()

    titanic_data = execute_query(sqlite_conn, queries.select_all_characters)

    pg_conn = connect_to_pg()

    execute_ddl(pg_conn, queries.create_titanic_table)

    insert_titanic_data(pg_conn, titanic_data)
    
    pg_conn.commit()
