from utils import *


def main():
    PROFESSIONS_DB = './data/professions.json'
    STUDENTS_DB = './data/students.json'

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
    main()
