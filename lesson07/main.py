from json import load


STOP_WORDS = ('close', 'quit', 'stop')


def check_fitness(student: list, profession: list) -> dict:
    student_skills = set(student['skills'])
    prof_skills = set(profession['skills'])

    has_key = list(prof_skills & student_skills)
    lacks_key = list(prof_skills - student_skills)
    fit_percent = round((len(has_key) / len(profession['skills'])) * 100)

    total_data = {
        "has": has_key,
        "lacks": lacks_key,
        "fit_percent": fit_percent
    }
    return total_data


def get_value_by_key(kw: str, user_value: str or int, db: list):
    """
    Gets a dictionary with data for the specified parameters.
    """
    for data in db:
        if data[kw] == user_value:
            return data


def get_pk_from_user(all_students: list) -> int:
    while True:
        print('Введите номер студента')
        student_number = input('>>> ').strip()

        if student_number in STOP_WORDS:
            quit()

        if not student_number.isdigit():
            continue

        student_number = int(student_number)

        if not is_valid_data('pk', student_number, all_students):
            print('У нас нет такого студента\n')
            continue

        return student_number


def get_profession_from_user(student_name: str, profession_name: list, all_professions: list) -> str:
    while True:
        print(f'Выберите специальность ({", ".join(profession_name)}) для оценки студента {student_name}')
        profession = input('>>> ').strip().title()

        if profession.lower() in STOP_WORDS:
            quit()

        if not is_valid_data('title', profession, all_professions):
            print('У нас нет такой специальности\n')
            continue

        return profession


def is_valid_data(data_key: str, data_value: int, all_students: list) -> bool:
    """
    Checks if the specified key exists in the student database.
    """
    for student in all_students:
        if student[data_key] == data_value:
            return True
    return False


def load_data(filepath: str) -> list:
    """
    Loads a list of students from a file.
    """
    with open(filepath, encoding='utf-8') as fh:
        data = load(fh)

    return data


def show_result(student: list, profession: list) -> None:
    total_data = check_fitness(student, profession)
    student_has = total_data["has"]
    student_lacks = total_data["lacks"]
    percent = total_data["fit_percent"]

    if percent == 100:
        print(f'\nПригодность {total_data["fit_percent"]}%')
        print(f'{student["full_name"]} владеет всеми необходимыми навыками.\n')

    elif not student_has:
        print(f'\nПригодность {total_data["fit_percent"]}%')
        print(f'{student["full_name"]} не владеет навыками из выбранной профессии.')
        print(f'Необходимо будет изучить: {", ".join(total_data["lacks"])}\n')

    else:
        print(f'\nПригодность {total_data["fit_percent"]}%')
        print(f'{student["full_name"]} знает: {", ".join(total_data["has"])}')
        print(f'{student["full_name"]} не знает: {", ".join(total_data["lacks"])}\n')


def main():
    ALL_PROFESSIONS = load_data(PROFESSIONS_DB)
    ALL_STUDENTS = load_data(STUDENTS_DB)

    while True:
        student_number = get_pk_from_user(ALL_STUDENTS)
        student_data = get_value_by_key('pk', student_number, ALL_STUDENTS)

        student_name = student_data["full_name"]
        profession_name = [prof['title'] for prof in ALL_PROFESSIONS]

        print(f'\nСтудент {student_name}')
        print(f'Знает {", ".join(student_data["skills"])}\n')

        user_profession = get_profession_from_user(student_name, profession_name, ALL_PROFESSIONS)

        profession = get_value_by_key('title', user_profession, ALL_PROFESSIONS)
        show_result(student_data, profession)


if __name__ == '__main__':
    PROFESSIONS_DB = './data/professions.json'
    STUDENTS_DB = './data/students.json'
    main()
