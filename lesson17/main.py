from settings import NEW_DB
from utils import create_db, create_tables, insert_values


def main() -> None:

    print(create_db(name_db=NEW_DB))
    print(create_tables(name_db=NEW_DB))
    print(insert_values(name_db=NEW_DB))

    print('Good Bye!')


if __name__ == '__main__':
    main()
