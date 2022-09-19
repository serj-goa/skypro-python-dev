from question import Question

from json import load
from random import shuffle
from string import digits
from typing import List

STOP_WORDS = ('close', 'exit', 'quit', 'stop')


def generate_questions_list(questions: list) -> List[Question]:
    """
    Generates a list of objects class Question in random order.
    """
    question_objects = []

    for question in questions:
        question_objects.append(Question(question['question'], question['difficulty'], question['answer']))

    shuffle(question_objects)

    return question_objects


def get_user_answer() -> str:
    """
    Gets the player's response.
    """
    while True:
        user_answer = input('>>> ')

        if user_answer in STOP_WORDS:
            return user_answer

        elif not user_answer or any(list(filter(lambda ch: ch not in digits, user_answer))):
            print('Ответ должен быть числом.\n')
            continue

        return user_answer


def load_data(filepath: str) -> list:
    """
    Loads a list with questions and their additional characteristics.
    """
    with open(filepath, encoding='utf-8') as fh:
        data = load(fh)
        return data


def show_result(player_answer: dict) -> None:
    """
    Displays game statistics to the user.
    """
    cnt_all_answer = 0
    cnt_corr_answer = 0
    points = 0

    for point in player_answer.values():
        points += point
        cnt_all_answer += 1

        if point > 0:
            cnt_corr_answer += 1

    print('Вот и все!')
    print(f'Отвечено на {cnt_corr_answer} вопроса из {cnt_all_answer}')
    print(f'Набранно {points} баллов')
