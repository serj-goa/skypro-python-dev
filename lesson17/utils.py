from connections import close_db_connection, db_connection, start_query_execution
from requests_db import ALL_TABLE_REQUESTS, ALL_USERS_REQUESTS, generate_table_request, req_insert_animals, req_insert_animal_breeds, \
                        req_insert_animal_colors, req_insert_outcome_subtypes, req_insert_outcome_types, \
                        req_insert_shelter_info
from settings import ANIMALS_DB

from csv import DictReader
from psycopg2 import connect


def add_users_to_db(name_db: str) -> str:
    """
    Adds users to the database.
    """

    connection, cursor = db_connection(user_db=name_db)

    try:
        for user_name, user_request in ALL_USERS_REQUESTS.items():
            start_query_execution(cursor, some_query=user_request)

        return 'The users has been successfully added to the database.'

    except Exception as error:
        return f'An error occurred while adding the {user_name}!\n{error}\n'

    finally:
        print(close_db_connection(connection, cursor))


def create_db(name_db: str) -> str:
    """
    Creates a database with the name specified in the parameters.
    """

    connection, cursor = db_connection()
    new_db = f'CREATE DATABASE {name_db}'

    try:
        return start_query_execution(cursor, some_query=new_db)

    except Exception as error:
        return f'Unexpected error!\n{error}'

    finally:
        print(close_db_connection(connection, cursor))


def create_tables(name_db: str) -> str:
    """
    Creates tables for the specified database.
    """

    connection, cursor = db_connection(user_db=name_db)

    try:
        for table_name, table_values in ALL_TABLE_REQUESTS.items():

            query = generate_table_request(table_name, table_values)
            start_query_execution(cursor, some_query=query)

        return f'Table creation completed successfully.'

    except Exception as error:
        return f'An error occurred while creating the "{table_name}" table!\n{error}\n'

    finally:
        print(close_db_connection(connection, cursor))


def get_csvfile_generator(filepath: str) -> dict:
    """
    Getting a generator from a csv-file.
    """

    with open(filepath, encoding='utf-8') as csv_file:

        for row in DictReader(csv_file):
            yield row


def insert_values(name_db: str) -> str:
    """
    Processes and sends requests for adding new values
    to the database specified in the parameters.
    """

    connection, cursor = db_connection(user_db=name_db)

    uniq_animals = set()
    breeds = dict()
    colors = dict()
    outcome_subtypes = dict()
    outcome_types = dict()
    animal_cnt = 1

    try:

        for row in get_csvfile_generator(ANIMALS_DB):

            if row['animal_id'] in uniq_animals:
                continue

            uniq_animals.add(row['animal_id'])

            if row['breed'] not in breeds:
                breeds[row['breed']] = len(breeds) + 1
                start_query_execution(cursor, some_query=req_insert_animal_breeds(row['breed']))

            if row['color1'] and row['color1'] not in colors and row['color1'] != 'NULL':
                colors[row['color1']] = len(colors) + 1
                start_query_execution(cursor, some_query=req_insert_animal_colors(row['color1']))

            if row['color2'] and row['color2'] not in colors and row['color2'] != 'NULL':
                colors[row['color2']] = len(colors) + 1
                start_query_execution(cursor, some_query=req_insert_animal_colors(row['color2']))

            if row['outcome_subtype'] not in outcome_subtypes and row['outcome_subtype'] != 'NULL':
                outcome_subtypes[row['outcome_subtype']] = len(colors) + 1
                start_query_execution(cursor, some_query=req_insert_outcome_subtypes(row['outcome_subtype']))

            if row['outcome_type'] not in outcome_types:
                outcome_types[row['outcome_type']] = len(colors) + 1
                start_query_execution(cursor, some_query=req_insert_outcome_types(row['outcome_type']))

            color1 = colors.get(row['color1'], 'NULL')
            color2 = colors.get(row['color2'], 'NULL')

            start_query_execution(cursor,
                                  some_query=req_insert_animals(values=(row['animal_id'], row['animal_type'],
                                                                        row['name'], breeds[row['breed']], color1,
                                                                        color2, row['date_of_birth'])))

            outcome_subtype = outcome_subtypes.get(row['outcome_subtype'], 'NULL')

            start_query_execution(cursor,
                                  some_query=req_insert_shelter_info(values=(row['animal_id'], outcome_subtype,
                                                                             row['outcome_month'], row['outcome_year'],
                                                                             outcome_types[row['outcome_type']],
                                                                             row['age_upon_outcome'])))
            print(f'Обработана запись {animal_cnt}')
            animal_cnt += 1

        return f'Insert values completed successfully.'

    except Exception as error:
        return f'An error occurred while insert values!\n{error}\n'

    finally:
        print(close_db_connection(connection, cursor))
