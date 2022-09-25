from interfaces.storage_interface import Storage


class Shop(Storage):
    def __init__(self, shop_name: str, items=None, capacity=20):
        if items is None:
            items = {}
        self.items = items
        self.name = shop_name
        self.__capacity = capacity
        self.__shop_volume = 5

    @property
    def capacity(self):
        return self.__capacity

    @property
    def shop_volume(self):
        return self.__shop_volume

    def add(self, name, cnt):
        current_volume = sum(list(self.items.values()))

        if (cnt + current_volume) > self.capacity:
            return f'Для получения товара в магазине недостаточно свободного места.'

        elif name not in self.items and len(self.items) == self.shop_volume:
            return f'Не возможно расширить ассортимент в магазине, достигнут предел уникальных товаров.'

        self.items[name] = self.items.get(name, 0) + cnt
        return f'Магазин принял {name} в количестве {cnt} шт.'

    def remove(self, name, cnt):
        if self.items[name] == cnt:
            del self.items[name]
        else:
            self.items[name] -= cnt

    def get_free_space(self):
        current_volume = sum(list(self.items.values()))

        if not current_volume:
            msg = f'\nСвободных мест в магазине - {self.capacity}\n'
            uniq_product = self.shop_volume
            product_capacity = self.capacity

            return msg, uniq_product, product_capacity

        elif current_volume == self.capacity:
            return '\nВ магазине нет свободного места.\n', 0, 0

        free_uniq_items = self.shop_volume - len(self.items)
        free_volume = self.capacity - current_volume
        msg = f'\nСвободных мест в магазине - {free_volume}\n'

        if free_uniq_items:
            msg = f'\nОбщий объём свободных мест в магазине - {free_volume}\n' \
                  f'Доступных мест для расширения ассортимента - {free_uniq_items}.\n'

        return msg, free_uniq_items, free_volume

    def get_items(self):
        if not self.items:
            return 'В магазине нет товаров.'

        all_products = 'В магазине в наличии:\n'

        for product, cnt in self.items.items():
            all_products += f'\n\t{product} : {cnt}'
        return all_products

    def get_unique_items_count(self):
        if not self.items:
            return 'В магазине нет товаров.'

        return f'В ассортименте магазина {len(self.items)} из {self.shop_volume} ' \
               f'уникальных товаров ({", ".join(self.items.keys())})'


class Store(Storage):
    def __init__(self, store_name: str, items: dict = None, capacity=100):
        if items is None:
            items = dict()
        self.items = items
        self.name = store_name
        self.__capacity = capacity
        self.__shop_volume = None

    @property
    def capacity(self):
        return self.__capacity

    @property
    def shop_volume(self):
        return self.__shop_volume

    def add(self, name, cnt):
        current_volume = sum(list(self.items.values()))

        if (cnt + current_volume) > self.capacity:
            return f'Для получения товара на складе недостаточно свободного места.\n'

        self.items[name] = self.items.get(name, 0) + cnt
        return f'Склад принял {name} в количестве {cnt} шт.\n'

    def remove(self, name, cnt):
        if self.items[name] == cnt:
            del self.items[name]
        else:
            self.items[name] -= cnt

    def get_free_space(self):
        current_volume = sum(list(self.items.values()))

        if not current_volume:
            msg = f'\nНа складе {self.capacity} свободных мест.'
            uniq_product = self.shop_volume
            product_capacity = self.capacity

            return msg, uniq_product, product_capacity

        elif current_volume == self.capacity:
            return '\nНа складе нет свободного места.', 0, 0

        free_uniq_items = 1
        free_volume = self.capacity - current_volume
        msg = f'\nСвободных мест на складе - {self.capacity - current_volume}'

        return msg, free_uniq_items, free_volume

    def get_items(self):
        if not self.items:
            return 'На складе нет товаров.'

        all_products = 'В наличии на складе:\n'

        for product, cnt in self.items.items():
            all_products += f'\n\t{product} : {cnt}'
        return all_products

    def get_unique_items_count(self):
        if not self.items:
            return 'На складе нет товаров.'

        return f'Уникальных товаров на складе - {len(self.items)} ({", ".join(self.items.keys())})\n'
