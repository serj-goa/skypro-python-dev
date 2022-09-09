from collections import Counter
from random import shuffle


GAME_LETTERS = {
    "а": 8, "б": 2, "в": 4, "г": 2, "д": 4, "е": 8, "ё": 1, "ж": 1,
    "з": 2, "и": 5., "й": 1, "к": 4, "л": 4, "м": 3, "н": 5, "о": 10,
    "п": 4, "р": 5, "с": 5, "т": 5, "у": 4, "ф": 1, "х": 1, "ц": 1,
    "ч": 1, "ш": 1, "щ": 1, "ъ": 1, "ы": 2, "ь": 2, "э": 1, "ю": 1, "я": 2
}
SCORE = {3: 3, 4: 6, 5: 7, 6: 8, 7: 9}  # 7 letters = 9 points
STOP_WORDS = ('stop', 'стоп')


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


def get_uniq_letters(ltr_count: int) -> list:
    """
    Gets unique letters for the player.
    """
    game_letters = []

    for i in range(ltr_count):
        all_letters = list(GAME_LETTERS.keys())
        shuffle(all_letters)

        ltr = all_letters.pop()

        game_letters.append(ltr)
        GAME_LETTERS[ltr] -= 1

        if not GAME_LETTERS[ltr]:
            del GAME_LETTERS[ltr]

    return game_letters


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


def show_score(player_name: str, game_score: dict) -> None:
    """
    Prints game results to console.
    """
    if not game_score:
        print('\nСпасибо за игру, до встречи!')

    else:
        print(f'\nВыигрывает {player_name}.\nСчёт ', end='')
        print(*list(game_score.values()), sep=' : ')
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
        player_answer = input('Напишите слово: ').strip()

        if player_answer in STOP_WORDS:
            run = False
            show_score(current_player, game_score)
            continue

        cor_player_word = is_correct_word(player_answer, current_player_letters)

        if cor_player_word and player_answer in ALL_WORDS:
            remove_old_letters(player_answer, current_player_letters)

            new_ltrs_cnt += len(player_answer)
            new_ltrs = get_uniq_letters(new_ltrs_cnt)
            current_player_letters.extend(new_ltrs)

            player_score = SCORE[len(player_answer)]
            add_player_score(game_score, current_player, player_score)

            print('Такое слово есть.')
            print(f'{current_player} получает {player_score} баллов.')

        else:
            print('Такого слова нет.')

            new_ltrs = get_uniq_letters(new_ltrs_cnt)
            current_player_letters.extend(new_ltrs)

        if not GAME_LETTERS:
            run = False
            show_score(current_player, game_score)


if __name__ == '__main__':

    ALL_WORDS_DB = 'ru_word.txt'
    ALL_WORDS = get_all_words(ALL_WORDS_DB)

    main()
