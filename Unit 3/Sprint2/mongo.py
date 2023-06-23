from cgitb import reset
import pymongo
from sqlite_ex import connect_to_sqlite, execute_query
import queries
from pprint import pprint


def connect_to_mongo(db_name):
    client = pymongo.MongoClient("mongodb+srv://rey:<password>@cluster0.nxqxanr.mongodb.net/?retryWrites=true&w=majority")
    db = client[db_name]
    return db



def build_character_dicts(character_tuples):
    """ Convert list of tupes to list of dicts"""
    result = []

    for tuple in character_tuples:
        result.append(build_character_dict(tuple))
    return result


def build_character_dict(character_tuple):
    """ convert single character tuple to dict"""
    d = {
        'character_id' : character_tuple[0],
        'name' : character_tuple[1],
        'level' : character_tuple[2],
        'exp' : character_tuple[3],
        'hp' : character_tuple[4],
        'strength' : character_tuple[5],
        'intelligence' : character_tuple[6],
        'dexterity' : character_tuple[7],
        'wisdom' : character_tuple[8],
        'items' : get_item_dict(character_tuple[0])
    }
    return d


def get_item_dict(character_id):
    conn = connect_to_sqlite()
    query = f"""
    SELECT ai*
    FROM charactercreator_character_inventory as ci
    JOIN armory_item as ai
        ON ai.item_id = ci.item_id
    WHERE ci.character_id = {character_id}
    """
    items_tuple = execute_query(conn, query)
    result = []
    for tuple in items_tuple:
        result.append(build_item_dict(tuple))
    return result


def build_item_dict(item_tuple):
    return {
        'item_id' : item_tuple[0],
        'name' : item_tuple[1],
        'value' : item_tuple[2],
        'weight' : item_tuple[3]
    }

if __name__ == '__main__':
    # Create mongo connection
    db = connect_to_mongo('rpg')
    # create sqlite conn
    sqlite_conn = connect_to_sqlite()
    # query for characer
    character_tuples = execute_query(sqlite_conn, queries.select_all_characters)
    pprint(character_tuples)
    # convert to dict
    character_dicts = build_character_dict(character_tuples)
    # insert into mongo
    # db.characters.insert_many(character_dicts)