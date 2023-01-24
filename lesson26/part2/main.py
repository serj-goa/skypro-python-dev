import csv
import os


def get_by_date(date, name=None, filename='dump.csv'):
    fields = ['date', 'open', 'high', 'low', 'close', 'volume', 'Name']

    current_dir = os.path.dirname(__file__)
    res_file_name = 'sorted_for_date.csv'
    res_filepath = os.path.join(current_dir, res_file_name)

    dictobj = csv.DictReader(open(res_filepath))
    dictobj = list(dictobj)

    size = len(dictobj) - 1
    start = -1

    f0 = 0
    f1 = 1
    f2 = 1
    mid = None
    while (f2 < size + 1):
        f0 = f1
        f1 = f2
        f2 = f1 + f0

    while (f2 > 1):
        index = min(start + f0, size)

        if dictobj[index]['date'] < date:
            f2 = f1
            f1 = f0
            f0 = f2 - f1
            start = index

        elif dictobj[index]['date'] > date:
            f2 = f0
            f1 = f1 - f0
            f0 = f2 - f1

        else:
            mid = index
            break

    if (f1) and (dictobj[size]['date'] == date):
        mid = size

    begin = max(0, mid)
    end = min(mid + 1, size)

    if mid:
        res_filepath = os.path.join(current_dir, filename)
        writer = csv.DictWriter(open(res_filepath, "w", newline=''), fieldnames=fields)
        writer.writeheader()
        list_rows = []

        if name:
            while dictobj[begin]['date'] == date:
                if dictobj[begin]['Name'] == name:
                    writer.writerow(dictobj[begin])
                    list_rows.append(dictobj[begin])
                begin -= 1

                if begin < 1:
                    break

            while dictobj[end]['date'] == date:
                if dictobj[end]['Name'] == name:
                    writer.writerow(dictobj[end])
                    list_rows.append(dictobj[end])
                end += 1

                if end > size - 1:
                    break

        else:
            while dictobj[begin]['date'] == date:
                writer.writerow(dictobj[begin])
                list_rows.append(dictobj[begin])
                begin -= 1

                if begin < 1:
                    break

            while dictobj[end]['date'] == date:
                writer.writerow(dictobj[end])
                list_rows.append(dictobj[end])
                end += 1

                if end > size - 1:
                    break

        return list(list_rows)

    return None


if __name__ == '__main__':
    rez = get_by_date(date="2013-02-11", name="PCLN")

    for each in rez:
        print(each)
