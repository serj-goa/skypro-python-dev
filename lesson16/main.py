from connections import db_connection
from utils import get_user_number, run_user_choice, show_program_menu


def main() -> None:

    connection, cursor = db_connection()

    if cursor is None:
        print(connection)  # If the connection fails, the variable contains the error message.

        return None

    try:
        while True:

            show_program_menu()
            user_choice = get_user_number()
            run = run_user_choice(cursor, data=user_choice)

            if not run:
                break

    except KeyboardInterrupt:
        print('The program has been completed.')

    except Exception as error:
        print(f'Unexpected error!\n{error}')

    finally:

        cursor.close()
        connection.close()

    print('Good Bye!')


if __name__ == '__main__':
    main()
