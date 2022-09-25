from storages import Shop, Store
from storage_requests import Request
from utils import show_start_menu, get_user_number, get_user_text, load_data

STOP_WORDS = ('close', 'quit', 'stop')


def main():
    all_products = load_data('data/products.json')

    print('\nДобро пожаловать в тестовую версию логистического бота.\n')

    print('Давайте создадим склад.')
    print('Введите название оптового склада:')
    store_name = get_user_text()

    store = Store(store_name=store_name, items=all_products)
    print(f'На склад {store_name} отправлены товары.\n')
    print(store.get_items())

    print('\nДавайте создадим магазин.')
    print('Введите название магазина:')
    shop_name = get_user_text()

    shop = Shop(shop_name=shop_name)

    request_store_to_shop = Request(store, shop)
    request_shop_to_store = Request(shop, store)

    commands = {
        1: request_store_to_shop.send_products,
        2: request_shop_to_store.send_products,
        3: request_store_to_shop.sell_products,
        4: request_shop_to_store.sell_products,
        5: shop.get_items,
        6: store.get_items,
    }

    while True:
        print('\nВыберите номер команды из списка:')
        show_start_menu()
        user_choice = get_user_number(limit=len(commands))

        if user_choice in STOP_WORDS:
            break

        elif user_choice < 5:
            print('\nВведите наименование товара (апельсины/бананы...):')
            product_name = get_user_text()

            print('\nВведите количество товара:')
            product_count = get_user_number()

            commands[user_choice](product_name, product_count)  # type: Request

        elif user_choice < 7:
            print(commands[user_choice]())  # type: Shop or Store

        if sum(shop.items.values()) == shop.capacity:
            print('\nМагазин полность заполнен.')

        input('\nНажмите Ввод для продолжения...')

    print('Спасибо за работу, до встречи!')


if __name__ == '__main__':

    main()
