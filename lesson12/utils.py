from json import load
from string import hexdigits, punctuation
from typing import Union

STOP_WORDS = ('close', 'quit', 'stop')


def show_start_menu():
    print('''-------------------------------------------
    [1] отправить товар со склада в магазин.
    [2] вернуть товар из магазина на склад.
    [3] Продать товар со склада.
    [4] Продать товар с магазина.
    [5] проверить наличие товара в магазине.
    [6] проверить наличие товара на складе.
-------------------------------------------''')


def get_user_text() -> str:
    """
    Handles user input as required.
    """
    while True:
        player_answer = input('>>> ').strip()
        incorrect_chars = any(list(filter(lambda ch: ch in hexdigits or ch in punctuation, player_answer)))

        if incorrect_chars:
            print(f'Введите слово используя только кирилицу.\n')
            continue

        return player_answer


def get_user_number(limit=None) -> Union[int, str]:
    """
    Getting the menu item number.
    """
    while True:
        user_choice = input('>>> ').strip().lower()

        if user_choice in STOP_WORDS:
            return user_choice

        elif not user_choice.isdigit():
            print('Введите номер пункта меню.')
            continue

        user_choice = int(user_choice)

        if limit and not 0 < user_choice < (limit + 1):
            continue

        return user_choice


def load_data(filepath: str) -> dict:
    """
    Loads a list with questions and their additional characteristics.
    """
    with open(filepath, encoding='utf-8') as fh:
        data = load(fh)
        return data
