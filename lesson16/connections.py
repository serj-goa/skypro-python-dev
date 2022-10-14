from settings import HOST_PG, NAME_DB, PORT_PG, PSW_PG, USER_PG

from psycopg2 import connect, Error


def db_connection() -> tuple:

    try:
        connection = connect(user=USER_PG, password=PSW_PG, host=HOST_PG, port=PORT_PG, database=NAME_DB)
        cursor = connection.cursor()

    except (Exception, Error) as error:
        return f'Connection FAILED!\n{error}\n', None

    return connection, cursor
