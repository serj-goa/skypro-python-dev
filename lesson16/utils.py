from requests import get_ads_by_author, get_ads_by_author_and_price, \
                     get_ads_by_city, get_ads_by_price_range, get_all_ads

from psycopg2 import connect
from re import findall


def get_user_text() -> str:
    """
    Get a number from the user.
    """

    while True:
        user_text = input('>>> ')

        if not user_text:
            continue

        word_cnt = len(findall(r'[а-яА-ЯёЁ]+', user_text))

        if word_cnt == 1:
            return user_text.title()

        elif word_cnt > 1:
            print('Введите одно слово.\n')
            continue

        elif not user_text.isalpha():
            print('Текст должен состоять только из букв.\n')
            continue

        print('Введите текст кириллицей.\n')


def get_user_number() -> str:
    """
    Get a text from the user.
    """

    while True:
        user_text = input('>>> ')

        if not user_text:
            continue

        elif user_text.isdigit():
            return user_text

        print('Введите целое число.\n')


def run_user_choice(cursor: connect, data: str):
    """
    Launch actions according to the selected menu item.
    """

    match data:

        case '0':
            return False

        case '1':
            records = get_all_ads(cursor)

        case '2':
            print('Введите имя автора объявления:')
            author = get_user_text()

            records = get_ads_by_author(cursor, author)

        case '3':
            print('Введите цену от:')
            starting_price = get_user_number()

            print('Введите цену до:')
            final_price = get_user_number()

            records = get_ads_by_price_range(cursor, starting_price, final_price)

        case '4':
            print('Введите город:')
            city = get_user_text()

            records = get_ads_by_city(cursor, city)

        case '5':
            print('Введите имя автора объявления:')
            author = get_user_text()

            print('Введите ожидаемую цену:')
            price = get_user_number()

            records = get_ads_by_author_and_price(cursor, author, price)

        case _:
            print('Указанный пункт меню отсутствует.')
            return True

    show_all_ads(data_records=records)

    return True


def show_all_ads(data_records: list) -> None:
    """
    Show of search result.
    """
    for record in data_records:

        description = record[2].strip() if record[2] is not None else ''

        print(f'{record[0].strip()} - {record[1]} руб.\n')

        if description:
            print(description)

        print(f'{record[3].strip()} ({record[4].strip()})\n')
        print('-' * 10, end='\n\n')

    input('\nНажмите ENTER для продолжения...')


def show_program_menu() -> None:
    """
    Show program menu to user.
    """
    print(
        """
        ------------------------------------------------------------
        [1] - Вывести все актуальные объявления.
        [2] - Вывести объявления указанного автора.
        [3] - Вывести объявления по диапазону цен.
        [4] - Вывести объявления для указанного города.
        [5] - Вывести объявления для указанного автора и цены.
        
        [0] - Выход из программы
        ------------------------------------------------------------"""
    )
