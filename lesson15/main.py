from utils import add_uniq_key, append_data_to_file, create_empty_file, get_csvfile_generator


def main():

    ads_db = 'datasets/ads.csv'
    new_files = (
        'new_datasets/ads.csv',
        'new_datasets/author.csv',
        'new_datasets/address.csv'
    )

    for new_file in new_files:
        create_empty_file(filepath=new_file)

    all_authors = {}
    all_addresses = {}

    for row in get_csvfile_generator(filepath=ads_db):

        add_uniq_key(data=all_authors, some_key=row['author'])
        add_uniq_key(data=all_addresses, some_key=row['address'])

        row['author'] = all_authors[row['author']]
        row['address'] = all_addresses[row['address']]

        append_data_to_file(filepath=new_files[0], data=row.values())

    for key, value in all_authors.items():
        append_data_to_file(filepath=new_files[1], data=(value, key))

    for key, value in all_addresses.items():
        append_data_to_file(filepath=new_files[2], data=(value, key))


if __name__ == '__main__':
    main()
