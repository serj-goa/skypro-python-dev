from csv import DictReader as csv_DictReader
from json import dump as json_dump


def csv_to_json(csv_filepath: str, json_filepath: str, ads=False) -> None:
    """
     Convert csv file to json.
    """

    with open(csv_filepath, encoding='utf-8') as csv_file:
        file_data = []

        for row in csv_DictReader(csv_file):

            if ads:
                row = correct_ads(row)

            file_data.append(row)

    with open(json_filepath, 'w', encoding='utf-8') as json_file:
        json_dump(file_data, json_file, indent=4, ensure_ascii=False)


def correct_ads(row: dict) -> dict:
    row["price"] = int(row["price"])
    row["description"] = row["description"] if row["description"] else ""

    return row


if __name__ == '__main__':
    csv_to_json(csv_filepath='datasets/ads.csv', json_filepath='datasets/ads.json', ads=True)
    csv_to_json(csv_filepath='datasets/categories.csv', json_filepath='datasets/categories.json')
