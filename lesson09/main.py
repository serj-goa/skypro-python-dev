from utils import get_pk_from_user, get_student_by_key, is_valid_login, load_data, show_result


def main():

    students_db: str = './data/students.json'
    ALL_STUDENTS: list = load_data(students_db)

    while True:
        user_pk: int = get_pk_from_user(ALL_STUDENTS)
        student_data: dict = get_student_by_key(user_pk, ALL_STUDENTS)
        valid_login: bool = is_valid_login(student_data)
        show_result(valid_login, student_data)


if __name__ == '__main__':
    main()
