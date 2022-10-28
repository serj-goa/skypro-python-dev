def wrapper_int(func):
    num = {
        'один': 1,
        'два': 2,
        'три': 3,
        'четыре': 4,
        'пять': 5,
    }
    error_not_num_key = 'TypeError: справа от знака "+" непонятный текст. Если что, я понимаю текстом цифры с 1 по 5.'
    error_type = "TypeError: unsupported operand type(s) for +: 'Int' and 'tuple'"

    def inner(self, other):

        if isinstance(other, int or float):
            return func(self, other)

        elif type(other) != str:
            return error_type

        elif other.isdigit():
            return func(self, int(other))

        number = num.get(other, False)

        if number:
            return func(self, number)

        return error_not_num_key

    return inner


class Int(int):

    @wrapper_int
    def __add__(self, other):
        return super().__add__(other)


if __name__ == '__main__':

    x = Int(5)
    print(f'x = {x}')
    print(f"x + '5' = {x + '5'}")  # 10
    print(f"x + 'один' = {x + 'один'}")  # 6
    print(f"x + 'пять' = {x + 'пять'}")  # 10
    print(f"x + 'шесть' = {x + 'шесть'}")  # TypeError: справа от знака "+" непонятный текст. Если что, я понимаю текстом цифры с 1 по 5.
    print(f"x + 'a' = {x + 'a'}")  # TypeError: справа от знака "+" непонятный текст. Если что, я понимаю текстом цифры с 1 по 5.
    print(f"x + (1,) = {x + (1,)}")  # TypeError: unsupported operand type(s) for +: 'Int' and 'tuple'
