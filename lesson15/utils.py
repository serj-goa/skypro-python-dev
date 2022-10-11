from csv import DictReader, writer
from typing import Any


def add_uniq_key(data: dict, some_key: str) -> None:
    """
    Creates unique keys in an ordinal dictionary.
    """

    if some_key not in data:
        data[some_key] = len(data) + 1


def append_data_to_file(filepath: str, data: Any) -> None:
    """
    Append data to file.
    """

    with open(filepath, 'a', encoding='utf-8', newline='') as csv_file:
        writer(csv_file).writerow(data)


def create_empty_file(filepath: str) -> None:
    """
    Creates a new empty file at the specified path.
    """

    with open(filepath, 'w'):
        ...


def get_csvfile_generator(filepath: str) -> dict:
    """
    Getting a generator from a csv-file.
    """

    with open(filepath, encoding='utf-8') as csv_file:
        csv_reader = DictReader(csv_file)

        for row in csv_reader:
            yield row
