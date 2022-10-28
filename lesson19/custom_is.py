from typing import Any


def iss(arg1: Any, arg2: Any) -> None:
    """
    Custom python operator "is".
    """

    arg1_id = id(arg1)
    arg2_id = id(arg2)

    data_info = {
        'id первой переменной:': arg1_id,
        'id второй переменной:': arg2_id,
        'Значение первой переменной:': arg1,
        'Значение второй переменной:': arg2,
    }

    if arg1_id == arg2_id:
        print('Две переменные ссылаются на один и тот же адрес в памяти, имеют одинаковые значения.')

    elif arg1_id != arg2_id and arg1 == arg2:
        print('Две переменные ссылаются на разные адреса в памяти, имеют одинаковые значения.')

    else:
        print('Две переменные ссылаются на разные адреса в памяти, имеют разные значения.')

    for key, value in data_info.items():
        print(key, value)

    print()


if __name__ == '__main__':

    x = y = [1, [2]]
    iss(x, y)

    x, y = [1, [2]], [1, [2]]
    iss(x, y)

    x = [1, [2]]
    y = x.copy()
    y[1] = 2
    iss(x, y)

    A = 'spam'
    B = A
    B = 'shrubbery'
    iss(A, B)

    A = ['spam']
    B = A
    B[0] = 'shrubbery'
    iss(A, B)

    A = ['spam']
    B = A[:]
    B[0] = 'shrubbery'
    iss(A, B)

    iss([], [])
    iss('', '')
    iss({}, {})

    x = y = [1, True, [1, 2]]
    y[2] = [-1, -2]
    iss(x, y)

    x = 5
    y = 5
    iss(x, y)
