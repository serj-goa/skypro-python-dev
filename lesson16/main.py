from settings import HOST_PG, NAME_DB, PORT_PG, PSW_PG, USER_PG
from utils import get_user_number, run_user_choice, show_program_menu

from psycopg2 import connect, Error


def main() -> None:
    try:
        db_connection = connect(user=USER_PG, password=PSW_PG, host=HOST_PG, port=PORT_PG, database=NAME_DB)
        cursor = db_connection.cursor()

        while True:

            show_program_menu()
            user_choice = get_user_number()
            run = run_user_choice(cursor, data=user_choice)

            if not run:
                break

    except (Exception, Error) as error:
        print(error)

    finally:
        if db_connection:

            db_connection.close()
            cursor.close()


if __name__ == '__main__':
    main()
