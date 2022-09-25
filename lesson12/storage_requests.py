from utils import get_user_text


class Request:
    def __init__(self, from_, to, product=None, amount=3):
        self.from_ = from_
        self.to = to
        self.product = product
        self.amount = amount

    def __repr__(self):
        return f'Доставить {self.amount} {self.product} из {self.from_} в {self.to}'

    @staticmethod
    def is_agree_user() -> bool:
        user_answer = get_user_text()
        return True if user_answer == 'да' else False

    def sell_products(self, product_name: str, cnt: int):
        if product_name not in self.from_.items:
            print('Указанного товара нет в наличии.')

        elif cnt <= self.from_.items[product_name]:
            self.from_.remove(product_name, cnt)
            print(f'\nПродажа {product_name} : {cnt} шт. - осуществлена успешно.\n')

        else:
            print(f'\nВы хотите продать товара больше, чем его в наличии.\n'
                  f'Хотите продать {self.from_.items[product_name]} ({product_name})?\n'
                  f'Для подтверждения операции сделайте выбор (да/нет):')

            if self.is_agree_user():
                current_product_cnt = self.from_.items[product_name]
                self.from_.remove(product_name, current_product_cnt)
                print(f'\nПродажа {product_name} : {current_product_cnt} шт. - осуществлена успешно.\n')

            else:
                print(f'\nПродажа товара {product_name} : {cnt} - отменена.\n')

    def send_products(self, product_name: str, cnt: int):
        data = self.to.get_free_space()

        msg = data[0]
        free_uniq_items = data[1]
        free_volume = data[2]

        if product_name not in self.from_.items:
            print('Указанного товара нет в наличии.')

        elif cnt > self.from_.items[product_name]:
            print('Для отправки недостаточно едениц товара.')

        elif (not free_uniq_items and not free_volume) or (not free_uniq_items and product_name not in self.to.items):
            print(msg)

        elif cnt > free_volume:
            remainder_product = cnt - free_volume

            print(f'\nВы отправляете товара больше, чем доступно свободного места.\n'
                  f'Хотите чтобы {self.to.name} принял {free_volume} ({product_name}), '
                  f'а остаток {remainder_product} ({product_name}) вернулся обратно?\n'
                  f'Для подтверждения операции сделайте выбор (да/нет):')

            if self.is_agree_user():
                print(self.to.add(product_name, free_volume))
                self.from_.remove(product_name, free_volume)
                print(f'\nОстаток {product_name} : {remainder_product} шт. - возвращены обратно.\n')

            else:
                print(f'\nПередача товара {product_name} : {cnt} - отменена.\n')

        else:
            print(self.to.add(product_name, cnt))
            self.from_.remove(product_name, cnt)
