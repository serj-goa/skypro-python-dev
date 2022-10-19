ALL_TABLE_REQUESTS = {
    'animal_breeds': 'fk_id SERIAL PRIMARY KEY, '
                     'breed VARCHAR(25) NOT NULL',

    'animal_colors': 'fk_id SERIAL PRIMARY KEY, '
                     'color VARCHAR(15) NOT NULL',

    'outcome_subtypes': 'fk_id SERIAL PRIMARY KEY, '
                        'outcome_subtype VARCHAR(25) NOT NULL',

    'outcome_types': 'fk_id SERIAL PRIMARY KEY, '
                     'outcome_type VARCHAR(25) NOT NULL',

    'animals': 'animal_id VARCHAR(10) PRIMARY KEY, '
               'animal_type VARCHAR(15) NOT NULL, '
               'name VARCHAR(20), '
               'fk_animal_breed INTEGER, '
               'fk_animal_color_1 INTEGER NOT NULL, '
               'fk_animal_color_2 INTEGER, '
               'date_of_birth TIMESTAMP, '
               'FOREIGN KEY (fk_animal_breed) REFERENCES animal_breeds (fk_id), '
               'FOREIGN KEY (fk_animal_color_1) REFERENCES animal_colors (fk_id), '
               'FOREIGN KEY (fk_animal_color_2) REFERENCES animal_colors (fk_id)',

    'shelter_info': 'pk_id SERIAL PRIMARY KEY, '
                    'animal_id VARCHAR(10) NOT NULL, '
                    'fk_outcome_subtype INTEGER, '
                    'outcome_month INTEGER, '
                    'outcome_year INTEGER, '
                    'fk_outcome_type INTEGER, '
                    'age_upon_outcome VARCHAR(50), '
                    'FOREIGN KEY (animal_id) REFERENCES animals (animal_id), '
                    'FOREIGN KEY (fk_outcome_subtype) REFERENCES outcome_subtypes (fk_id), '
                    'FOREIGN KEY (fk_outcome_type) REFERENCES outcome_types (fk_id)'
}


def generate_table_request(table_name: str, values: str) -> str:
    return f'CREATE TABLE IF NOT EXISTS {table_name} ({values})'


def req_insert_animals(values: tuple) -> str:

    animal_id, animal_type, name, fk_animal_breed, fk_animal_color_1, fk_animal_color_2, date_of_birth = values

    fk_animal_breed = int(fk_animal_breed)
    fk_animal_color_1 = int(fk_animal_color_1)
    fk_animal_color_2 = int(fk_animal_color_2) if type(fk_animal_color_2) == int else 'NULL'

    return f"""
        INSERT INTO animals 
            (animal_id, animal_type, name, fk_animal_breed, fk_animal_color_1, fk_animal_color_2, date_of_birth)
        VALUES 
            ('{animal_id}', '{animal_type}', '{name}', {fk_animal_breed}, {fk_animal_color_1}, {fk_animal_color_2}, '{date_of_birth}')
    """


def req_insert_animal_breeds(value: str) -> str:
    return f"""
        INSERT INTO 
            animal_breeds (breed)
        VALUES ('{value}')
    """


def req_insert_animal_colors(value: str) -> str:
    return f"""
        INSERT INTO animal_colors (color)
        VALUES ('{value}')
    """


def req_insert_outcome_subtypes(value: str) -> str:
    return f"""
        INSERT INTO outcome_subtypes (outcome_subtype)
        VALUES ('{value}')
    """


def req_insert_outcome_types(value: str) -> str:
    return f"""
        INSERT INTO outcome_types (outcome_type)
        VALUES ('{value}')
    """


def req_insert_shelter_info(values: tuple) -> str:

    animal_id, fk_outcome_subtype, outcome_month, outcome_year, fk_outcome_type, age_upon_outcome = values

    fk_outcome_subtype = int(fk_outcome_subtype)
    outcome_month = int(outcome_month)
    outcome_year = int(outcome_year)
    fk_outcome_type = int(fk_outcome_type)

    return f"""
        INSERT INTO shelter_info 
            (animal_id, fk_outcome_subtype, outcome_month, outcome_year, fk_outcome_type, age_upon_outcome)
        VALUES 
            ('{animal_id}', {fk_outcome_subtype}, {outcome_month}, 
            {outcome_year}, {fk_outcome_type}, '{age_upon_outcome}')
    """
