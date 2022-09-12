from collections import Counter
from random import shuffle
from string import hexdigits, punctuation


LETTERS_DATA = {
    "а": (8, 1), "б": (2, 3), "в": (4, 1), "г": (2, 3), "д": (4, 2), "е": (8, 1),
    "ё": (1, 3), "ж": (1, 5), "з": (2, 5), "и": (5, 1), "й": (1, 4), "к": (4, 2),
    "л": (4, 2), "м": (3, 2), "н": (5, 1), "о": (10, 1), "п": (4, 2), "р": (5, 1),
    "с": (5, 1), "т": (5, 1), "у": (4, 2), "ф": (1, 10), "х": (1, 5), "ц": (1, 5),
    "ч": (1, 5), "ш": (1, 8), "щ": (1, 10), "ъ": (1, 10), "ы": (2, 4), "ь": (2, 3),
    "э": (1, 8), "ю": (1, 8), "я": (2, 3)
}
SCORE = {3: 3, 4: 6, 5: 7, 6: 8, 7: 9}  # 7 letters = 9 points
STOP_WORDS = ('close', 'quit', 'stop')
game_letters = {letter: data[0] for letter, data in LETTERS_DATA.items() if data[0] > 0}


def add_player_score(game_score: dict, player_name: str, player_score: int) -> None:
    """
    Adds points to the player.
    """
    if player_name not in game_score:
        game_score[player_name] = player_score

    else:
        game_score[player_name] += player_score


def get_all_words(filepath: str) -> list:
    """
    Gets a list of all words for the game.
    """
    with open(filepath, 'r', encoding='utf-8') as fh:
        all_words = list(map(lambda word: word.strip(), fh.readlines()))
        return all_words


def get_player_answer(player_name: str) -> str:
    """
    Handles player input as required.
    """
    while True:
        player_answ = input('Напишите слово: ').strip().lower()
        incorrect_chars = any(list(filter(lambda ch: ch in hexdigits or ch in punctuation, player_answ)))

        if not incorrect_chars or player_answ in STOP_WORDS:
            return player_answ

        print(f'{player_name} введите слово используя только кирилицу.\n')


def get_player_points(player_answer: str):
    """
    Calculates user points.
    """

    letter_points = 0

    for ltr in player_answer:
        letter_points += LETTERS_DATA[ltr][1]

    player_score = SCORE[len(player_answer)] + letter_points

    return player_score


def get_uniq_letters(ltr_count: int) -> list:
    """
    Gets unique letters for the player.
    """
    available_letters = []

    for i in range(ltr_count):
        all_letters = list(game_letters.keys())
        shuffle(all_letters)

        ltr = all_letters.pop()

        available_letters.append(ltr)
        game_letters[ltr] -= 1

        if not game_letters[ltr]:
            del game_letters[ltr]

    return available_letters


def is_correct_word(word: str, letters: list) -> bool:
    """
    Checks the word of the player with requirements.
    """
    if len(word) > len(letters):
        return False

    ltrs_in_word = Counter(word)
    player_ltrs = Counter(letters)

    for ltr, cnt in ltrs_in_word.items():
        if cnt > player_ltrs[ltr]:
            return False

    return True


def remove_old_letters(word: str, letters: list) -> None:
    """
    Removes used letters from the game.
    """
    for ltr in word:
        letters.remove(ltr)


def show_score(player_1: str, player_2: str, game_score: dict) -> None:
    """
    Prints game results to console.
    """
    player_1_score = game_score.get(player_1, 0)
    player_2_score = game_score.get(player_2, 0)

    if not game_score:
        print('\nСпасибо за игру, до встречи!')

    elif player_1_score > player_2_score:
        print(f'\nПоздравляем, выигрывает {player_1}.\nСчёт ', end='')
        print(f'{player_1_score} : {player_2_score}')
        print('\nСпасибо за игру, до скорой встречи!')

    elif player_1_score < player_2_score:
        print(f'\nПоздравляем, выигрывает {player_2}.\nСчёт ', end='')
        print(f'{player_1_score} : {player_2_score}')
        print('\nСпасибо за игру, до скорой встречи!')

    else:
        print(f'\n{player_1} и {player_2} поздравляем с ничьёй!\nСчёт ', end='')
        print(f'{player_1_score} : {player_2_score}')
        print('\nСпасибо за игру, до скорой встречи!')


def main():
    letters_count = 7

    print('Привет.\nМы начинаем играть в Scrabble\n')
    print('Как зовут первого игрока?')
    player_1 = input('>>> ')

    print('\nКак зовут второго игрока?')
    player_2 = input('>>> ')

    print(f'\n{player_1} vs {player_2}\n(раздаю случайные буквы)\n')

    player_1_letters = get_uniq_letters(letters_count)
    player_2_letters = get_uniq_letters(letters_count)

    print(f'{player_1} - буквы \"{", ".join(player_1_letters)}\"')
    print(f'{player_2} - буквы \"{", ".join(player_2_letters)}\"')

    run = True
    step = 0
    game_score = {}

    while run:
        new_ltrs_cnt = 1
        current_player = player_1 if not step % 2 else player_2
        current_player_letters = player_1_letters if not step % 2 else player_2_letters
        step += 1

        print(f'\nХодит {current_player} - буквы: \"{", ".join(current_player_letters)}\"')
        player_answer = get_player_answer(current_player)

        if player_answer in STOP_WORDS:
            run = False
            show_score(player_1, player_2, game_score)
            continue

        cor_player_word = is_correct_word(player_answer, current_player_letters)

        if cor_player_word and player_answer in ALL_WORDS:
            remove_old_letters(player_answer, current_player_letters)

            new_ltrs_cnt += len(player_answer)

            if new_ltrs_cnt > sum(game_letters.values()):
                new_ltrs_cnt = sum(game_letters.values())

            new_ltrs = get_uniq_letters(new_ltrs_cnt)
            current_player_letters.extend(new_ltrs)

            player_score = get_player_points(player_answer)
            add_player_score(game_score, current_player, player_score)

            print('Такое слово есть.')
            print(f'{current_player} получает {player_score} баллов.')

        else:
            print('Такого слова нет.')

            new_ltrs = get_uniq_letters(new_ltrs_cnt)
            current_player_letters.extend(new_ltrs)

        if not game_letters:
            run = False
            show_score(player_1, player_2, game_score)


if __name__ == '__main__':

    ALL_WORDS_DB = 'ru_word.txt'
    ALL_WORDS = get_all_words(ALL_WORDS_DB)

    main()
