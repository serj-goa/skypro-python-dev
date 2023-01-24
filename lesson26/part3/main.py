import csv
import os


data_hesh = {}


def is_hesh(dict_data):
    global data_hesh
    if dict_data in data_hesh:
        return data_hesh[dict_data]
    return None


def select_sorted(sort_columns=["high"], limit=30, group_by_name=False, order='desc', filename='dump.csv'):
    current_dir = os.path.dirname(__file__)
    fields = ['date', 'open', 'high', 'low', 'close', 'volume', 'Name']
    global data_hesh
    dict_data = str({'sort_columns': sort_columns,
                     'limit': limit,
                     'group_by_name': group_by_name,
                     'order': order})                
    hesh = is_hesh(dict_data)

    if hesh:
        list_rows = hesh

    else:
        
        res_file_name = 'all_stocks_5yr.csv'
        res_filepath = os.path.join(current_dir, res_file_name)

        is_reverse = True if order == 'asc' else False
        dictobj = csv.DictReader(open(res_filepath))

        if len(sort_columns) == 1:
            list_rows = sorted(dictobj, key=lambda d: d[sort_columns[0]], reverse=is_reverse)
            
        elif len(sort_columns) == 2:
            list_rows = sorted(dictobj, key=lambda d: (d[sort_columns[0]],
                                                       d[sort_columns[1]]), 
                                                       reverse=is_reverse)
        elif len(sort_columns) == 3:
            list_rows = sorted(dictobj, key=lambda d: (d[sort_columns[0]],
                                                       d[sort_columns[1]],
                                                       d[sort_columns[2]]), 
                                                       reverse=is_reverse)
        elif len(sort_columns) == 4:
            list_rows = sorted(dictobj, key=lambda d: (d[sort_columns[0]],
                                                       d[sort_columns[1]],
                                                       d[sort_columns[2]],
                                                       d[sort_columns[3]]), 
                                                       reverse=is_reverse)
        elif len(sort_columns) == 5:
            list_rows = sorted(dictobj, key=lambda d: (d[sort_columns[0]],
                                                       d[sort_columns[1]],
                                                       d[sort_columns[2]],
                                                       d[sort_columns[3]],
                                                       d[sort_columns[4]]), 
                                                       reverse=is_reverse)
        elif len(sort_columns) == 6:
            list_rows = sorted(dictobj, key=lambda d: (d[sort_columns[0]],
                                                       d[sort_columns[1]],
                                                       d[sort_columns[2]],
                                                       d[sort_columns[3]],
                                                       d[sort_columns[4]],
                                                       d[sort_columns[5]]), 
                                                       reverse=is_reverse)
        else:
            list_rows = sorted(dictobj, key=lambda d: d["high"], reverse=is_reverse)

        list_rows = list_rows[:limit]
        dict_rows = {}

        if group_by_name:
            for each in list_rows:
                name = each["Name"]

                if name in dict_rows:
                    m_dict = dict_rows[name]
                    m_dict['date'] = min(m_dict['date'], each['date'])

                    for i in fields[1:-2]:
                        m_dict[i] = str((float(m_dict[i]) + float(each[i])) / 2)

                    m_dict['volume'] = str(int(m_dict['volume']) + int(each['volume']))
                    m_dict['Name'] = each['Name']
                    dict_rows[name] = m_dict

                else:
                    dict_rows[name] = each

            list_rows = dict_rows.values()
        data_hesh[dict_data] = list_rows

    res_filepath = os.path.join(current_dir, filename)
    writer = csv.DictWriter(open(res_filepath, "w", newline=''), fieldnames=fields)
    writer.writeheader()

    for i in list_rows:
        writer.writerow(i)
        print(i)

    return list(list_rows)


if __name__ == '__main__':

    print('-1-')
    select_sorted(sort_columns=["high", "close"], limit=5, group_by_name=False, order='asc', filename='dump1.csv')

    print('-2-')
    select_sorted(sort_columns=["close"], limit=5, group_by_name=True, order='asc', filename='dump2.csv')

    print('-3-')
    select_sorted(sort_columns=["high", "close"], limit=5, group_by_name=False, order='asc', filename='dump3.csv')
