from json import load
from re import search
from typing import Union

STOP_WORDS: tuple = ('close', 'quit', 'stop')


def get_pk_from_user(all_students: list) -> int:
    """
    Obtaining a student key from a user.
    """
    while True:
        print('Введите номер студента')
        user_data: str = input('>>> ').strip()

        if user_data in STOP_WORDS:
            quit()

        elif not user_data.isdigit():
            continue

        user_pk: int = int(user_data)

        if not is_valid_data(user_pk, all_students):
            print('У нас нет такого студента\n')
            continue

        return user_pk


def get_student_by_key(student_pk: int, db: list) -> Union[dict, None]:
    """
    Get student data by key.
    """
    for student_data in db:  # student_data: dict
        if student_data["pk"] == student_pk:  # student_pk: int
            return student_data
    return None


def is_valid_data(user_pk: int, all_students: list) -> bool:
    """
    Checks if the specified key exists in the student`s database.
    """
    for student in all_students:  # student: dict
        if student["pk"] == user_pk:
            return True
    return False


def is_valid_login(student_data: dict) -> bool:
    """
    Checks if the student's login is correct.
    """

    student_login: str = student_data["login"]

    # The full regex looks unreadable, implicit, and complex, which goes against Python's principles.
    # regexp = r"(?=.*\d)(?=.*[a-z])(?=.*[.,/?`~!@#$%^&*()\-_+='\":;])(?=^[^A-Z].*[A-Z])(?=.+[a-zA-Z\d]$).{4,}"
    #
    # if search(regexp, student_login):
    #     return True
    #
    # return False

    # 1.Первая буква не может быть заглавной и 2.Знаки (помимо букв и цифр) не могут быть последними
    if not (search(r'^[^A-Z].{2,}[a-zA-Z\d]$', student_login)):
        return False

    # Логин должен состоять минимум из одной:
    # 1. Строчной буквы
    if not (search(r'[a-z]+', student_login)):
        return False

    # 2. Заглавной буквы
    if not (search(r'^[^A-Z].*[A-Z]+.*', student_login)):
        return False

    # 3. Дополнительного символа
    if not (search(r'.*[\W|_]+.*[a-zA-Z\d]$', student_login)):
        return False

    # 4. Цифры
    if not (search(r'\d+', student_login)):
        return False

    return True


def load_data(filepath: str) -> list:
    """
    Loads a list of students from a file.
    """
    with open(filepath, encoding='utf-8') as fh:
        data = load(fh)

    return data


def show_result(valid_login: bool, student_data: dict) -> None:
    """
    Displays the results of data processing to the user.
    """
    print(f'\nСтудент {student_data["full_name"]} ввёл логин {student_data["login"]}')

    if valid_login:
        answer = 'корректный'
    else:
        answer = 'НЕ корректный'
    print(f'Выбранный логин {answer}.\n')
