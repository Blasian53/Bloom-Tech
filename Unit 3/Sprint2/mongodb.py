from distutils.util import execute
import pymongo
import sqlite3


def connect_to_mongol(db_name):
    client = pymongo.MongoClient("mongodb+srv://rey:mwhnWRqfUlwmR8Af@cluster0.nxqxanr.mongodb.net/?retryWrites=true&w=majority")
    db = client[db_name]
    return db


def connect_to_sq(db="rpg_db.sqlite3"):
    return sqlite3.connect(db)


def execute_query(conn, query):
    return conn.execute(query).fetchall()


def doc_creation(db, curs, character_table_query, item_table_query, weapon_table_query):
    weapons = execute_query(curs, weapon_table_query)
    characters = execute_query(curs, character_table_query)

    for char in characters:
        item_character_query = item_table_query.format("\'%s\'" % char[1])
        item_names = execute_query(curs, item_character_query)
        weapon_names = []
        for item in item_names:
            if item in weapons:
                weapon_names.append(item[0])
            
        document = {
        'character_id' : char[0],
        'name' : char[1],
        'level' : char[2],
        'exp' : char[3],
        'hp' : char[4],
        'strength' : char[5],
        'intelligence' : char[6],
        'dexterity' : char[7],
        'wisdom' : char[8],
        'items' : item_names,
        'weapons' : weapon_names
        }



def show_all(db):
    all_docs = list(db.find())
    return all_docs



GET_CHARACTER_TABLE = """
SELECT *
FROM charactercreator_character
"""

GET_ITEM_TABLE = """
SELECT ai.name as item_name
FROM (SELECT *
FROM charactercreator_character as cc
INNER JOIN charactercreator_character_inventory as ci
	ON ci.character_id = cc.character_id ) as char_ci
INNER JOIN armory_item as ai
	ON ai.item_id = char_ci.item_id
AND char_ci.name = {}
"""

GET_WEAPON_TABLE = """
SELECT aw_ai.name
FROM (
SELECT *
FROM armory_item as ai
INNER JOIN armory_weapon as aw
	ON aw.item_ptr_id = ai.item_id ) as aw_ai
INNER JOIN (
SELECT *
FROM charactercreator_character as cc
INNER JOIN charactercreator_character_inventory as ci
	ON cc.character_id = ci.character_id ) as char_ci
WHERE aw_ai.item_id = char_ci.item_id

"""


if __name__ == '__main__':
    client = connect_to_mongol('rpg_data')
    sl_conn = connect_to_sq()
    sl_curs = sl_conn.cursor()

    db = client.rpg_data.rpg_data
    db.drop({})
    doc_creation(db, sl_curs, GET_CHARACTER_TABLE,GET_ITEM_TABLE,GET_WEAPON_TABLE)

    print(show_all(db))

