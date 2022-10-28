class Int(int):
    NUM = {
        'один': 1,
        'два': 2,
        'три': 3,
        'четыре': 4,
        'пять': 5,
    }
    error_not_num_key = 'TypeError: справа от знака "+" непонятный текст. Если что, я понимаю текстом цифры с 1 по 5.'
    error_type = "TypeError: unsupported operand type(s) for +: 'Int' and 'tuple'"

    def __add__(self, other):

        if isinstance(other, int or float):
            return super().__add__(other)

        elif type(other) != str:
            return self.error_type

        elif other.isdigit():
            return super().__add__(int(other))

        answ = self.NUM.get(other, False)

        if answ:
            return super().__add__(answ)

        return self.error_not_num_key


if __name__ == '__main__':

    x = Int(5)
    print(f'x = {x}')
    print(f"x + '5' = {x + '5'}")  # 10
    print(f"x + 'один' = {x + 'один'}")  # 6
    print(f"x + 'пять' = {x + 'пять'}")  # 10
    print(f"x + 'шесть' = {x + 'шесть'}")  # TypeError: справа от знака "+" непонятный текст. Если что, я понимаю текстом цифры с 1 по 5.
    print(f"x + 'a' = {x + 'a'}")  # TypeError: справа от знака "+" непонятный текст. Если что, я понимаю текстом цифры с 1 по 5.
    print(f"x + (1,) = {x + (1,)}")  # TypeError: unsupported operand type(s) for +: 'Int' and 'tuple'
