from utils import get_user_data, parse_command, run_command, run_sort_command, show_result

from typing import List, Tuple


def main():

    log_file = 'data/apache_logs.txt'
    stop_words = ('close', 'exit', 'quit', 'stop')

    while True:

        user_input: str = get_user_data(stop_words=stop_words)

        if user_input in stop_words:
            break

        user_data: List[Tuple] = parse_command(user_input)  # [(command, argument)]

        result_log = run_command(filepath=log_file, data=user_data[0])

        if len(user_data) == 2:
            if user_data[1][0] in ('filter', 'limit', 'map',):
                result_log = run_command(data=user_data[1], data_logs=result_log)

            else:
                result_log = run_sort_command(data=user_data[1], data_logs=result_log)

        show_result(result_log)
        print()


if __name__ == '__main__':
    try:
        main()

    except KeyboardInterrupt:
        print('Программа остановлена.')

    print('\nСпасибо за работу, до встречи!')
