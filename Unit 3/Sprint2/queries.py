select_all_characters = """
SELECT *
FROM charactercreator_character
"""

create_character_table = """
CREATE TABLE IF NOT EXISTS character (
    character_id SERIAL PRIMARY KEY,
    name VARCHAR(30) NOT NULL,
    level INT NOT NULL,
    exp INT NOT NULL,
    hp INT NOT NULL,
    strength INT NOT NULL,
    intelligence INT NOT NULL,
    dexterity INT NOT NULL,
    wisdom INT NOT NULL
)
"""

create_titanic_table = """
CREATE TABLE IF NOT EXISTS titanic (
    survived BOOL NOT NULL,
    pclass INT NOT NULL,
    name VARCHAR(30) NOT NULL,
    sex VARCHAR(10) NOT NULL,
    age INT NOT NULL,
    sib_spouses INT NOT NULL,
    par_children INT NOT NULL,
    fare FLOAT NOT NULL
)
"""


create_demo_table = """
CREATE TABLE IF NOT EXISTS demo (
    S
)
"""