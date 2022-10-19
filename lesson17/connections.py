from settings import HOST_PG, PORT_PG, PSW_PG, USER_PG

from psycopg2 import connect, Error


def close_db_connection(connection: connect, cursor: connect) -> str:
    """
    Closes the connection to the database.
    """

    try:
        cursor.close()
        connection.close()

    except (Error, Exception) as error:
        return f'Error closing database connection!\n{error}\n'

    return 'The database connection was closed successfully.\n'


def db_connection(user_db: str = None) -> tuple:
    """
    Creates a connection to the database.
    """

    try:
        connection = connect(user=USER_PG, password=PSW_PG, host=HOST_PG, port=PORT_PG, database=user_db)
        connection.autocommit = True

        cursor = connection.cursor()

    except (Error, Exception) as error:
        return f'Connection FAILED!\n{error}\n', None

    return connection, cursor


def start_query_execution(cursor: connect, some_query: str) -> str:
    """
    Start executing the received request.
    """

    try:
        cursor.execute(some_query)

    except (Error, Exception) as error:
        f'Request execution error!\n{error}\n'

    return f'Request completed successfully.\n'
