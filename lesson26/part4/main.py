import os


def get_by_date(date, name=None, filename='dump.csv') -> None:
    fields = 'date,open,high,low,close,volume,Name\n'

    current_dir = os.path.dirname(__file__)
    data_file_name = 'sorted_for_date.csv'
    data_filepath = os.path.join(current_dir, data_file_name)

    file_data = open(data_filepath)

    res_filepath = os.path.join(current_dir, filename)
    file_rezult = open(res_filepath, 'w')
    file_rezult.write(fields)

    i = 0
    str = ' '
    if name:
        name = ',' + name + '\n'

        while str:
            try:
                str = next(file_data)

                if date in str:
                    if name in str:
                        file_rezult.write(str)
                        print(str.strip())
            except:
                str = None

            i += 1
    else:
        while str:
            try:
                str = next(file_data)

                if date in str:
                    file_rezult.write(str)
                    print(str.strip())
            except:
                str = None

            i += 1
            
    file_rezult.close()
    file_data.close()

    return None


if __name__ == '__main__':
    rez = get_by_date(date="2018-01-26", name="PG", filename='dump.csv')
