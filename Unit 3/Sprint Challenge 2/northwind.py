import sqlite3

expensive_items = """
SELECT *
FROM Product
ORDER BY UnitPrice DESC
LIMIT 10
"""

avg_hire_age = """
SELECT avg(HireDate - BirthDate)
FROM Employee
"""

ten_most_expensive = """
SELECT ProductName, UnitPrice, CompanyName
FROM Product
INNER JOIN Supplier
ON Product.SupplierId = Supplier.Id
ORDER BY UnitPrice DESC
LIMIT 10
"""

largest_category = """
SELECT c.CategoryName, COUNT(DISTINCT p.Id)
FROM Category c, Product p WHERE c.Id = p.CategoryId
GROUP BY 1 ORDER BY 2 DESC LIMIT 1
"""


def connect_to_sqlite(db='northwind_small.sqlite3'):
    return sqlite3.connect(db)


def execute_query(conn, query):
    cur = conn.cursor()
    cur.execute(query)
    return cur.fetchall()


if __name__ == '__main__':
    sq_conn = connect_to_sqlite()
    execute_query(sq_conn, expensive_items)
    execute_query(sq_conn, avg_hire_age)

    sq_conn.commit()
