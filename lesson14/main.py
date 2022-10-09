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

        cmd_name = user_data[0][0]
        cmd_argument = user_data[0][1]

        result_log = run_command(cmd_name, cmd_argument, filepath=log_file)

        if cmd_name in ('unique', 'sort'):
            result_log = run_sort_command(cmd_name, cmd_argument, data_log=result_log)

        if len(user_data) == 2:

            cmd_name = user_data[1][0]
            cmd_argument = user_data[1][1]

            if cmd_name in ('filter', 'limit', 'map',):
                result_log = run_command(cmd_name, cmd_argument, data_log=result_log)

            else:
                result_log = run_sort_command(cmd_name, cmd_argument, data_log=result_log)

        show_result(result_log)
        print()


if __name__ == '__main__':

    try:
        main()

    except KeyboardInterrupt:
        print('Программа остановлена.')

    print('\nСпасибо за работу, до встречи!')
