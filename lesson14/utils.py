from typing import List, Tuple


def command_filter(kw: str, some_data: List[str]) -> list:
    """
    Returns a value matching the search key.
    """

    for data in some_data:

        if kw in data:
            return some_data

    return []


def command_limit(kw: int):
    """
    Returns the value of the counter to get the required amount of data.
    """
    return kw - 1


def command_map(kw: str, some_data: List[str]) -> list:
    """
    Returns the selected data type according to the user-specified key.
    """

    try:
        data_index = int(kw)

    except ValueError:
        return some_data

    if data_index in range(len(some_data)):
        return [some_data[data_index]]

    return some_data


def command_sort(kw: str, some_data: list) -> list:
    """
    Sorts the data according to the specified keys.
    """

    reverse = True if kw == 'desc' else False
    sort_data = sorted(some_data, reverse=reverse)

    return sort_data


def command_unique(kw: str, some_data: list) -> list:
    """
    Selects how many unique value from the received data.
    """

    if kw == '-':

        logs_data = [' '.join(data) for data in some_data]
        uniq_data = [data.split() for data in set(logs_data)]

        return uniq_data

    return some_data


COMMANDS = {
    'filter': command_filter,
    'limit': command_limit,
    'map': command_map,
    'sort': command_sort,
    'unique': command_unique
}


def get_user_data(stop_words='stop', kw='|') -> str:
    """
    Getting a command from the user.
    """

    while True:

        some_data = input('Введите команду\n>>> ').strip()

        if some_data.lower() in stop_words:
            return some_data.lower()

        elif len(some_data) <= 4:
            print('Запрос слишком короткий. Введите команду и необходимый аргумент.\n')
            continue

        elif some_data.count(kw) > 1:
            print('Программа принимает не более двух команд. Пожалуйста повторите свой запрос.\n')
            continue

        is_valid = is_valid_data(text=some_data)

        if not is_valid:
            continue

        return some_data


def get_file_generator(filepath: str):
    """
    Obtaining a generator from a file descriptor.
    """

    with open(filepath, 'r', encoding='utf-8') as file:
        for string in file:
            yield string


def is_valid_data(text: str) -> bool:
    """
    Checks the command and argument for compliance with the requirements.
    """

    valid_cmd = False
    valid_data = True

    for data in text.split('|'):
        data = data.strip()

        for cmd in COMMANDS.keys():

            if data.startswith(cmd):
                valid_cmd = True

            if data.endswith(cmd):
                valid_data = False

    if not valid_cmd:
        print('Запрос содержит некорректную команду.\n')

    elif not valid_data:
        print('Запрос содержит некорректный аргумент.\n')

    return valid_cmd and valid_data


def parse_command(some_text: str) -> List[Tuple]:
    """
    Getting a command with arguments from the data received from the user.
    """

    some_data = [command.strip() for command in some_text.split('|')]
    user_cmd = []

    for data in some_data:
        for cmd in COMMANDS.keys():
            if data.startswith(cmd):
                user_cmd.append((cmd, data.strip(cmd + ' ')))

    return user_cmd


def parse_string(string: str) -> List[str]:
    """
    Getting data from a string with logs.
    """

    string = string.replace(' - - ', ' ').strip()

    time_data_start = string.find('[')
    time_data_end = string.find(']')

    ip_addr = string[:time_data_start - 1]
    time_data = string[time_data_start + 1:time_data_end]
    log_data = string[time_data_end + 2:]

    return [ip_addr, time_data, log_data]


def run_command(data: tuple, filepath: str = None, data_logs: list = None) -> List[str]:
    """
    Run commands that will process the data and generate a list.
    """

    command = COMMANDS[data[0]]
    cmd_argument = data[1]
    cnt_iter = None

    if data[0] == 'limit':
        try:
            cnt_iter = int(data[1])

        except ValueError:
            cnt_iter = -1

    flag = True if data[0] in ('filter', 'map') else False
    log_parse = False
    result_data = []

    if data_logs is None:
        data_logs = get_file_generator(filepath)
        log_parse = True

    for log in data_logs:

        if cnt_iter == 0:
            break

        elif cnt_iter is not None:
            cnt_iter = command(kw=cnt_iter)

        if log_parse:
            log = parse_string(string=log)  # List[str]

        if flag:
            log = command(kw=cmd_argument, some_data=log)  # List[str]

        if log:
            result_data.append(log)

    if data[0] in ('unique', 'sort'):
        result_data = command(kw=cmd_argument, some_data=result_data)

    return result_data


def run_sort_command(data: tuple, data_logs: list) -> List[str]:
    """
    Run commands that work with the collected data.
    """

    command = COMMANDS[data[0]]
    cmd_argument = data[1]

    return command(kw=cmd_argument, some_data=data_logs)


def show_result(data_logs: list) -> None:
    """
    Displays search results.
    """

    print('----------------------------')

    for log in data_logs:
        print(*log, sep='\n', end='\n\n')

    print('----------------------------')
