from typing import List, Tuple


def command_filter(kw: str, some_data: List[str]) -> list:
    """
    Returns a value matching the search key.
    """

    for data in some_data:

        if kw in data:
            return some_data

    return []


def command_limit(kw: int) -> int:
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


def get_count_number(data: str) -> int:
    """
    Gets the counter number.
    """

    try:
        return int(data)

    except ValueError:
        return -1


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

        if not is_valid_data(text=some_data):
            continue

        return some_data


def get_file_generator(filepath: str):
    """
    Getting a generator from a file descriptorObtaining a generator from a file descriptor.
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


def run_command(cmd_name: str, cmd_argument: str, filepath: str = None, data_log: list = None) -> list:
    """
    Run commands that will process the data and generate a list.
    """

    iter_counter = get_count_number(cmd_argument) if cmd_name == 'limit' else None
    flag = True if cmd_name in ('filter', 'map') else False
    parse_data_by_string = False
    result_data = []

    if data_log is None:
        data_log = get_file_generator(filepath)
        parse_data_by_string = True

    for log in data_log:

        if iter_counter == 0:
            break

        elif iter_counter is not None:
            iter_counter = COMMANDS[cmd_name](kw=iter_counter)

        if parse_data_by_string:
            log = parse_string(string=log)  # List[str]

        if flag:
            log = COMMANDS[cmd_name](kw=cmd_argument, some_data=log)  # List[str]

        if log:
            result_data.append(log)

    return result_data


# def run_sort_command(data: tuple, data_log: list) -> list:
def run_sort_command(cmd_name: str, cmd_argument: str, data_log: list) -> list:
    """
    Run commands that work with the collected data.
    """

    return COMMANDS[cmd_name](kw=cmd_argument, some_data=data_log)


def show_result(data_logs: list) -> None:
    """
    Displays search results.
    """

    print('----------------------------')

    for log in data_logs:
        print(*log, sep='\n', end='\n\n')

    print('----------------------------')
